from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from main import views
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render_to_response
from django.template import Context

#import datetime
import json
from leads.models import Leads, WPPLeads, PicassoLeads, TagLeadDetail
from datetime import datetime,timedelta
from collections import OrderedDict
from leads.models import Location, Timezone
import pytz 
from reports.models import Region

from django.http import Http404
from django.conf import settings
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User, Group

# Create your views here.
@login_required
def crm_management(request):
    if request.user.groups.filter(name='CRM-MANAGER'):
        
        leads_list = list()
        limit = 10
        on_page = request.GET.get('page', 1)
        if on_page == 1:
            offset = 0
        else:
            offset = limit * on_page - 1 

        regions = Region.objects.all()
        regions_list = list()
        for region in regions:
            region_dict = {'name':region.name,
                           'location':region.location_list()}
            regions_list.append(region_dict)

        if request.is_ajax():
 
            region = request.GET.get('region') if request.GET.get('region') else ''
            process_type = request.GET.get('process') if request.GET.get('process') else ''
            lead_status = request.GET.get('status') if request.GET.get('status') else ''
            lead_sub_status = request.GET.get('sub_status') if request.GET.get('sub_status') else ''
            lead_appointment = request.GET.get('appointment') if request.GET.get('appointment') else None

            has_region = False
            loc_list = list()
            if str(region) != 'all':
                has_region = True
                region = Region.objects.filter(name=region)
                
                locations_list =  region[0].location_list().split(',')
                
                loc_list = [str(loc).strip() for loc in locations_list]

            if not lead_appointment:
                
                if lead_status == lead_sub_status:
                    if has_region:
                        query = {'lead_status': lead_status, 'country__in':loc_list}
                    else:
                        query = {'lead_status': lead_status}
                else:
                    if has_region:
                        query = {'lead_status' : lead_status,'lead_sub_status' :lead_sub_status, 
                        'country__in':loc_list}
                    else:
                        query = {'lead_status' : lead_status,'lead_sub_status' :lead_sub_status}

                if process_type == "WPP":

                    leads = WPPLeads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("WPP"), **query).values(
                        'id', 'sf_lead_id','customer_id', 'company', 'first_name', 'created_date','appointment_date', 'phone', 'phone_optional', 'country'
                        )[offset:limit]
                    leads_count = WPPLeads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("WPP"), **query).count()

                elif process_type == "Picasso Audits":
                    
                    if loc_list:
                        query = {'lead_status': lead_status, 'country__in':loc_list}
                    else:
                        query = {'lead_status': lead_status}

                    leads = PicassoLeads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("Picasso Audits"), **query).values(
                        'id', 'sf_lead_id','customer_id', 'company', 'first_name', 'created_date', 'phone', 'country')[offset:limit]
                    leads_count = PicassoLeads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("Picasso Audits"), **query).count()
                    
                elif process_type == "RLSA":
                    
                    leads = Leads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("RLSA"), **query).values(
                        'id', 'sf_lead_id','customer_id', 'company', 'first_name', 'created_date', 'appointment_date', 'phone', 'phone_optional', 'country'
                        ).order_by('-created_date')[offset:limit]
                    
                    leads_count = Leads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("RLSA"), **query).count()
                    
                elif process_type == "Shopping":

                    leads = Leads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("Shopping"), **query).values(
                        'id', 'sf_lead_id','customer_id', 'company', 'first_name', 'created_date', 'appointment_date', 'phone', 'phone_optional', 'country'
                        )[offset:limit]
                    leads_count = Leads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("Shopping"), **query).count()

                elif process_type == "Shopping Argos":
                    leads = Leads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("Shopping Argos"), **query).values(
                        'id', 'sf_lead_id','customer_id', 'company', 'first_name', 'created_date', 'appointment_date', 'phone', 'phone_optional', 'country'
                        )[offset:limit]
                    leads_count = Leads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("Shopping Argos"), **query).count()
                    

                else: # Tag
                    exclude_types = settings.PROCESS_TYPE_MAPPING.get("RLSA") + settings.PROCESS_TYPE_MAPPING.get("Shopping Argos") + settings.PROCESS_TYPE_MAPPING.get("Shopping")
                    leads = Leads.objects.filter(**query).exclude(type_1__in = exclude_types).values('id', 'sf_lead_id','customer_id', 'company', 'first_name', 'created_date',  'appointment_date', 'phone', 'phone_optional', 'country'
                        )[offset:limit]
                    leads_count = Leads.objects.filter(**query).exclude(type_1__in = exclude_types).count()
                    
            else:
                
                user_group = request.user.groups.filter(name='CRM-MANAGER')
                leads = get_filtered_leads(user_group,process_type,lead_status,lead_sub_status,lead_appointment,limit,offset,has_region,loc_list) 
                leads_count = leads.count()    
                             
            all_leads = get_leads(leads, leads_list)
            
            try:
                return HttpResponse(json.dumps({'leads_list': all_leads}), content_type="application/json")
            except Exception as e:
                print e

        context = {'crm_manager_text': json.dumps(settings.LEAD_STATUS_SUB_STATUS_MAPPING), 'regions':json.dumps(regions_list)}
        return render(request,'crm/manager_home.html',context)

    elif request.user.groups.filter(name='CRM-AGENT'):
        return redirect('mini_crm.views.crm_agent')
    else:
        raise Http404


def get_leads(leads, leads_list):
    for lead in leads:
        appointment_date = datetime.strftime(lead.get('appointment_date'), "%d/%m/%Y %I:%M %P") if lead.get('appointment_date') else lead.get('appointment_date') ,
        phone_optional =  lead.get('phone_optional')
        
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
            leads = get_filtered_leads(user_group,'TAG',lead_status,lead_sub_status,lead_appointment,'','','','')
            leads_data = get_json_leads(leads)
            response_json = leads_data
            res = HttpResponse(json.dumps(response_json), content_type="application/json")
            return res
        context ={
            'lead_status':settings.LEAD_STATUS_SUB_STATUS_MAPPING['TAG'].keys(),
            'lead_status_sub_status_mapping':json.dumps({'lead_status_sub_status_mapping':settings.LEAD_STATUS_SUB_STATUS_MAPPING},encoding="utf-8")
        }
        return render(request,'crm/agent_home.html',context)
    else:
        raise Http404


def get_filtered_leads(user_group,process,lead_status,lead_sub_status,lead_appointment,limit,offset,has_region,loc_list):
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
            
            # leads = get_leads_based_on_appointment_manager(process,lead_appointment,limit,offset,has_region,loc_list,start_date_time,end_date_time)
            
            leads = Leads.objects.filter(lead_status="In Queue", appointment_date_in_ist__gte=start_date_time,appointment_date_in_ist__lte=end_date_time).values(
                'id', 'sf_lead_id','customer_id', 'company', 'first_name', 'created_date',  'appointment_date', 'phone', 'phone_optional', 'country')
    else:
        if  user_group[0].name == 'CRM-AGENT':
            leads = Leads.objects.filter(lead_status=lead_status,lead_sub_status=lead_sub_status)
        else:
            #manager
            # leads = get_leads_based_on_appointment_manager(process,lead_appointment,limit,offset,has_region,loc_list,start_date_time,end_date_time)
            
            leads = Leads.objects.filter(lead_status=lead_status,lead_sub_status=lead_sub_status).values(
                'id', 'sf_lead_id','customer_id', 'company', 'first_name', 'created_date',  'appointment_date', 'phone', 'phone_optional', 'country')

    return leads

# def get_leads_based_on_appointment_manager(process_type,lead_appointment,limit,offset,has_region,loc_list,start_date_time,end_date_time):
    
#     if has_region:
#         query = {'country__in':loc_list, 'appointment_date_in_ist__gte':start_date_time, 'appointment_date_in_ist__lte':end_date_time}
#     else:
#         query = {'appointment_date_in_ist__gte':start_date_time, 'appointment_date_in_ist__lte':end_date_time}
    
#     if process_type == "WPP":

#         leads = WPPLeads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("WPP"), **query).values(
#             'id', 'sf_lead_id','customer_id', 'company', 'first_name', 'created_date','appointment_date', 'phone', 'phone_optional', 'country'
#             )[offset:limit]
#         leads_count = WPPLeads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("WPP"), **query).count()
       

#     elif process_type == "Picasso Audits":

#         if loc_list:
#             query = {'country__in':loc_list}
#         else:
#             query = {}

#         leads = PicassoLeads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("Picasso Audits"), **query).values(
#             'id', 'sf_lead_id','customer_id', 'company', 'first_name', 'created_date', 'phone', 'country')[offset:limit]
#         leads_count = PicassoLeads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("Picasso Audits"), **query).count()

#     elif process_type == "RLSA":
        
#         leads = Leads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("RLSA"), **query).values(
#             'id', 'sf_lead_id','customer_id', 'company', 'first_name', 'created_date', 'appointment_date', 'phone', 'phone_optional', 'country'
#             ).order_by('-created_date')[offset:limit]
        
#         leads_count = Leads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("RLSA"), **query).count()
        

#     elif process_type == "Shopping":
        
#         leads = Leads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("Shopping"), **query).values(
#             'id', 'sf_lead_id','customer_id', 'company', 'first_name', 'created_date', 'appointment_date', 'phone', 'phone_optional', 'country'
#             )[offset:limit]
#         leads_count = Leads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("Shopping"), **query).count()
        

#     elif process_type == "Shopping Argos":
#         leads = Leads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("Shopping Argos"), **query).values(
#             'id', 'sf_lead_id','customer_id', 'company', 'first_name', 'created_date', 'appointment_date', 'phone', 'phone_optional', 'country'
#             )[offset:limit]
#         leads_count = Leads.objects.filter(type_1__in = settings.PROCESS_TYPE_MAPPING.get("Shopping Argos"), **query).count()
        

#     else: # Tag

#         exclude_types = settings.PROCESS_TYPE_MAPPING.get("RLSA") + settings.PROCESS_TYPE_MAPPING.get("Shopping Argos") + settings.PROCESS_TYPE_MAPPING.get("Shopping")
        
#         leads = Leads.objects.filter(**query).exclude(type_1__in = exclude_types).values('id', 'sf_lead_id','customer_id', 'company', 'first_name', 'created_date',  'appointment_date', 'phone', 'phone_optional', 'country'
#             )[offset:limit]
#         leads_count = Leads.objects.filter(**query).exclude(type_1__in = exclude_types).count()

#     return leads
        


def get_json_leads(leads):
	leads_data = list()
	for lead in leads:
		lead_dict = {
		'lead_owner':lead.lead_owner_name,
		'lead_status':lead.lead_status,
		'lead_sub_status':lead.lead_sub_status if hasattr(lead, 'lead_sub_status') and lead.lead_sub_status else '',
		'lead_id':lead.id,
		'sf_lead_id':lead.sf_lead_id,
		'customer_id':lead.customer_id,
		'company':lead.company,
		'customer_name':lead.first_name + '' + lead.last_name,
		'appointment_time':datetime.strftime(lead.appointment_date, "%d/%m/%Y %I:%M %P") if hasattr(lead, 'appointment_date') and lead.appointment_date else '',
		'phone':lead.phone,
		'phone_optional':lead.phone_optional if hasattr(lead, 'phone_optional') else '',
		'web_master_no':'',
		'location':'',
		'rescheduled':True if hasattr(lead, 'rescheduled_appointment') and lead.rescheduled_appointment else False,
		'lead_owner_name':lead.lead_owner_name,
		'team':lead.team,
		'date_of_installation':datetime.strftime(lead.date_of_installation, "%d/%m/%Y") if lead.date_of_installation else '',
		'first_contacted_on':datetime.strftime(lead.first_contacted_on, "%d/%m/%Y %I:%M %P") if hasattr(lead, 'first_contacted_on') and lead.first_contacted_on else '',
		'dials':lead.dials if hasattr(lead, 'dials') and lead.dials else 0
		}
		if lead_dict['appointment_time']:
			date_time = lead_dict['appointment_time'].split(' ')
			lead_dict['apmnt_date'] = date_time[0]
			lead_dict['apmnt_time'] = date_time[1] + ' ' + date_time[2]	
		leads_data.append(lead_dict)
	   
	return leads_data


@login_required
def lead_history(request):
	if request.user.groups.filter(name='CRM-AGENT'):
		lead_status = request.GET.get('status')
		process_type = 'TAG'
		if request.is_ajax():
			if lead_status == 'In Queue':
				if process_type == 'TAG':
					exclude_types = settings.PROCESS_TYPE_MAPPING.get("RLSA") + settings.PROCESS_TYPE_MAPPING.get("Shopping Argos") + settings.PROCESS_TYPE_MAPPING.get("Shopping")
					leads = Leads.objects.filter(lead_status=lead_status).exclude(type_1__in=exclude_types)
				elif process_type == 'SHOPPING':
					leads = Leads.objects.filter(lead_status=lead_status,type_1__in = settings.PROCESS_TYPE_MAPPING.get("Shopping"))
				elif process_type == 'RLSA':
					leads = Leads.objects.filter(lead_status=lead_status,type_1__in = settings.PROCESS_TYPE_MAPPING.get("RLSA"))
				elif process_type == 'WPP':
					leads = WPPLeads.objects.filter(lead_status=lead_status,type_1__in = settings.PROCESS_TYPE_MAPPING.get("WPP"))
				elif process_type == 'Picasso Audits':
					leads = PicassoLeads.objects.filter(lead_status=lead_status,type_1__in = settings.PROCESS_TYPE_MAPPING.get("Picasso Audits"))
				else:
					leads = Leads.objects.filter(lead_status=lead_status,type_1__in = settings.PROCESS_TYPE_MAPPING.get("Shopping Argos"))
			else:
				exclude_types = settings.PROCESS_TYPE_MAPPING.get("RLSA") + settings.PROCESS_TYPE_MAPPING.get("Shopping Argos") + settings.PROCESS_TYPE_MAPPING.get("Shopping")
				if process_type == 'TAG':
					leads = Leads.objects.filter(appointment_date__isnull=False,rescheduled_appointment__isnull=False,lead_status='In Progress',lead_sub_status__in=['IP - CALL BACK','IP - Appointment Rescheduled - IS (GS)','IP - Code Sent']).exclude(type_1__in = exclude_types)
				elif process_type == 'SHOPPING':
					leads = Leads.objects.filter(appointment_date__isnull=False,rescheduled_appointment__isnull=False,lead_status='In Progress',lead_sub_status__in=['IP - CALL BACK','IP - Appointment Rescheduled - IS (GS)','IP - Code Sent'],type_1__in = settings.PROCESS_TYPE_MAPPING.get("Shopping"))
				elif process_type == 'RLSA':
					leads = Leads.objects.filter(appointment_date__isnull=False,rescheduled_appointment__isnull=False,lead_status='In Progress',lead_sub_status__in=['IP - CALL BACK','IP - Appointment Rescheduled - IS (GS)','IP - Code Sent'],type_1__in = settings.PROCESS_TYPE_MAPPING.get("RLSA"))
				elif process_type == 'WPP':
					leads = WPPLeads.objects.filter(appointment_date__isnull=False,rescheduled_appointment__isnull=False,lead_status='In Progress',lead_sub_status__in=['IP - CALL BACK','IP - Appointment Rescheduled - IS (GS)','IP - Code Sent'],type_1__in = settings.PROCESS_TYPE_MAPPING.get("WPP"))
				elif process_type == 'Picasso Audits':
					leads = list()
				else:
					leads = Leads.objects.filter(appointment_date__isnull=False,rescheduled_appointment__isnull=False,lead_status='In Progress',lead_sub_status__in=['IP - CALL BACK','IP - Appointment Rescheduled - IS (GS)','IP - Code Sent'],type_1__in = settings.PROCESS_TYPE_MAPPING.get("Shopping Argos"))

			res = HttpResponse(json.dumps(get_json_leads(leads)), content_type="application/json")
			return res
		return render(request,'crm/lead_and_history.html')
	else:
		raise Http404		


@login_required
def search_leads(request):
    searching_lead_id = request.GET.get('q')
    returning_data = list()
    try:
        normal_leads = Leads.objects.values('customer_id', 'type_1', 'url_1', 'lead_status', 'id', 'sf_lead_id').filter(Q(customer_id=searching_lead_id) | Q(sf_lead_id=searching_lead_id))
        if normal_leads:
            for each in list(normal_leads):
            	if each['type_1'] in ['Google Shopping Setup', 'Existing Datafeed Optimization','Google Shopping Migration']:
            		each['process_type'] = 'Shopping'
            	elif each['type_1'] in ['RLSA Bulk Implementation']:
            		each['process_type'] = 'RLSA'
            	else:
            		each['process_type'] = 'TAG'
            returning_data += list(normal_leads)
    except ObjectDoesNotExist:
        pass
    try:
        picasso_leads = PicassoLeads.objects.values('customer_id', 'type_1', 'url_1', 'lead_status', 'id', 'sf_lead_id').filter(Q(customer_id=searching_lead_id) | Q(sf_lead_id=searching_lead_id))
        if picasso_leads:
            for each in list(picasso_leads):
            	if each['type_1'] in ['BOLT']:
            		each['process_type'] = 'BOLT'
            	else:
            		each['process_type'] = 'Picasso' 
            returning_data += list(picasso_leads)

    except ObjectDoesNotExist:
        pass
    try:
        wpp_leads = WPPLeads.objects.values('customer_id', 'type_1', 'url_1', 'lead_status', 'id', 'sf_lead_id').filter(Q(customer_id=searching_lead_id) | Q(sf_lead_id=searching_lead_id))
        if wpp_leads:
            for each in list(wpp_leads):
            		each['process_type'] = 'WPP'
            returning_data += list(wpp_leads)
    except ObjectDoesNotExist:
        pass

    return render(request,'crm/search_result.html',{'returning_data':returning_data, 'resultcount':len(returning_data),'q_id':searching_lead_id})


@login_required
def lead_details(request, lid, sf_lead_id, ctype):
    lead = None
    if ctype in ['TAG','Shopping','RLSA','ShoppingArgos']:
        lead = Leads.objects.get(id=lid,sf_lead_id=sf_lead_id)
    elif ctype == 'WPP':
        lead = WPPLeads.objects.get(id=lid,sf_lead_id=sf_lead_id)
    else:
        lead = PicassoLeads.objects.get(id=lid,sf_lead_id=sf_lead_id)

    return render(request,'crm/lead_details.html',{'lead':lead, 'ctype':ctype})


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
            if lead_type in ['WPP','Bolt Build','WPP - Nomination']:
                current_lead = WPPLeads.objects.get(id=lead_id)
                if not assign:
                    appointment_conflict = WPPLeads.objects.filter(
                        appointment_date_in_ist=current_lead.appointment_date_in_ist, 
                        lead_owner_email=lead_owner)
                    assign = False if appointment_conflict else True
            else: 
                current_lead = Leads.objects.get(id=lead_id)
                if not assign:
                    appointment_conflict = Leads.objects.filter(type_1=lead_type,lead_owner_email=lead_owner,
                        lead_status__in=['Attempting Contact','In Queue','ON CALL','In Progress'], 
                        appointment_date_in_ist=current_lead.appointment_date_in_ist)
                    assign = False if appointment_conflict else True        
        if assign:
            current_lead.lead_owner_name = assignee_name
            current_lead.lead_owner_email = lead_owner
            current_lead.save()
            resp['success'] = True
        else:
            resp['success'] = False   
        resp['name'] = assignee_name
        resp['email'] = lead_owner
        return HttpResponse(json.dumps(resp))
    else:
        raise Http403


def get_crm_agents_emails(request):
    agents_email_list = list()
    search_keyword = request.GET.get('search_key')
    all_emails = User.objects.values('email').filter(email__icontains = search_keyword, groups__name='CRM-AGENT')[:20]
    for each in all_emails:
        agents_email_list.append(each['email'])
    response = {'data':agents_email_list}
    return HttpResponse(json.dumps(response))

def delete_lead(request, lid, ctype):
    if request.user.groups.filter(name='CRM-MANAGER'):
        if ctype == "WPP":
            if WPPLeads.objects.all().count():
                lead = WPPLeads.objects.get(id=lid)
                lead.delete()
        elif ctype == "PicassoAudits":
            if PicassoLeads.objects.all().count():
                lead = PicassoLeads.objects.get(id=lid)
                lead.delete()
        elif ctype == "RLSA" or "Shopping" or "ShoppingArgos" or "TAG":
            
            if TagLeadDetail.objects.all().count():
                lead = TagLeadDetail.objects.get(lead_id=lid)
                lead.delete()
            if Leads.objects.all().count():
                lead = Leads.objects.get(id=lid)
                lead.delete()
        return redirect(reverse("all-leads") + "?ptype=" + ctype)
