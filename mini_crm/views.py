from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from main import views
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render_to_response
from django.template import Context
import json
from leads.models import Leads, WPPLeads, PicassoLeads
from datetime import datetime,timedelta
from collections import OrderedDict
from leads.models import Location, Timezone
import pytz
from reports.models import Region 

from django.http import Http404

# Create your views here.
@login_required
def crm_management(request):
    if request.user.groups.filter(name='CRM-MANAGER'):
        # import ipdb; ipdb.set_trace()
        leads_list = list()
        limit = 10
        on_page = request.GET.get('page', 1)
        if on_page == 1:
            offset = 0
        else:
            offset = limit * on_page - 1 

        regions = Region.objects.all()
        if request.is_ajax():
            process_type = ''
            lead_status =  ''
            lead_sub_status = ''
            lead_appointment = None
            if request.GET.get('process'):
                process_type = request.GET.get('process')
            if request.GET.get('status'):
                lead_status = request.GET.get('status')
            if request.GET.get('sub_status'):
                lead_sub_status = request.GET.get('sub_status')
            if request.GET.get('appointment'):
                lead_appointment = request.GET.get('appointment')    


            if not lead_appointment:
                if lead_status == lead_sub_status:
                    query = {'lead_status': lead_status}
                else:
                    query = {'lead_status' : lead_status,'lead_sub_status' :lead_sub_status}
                if process_type == "WPP":
                    # print settings.PROCESS_TYPE_MAPPING.get(process_type), lead_status, lead_sub_status

                    leads = WPPLeads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("WPP"), **query).values(
                        'customer_id', 'company', 'first_name', 'created_date','appointment_date', 'phone', 'phone_optional', 'country'
                        )[offset:limit]
                    leads_count = WPPLeads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("WPP"), **query).count()
                    # print "WPP", leads_count

                elif process_type == "Picasso Audits":
                    # print settings.PROCESS_TYPE_MAPPING.get(process_type), lead_status, lead_sub_status

                    leads = PicassoLeads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("Picasso Audits"), lead_status = lead_status).values(
                        'customer_id', 'company', 'first_name', 'created_date', 'phone', 'country')[offset:limit]
                    leads_count = PicassoLeads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("Picasso Audits"), lead_status = lead_status).count()
                    # print "Picasso Audits", leads_count

                elif process_type == "RLSA":
                    # print settings.PROCESS_TYPE_MAPPING.get(process_type), lead_status, lead_sub_status

                    leads = Leads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("RLSA"), **query).values(
                        'customer_id', 'company', 'first_name', 'created_date', 'appointment_date', 'phone', 'phone_optional', 'country'
                        ).order_by('-created_date')[offset:limit]
                    leads_count = Leads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("RLSA"), **query).count()
                    # print "RLSA", leads_count

                elif process_type == "Shopping":
                    # print settings.PROCESS_TYPE_MAPPING.get(process_type), lead_status, lead_sub_status

                    leads = Leads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("Shopping"), **query).values(
                        'customer_id', 'company', 'first_name', 'created_date', 'appointment_date', 'phone', 'phone_optional', 'country'
                        )[offset:limit]
                    leads_count = Leads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("Shopping"), **query).count()
                    # print "Shopping", leads_count

                elif process_type == "Shopping Argos":
                    # print settings.PROCESS_TYPE_MAPPING.get(process_type), lead_status, lead_sub_status

                    leads = Leads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("Shopping Argos"), **query).values(
                        'customer_id', 'company', 'first_name', 'created_date', 'appointment_date', 'phone', 'phone_optional', 'country'
                        )[offset:limit]
                    leads_count = Leads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("Shopping Argos"), **query).count()
                    # print "Shopping Argos", leads_count

                else: # Tag
                    exclude_types = settings.PROCESS_TYPE_MAPPING.get("RLSA") + settings.PROCESS_TYPE_MAPPING.get("Shopping Argos") + settings.PROCESS_TYPE_MAPPING.get("Shopping")
                    # print exclude_types, lead_status, lead_sub_status
                    leads = Leads.objects.exclude(type_1__in = exclude_types, **query).values('customer_id', 'company', 'first_name', 'created_date',  'appointment_date', 'phone', 'phone_optional', 'country'
                        )[offset:limit]
                    leads_count = Leads.objects.exclude(type_1__in = exclude_types, **query).count()
                    # print "TAG",leads_count
                    
            else:
                
                user_group = request.user.groups.filter(name='CRM-MANAGER')
                leads = get_filtered_leads(user_group,'TAG',lead_status,lead_sub_status,lead_appointment) 
                leads_count = leads.count()    
                             
            all_leads = get_leads(leads, leads_list)
            
            try:
                return HttpResponse(json.dumps({'leads_list': all_leads}), content_type="application/json")
            except Exception as e:
                print e

        context = {'crm_manager_text': json.dumps(settings.LEAD_STATUS_SUB_STATUS_MAPPING)}
        return render(request,'crm/manager_home.html',context)

    elif request.user.groups.filter(name='CRM-AGENT'):
        return redirect('mini_crm.views.crm_agent')
    else:
        raise Http404


def get_leads(leads, leads_list):
    for lead in leads:
        
        try:
            appointment_date = datetime.strftime(lead['appointment_date'], "%d/%m/%Y %I:%M %P")
        except:
            appointment_date = None
        try:
            phone_optional = lead['phone_optional']
        except:
            phone_optional = None
        
        lead_dict = {'c_id':lead['customer_id'],
                     'company':lead['company'], 
                     'customer_name':lead['first_name'],
                     'created_date':datetime.strftime(lead['created_date'], "%d/%m/%Y %I:%M %P") if lead['created_date'] else '',  
                     'appointment_time': appointment_date,
                     'phone_number':lead['phone'], 
                     'additional_phone_number':phone_optional, 
                     'web_master_number':'', 
                     'location':lead['country']}
        
        leads_list.append(lead_dict)
       
    return leads_list


def crm_agent(request):
    if request.user.groups.filter(name='CRM-MANAGER'):
        return redirect('mini_crm.views.crm_management')
    elif request.user.groups.filter(name='CRM-AGENT'):
        if request.is_ajax():
            leads_data = list()
            lead_status =  ''
            lead_sub_status = ''
            lead_appointment = None
            if request.GET.get('status'):
                lead_status = request.GET.get('status')
            if request.GET.get('sub_status'):
                lead_sub_status = request.GET.get('sub_status')
            if request.GET.get('appointment'):
                lead_appointment = request.GET.get('appointment')
            user_group = request.user.groups.filter(name='CRM-AGENT')
            leads = get_filtered_leads(user_group,'TAG',lead_status,lead_sub_status,lead_appointment)
            for lead in leads:
                lead_dict = {
                'lead_status':lead.lead_status,
                'customer_id':lead.customer_id,
                'company':lead.company,
                'customer_name':lead.first_name + '' + lead.last_name,
                'appointment_time':datetime.strftime(lead.appointment_date, "%d/%m/%Y %I:%M %P") if lead.appointment_date else '',
                'phone':lead.phone,
                'phone_optional':lead.phone_optional,
                'web_master_no':'',
                'location':''
                }
                leads_data.append(lead_dict)
            response_json = leads_data
            res = HttpResponse(json.dumps(response_json, indent=4), content_type="application/json")
            return res
        context ={
            'lead_status':settings.LEAD_STATUS_SUB_STATUS_MAPPING['TAG'].keys(),
            'lead_status_sub_status_mapping':json.dumps({'lead_status_sub_status_mapping':settings.LEAD_STATUS_SUB_STATUS_MAPPING},encoding="utf-8")
        }
        return render(request,'crm/agent_home.html',context)
    else:
        raise Http404


def get_filtered_leads(user_group,process,lead_status,lead_sub_status,lead_appointment):
    if lead_appointment and lead_appointment != 'Fresh Appointment':
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
        if user_group[0].name == 'CRM-AGENT':
            leads = Leads.objects.filter(lead_status="In Queue", appointment_date_in_ist__gte=start_date_time,appointment_date_in_ist__lte=end_date_time)
        else:
            #manager
            leads = Leads.objects.filter(lead_status="In Queue", appointment_date_in_ist__gte=start_date_time,appointment_date_in_ist__lte=end_date_time).values('customer_id', 'company', 'first_name', 'created_date',  'appointment_date', 'phone', 'phone_optional', 'country')
    else:
        if  user_group[0].name == 'CRM-AGENT':
            leads = Leads.objects.filter(lead_status=lead_status,lead_sub_status=lead_sub_status)
        else:
            #manager
            leads = Leads.objects.filter(lead_status=lead_status,lead_sub_status=lead_sub_status).values('customer_id', 'company', 'first_name', 'created_date',  'appointment_date', 'phone', 'phone_optional', 'country')

    return leads