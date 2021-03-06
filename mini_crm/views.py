from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from django.template import Context
from django.core.urlresolvers import reverse
from django.core.exceptions import PermissionDenied
import json
from leads.models import Leads, WPPLeads, PicassoLeads, TagLeadDetail, LeadHistory, Language, Team
from datetime import datetime,timedelta

import pytz 
from reports.models import Region
from django.http import Http404, HttpResponseForbidden, HttpResponse
from django.conf import settings
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User, Group
from django.views.decorators.csrf import csrf_exempt
from lib.helpers import (get_unique_uuid)

import uuid, os
from lib.helpers import save_file, get_ist_pst_converted_timestamps
import mimetypes

from django.template.loader import get_template
from lib.helpers import send_mail
from django.forms.models import model_to_dict

import ast
import csv

from django.core import exceptions


# Create your views here.
@login_required
def crm_management(request):
    if request.user.groups.filter(name='CRM-MANAGER'):
        
        leads_list = list()
        limit = int(request.GET.get('limit', 10))
        on_page = int(request.GET.get('page', 1))
        if on_page <= 1:
            offset = 0
        else:
            on_page -= 1;
            offset = limit * on_page
            limit = offset + limit  
        
        regions = Region.objects.all()
        regions_list = list()
        for region in regions:
            region_dict = {'name':region.name,
                           'location':region.location_list()}
            regions_list.append(region_dict)

        download_csv = True if request.GET.get('download_csv') else False

        if request.method == 'GET' and not download_csv and not request.is_ajax():
            context = {'crm_manager_text': json.dumps(settings.LEAD_STATUS_SUB_STATUS_MAPPING), 'regions':json.dumps(regions_list), 'manager':True}
            return render(request,'crm/manager_home.html',context)
        else:
            region = request.GET.get('region') if request.GET.get('region') else ''
            process_type = request.GET.get('process') if request.GET.get('process') else ''
            lead_status = request.GET.get('status') if request.GET.get('status') else ''
            lead_sub_status = request.GET.get('sub_status') if request.GET.get('sub_status') else ''
            lead_appointment = request.GET.get('appointment') if request.GET.get('appointment') else None
            start_date = datetime.strptime(str(request.GET.get('start_date')), "%m/%d/%Y") if request.GET.get('start_date') else None
            end_date = datetime.strptime(str(request.GET.get('end_date')), "%m/%d/%Y") if request.GET.get('end_date') else None
            

            has_region = False
            loc_list = list()
            if str(region) != 'all':
                has_region = True
                region = Region.objects.filter(name=region)

                locations_list =  region[0].location_list().split(',')

                loc_list = [str(loc).strip() for loc in locations_list]

            if not lead_appointment and not download_csv:

                if lead_status == lead_sub_status:
                    if has_region:

                        query = {'lead_status': lead_status, 'country__in':loc_list, 'is_delete':False}

                        if start_date and end_date:
                            query.update({'created_date__gte':start_date, 'created_date__lt':end_date})
                     
                    else:

                        query = {'lead_status': lead_status, 'is_delete':False}

                        if start_date and end_date:
                            query.update({'created_date__gte':start_date, 'created_date__gte':start_date, 'created_date__lt':end_date})
                        
                            
                else:
                    if has_region:

                        query = {'lead_status' : lead_status,'lead_sub_status' :lead_sub_status,
                        'country__in':loc_list, 'is_delete':False}

                        if start_date and end_date:
                            query.update({'created_date__gte':start_date, 'created_date__gte':start_date, 'created_date__lt':end_date})

                    else:

                        query = {'lead_status' : lead_status,'lead_sub_status' :lead_sub_status, 'is_delete':False}

                        if start_date and end_date:
                            query.update({'created_date__gte':start_date, 'created_date__lt':end_date})

                if process_type == "WPP":

                    leads = WPPLeads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("WPP"), **query).values(
                        'id', 'sf_lead_id','customer_id', 'company', 'first_name', 'created_date','appointment_date', 'phone', 'phone_optional', 'country','type_1'
                        )[offset:limit]
                    leads_count = WPPLeads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("WPP"), **query).count()

                elif process_type == "Picasso Audits":

                    if loc_list:

                        query = {'lead_status': lead_status, 'country__in':loc_list, 'is_delete':False}
                        if start_date and end_date:
                            query.update({'created_date__gte':start_date, 'created_date__lt':end_date})

                    else:
                        
                        query = {'lead_status': lead_status, 'is_delete':False}
                        if start_date and end_date:
                            query.update({'created_date__gte':start_date, 'created_date__lt':end_date})

                    leads = PicassoLeads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("Picasso Audits"), **query).values(
                        'id', 'sf_lead_id','customer_id', 'company', 'first_name', 'created_date', 'phone', 'country','type_1')[offset:limit]
                    leads_count = PicassoLeads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("Picasso Audits"), **query).count()

                elif process_type == "RLSA":

                    leads = Leads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("RLSA"), **query).values(
                        'id', 'sf_lead_id','customer_id', 'company', 'first_name', 'created_date', 'appointment_date_in_ist', 'phone', 'phone_optional', 'country','type_1'
                        ).order_by('-created_date')[offset:limit]

                    leads_count = Leads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("RLSA"), **query).count()

                elif process_type == "Shopping":

                    leads = Leads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("Shopping"), **query).values(
                        'id', 'sf_lead_id','customer_id', 'company', 'first_name', 'created_date', 'appointment_date_in_ist', 'phone', 'phone_optional', 'country','type_1'
                        )[offset:limit]
                    leads_count = Leads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("Shopping"), **query).count()

                elif process_type == "ShoppingArgos":
                    leads = Leads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("Shopping Argos"), **query).values(
                        'id', 'sf_lead_id','customer_id', 'company', 'first_name', 'created_date', 'appointment_date_in_ist', 'phone', 'phone_optional', 'country','type_1'
                        )[offset:limit]
                    leads_count = Leads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("Shopping Argos"), **query).count()
                    
                elif process_type == "tag_and_shopping":

                    if query['lead_status'].startswith('TAG'):
                        query['lead_status'] = query['lead_status'].replace("TAG",'').strip()
                        exclude_types = settings.PROCESS_TYPE_MAPPING.get("RLSA") + settings.PROCESS_TYPE_MAPPING.get("Shopping Argos") + settings.PROCESS_TYPE_MAPPING.get("Shopping")
                        leads = Leads.objects.filter(**query).exclude(type_1__in = exclude_types).values('id', 'sf_lead_id','customer_id', 'company', 'first_name', 'created_date',  'appointment_date_in_ist', 'phone', 'phone_optional', 'country','type_1'
                            )[offset:limit]
                        leads_count = Leads.objects.filter(**query).exclude(type_1__in = exclude_types).count()
                        
                    elif query['lead_status'].startswith('Shopping'):
                        query['lead_status'] = query['lead_status'].replace("Shopping",'').strip()
                        leads = Leads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("Shopping"), **query).values(
                        'id', 'sf_lead_id','customer_id', 'company', 'first_name', 'created_date', 'appointment_date_in_ist', 'phone', 'phone_optional', 'country','type_1'
                        )[offset:limit]
                        leads_count = Leads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("Shopping"), **query).count()
                        
                    else:
                        query['lead_status'] = query['lead_status']
                        exclude_types = settings.PROCESS_TYPE_MAPPING.get("RLSA")
                        leads = Leads.objects.filter(**query).exclude(type_1__in = exclude_types).values('id', 'sf_lead_id','customer_id', 'company', 'first_name', 'created_date',  'appointment_date_in_ist', 'phone', 'phone_optional', 'country', 
                            'type_1')[offset:limit]
                        leads_count = Leads.objects.filter(**query).exclude(type_1__in = exclude_types).count()
                        
                else: # Tag
                    exclude_types = settings.PROCESS_TYPE_MAPPING.get("RLSA") + settings.PROCESS_TYPE_MAPPING.get("Shopping Argos") + settings.PROCESS_TYPE_MAPPING.get("Shopping")
                    leads = Leads.objects.filter(**query).exclude(type_1__in = exclude_types).values('id', 'sf_lead_id','customer_id', 'company', 'first_name', 'created_date',  'appointment_date_in_ist', 'phone', 'phone_optional', 'country','type_1'
                        )[offset:limit]
                    leads_count = Leads.objects.filter(**query).exclude(type_1__in = exclude_types).count()

            elif not download_csv and lead_appointment:
                user_group = request.user.groups.filter(name='CRM-MANAGER')
                current_user_email = request.user.email
                leads, leads_count = get_filtered_leads(user_group,process_type,lead_status,lead_sub_status,lead_appointment,current_user_email,limit,offset,has_region,loc_list, start_date, end_date, download_csv)
            
            elif download_csv and not lead_appointment:
                leads, lead_count = get_export_leads_no_appointment_manager(lead_status,lead_sub_status,has_region,loc_list,start_date,end_date,process_type,offset,limit)
                all_leads = get_leads(leads, [])
                return export_filtered_leads(all_leads,False) 

            elif download_csv and lead_appointment:
                user_group = request.user.groups.filter(name='CRM-MANAGER')
                current_user_email = request.user.email
                leads, leads_count = get_filtered_leads(user_group,process_type,lead_status,lead_sub_status,lead_appointment,current_user_email,limit,offset,has_region,loc_list, start_date, end_date, download_csv)
                all_leads = get_leads(leads, [])
                return export_filtered_leads(all_leads,False) 

            all_leads = get_leads(leads, leads_list)
            try:
                return HttpResponse(json.dumps({'leads_list': all_leads, 'leads_count':leads_count}), content_type="application/json")
            except Exception as e:
                print e

        context = {'crm_manager_text': json.dumps(settings.LEAD_STATUS_SUB_STATUS_MAPPING), 'regions':json.dumps(regions_list), 'manager':True}
        return render(request,'crm/manager_home.html',context)

    elif request.user.groups.filter(name='CRM-AGENT'):
        return redirect('mini_crm.views.lead_history')
    else:
        raise Http404


def get_leads(leads, leads_list):
    for lead in leads:
        appointment_date = datetime.strftime(lead.get('appointment_date_in_ist'), "%d/%m/%Y %I:%M %P") if lead.get('appointment_date_in_ist') else None
        phone_optional =  lead.get('phone_optional')
        process_type = None
        type_1 = lead.get('type_1')
        if type_1 in settings.PROCESS_TYPE_MAPPING.get('Shopping'):
            process_type = "Shopping"
        elif type_1 in settings.PROCESS_TYPE_MAPPING.get('Shopping Argos'):
            process_type = "Shopping - Argos"
        elif type_1 in settings.PROCESS_TYPE_MAPPING.get('RLSA'):
            process_type = "RLSA"
        elif type_1 in settings.PROCESS_TYPE_MAPPING.get('Picasso Audits'):
            process_type = "Picasso Audits"
        elif type_1 in settings.PROCESS_TYPE_MAPPING.get('WPP'):
            process_type = "WPP"
        else:
            process_type = "TAG"
                      
        lead_dict = {'id':lead['id'],
                     'sf_lead_id':lead['sf_lead_id'],
                     'c_id':lead['customer_id'],
                     'company':lead['company'],
                     'customer_name':lead['first_name'],
                     'created_date':datetime.strftime(lead.get('created_date'), "%d/%m/%Y %I:%M %P") if lead.get('created_date') else lead.get('created_date'),
                     'appointment_time': appointment_date,
                     'phone_number':lead['phone'], 
                     'additional_phone_number':phone_optional, 
                     'web_master_number':'', 
                     'location':lead['country'],
                     'type_1': process_type}
        
        leads_list.append(lead_dict)
    return leads_list


@login_required
def crm_agent(request):
    if request.user.groups.filter(name='CRM-MANAGER'):
        return redirect('mini_crm.views.crm_management')
    elif request.user.groups.filter(name='CRM-AGENT'):
        if request.GET:
            leads_data = list()
            lead_status =  ''
            lead_sub_status = ''
            lead_appointment = None
            start_date = datetime.strptime(str(request.GET.get('start_date')), "%m/%d/%Y").replace(hour=0,minute=0,second=0) if request.GET.get('start_date') else None
            end_date = datetime.strptime(str(request.GET.get('end_date')), "%m/%d/%Y").replace(hour=23,minute=59,second=59) if request.GET.get('end_date') else None
            download_csv = True if request.GET.get('download_csv') else False

            limit = int(request.GET.get('limit', 10))
            on_page = int(request.GET.get('page', 1))
            if on_page <= 1:
                offset = 0
            else:
                on_page -= 1;
                offset = limit * on_page
                limit = offset + limit
            
            if request.GET.get('status'):
                lead_status = request.GET.get('status')
            if request.GET.get('sub_status'):
                lead_sub_status = request.GET.get('sub_status')
            if request.GET.get('appointment'):
                lead_appointment = request.GET.get('appointment')
            user_group = request.user.groups.filter(name='CRM-AGENT')
            current_user_email = request.user.email
            leads, leads_count = get_filtered_leads(user_group,'TAG',lead_status,lead_sub_status,lead_appointment,current_user_email,limit,offset,'','',start_date, end_date,download_csv)
            leads_data = get_json_leads(leads,'TAG')
            if request.GET.get('download_csv'):
                return export_filtered_leads(leads_data,True) 
            else:
                response_json = {'leads_list': leads_data, 'leads_count':leads_count}
                res = HttpResponse(json.dumps(response_json), content_type="application/json")
                return res
        context ={
            'lead_status':settings.LEAD_STATUS_SUB_STATUS_MAPPING['TAG'].keys(),
            'lead_status_sub_status_mapping':json.dumps({'lead_status_sub_status_mapping':settings.LEAD_STATUS_SUB_STATUS_MAPPING},encoding="utf-8")
        }
        return render(request,'crm/agent_home.html',context)
    else:
        raise Http404


def get_filtered_leads(user_group,process,lead_status,lead_sub_status,lead_appointment,current_user_email,limit,offset,has_region,loc_list, start_date, end_date,download_csv):
    if lead_appointment and lead_appointment != 'Select':
        #Our Local timezone, to which we want to convert the UTC time.
        local_tz = pytz.timezone('Asia/Calcutta')
        #Add Timezone information toUTC time.
        now_utc = pytz.utc.localize(datetime.now())
        # Convert to local time.
        local_time = now_utc.astimezone(local_tz)
        local_time = local_time.replace(tzinfo=None)
        if lead_appointment == '30 minutes':
            start_date_time = local_time
            end_date_time = start_date_time + timedelta(minutes=30)
        if lead_appointment == '1 hour':
            start_date_time = local_time
            end_date_time = start_date_time + timedelta(minutes=60)
        if lead_appointment == 'Today':
            start_date_time = local_time.replace(hour=0,minute=0,second=0)
            end_date_time = local_time.replace(hour=23,minute=59,second=59)
        if lead_appointment == 'Tomorrow':
            tomorrow_date = local_time + timedelta(days=1)
            start_date_time = tomorrow_date.replace(hour=0,minute=0,second=0)
            end_date_time = tomorrow_date.replace(hour=23,minute=59,second=59)
        if lead_appointment == 'This week':
            current_date = local_time.date()
            year, week, dow = current_date.isocalendar()
            # Find the first day of the week.
            if dow == 7:
                # Since we want to start with Sunday, let's test for that condition.
                week_start = current_date
            else:
                # Otherwise, subtract `dow` number days to get the first day
                week_start = current_date - timedelta(dow)
            # Now, add 6 for the last day of the week (i.e., count up to Saturday)
            week_end = week_start + timedelta(6)
            start_date_time = datetime.combine(week_start, datetime.min.time()).replace(hour=0,minute=0,second=0)
            end_date_time =  datetime.combine(week_end, datetime.min.time()).replace(hour=23,minute=59,second=59)
        if lead_appointment == 'Without Appointment':
            start_date_time = ''
            end_date_time = ''
        if user_group[0].name == 'CRM-AGENT':
            if download_csv:
                leads, leads_count = get_export_leads_based_on_appointment_agent(lead_appointment,start_date,end_date,current_user_email)
            else:
                if lead_appointment == 'Without Appointment':
                    exclude_types = settings.PROCESS_TYPE_MAPPING.get("RLSA") + settings.PROCESS_TYPE_MAPPING.get("Shopping Argos") + settings.PROCESS_TYPE_MAPPING.get("Shopping")
                    query = {'appointment_date__isnull':True,'lead_status':'In Queue',
                            'lead_owner_email':current_user_email,
                            'is_delete':False}
                    if start_date and end_date:
                        query.update({'created_date__gte':start_date,'created_date__lte':end_date})
                    leads = Leads.objects.filter(**query).exclude(type_1__in=exclude_types)[offset:limit]
                    leads_count = Leads.objects.filter(**query).exclude(type_1__in=exclude_types).count()
                else:
                    query = {'lead_status__in':['Attempting Contact','In Queue'], 
                            'appointment_date_in_ist__gte':start_date_time,
                            'appointment_date_in_ist__lte':end_date_time,
                            'rescheduled_appointment_in_ist__gte':start_date_time,
                            'rescheduled_appointment_in_ist__lte':end_date_time,
                            'lead_owner_email':current_user_email,'is_delete':False}
                    if start_date and end_date:
                        query.update({'created_date__gte':start_date,'created_date__lte':end_date})
                    leads = Leads.objects.filter(**query)[offset:limit]
                    leads_count = Leads.objects.filter(**query).count()
        else:
            #manager
            if download_csv:
                leads, leads_count = get_export_leads_based_on_appointment_manager(process,lead_appointment,limit,offset,has_region,loc_list,start_date_time,end_date_time, start_date, end_date, download_csv)
            else:
                leads,leads_count = get_leads_based_on_appointment_manager(process,lead_appointment,limit,offset,has_region,loc_list,start_date_time,end_date_time, start_date, end_date)
            
            # leads = Leads.objects.filter(lead_status="In Queue", appointment_date_in_ist__gte=start_date_time,appointment_date_in_ist__lte=end_date_time).values(
            #     'id', 'sf_lead_id','customer_id', 'company', 'first_name', 'created_date',  'appointment_date_in_ist', 'phone', 'phone_optional', 'country')
    else:
        if user_group[0].name == 'CRM-AGENT':
            if download_csv:
                leads, leads_count = get_export_leads_no_appointment_agent(lead_status,lead_sub_status,start_date,end_date,current_user_email)
            else:
                if lead_status == 'In Queue':
                    query = {}
                else:
                    query = {'lead_sub_status': lead_sub_status}

                if start_date and end_date:
                    query.update({'created_date__gte':start_date,'created_date__lte':end_date})

                leads_count = Leads.objects.filter(lead_status=lead_status,
                            lead_owner_email=current_user_email,is_delete=False,**query).count()
                leads = Leads.objects.filter(lead_status=lead_status,
                        lead_owner_email=current_user_email,is_delete=False,**query)[offset:limit]
        else:
            #manager
            if download_csv:
                leads, leads_count = get_export_leads_based_on_appointment_manager(process,lead_appointment,limit,offset,has_region,loc_list,start_date_time,end_date_time, start_date, end_date, download_csv)
            else:
                leads, leads_count = get_leads_based_on_appointment_manager(process,lead_appointment,limit,offset,has_region,loc_list,start_date_time,end_date_time, start_date, end_date)
           
            # leads = Leads.objects.filter(lead_status=lead_status,lead_sub_status=lead_sub_status).values(
            #     'id', 'sf_lead_id','customer_id', 'company', 'first_name', 'created_date',  'appointment_date_in_ist', 'phone', 'phone_optional', 'country')
    return leads, leads_count


def get_leads_based_on_appointment_manager(process_type,lead_appointment,limit,offset,has_region,loc_list,start_date_time,end_date_time, start_date, end_date):
    if has_region:
        if lead_appointment == 'Without Appointment':

            query = {'country__in':loc_list, 'appointment_date__isnull':True, 'is_delete':False}

            if start_date and end_date:
                query.update({'created_date__gte':start_date, 'created_date__lt':end_date})
            
        elif lead_appointment != 'Select' or 'Without Appointment':

            query = {'country__in':loc_list, 'appointment_date_in_ist__gte':start_date_time, 
                    'appointment_date_in_ist__lte':end_date_time,
                    # 'rescheduled_appointment_in_ist__gte':start_date_time,
                    # 'rescheduled_appointment_in_ist__lte':end_date_time, 
                    'is_delete':False
                    }

            if start_date and end_date:
                query.update({'created_date__gte':start_date, 'created_date__lt':end_date})
            
        else:

            query = {'country__in':loc_list, 'is_delete':False}

            if start_date and end_date:
                query.update({'created_date__gte':start_date, 'created_date__lt':end_date})
            
    else:
        if lead_appointment == 'Without Appointment':

            query = {'appointment_date__isnull':True, 'is_delete':False}

            if start_date and end_date:
                query.update({'created_date__gte':start_date, 'created_date__lt':end_date})
                
        elif lead_appointment != 'Select' or 'Without Appointment':
            query = {'appointment_date_in_ist__gte':start_date_time,
                'appointment_date_in_ist__lte':end_date_time,
                # 'rescheduled_appointment_in_ist__gte':start_date_time,
                # 'rescheduled_appointment_in_ist__lte':end_date_time, 
                'is_delete':False,
            }
            if start_date and end_date:
                query.update({'created_date__gte':start_date, 'created_date__lt':end_date})
        else:
            query = {}

    if process_type == "WPP":
        leads = WPPLeads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("WPP"), **query).values(
            'id', 'sf_lead_id','customer_id', 'company', 'first_name', 'created_date','appointment_date', 'phone', 'phone_optional', 'country','type_1'
            )[offset:limit]
        leads_count = WPPLeads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("WPP"), **query).count()
        
    elif process_type == "Picasso Audits":

        if loc_list:

            query = {'country__in':loc_list, 'is_delete':False}
            if start_date and end_date:
                query.update({'created_date__gte':start_date, 'created_date__lt':end_date})

        else:
            query = {}

        leads = PicassoLeads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("Picasso Audits"), **query).values(
            'id', 'sf_lead_id','customer_id', 'company', 'first_name', 'created_date', 'phone', 'country','type_1')[offset:limit]
        leads_count = PicassoLeads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("Picasso Audits"), **query).count()

    elif process_type == "RLSA":

        leads = Leads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("RLSA"), **query).values(
            'id', 'sf_lead_id','customer_id', 'company', 'first_name', 'created_date', 'appointment_date_in_ist', 'phone', 'phone_optional', 'country','type_1'
            ).order_by('-created_date')[offset:limit]

        leads_count = Leads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("RLSA"), **query).count()
        
    elif process_type == "Shopping":
        leads = Leads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("Shopping"), **query).values(
            'id', 'sf_lead_id','customer_id', 'company', 'first_name', 'created_date', 'appointment_date_in_ist', 'phone', 'phone_optional', 'country','type_1'
            )[offset:limit]
        leads_count = Leads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("Shopping"), **query).count()
        
    elif process_type == "ShoppingArgos":
        leads = Leads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("Shopping Argos"), **query).values(
            'id', 'sf_lead_id','customer_id', 'company', 'first_name', 'created_date', 'appointment_date_in_ist', 'phone', 'phone_optional', 'country','type_1'
            )[offset:limit]
        leads_count = Leads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("Shopping Argos"), **query).count()
        
    elif process_type == "tag_and_shopping":
        exclude_types = settings.PROCESS_TYPE_MAPPING.get("RLSA")
        leads = Leads.objects.filter(**query).exclude(type_1__in = exclude_types).values('id', 'sf_lead_id','customer_id', 'company', 'first_name', 'created_date',  'appointment_date_in_ist', 'phone', 'phone_optional', 'country','type_1'
            )[offset:limit]
        leads_count = Leads.objects.filter(**query).exclude(type_1__in = exclude_types).count()
                    
    else: # Tag

        exclude_types = settings.PROCESS_TYPE_MAPPING.get("RLSA") + settings.PROCESS_TYPE_MAPPING.get("Shopping Argos") + settings.PROCESS_TYPE_MAPPING.get("Shopping")

        leads = Leads.objects.filter(**query).exclude(type_1__in = exclude_types).values('id', 'sf_lead_id','customer_id', 'company', 'first_name', 'created_date',  'appointment_date_in_ist', 'phone', 'phone_optional', 'country','type_1'
            )[offset:limit]
        leads_count = Leads.objects.filter(**query).exclude(type_1__in = exclude_types).count()

    return leads,leads_count


def get_json_leads(leads, process_type=None):
    leads_data = list()
    lead_detail = None
    for lead in leads:
        if process_type and process_type in ['TAG','Shopping','RLSA','Shopping Argos']:
            try:
                lead_detail = TagLeadDetail.objects.get(lead_id=lead)
            except:
                lead_detail = TagLeadDetail()
                lead_detail.lead_id = lead
                lead_detail.save()

        lead_dict = {
        'id':lead.id,
        'pla_sub_status':lead_detail.pla_sub_status if hasattr(lead_detail, 'pla_sub_status') and lead_detail.pla_sub_status  else '',
        'implemented_cod_is':lead_detail.implemented_code_is if hasattr(lead_detail, 'implemented_code_is') and lead_detail.implemented_code_is  else '',
        'is_backup_taken':lead_detail.is_backup_taken if hasattr(lead_detail, 'is_backup_taken') and lead_detail.is_backup_taken else '',
        'description':lead_detail.pla_sub_status if hasattr(lead_detail, 'description') and lead_detail.description else '',
        'service_segment':lead_detail.service_segment if hasattr(lead_detail, 'service_segment') and lead_detail.service_segment  else '',
        'rlsa_auth_approval':lead_detail.rlsa_auth_approval if hasattr(lead_detail, 'rlsa_auth_approval') and lead_detail.rlsa_auth_approval  else '',
        'lead_owner':lead.lead_owner_name,
        'lead_status':lead.lead_status,
        'lead_owner_email':lead.lead_owner_email,
        'type_1':lead.type_1 if hasattr(lead, 'type_1') and lead.type_1 else '',
        'first_name':lead.first_name,
        'last_name':lead.last_name,
        'timezone':lead.time_zone if hasattr(lead, 'time_zone') and lead.time_zone else '',
        'ecommerce':lead.ecommerce if hasattr(lead, 'ecommerce') and lead.ecommerce else '',
        'lead_sub_status':lead.lead_sub_status if hasattr(lead, 'lead_sub_status') and lead.lead_sub_status else '',
        'lead_id':lead.id,
        'sf_lead_id':lead.sf_lead_id,
        'customer_id':lead.customer_id,
        'company':lead.company,
        'customer_name':lead.first_name + '' + lead.last_name,
        'appointment_time':datetime.strftime(lead.appointment_date, "%d/%m/%Y %I:%M %P") if hasattr(lead, 'appointment_date') and lead.appointment_date else '',
        'appointment_date_in_ist':datetime.strftime(lead.appointment_date_in_ist, "%d-%m-%Y %I:%M %P") if hasattr(lead, 'appointment_date_in_ist') and lead.appointment_date_in_ist else '',
        'rescheduled_appointment':datetime.strftime(lead.rescheduled_appointment, "%d-%m-%Y %I:%M %P") if hasattr(lead, 'rescheduled_appointment') and lead.rescheduled_appointment else '',
        'rescheduled_appointment_in_ist':datetime.strftime(lead.rescheduled_date_in_ist, "%d-%m-%Y %I:%M %P") if hasattr(lead, 'rescheduled_appointment_in_ist') and lead.rescheduled_appointment_in_ist else '',
        'email_optional':lead.email_optional if hasattr(lead, 'email_optional') and lead.email_optional else '',
        'company':lead.country if hasattr(lead, 'country') and lead.country else '',
        'language':lead.language if hasattr(lead, 'language') and lead.language else '',
        'primary_contact_role':lead.primary_contact_role if hasattr(lead, 'primary_contact_role') and lead.primary_contact_role else '',
        'webmaster_phone':lead.webmaster_phone if hasattr(lead, 'webmaster_phone') and lead.webmaster_phone else '',
        'webmaster_name':lead.webmaster_name if hasattr(lead, 'webmaster_name') and lead.webmaster_name else '',
        'phone':lead.phone,
        'phone_optional':lead.phone_optional if hasattr(lead, 'phone_optional') else '',
        'web_master_no':'',
        'location':'',
        'rescheduled':True if hasattr(lead, 'rescheduled_appointment') and lead.rescheduled_appointment else False,
        'lead_owner_name':lead.lead_owner_name,
        'team':lead.team,
        'date_of_installation':datetime.strftime(lead.date_of_installation, "%d/%m/%Y") if lead.date_of_installation else '',
        'first_contacted_on':datetime.strftime(lead.first_contacted_on, "%d/%m/%Y %I:%M %P") if hasattr(lead, 'first_contacted_on') and lead.first_contacted_on else '',
        'dials':lead.dials if hasattr(lead, 'dials') and lead.dials else 0,
        'created_date':datetime.strftime(lead.created_date, "%d/%m/%Y %I:%M %P") if hasattr(lead, 'created_date') and lead.created_date else '',
        }
        if lead_dict.get('appointment_time'):
            local_tz = pytz.timezone('Asia/Calcutta')
            appointment_date = pytz.utc.localize(lead.appointment_date)
            appointment_date_in_ist = appointment_date.astimezone(local_tz)
            lead_dict['appointment_date_in_ist'] = datetime.strftime(appointment_date_in_ist, "%d-%m-%Y %I:%M %P")
            lead_dict['appointment_date'] = lead_dict['appointment_date_in_ist'].replace('/','-')
            date_time = lead_dict['appointment_date_in_ist'].split(' ')
            lead_dict['apmnt_date'] = date_time[0]
            lead_dict['apmnt_time'] = date_time[1] + ' ' + date_time[2]
        leads_data.append(lead_dict)

    return leads_data


@login_required
def lead_history(request):
    if request.user.groups.filter(name='CRM-AGENT'):
        lead_status = request.GET.get('status')
        process_type = 'TAG'
        current_user_email = request.user.email
        if request.is_ajax():
            exclude_types = settings.PROCESS_TYPE_MAPPING.get("RLSA") + settings.PROCESS_TYPE_MAPPING.get("Shopping Argos") + settings.PROCESS_TYPE_MAPPING.get("Shopping")
            if lead_status == 'In Queue':
                if process_type == 'TAG':
                    leads = Leads.objects.filter(lead_status=lead_status,
                            lead_owner_email=current_user_email,
                            is_delete=False).exclude(type_1__in=exclude_types)
                elif process_type == 'SHOPPING':
                    leads = Leads.objects.filter(lead_status=lead_status,
                            type_1__in = settings.PROCESS_TYPE_MAPPING.get("Shopping"),
                            lead_owner_email=current_user_email,is_delete=False)
                elif process_type == 'RLSA':
                    leads = Leads.objects.filter(lead_status=lead_status,
                            type_1__in = settings.PROCESS_TYPE_MAPPING.get("RLSA"),
                            lead_owner_email=current_user_email,is_delete=False)
                elif process_type == 'WPP':
                    leads = WPPLeads.objects.filter(lead_status=lead_status,
                            type_1__in = settings.PROCESS_TYPE_MAPPING.get("WPP"),
                            lead_owner_email=current_user_email,is_delete=False)
                elif process_type == 'Picasso Audits':
                    leads = PicassoLeads.objects.filter(lead_status=lead_status,
                            type_1__in = settings.PROCESS_TYPE_MAPPING.get("Picasso Audits"),
                            lead_owner_email=current_user_email,is_delete=False)
                else:
                    leads = Leads.objects.filter(lead_status=lead_status,
                            type_1__in = settings.PROCESS_TYPE_MAPPING.get("Shopping Argos"),
                            lead_owner_email=current_user_email,is_delete=False)
            elif lead_status == 'Without Appointment':
                if process_type == 'TAG':
                    leads = Leads.objects.filter(appointment_date__isnull=True,
                            lead_status='In Queue',lead_owner_email=current_user_email,
                            is_delete=False).exclude(type_1__in = exclude_types)
                elif process_type == 'SHOPPING':
                    leads = Leads.objects.filter(appointment_date__isnull=True,
                            lead_status='In Queue',
                            type_1__in = settings.PROCESS_TYPE_MAPPING.get("Shopping"),
                            lead_owner_email=current_user_email,is_delete=False)
                elif process_type == 'RLSA':
                    leads = Leads.objects.filter(appointment_date__isnull=True,
                            lead_status='In Queue',
                            type_1__in = settings.PROCESS_TYPE_MAPPING.get("RLSA"),
                            lead_owner_email=current_user_email,is_delete=False)
                elif process_type == 'WPP':
                    leads = WPPLeads.objects.filter(appointment_date__isnull=True,
                            lead_status='In Queue',
                            type_1__in = settings.PROCESS_TYPE_MAPPING.get("WPP"),
                            lead_owner_email=current_user_email,is_delete=False)
                elif process_type == 'Picasso Audits':
                    leads = list()
                else:
                    leads = Leads.objects.filter(appointment_date__isnull=True,
                            lead_status='In Queue',
                            type_1__in = settings.PROCESS_TYPE_MAPPING.get("Shopping Argos"),
                            lead_owner_email=current_user_email,is_delete=False)

            else:
                exclude_types = settings.PROCESS_TYPE_MAPPING.get("RLSA") + settings.PROCESS_TYPE_MAPPING.get("Shopping Argos") + settings.PROCESS_TYPE_MAPPING.get("Shopping")
                if process_type == 'TAG':
                    leads = Leads.objects.filter(appointment_date__isnull=False,
                            rescheduled_appointment__isnull=False,lead_status='In Progress',
                            lead_sub_status__in=['IP - CALL BACK',
                            'IP - Appointment Rescheduled - IS (GS)','IP - Code Sent'],
                            lead_owner_email=current_user_email,
                            is_delete=False).exclude(type_1__in = exclude_types)
                elif process_type == 'SHOPPING':
                    leads = Leads.objects.filter(appointment_date__isnull=False,
                            rescheduled_appointment__isnull=False,lead_status='In Progress',
                            lead_sub_status__in=['IP - CALL BACK',
                            'IP - Appointment Rescheduled - IS (GS)','IP - Code Sent'],
                            type_1__in = settings.PROCESS_TYPE_MAPPING.get("Shopping"),
                            lead_owner_email=current_user_email,is_delete=False)
                elif process_type == 'RLSA':
                    leads = Leads.objects.filter(appointment_date__isnull=False,
                            rescheduled_appointment__isnull=False,lead_status='In Progress',
                            lead_sub_status__in=['IP - CALL BACK',
                            'IP - Appointment Rescheduled - IS (GS)','IP - Code Sent'],
                            type_1__in = settings.PROCESS_TYPE_MAPPING.get("RLSA"),
                            lead_owner_email=current_user_email,is_delete=False)
                elif process_type == 'WPP':
                    leads = WPPLeads.objects.filter(appointment_date__isnull=False,
                            rescheduled_appointment__isnull=False,
                            lead_status='In Progress',
                            lead_sub_status__in=['IP - CALL BACK',
                            'IP - Appointment Rescheduled - IS (GS)','IP - Code Sent'],
                            type_1__in = settings.PROCESS_TYPE_MAPPING.get("WPP"),
                            lead_owner_email=current_user_email,is_delete=False)
                elif process_type == 'Picasso Audits':
                    leads = list()
                else:
                    leads = Leads.objects.filter(appointment_date__isnull=False,
                            rescheduled_appointment__isnull=False,
                            lead_status='In Progress',
                            lead_sub_status__in=['IP - CALL BACK',
                            'IP - Appointment Rescheduled - IS (GS)','IP - Code Sent'],
                            type_1__in = settings.PROCESS_TYPE_MAPPING.get("Shopping Argos"),
                            lead_owner_email=current_user_email,is_delete=False)
            return HttpResponse(json.dumps(get_json_leads(leads,process_type)), content_type="application/json")
        return render(request,'crm/lead_and_history.html')
    else:
        raise Http404


@login_required
def search_leads(request):
    search_query = request.GET.get('q')
    results = list()
    try:
        normal_leads = Leads.objects.values('customer_id', 'type_1', 'url_1', 'lead_status', 'id', 'sf_lead_id', 'lead_owner_name', 'date_of_installation').filter(
            Q(customer_id= search_query) | Q(sf_lead_id= search_query) ,is_delete=False )
        if normal_leads:
            for each in list(normal_leads):
                if each['type_1'] in ['Google Shopping Setup', 'Existing Datafeed Optimization','Google Shopping Migration', 'Project Argos- Feed Performance Optimization']:
                    each['process_type'] = 'Shopping'
                elif each['type_1'] in ['RLSA Bulk Implementation']:
                    each['process_type'] = 'RLSA'
                else:
                    each['process_type'] = 'TAG'
            results += list(normal_leads)
    except ObjectDoesNotExist:
        pass
    # try:
    #     picasso_leads = PicassoLeads.objects.values('customer_id', 'type_1', 'url_1', 'lead_status', 'id', 'sf_lead_id',  'lead_owner_name', 'date_of_installation').filter(
    #         Q(customer_id= search_query) | Q(sf_lead_id= search_query) ,is_delete=False)
    #     if picasso_leads:
    #         for each in list(picasso_leads):
    #             if each['type_1'] in ['BOLT']:
    #                 each['process_type'] = 'BOLT'
    #             else:
    #                 each['process_type'] = 'Picasso'
    #         results += list(picasso_leads)

    # except ObjectDoesNotExist:
    #     pass
    # try:
    #     wpp_leads = WPPLeads.objects.values('customer_id', 'type_1', 'url_1', 'lead_status', 'id', 'sf_lead_id' , 'lead_owner_name', 'date_of_installation').filter(Q(customer_id=search_query) | Q(sf_lead_id=search_query) ,is_delete=False)
    #     if wpp_leads:
    #         for each in list(wpp_leads):
    #             each['process_type'] = 'WPP'
    #         results += list(wpp_leads)
    # except ObjectDoesNotExist:
    #     pass

    return render(request, 'crm/search_result.html', {'returning_data': results,
                                                      'resultcount': len(results),
                                                      'q_id': search_query})


@login_required
def lead_details(request, lid, sf_lead_id, ctype):
    lead = None
    lead_detail = None
    lead_status = ''
    primary_role = []
    team_list = []
    language_list = []
    context = {}
    try:
        if ctype in ['TAG', 'Shopping', 'RLSA', 'ShoppingArgos']:
            try:
                lead = Leads.objects.get(id=lid, sf_lead_id=sf_lead_id)
                lead_status = settings.LEAD_STATUS
                feed_optimisation_status = settings.FEED_OPTIMISATION_STATUS
                primary_role = ['Owner', 'Marketing', 'Webmaster']
                language = Language.objects.filter(is_active=True)
                try:
                    team = Team.objects.filter(belongs_to__in=['TAG', 'TAG-WPP', 'TAG-PICASSO', 'ALL'])
                except ObjectDoesNotExist:
                    print "No teams with this filter parameters"
                pla_sub_status = settings.PLA_SUB_STATUS
                if lead.type_1 == 'Existing Datafeed Optimization':
                    pla_sub_status.remove('Existing Datafeed Optimization')
                implemented_code_list = ['Different / Alternate', 'Same as specified by the Google rep']
                team_list = []
                language_list = []
                for i in language:
                    language_list.append(str(i.language_name))
                for i in team:
                    team_list.append(str(i.team_name))
                    try:
                        lead_detail = TagLeadDetail.objects.get(lead_id=lead)
                    except:
                        lead_detail = TagLeadDetail()
                        lead_detail.lead_id = lead
                        lead_detail.save()
            except ObjectDoesNotExist:
                print "No lead with this Salesforce ID"
        elif ctype == 'WPP':
            try:
                lead = WPPLeads.objects.get(id=lid,sf_lead_id=sf_lead_id)
            except ObjectDoesNotExist:
                print "No WPP Lead with this Salesforce ID"
        else:
            try:
                lead = PicassoLeads.objects.get(id=lid,sf_lead_id=sf_lead_id)
            except ObjectDoesNotExist:
                print "No Picasso Lead with this Salesforce ID"

        context = {'lead':lead,'lead_detail':lead_detail,
                'status':lead_status,'role':primary_role,
                'language':language_list,'team':team_list,
                'ctype':ctype,
                'comment':lead.regalix_comment,
                'dail_num':len(lead.regalix_comment.split("Dail")) - 1,
                'name':request.user.first_name,
                'pla_sub_status':pla_sub_status,
                'implemented_code_list':implemented_code_list,
                'feed_optimisation_status':feed_optimisation_status,
                'success': True
                }

    except Exception as e:
        print e
        context['success'] = False

    if request.user.groups.filter(name='CRM-MANAGER'):
        context['manager'] = True
    else:
        context['manager'] = False
    return render(request, 'crm/lead_details.html',context)


@login_required
def lead_owner_avalibility(request):
    if request.user.groups.filter(name='CRM-MANAGER'):
        lead_owner = request.GET.get('lead_owner_email')
        lead_id = request.GET.get('id')
        lead_type = request.GET.get('type')

        user = User.objects.get(email=lead_owner)
        assignee_name = user.first_name + ' ' + user.last_name
        resp = {}
        assign = False

        if lead_type in ['Picasso','BOLT']:
            assign = True
        else:
            if request.GET.get('override_appointment', 'False') == 'True':
                assign = True
            if not assign and lead_type in ['WPP','Bolt Build','WPP - Nomination']:
                current_lead = WPPLeads.objects.get(id=lead_id)
                if not assign:
                    appointment_conflict = WPPLeads.objects.filter(
                        appointment_date_in_ist=current_lead.appointment_date_in_ist,
                        lead_owner_email=lead_owner)
                    assign = False if appointment_conflict else True
            elif not assign:
                current_lead = Leads.objects.get(id=lead_id)
                if current_lead.appointment_date_in_ist:
                    appointment_conflict = Leads.objects.filter(type_1=lead_type,lead_owner_email=lead_owner,
                            lead_status__in=['Attempting Contact','In Queue','ON CALL','In Progress'],
                            appointment_date_in_ist=current_lead.appointment_date_in_ist)
                    assign = False if appointment_conflict else True
                else:
                    assign = True
        if assign:
            # Store this action as part of history
            lh = LeadHistory()
            lh.lead_id = current_lead.id
            lh.modified_by = request.user.first_name + ' ' +request.user.last_name
            lh.action_type = 'owner_change'
            lh.previous_owner = current_lead.lead_owner_name
            lh.current_owner = lead_owner
            lh.save()
            # Assigning to the new owner
            current_lead.lead_owner_name = assignee_name
            current_lead.lead_owner_email = lead_owner
            current_lead.save()

            if request.GET.get('send_mail') == 'True':
                if lead_type in ['WPP','Bolt Build','WPP - Nomination']:
                    assigning_lead_info = WPPLeads.objects.values('id', 'sf_lead_id', 'customer_id','appointment_time_in_ist', 'code_1', 'type_1', 'phone', 'first_name', 'last_name', 'company', 'url_1').get(id=lead_id)
                    assigning_lead_info['process'] = 'WPP'
                else:
                    assigning_lead_info = Leads.objects.values('id', 'sf_lead_id', 'customer_id','appointment_date_in_ist', 'code_1', 'type_1', 'phone', 'first_name', 'last_name', 'company', 'url_1').get(id=lead_id)
                    assigning_lead_info['process'] = 'TAG'

                assigning_lead_info['lead_url'] = str(request.META['wsgi.url_scheme'])+"://"+str(request.META['HTTP_HOST'])+"/crm/lead-details/"+str(assigning_lead_info['id'])+"/"+str(assigning_lead_info['sf_lead_id'])+"/"+str(assigning_lead_info['process'])

                # Mail to assignee
                mail_subject = "New Lead Assigned to you - "+str(assigning_lead_info['customer_id'])
                mail_from = str(request.user.email)
                mail_to = request.GET.get('lead_owner_email')
                bcc = set([])
                attachments = list()
                mail_body = get_template('leads/email_templates/lead_assigning_mail.html').render(Context({'data':assigning_lead_info}))
                send_mail(mail_subject, mail_body, mail_from, mail_to, list(bcc), attachments, template_added=True)

                # Notification to manager
                mail_subject = "You Assigned Lead - "+str(assigning_lead_info['customer_id'])+" to "+str(current_lead.lead_owner_name)
                assigning_lead_info['assignee_name'] = str(current_lead.lead_owner_name)
                mail_to = request.user.email
                assigning_lead_info['manager'] =request.user.first_name + ' ' +request.user.last_name
                mail_body = get_template('leads/email_templates/lead_assigning_mail.html').render(Context({'data':assigning_lead_info}))
                send_mail(mail_subject, mail_body, mail_from, mail_to, list(bcc), attachments, template_added=True)
            resp['success'] = True
        else:
            resp['success'] = False
        resp['name'] = assignee_name
        resp['email'] = lead_owner
        return HttpResponse(json.dumps(resp))
    else:
        return HttpResponseForbidden()


@login_required
def get_crm_agents_emails(request):
    agents_email_list = list()
    search_keyword = request.GET.get('search_key')
    all_emails = User.objects.values('email').filter(email__icontains=search_keyword, groups__name__in=['CRM-AGENT', 'CRM-MANAGER'])[:20]
    for each in all_emails:
        agents_email_list.append(each['email'])
    response = {'data':agents_email_list}
    return HttpResponse(json.dumps(response))


@login_required
def delete_lead(request, lid, ctype):
    if request.user.groups.filter(name='CRM-MANAGER'):
        
        if ctype == "WPP":
            try:
                lead = WPPLeads.objects.get(id=lid)
                lead_cid = lead.customer_id
                lead.is_delete = True
                lead.save()
            except ObjectDoesNotExist, e:
                print "Cound not find lead object with the provided lead ID : ",lid, e

        elif ctype == "PicassoAudits":
            try:
                lead = PicassoLeads.objects.get(id=lid)
                lead_cid = lead.customer_id
                lead.is_delete = True
                lead.save()
            except ObjectDoesNotExist, e:
                print "Cound not find lead object with the provided lead ID : ",lid, e

        elif ctype == "RLSA" or "Shopping" or "ShoppingArgos" or "TAG":
            try:
                lead = Leads.objects.get(id=lid)
                lead_cid = lead.customer_id
                lead.is_delete = True
                lead.save()
            except ObjectDoesNotExist, e:
                print "Cound not find lead object with the provided lead ID : ",lid, e

        lh = LeadHistory()
        lh.lead_id = lead.pk
        lh.action_type = 'Deleted'
        lh.modified_by = request.user.first_name + ' ' +request.user.last_name
        lh.modifications = "This lead is Deleted by " + request.user.first_name + ' ' +request.user.last_name
        lh.save()

        return redirect(reverse("all-leads") + "?customer_id=" + lead_cid + "&ptype=" + ctype )
    else:
        raise PermissionDenied()


@login_required
@csrf_exempt
def clone_lead(request):
    process_type = request.POST.get('process_type')
    lead_id = request.POST.get('lead_id')
    if process_type in ['WPP']:
        obj = WPPLeads.objects.get(pk=lead_id)
        url = str(request.META['wsgi.url_scheme'])+"://"+str(request.META['HTTP_HOST'])+"/crm/lead-details/"+str(obj.id)+"/"+str(obj.sf_lead_id)+"/"+str(process_type)
        obj.pk = None
        obj.date_of_installation = None
        obj.sf_lead_id = get_unique_uuid(process_type)
        obj.lead_status = 'In Queue'
        obj.lead_owner_name = ''
        obj.lead_owner_email = ''
        obj.regalix_comment = ""
        obj.additional_notes = ""
        obj.first_contacted_on = None
        obj.lead_sub_status = None
        obj.dials = 0
        obj.created_date = datetime.now()
        obj.save()

        lh = LeadHistory()
        lh.lead_id = obj.pk
        lh.action_type = 'clone'
        lh.modified_by = request.user.first_name + ' ' +request.user.last_name
        lh.modifications = "This lead is cloned from <a href="+url+">"+str(obj.customer_id)+"</a>."
        lh.modified_by = request.user.first_name + ' ' +request.user.last_name
        lh.save()

        return HttpResponse(json.dumps({'process_type': process_type, 'sf_id':obj.sf_lead_id, 'id':obj.pk}), content_type="application/json")
    elif process_type in ['Picasso', 'BOLT']:
        obj = PicassoLeads.objects.get(pk=lead_id)
        url = str(request.META['wsgi.url_scheme'])+"://"+str(request.META['HTTP_HOST'])+"/crm/lead-details/"+str(obj.id)+"/"+str(obj.sf_lead_id)+"/"+str(process_type)
        obj.pk = None
        obj.date_of_installation = None
        obj.sf_lead_id = get_unique_uuid(process_type)
        obj.lead_status = 'In Queue'
        obj.lead_owner_name = ''
        obj.lead_owner_email = ''
        obj.regalix_comment = ""
        obj.additional_notes = ""
        obj.created_date = datetime.now()
        obj.save()

        lh = LeadHistory()
        lh.lead_id = obj.pk
        lh.action_type = 'clone'
        lh.modified_by = request.user.first_name + ' ' +request.user.last_name
        lh.modifications = "This lead is cloned from <a href="+url+">"+str(obj.customer_id)+"</a>."
        lh.modified_by = request.user.first_name + ' ' +request.user.last_name
        lh.save()

        return HttpResponse(json.dumps({'process_type': process_type, 'sf_id':obj.sf_lead_id, 'id':obj.pk}), content_type="application/json")
    elif process_type in ['TAG', 'Shopping', 'ShoppingArgos', 'RLSA']:
        obj = Leads.objects.get(pk=lead_id)
        url = str(request.META['wsgi.url_scheme'])+"://"+str(request.META['HTTP_HOST'])+"/crm/lead-details/"+str(obj.id)+"/"+str(obj.sf_lead_id)+"/"+str(process_type)
        obj.pk = None
        obj.date_of_installation = None
        obj.sf_lead_id = get_unique_uuid(process_type)
        obj.lead_status = 'In Queue'
        obj.lead_owner_name = ''
        obj.lead_owner_email = ''
        obj.regalix_comment = ""
        obj.first_contacted_on = None
        obj.appointment_date_in_ist = None
        obj.comment_1 = ""
        obj.code_1 = ""
        obj.dials = 0
        obj.created_date = datetime.now()
        obj.created_by = str(request.user.email)
        obj.save()
        
        lh = LeadHistory()
        lh.lead_id = obj.pk
        lh.action_type = 'clone'
        lh.modified_by = request.user.first_name + ' ' +request.user.last_name
        lh.modifications = "This lead is cloned from <a href="+url+">"+str(obj.customer_id)+"</a>."
        lh.modified_by = request.user.first_name + ' ' +request.user.last_name
        lh.save()

        return HttpResponse(json.dumps({'process_type': process_type, 'sf_id':obj.sf_lead_id, 'id':obj.pk}), content_type="application/json")
    else:
        response = {'msg':'Failed to clone'}
        return HttpResponse(json.dumps(response),content_type='application/json')


@login_required
def save_image_file(request):
    lh = LeadHistory()
    if request.FILES.getlist('file'):
        img_files = request.FILES.getlist('file')

        if not os.path.isdir(settings.MEDIA_ROOT):
            os.makedirs(settings.MEDIA_ROOT)

        for img_file in img_files:
            lh = LeadHistory()
            original_file_name, file_extension = img_file.name.split(".")
            new_file_name = str(uuid.uuid4()) + "." + file_extension

            file_path = os.path.join(settings.MEDIA_ROOT,new_file_name)
            try:
                save_file(img_file, file_path)
                response = {'msg':'Image uploaded successfully','success':True}
            except:
                response = {'msg':'Failed to upload image, please try after sometime.','success':False}
            lh.original_image_name = img_file.name
            lh.image_guid = new_file_name
            lh.action_type = 'image'
            lh.lead_id = request.POST['lead_id']
            lh.modified_by = request.user.first_name + ' ' +request.user.last_name
            '''
                update file_path and file.name as Original File name in the DB
            '''
            lh.save()
    else:
        lh.image_link = request.POST.get('image_link')
        lh.action_type = 'image_link'
        response = {'msg':'Link added successfully' ,'success':True}
        lh.lead_id = request.POST['lead_id']
        lh.modified_by = request.user.first_name + ' ' +request.user.last_name
        lh.save()
    return HttpResponse(json.dumps(response),content_type="application/json")


@login_required
def get_lead_history(request):
    lead_id = request.GET.get('lead_id')
    lead_history_list = list()
    if lead_id:
        leads = LeadHistory.objects.filter(lead_id=lead_id).order_by('-modified_date')
        local_tz = pytz.timezone('Asia/Calcutta')
        for lead in leads:
            created_date = pytz.utc.localize(lead.created_date)
            created_date = created_date.astimezone(local_tz)           
            lead_history_dict = {
                'lead_id':lead.lead_id,
                'modified_by':lead.modified_by,
                'action_type':lead.action_type,
                'modifications':lead.modifications,
                'image_link':lead.image_link,
                'image_guid':lead.image_guid,
                'original_image_name':lead.original_image_name,
                'previous_owner':lead.previous_owner,
                'current_owner':lead.current_owner,
                'image_path':"/media/"+lead.image_guid if lead.image_guid else '',
                'image_size':round(float(os.path.getsize(os.path.join(settings.MEDIA_ROOT,lead.image_guid))) /(1024*1024),2) if lead.image_guid else '',
                'created_date':datetime.strftime(created_date, "%d-%m-%Y %I:%M %P"),
            }
            lead_history_list.append(lead_history_dict)
        return HttpResponse(json.dumps(lead_history_list),content_type='application/json')
    else:
        return HttpResponse(json.dumps([]), content_type='application/json')


@login_required
def download_image_file(request):
    lead = LeadHistory.objects.get(image_guid=request.GET.get('image_guid'))
    image_path = os.path.join(settings.MEDIA_ROOT,lead.image_guid)
    mimetype, encoding = mimetypes.guess_type(image_path)
    response = HttpResponse(content_type=mimetype)
    response['Content-Disposition'] = 'attachment; filename=%s' % lead.original_image_name
    response.write(file(image_path, "rb").read())
    return response


@login_required
@csrf_exempt
def update_lead(request):
    resp = {}
    if request.method == 'POST':
        data = ast.literal_eval(json.dumps(request.POST))
        lead_fields = settings.LEAD_FIELDS
        lead_details_fields = settings.TAGLEAD_DETAILS_FIELDS
        lead_dict = {}
        lead_detail_dict = {}

        lh = LeadHistory()
        #lh.lead_id = lead.id
        edited_list = []
        edited_dict = {}

        for key,val in data.items():
            if key in lead_fields:
                lead_dict[key] = val

        for key,val in data.items():
            if key in lead_details_fields:
                lead_detail_dict[key] = val

        try:
            lead = Leads.objects.get(sf_lead_id=lead_dict['sf_lead_id'])
            lh.lead_id = lead.id
            l_dict =  model_to_dict(lead)
            for key,val in lead_dict.items():
                if key != 'sf_lead_id':
                    edited_dict[key] = [l_dict[key] if l_dict[key] != 'None' or l_dict[key] != 'null' else '',val]

            if data.get('installation_date'):
                temp_date_of_installation = data['installation_date'].replace('.','').replace('-','/')
                edited_dict['installation_date'] = [datetime.strftime(lead.date_of_installation, '%d-%m-%Y %I:%M %p') if lead.date_of_installation else '',data['installation_date'].replace('.','').replace('/','-')]
                lead.date_of_installation = datetime.strptime(str(temp_date_of_installation), '%d/%m/%Y %I:%M %p')
            if data.get('appointment_date_on'):
                temp_appointment_date_on = data['appointment_date_on'].replace('.','').replace('-','/')
                edited_dict['appointment_date_on'] = [datetime.strftime(lead.appointment_date, '%d-%m-%Y %I:%M %p') if lead.appointment_date else '',data['appointment_date_on'].replace('.','').replace('/','-')]
                lead.appointment_date = datetime.strptime(str(temp_appointment_date_on), '%d/%m/%Y %I:%M %p')
            if data.get('rescheduled_date_on'):
                temp_rescheduled_date_on = data['rescheduled_date_on'].replace('.','').replace('-','/')
                edited_dict['rescheduled_date_on'] = [datetime.strftime(lead.rescheduled_appointment, '%d-%m-%Y %I:%M %p') if lead.rescheduled_appointment else '',data['rescheduled_date_on'].replace('.','').replace('/','-')]
                lead.rescheduled_appointment = datetime.strptime(str(temp_rescheduled_date_on), '%d/%m/%Y %I:%M %p')
            if data.get('first_contacted'):
                temp_first_contacted_on = data['first_contacted'].replace('.','').replace('-','/')           
                edited_dict['first_contacted'] = [datetime.strftime(lead.first_contacted_on, '%d-%m-%Y %I:%M %p') if lead.first_contacted_on else '',data['first_contacted'].replace('.','').replace('/','-')]
                lead.first_contacted_on = datetime.strptime(str(temp_first_contacted_on), '%d/%m/%Y %I:%M %p')
            if data.get('lead_status') in ['In Queue','Implemented','ON CALL']:
                lead.lead_sub_status = ''

            if data.get('feed_optimisation_status') == 'None':
                lead.feed_optimisation_sub_status = None

            lead.regalix_comment += data.get('reg_comment')

            if data.get('grep_email'):
                try:
                    google_user = User.objects.get(email=data.get('grep_email'))
                    lead.google_rep_name = google_user.first_name + ' ' + google_user.last_name
                    lead.google_rep_email = google_user.email
                except ObjectDoesNotExist:
                    print "no user with this mail ID"

            if data.get('grep_manager_email'):
                try:
                    google_user = User.objects.get(email=data.get('grep_manager_email'))
                    lead.google_rep_manager_name = google_user.first_name + ' ' + google_user.last_name
                    lead.google_rep_manager_email = google_user.email
                except ObjectDoesNotExist:
                    print "no user with this mail ID"

            # mail function on lead status change
            if str(data.get('lead_status')) in ["In Queue", "Attempting Contact", "In Progress", "In Active","Implemented", "ON CALL", "Pending QC - WIN", "Pending QC - In Active", "Rework Required - In Active", "Pending QC - Dead Lead", "Rework Fixed - Win", "Rework Fixed - In Active"]:

                if lead.type_1 in ['Google Shopping Setup', 'Existing Datafeed Optimization','Google Shopping Migration', 'Project Argos- Feed Performance Optimization']:
                    process_type = "Shopping"
                elif lead.type_1 in ['RLSA', 'rlsa', 'RLSA Bulk Implementation']:
                    process_type = "RLSA"
                else:
                    process_type = "TAG"

                mail_subject = "Lead status has been changed ("+str(lead.customer_id)+" - "+process_type+")"
                mail_from = 'Lead Status Changed <google@regalix-inc.com>'
                crm_managers_mails = User.objects.values_list('email').filter(groups__name='CRM-MANAGER')
                mail_to = list()
                for mail_id in crm_managers_mails:
                    mail_to.append(mail_id)
                bcc = set([])
                attachments = list()
                mail_body = get_template('leads/email_templates/lead_status_changed_mail.html').render(Context({
                    'url':str(request.META['wsgi.url_scheme'])+"://"+str(request.META['HTTP_HOST'])+"/crm/lead-details/"+str(lead.id)+"/"+str(lead.sf_lead_id)+"/TAG",
                    'lead_status': data['lead_status'],
                    'prev_lead_status':data['prev_lead_status']}))
                send_mail(mail_subject, mail_body, mail_from, mail_to, list(bcc), attachments, template_added=True)

            lead.save()
            lead = Leads.objects.filter(sf_lead_id=request.POST.get('sf_lead_id')).update(**lead_dict)
            try:
                temp = Leads.objects.filter(sf_lead_id=request.POST.get('sf_lead_id'))
                lead_detail = TagLeadDetail.objects.get(lead_id=temp)

                l_detail_dict =  model_to_dict(lead_detail)

                for key,val in lead_detail_dict.items():
                    edited_dict[key] = [l_detail_dict[key] if l_detail_dict[key] != 'None' or l_detail_dict[key] != 'null' else '',val]

                if data.get('qc_on_date'):
                    temp_qc_on = data['qc_on_date'].replace('.','').replace('-','/')
                    edited_dict['qc_on_date'] = [datetime.strftime(lead_detail.qc_on, '%d-%m-%Y %I:%M %p') if lead_detail.qc_on else '',data['qc_on_date'].replace('.','').replace('/','-')]
                    lead_detail.qc_on = datetime.strptime(str(temp_qc_on), '%d/%m/%Y %I:%M %p')

                if data.get('last_contacted_date'):
                    temp_last_call_time = data['last_contacted_date'].replace('.','').replace('-','/')
                    edited_dict['last_contacted_date'] = [datetime.strftime(lead.last_contacted_on, '%d-%m-%Y %I:%M %p') if lead_detail.last_contacted_on else '',data['last_contacted_date'].replace('.','').replace('/','-')]
                    lead_detail.last_contacted_on = datetime.strptime(str(temp_last_call_time), '%d/%m/%Y %I:%M %p')

                if data.get('call_win'):
                    temp_call_win = data['call_win'].replace('.','').replace('-','/')
                    edited_dict['call_win'] = [datetime.strftime(lead.on_call_win, '%d-%m-%Y %I:%M %p') if lead_detail.on_call_win else '',data['call_win'].replace('.','').replace('/','-')]
                    lead_detail.on_call_win = datetime.strptime(str(temp_call_win), '%d/%m/%Y %I:%M %p')

                if data.get('qc_exception_date'):
                    temp_qc_exception = data['qc_exception_date'].replace('.','').replace('-','/')
                    edited_dict['qc_exception_date'] = [datetime.strftime(lead.qc_exception, '%d-%m-%Y %I:%M %p') if lead_detail.qc_exception else '',data['qc_exception_date'].replace('.','').replace('/','-')]
                    lead_detail.qc_exception = datetime.strptime(str(temp_qc_exception), '%d/%m/%Y %I:%M %p')

                edited_list.append(edited_dict)
                if edited_dict:
                    lh.action_type = 'edited'
                    lh.modified_by = request.user.first_name + ' ' +request.user.last_name
                    lh.modifications = json.dumps(edited_list)
                    lh.save()

                lead_detail.save()

                lead_detail = TagLeadDetail.objects.filter(lead_id=temp).update(**lead_detail_dict)
            except Exception as e:
                print e

            resp['success'] = True
        except Exception as e:
            print e
            resp['success'] = False
    return HttpResponse(json.dumps(resp),content_type='application/json')


@login_required
@csrf_exempt
def add_lead_comment(request):
    # import ipdb; ipdb.set_trace()
    resp = {}
    if request.method == 'POST':
        data = request.POST
        try:
            lead = Leads.objects.get(id=data['id'])
            lead.regalix_comment += data['regalix_comment']
            lead.save()
            resp['regalix_comment'] = lead.regalix_comment
            resp['success'] = True
        except:
            resp['success'] = False
    return HttpResponse(json.dumps(resp))


@login_required
def get_lead_sub_status(request):
    if request.method == 'GET':
        ctype = request.GET.get('ctype')
        lead_status = request.GET.get('lead_status')
        lead_status = lead_status.replace('%20',' ')
        lead_sub_status = None
        if ctype in ['TAG','Shopping','RLSA','ShoppingArgos']:
            if lead_status == 'Attempting Contact':
                lead_sub_status = settings.LEAD_STATUS_SUB_STATUS_MAPPING[ctype]["Attempting Contact"]
            elif lead_status == 'In Progress':
                lead_sub_status = settings.LEAD_STATUS_SUB_STATUS_MAPPING[ctype]["In Progress"]
            elif lead_status == 'Pending QC - In Active':
                lead_sub_status = settings.LEAD_STATUS_SUB_STATUS_MAPPING[ctype]["Pending QC - In Active"]
            elif lead_status == 'Pending QC - WIN':
                lead_sub_status = settings.LEAD_STATUS_SUB_STATUS_MAPPING[ctype]["Pending QC - WIN/Implemented"] = ["Imp - 1 Conversion", "Imp - 1 Impression"]
            elif lead_status == 'Rework Required - In Active':
                lead_sub_status = settings.LEAD_STATUS_SUB_STATUS_MAPPING[ctype]["Rework Required - Inactive"]= ["Rework Required - Inactive"]
            elif lead_status == "Rework Fixed - Win":
                lead_sub_status = settings.LEAD_STATUS_SUB_STATUS_MAPPING[ctype]["Rework Fixed - Win"] =["Rework Fixed - Win"]
            elif lead_status == "Rework Fixed - In Active":
                lead_sub_status = settings.LEAD_STATUS_SUB_STATUS_MAPPING[ctype]["Rework Fixed - Inactive"] =["Rework Fixed - Inactive"]
            elif lead_status == "In Active":
                lead_sub_status = settings.LEAD_STATUS_SUB_STATUS_MAPPING[ctype]["Inactive"] = ["Inactive"]
            elif lead_status == "Pending QC - Dead Lead":
                lead_sub_status = settings.LEAD_STATUS_SUB_STATUS_MAPPING[ctype]["Pending QC - Dead Lead"] = ["Pending QC - Dead Lead"]
    resp = {'success':True,'lead_sub_status':lead_sub_status}
    return HttpResponse(json.dumps(resp),content_type='application/json')


@login_required
def get_feed_optimisation_sub_status(request):
    if request.method == 'GET':
        feed_optimisation_status = request.GET.get('feed_optimisation_status')
        feed_optimisation_status = feed_optimisation_status.replace('%20',' ')
        feed_optimisation_sub_status = None
        if feed_optimisation_status == 'Feed Audit':
            feed_optimisation_sub_status = settings.FEED_OPTIMISATION_SUB_STATUS[feed_optimisation_status]
        elif feed_optimisation_status == 'Feed Optimization':
            feed_optimisation_sub_status = settings.FEED_OPTIMISATION_SUB_STATUS[feed_optimisation_status]
        elif feed_optimisation_status == 'Feed Testing':
            feed_optimisation_sub_status = settings.FEED_OPTIMISATION_SUB_STATUS[feed_optimisation_status]
        elif feed_optimisation_status == 'Feed Upload':
            feed_optimisation_sub_status = settings.FEED_OPTIMISATION_SUB_STATUS[feed_optimisation_status]
        elif feed_optimisation_status == 'Implementation':
            feed_optimisation_sub_status = settings.FEED_OPTIMISATION_SUB_STATUS[feed_optimisation_status]
        elif feed_optimisation_status == "Rework":
            feed_optimisation_sub_status = settings.FEED_OPTIMISATION_SUB_STATUS[feed_optimisation_status]
        elif feed_optimisation_status == "Inactive":
            feed_optimisation_sub_status = settings.FEED_OPTIMISATION_SUB_STATUS[feed_optimisation_status]
    resp = {'success':True,'feed_optimisation_sub_status':feed_optimisation_sub_status}
    return HttpResponse(json.dumps(resp), content_type='application/json')


@login_required
def user_appointmnets(request): 
    if request.user.groups.filter(name='CRM-AGENT'):
        response = list()
        user_appointment_leads = Leads.objects.values('customer_id','appointment_date_in_ist', 'rescheduled_appointment_in_ist').filter( lead_owner_email=request.user.email,lead_status__in=['In Queue'])
        for appointment in user_appointment_leads:
            data = dict()
            appointment_date = None
            if appointment['appointment_date_in_ist'] or appointment['rescheduled_appointment_in_ist']:
                if appointment['rescheduled_appointment_in_ist']:
                    appointment_date = datetime.strptime(str(appointment['rescheduled_appointment_in_ist']), '%Y-%m-%d %H:%M:%S')
                else:
                    appointment_date = datetime.strptime(str(appointment['appointment_date_in_ist']), '%Y-%m-%d %H:%M:%S')
            
            data['customer_id'] = appointment['customer_id']
            data['appointment_time'] = str(appointment_date) if appointment_date else ""
            response.append(data)
        return HttpResponse(json.dumps(response), content_type='application/json')
    else:
        return HttpResponse(json.dumps([]), content_type='application/json')


@login_required
def deleted_leads(request):
    if request.user.groups.filter(name='CRM-MANAGER'):
        if request.is_ajax():
            limit = int(request.GET.get('limit', 10))
            on_page = int(request.GET.get('page', 1))
            process_type = request.GET.get('process_name', 'TAG')
            if on_page <= 1:
                offset = 0
            else:
                on_page -= 1;
                offset = limit * on_page
                limit = offset + limit  
            
            try:
                if process_type == "Shopping":
                    all_leads = Leads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("Shopping"),is_delete=True ).values(
                                'id','customer_id', 'company', 'sf_lead_id', 'first_name', 'last_name','url_1','appointment_date_in_ist','is_delete')
                    leads = list(all_leads[offset:limit])
                    leads_count =  all_leads.count()
                    return HttpResponse(json.dumps({'leads_list': leads, 'leads_count':leads_count, 'success':True, 'process_type':'Shopping'}), content_type="application/json")
                elif process_type ==  "RLSA":
                    all_leads = Leads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("RLSA"),is_delete=True).values(
                                'id','customer_id', 'company', 'sf_lead_id', 'first_name', 'last_name','url_1','appointment_date_in_ist','is_delete')
                    leads = list(all_leads[offset:limit])
                    leads_count =  all_leads.count()
                    return HttpResponse(json.dumps({'leads_list': leads, 'leads_count':leads_count, 'success':True, 'process_type':'RLSA'}), content_type="application/json")
                elif  process_type ==  "ShoppingArgos":
                    all_leads = Leads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("Shopping Argos"),is_delete=True).values(
                                'id','customer_id', 'company', 'sf_lead_id', 'first_name', 'last_name','url_1','appointment_date_in_ist','is_delete')
                    leads = list(all_leads[offset:limit])
                    leads_count =  all_leads.count()
                    return HttpResponse(json.dumps({'leads_list': leads, 'leads_count':leads_count, 'success':True, 'process_type':'ShoppingArgos'}), content_type="application/json")
                else:
                    exclude_types = settings.PROCESS_TYPE_MAPPING.get("RLSA") + settings.PROCESS_TYPE_MAPPING.get("Shopping Argos") + settings.PROCESS_TYPE_MAPPING.get("Shopping")
                    all_leads = Leads.objects.filter(is_delete=True).exclude(type_1__in = exclude_types).values('id','customer_id', 'company', 'first_name', 'sf_lead_id', 'last_name','url_1','appointment_date_in_ist','is_delete')
                    leads = list(all_leads[offset:limit])
                    leads_count =  all_leads.count()
                    return HttpResponse(json.dumps({'leads_list': leads, 'leads_count':leads_count, 'success':True, 'process_type':'TAG'}), content_type="application/json")
            except Object.DoesNotExist:
                return HttpResponse(json.dumps({'msg':'Server error occurred. Please try again later.', 'success':False}), content_type="application/json")
                    
        return render(request, 'crm/deleted_leads.html', {'crm_manager_text': json.dumps(settings.LEAD_STATUS_SUB_STATUS_MAPPING) })
    else:
        raise exceptions.PermissionDenied


@login_required
@csrf_exempt
def restore_lead(request):
    lead_id = request.POST.get('lead_id')
    try:
        lead = Leads.objects.get(id=lead_id)
        lead.is_delete = False
        lead.save()
        
        lh = LeadHistory()
        lh.lead_id = lead.pk
        lh.action_type = 'Restored'
        lh.modified_by = request.user.first_name + ' ' +request.user.last_name
        lh.modifications = "This lead is Restored by " + request.user.first_name + ' ' +request.user.last_name
        lh.save()

        return HttpResponse(json.dumps({'msg':'Successfully Restored lead', 'success':True}), content_type="application/json")
    except ObjectDoesNotExist:
        return HttpResponse(json.dumps({'msg':'Failed to Restore', 'success':False}),content_type='application/json')


def export_filtered_leads(leads,is_agent):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="export_leads.csv"'
    response.write(u'\ufeff'.encode('utf8'))
    writer = csv.writer(response)
    if is_agent:
        header_fields = ['CID', 'Company', 'Customer Name', 'Created Date', 'Appointment time', 'Phone No', 
                        'Additional Ph No', 'Web Master No.', 'Location']
    else:
        header_fields = ['CID', 'Company', 'Customer Name', 'Created Date', 'Appointment time',
                        'Phone No', 'Additional Ph No', 'Web Master No.', 'Location', 
                        'Process Type']
    writer.writerow(header_fields) 
    if leads:
        if is_agent:  
            for lead in leads:
                writer.writerow([lead['customer_id'].encode('utf-8'),lead['company'].encode('utf-8'),
                                lead['customer_name'].encode('utf-8'),
                                lead['created_date'].encode('utf-8'),
                                lead['appointment_time'].encode('utf-8'),
                                lead['phone'].encode('utf-8'),
                                lead['phone_optional'].encode('utf-8'),
                                lead['web_master_no'].encode('utf-8'),
                                lead['location'].encode('utf-8')])

        else:
            for lead in leads:
                writer.writerow([lead['c_id'].encode('utf-8'), lead['company'].encode('utf-8'),
                                lead['customer_name'].encode('utf-8'), 
                                lead['created_date'].encode('utf-8'),
                                lead['appointment_time'].encode('utf-8') if lead['appointment_time']  else lead['appointment_time'],
                                lead['phone_number'].encode('utf-8'),
                                lead['additional_phone_number'].encode('utf-8'),
                                lead['web_master_number'].encode('utf-8'), 
                                lead['location'].encode('utf-8'),lead['type_1'].encode('utf-8')])
    return response   


def get_export_leads_based_on_appointment_manager(process_type,lead_appointment,limit,offset,has_region,loc_list,start_date_time,end_date_time, start_date, end_date, download_csv):
    if has_region:
        if lead_appointment == 'Without Appointment':

            query = {'country__in':loc_list, 'appointment_date__isnull':True, 'is_delete':False}

            if start_date and end_date:
                query.update({'created_date__gte':start_date, 'created_date__lt':end_date})
            
        elif lead_appointment != 'Select' or 'Without Appointment':

            query = {'country__in':loc_list, 'appointment_date_in_ist__gte':start_date_time, 
                    'appointment_date_in_ist__lte':end_date_time,
                    # 'rescheduled_appointment_in_ist__gte':start_date_time,
                    # 'rescheduled_appointment_in_ist__lte':end_date_time, 
                    'is_delete':False
                    }

            if start_date and end_date:
                query.update({'created_date__gte':start_date, 'created_date__lt':end_date})
            
        else:

            query = {'country__in':loc_list, 'is_delete':False}

            if start_date and end_date:
                query.update({'created_date__gte':start_date, 'created_date__lt':end_date})
            
    else:
        if lead_appointment == 'Without Appointment':

            query = {'appointment_date__isnull':True, 'is_delete':False}

            if start_date and end_date:
                query.update({'created_date__gte':start_date, 'created_date__lt':end_date})
                
        elif lead_appointment != 'Select' or 'Without Appointment':
            query = {'appointment_date_in_ist__gte':start_date_time,
                'appointment_date_in_ist__lte':end_date_time,
                # 'rescheduled_appointment_in_ist__gte':start_date_time,
                # 'rescheduled_appointment_in_ist__lte':end_date_time, 
                'is_delete':False,
            }
            if start_date and end_date:
                query.update({'created_date__gte':start_date, 'created_date__lt':end_date})
        else:
            query = {}

    if process_type == "WPP":
        leads = WPPLeads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("WPP"), **query).values(
            'id', 'sf_lead_id','customer_id', 'company', 'first_name', 'created_date','appointment_date', 'phone', 'phone_optional', 'country','type_1'
            )
        leads_count = WPPLeads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("WPP"), **query).count()
        
    elif process_type == "Picasso Audits":

        if loc_list:

            query = {'country__in':loc_list, 'is_delete':False}
            if start_date and end_date:
                query.update({'created_date__gte':start_date, 'created_date__lt':end_date})

        else:
            query = {}

        leads = PicassoLeads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("Picasso Audits"), **query).values(
            'id', 'sf_lead_id','customer_id', 'company', 'first_name', 'created_date', 'phone', 'country','type_1')
        leads_count = PicassoLeads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("Picasso Audits"), **query).count()

    elif process_type == "RLSA":

        leads = Leads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("RLSA"), **query).values(
            'id', 'sf_lead_id','customer_id', 'company', 'first_name', 'created_date', 'appointment_date_in_ist', 'phone', 'phone_optional', 'country','type_1'
            ).order_by('-created_date')

        leads_count = Leads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("RLSA"), **query).count()
        
    elif process_type == "Shopping":
        leads = Leads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("Shopping"), **query).values(
            'id', 'sf_lead_id','customer_id', 'company', 'first_name', 'created_date', 'appointment_date_in_ist', 'phone', 'phone_optional', 'country','type_1'
            )
        leads_count = Leads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("Shopping"), **query).count()
        
    elif process_type == "ShoppingArgos":
        leads = Leads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("Shopping Argos"), **query).values(
            'id', 'sf_lead_id','customer_id', 'company', 'first_name', 'created_date', 'appointment_date_in_ist', 'phone', 'phone_optional', 'country','type_1'
            )
        leads_count = Leads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("Shopping Argos"), **query).count()
        
    elif process_type == "tag_and_shopping":
        exclude_types = settings.PROCESS_TYPE_MAPPING.get("RLSA")
        leads = Leads.objects.filter(**query).exclude(type_1__in = exclude_types).values('id', 'sf_lead_id','customer_id', 'company', 'first_name', 'created_date',  'appointment_date_in_ist', 'phone', 'phone_optional', 'country','type_1'
            )
        leads_count = Leads.objects.filter(**query).exclude(type_1__in = exclude_types).count()
                    
    else: # Tag

        exclude_types = settings.PROCESS_TYPE_MAPPING.get("RLSA") + settings.PROCESS_TYPE_MAPPING.get("Shopping Argos") + settings.PROCESS_TYPE_MAPPING.get("Shopping")

        leads = Leads.objects.filter(**query).exclude(type_1__in = exclude_types).values('id', 'sf_lead_id','customer_id', 'company', 'first_name', 'created_date',  'appointment_date_in_ist', 'phone', 'phone_optional', 'country','type_1'
            )
        leads_count = Leads.objects.filter(**query).exclude(type_1__in = exclude_types).count()

    return leads,leads_count


def get_export_leads_no_appointment_manager(lead_status,lead_sub_status,has_region,loc_list,start_date,end_date,process_type,offset,limit):
    if lead_status == lead_sub_status:
        if has_region:

            query = {'lead_status': lead_status, 'country__in':loc_list, 'is_delete':False}

            if start_date and end_date:
                query.update({'created_date__gte':start_date, 'created_date__lt':end_date})
         
        else:

            query = {'lead_status': lead_status, 'is_delete':False}

            if start_date and end_date:
                query.update({'created_date__gte':start_date, 'created_date__gte':start_date, 'created_date__lt':end_date})
            
                
    else:
        if has_region:

            query = {'lead_status' : lead_status,'lead_sub_status' :lead_sub_status,
            'country__in':loc_list, 'is_delete':False}

            if start_date and end_date:
                query.update({'created_date__gte':start_date, 'created_date__gte':start_date, 'created_date__lt':end_date})

        else:

            query = {'lead_status' : lead_status,'lead_sub_status' :lead_sub_status, 'is_delete':False}

            if start_date and end_date:
                query.update({'created_date__gte':start_date, 'created_date__lt':end_date})

    if process_type == "WPP":

        leads = WPPLeads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("WPP"), **query).values(
            'id', 'sf_lead_id','customer_id', 'company', 'first_name', 'created_date','appointment_date', 'phone', 'phone_optional', 'country','type_1'
            )
        leads_count = WPPLeads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("WPP"), **query).count()

    elif process_type == "Picasso Audits":

        if loc_list:

            query = {'lead_status': lead_status, 'country__in':loc_list, 'is_delete':False}
            if start_date and end_date:
                query.update({'created_date__gte':start_date, 'created_date__lt':end_date})

        else:
            
            query = {'lead_status': lead_status, 'is_delete':False}
            if start_date and end_date:
                query.update({'created_date__gte':start_date, 'created_date__lt':end_date})

        leads = PicassoLeads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("Picasso Audits"), **query).values(
            'id', 'sf_lead_id','customer_id', 'company', 'first_name', 'created_date', 'phone', 'country','type_1')
        leads_count = PicassoLeads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("Picasso Audits"), **query).count()

    elif process_type == "RLSA":

        leads = Leads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("RLSA"), **query).values(
            'id', 'sf_lead_id','customer_id', 'company', 'first_name', 'created_date', 'appointment_date_in_ist', 'phone', 'phone_optional', 'country','type_1'
            ).order_by('-created_date')

        leads_count = Leads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("RLSA"), **query).count()

    elif process_type == "Shopping":

        leads = Leads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("Shopping"), **query).values(
            'id', 'sf_lead_id','customer_id', 'company', 'first_name', 'created_date', 'appointment_date_in_ist', 'phone', 'phone_optional', 'country','type_1'
            )
        leads_count = Leads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("Shopping"), **query).count()

    elif process_type == "ShoppingArgos":
        leads = Leads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("Shopping Argos"), **query).values(
            'id', 'sf_lead_id','customer_id', 'company', 'first_name', 'created_date', 'appointment_date_in_ist', 'phone', 'phone_optional', 'country','type_1'
            )[offset:limit]
        leads_count = Leads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("Shopping Argos"), **query).count()
        
    elif process_type == "tag_and_shopping":

        if query['lead_status'].startswith('TAG'):
            query['lead_status'] = query['lead_status'].replace("TAG",'').strip()
            exclude_types = settings.PROCESS_TYPE_MAPPING.get("RLSA") + settings.PROCESS_TYPE_MAPPING.get("Shopping Argos") + settings.PROCESS_TYPE_MAPPING.get("Shopping")
            leads = Leads.objects.filter(**query).exclude(type_1__in = exclude_types).values('id', 'sf_lead_id','customer_id', 'company', 'first_name', 'created_date',  'appointment_date_in_ist', 'phone', 'phone_optional', 'country','type_1'
                )
            leads_count = Leads.objects.filter(**query).exclude(type_1__in = exclude_types).count()
            
        elif query['lead_status'].startswith('Shopping'):
            query['lead_status'] = query['lead_status'].replace("Shopping",'').strip()
            leads = Leads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("Shopping"), **query).values(
            'id', 'sf_lead_id','customer_id', 'company', 'first_name', 'created_date', 'appointment_date_in_ist', 'phone', 'phone_optional', 'country','type_1'
            )[offset:limit]
            leads_count = Leads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("Shopping"), **query).count()
            
        else:
            query['lead_status'] = query['lead_status']
            exclude_types = settings.PROCESS_TYPE_MAPPING.get("RLSA")
            leads = Leads.objects.filter(**query).exclude(type_1__in = exclude_types).values('id', 'sf_lead_id','customer_id', 'company', 'first_name', 'created_date',  'appointment_date_in_ist', 'phone', 'phone_optional', 'country', 
                'type_1')
            leads_count = Leads.objects.filter(**query).exclude(type_1__in = exclude_types).count()
            
    else: # Tag
        exclude_types = settings.PROCESS_TYPE_MAPPING.get("RLSA") + settings.PROCESS_TYPE_MAPPING.get("Shopping Argos") + settings.PROCESS_TYPE_MAPPING.get("Shopping")
        leads = Leads.objects.filter(**query).exclude(type_1__in = exclude_types).values('id', 'sf_lead_id','customer_id', 'company', 'first_name', 'created_date',  'appointment_date_in_ist', 'phone', 'phone_optional', 'country','type_1'
            )
        leads_count = Leads.objects.filter(**query).exclude(type_1__in = exclude_types).count()

    return leads, leads_count


def get_export_leads_based_on_appointment_agent(lead_appointment,start_date,end_date,current_user_email):
    if lead_appointment == 'Without Appointment':
        exclude_types = settings.PROCESS_TYPE_MAPPING.get("RLSA") + settings.PROCESS_TYPE_MAPPING.get("Shopping Argos") + settings.PROCESS_TYPE_MAPPING.get("Shopping")
        query = {'appointment_date__isnull':True,'lead_status':'In Queue',
                'lead_owner_email':current_user_email,
                'is_delete':False}
        if start_date and end_date:
            query.update({'created_date__gte':start_date,'created_date__lte':end_date})
        leads = Leads.objects.filter(**query).exclude(type_1__in=exclude_types)
           
    else:
        query = {'lead_status__in':['Attempting Contact','In Queue'], 
                'appointment_date_in_ist__gte':start_date_time,
                'appointment_date_in_ist__lte':end_date_time,
                'rescheduled_appointment_in_ist__gte':start_date_time,
                'rescheduled_appointment_in_ist__lte':end_date_time,
                'lead_owner_email':current_user_email,'is_delete':False}
        if start_date and end_date:
            query.update({'created_date__gte':start_date,'created_date__lte':end_date})
        leads = Leads.objects.filter(**query)

    leads_count = leads.count()
    return leads, leads_count


def get_export_leads_no_appointment_agent(lead_status,lead_sub_status,start_date,end_date,current_user_email):
    if lead_status == 'In Queue':
        query = {}
    else:
        query = {'lead_sub_status': lead_sub_status}

    if start_date and end_date:
        query.update({'created_date__gte':start_date,'created_date__lte':end_date})

    leads_count = Leads.objects.filter(lead_status=lead_status,
                lead_owner_email=current_user_email,is_delete=False,**query).count()
    leads = Leads.objects.filter(lead_status=lead_status,
            lead_owner_email=current_user_email,is_delete=False,**query)
    return leads, leads_count

