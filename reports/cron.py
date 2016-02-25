import kronos
from reports.report_services import ReportService
from django.conf import settings
from datetime import datetime, timedelta
import logging
from lib.salesforce import SalesforceApi
from leads.models import Leads, SfdcUsers, WPPLeads, PicassoLeads
from django.core.exceptions import ObjectDoesNotExist
import pytz
from representatives.models import GoogeRepresentatives, RegalixRepresentatives
import json
import gspread
from oauth2client.client import SignedJwtAssertionCredentials
from reports.models import CallLogAccountManager
from datetime import datetime
from lib.helpers import (send_mail)
from django.template.loader import get_template
from django.template import Context
from reports.models import Region, LeadsReport

logging.basicConfig(filename='/tmp/cronjob.log',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%d/%b/%Y %H:%M:%S',
                    level=logging.DEBUG)


@kronos.register('*/10 * * * *')
def get_updated_leads():
    """ Get Current Quarter updated Leads from SFDC """
    end_date = datetime.now(pytz.UTC)    # we need to use UTC as salesforce API requires this
    start_date = end_date - timedelta(minutes=10)
    start_date = SalesforceApi.convert_date_to_salesforce_format(start_date)
    end_date = SalesforceApi.convert_date_to_salesforce_format(end_date)
    logging.info("Current Quarted Updated Leads from %s to %s" % (start_date, end_date))
    logging.info("Connecting to SFDC %s" % (datetime.utcnow()))
    sf = SalesforceApi.connect_salesforce()
    logging.info("Connect Successfully")
    select_items = settings.SFDC_FIELDS
    tech_team_id = settings.TECH_TEAM_ID
    code_type = 'Picasso'
    where_clause_all = "WHERE (LastModifiedDate >= %s AND LastModifiedDate <= %s) AND LastModifiedById != '%s' AND Code_Type__c != '%s'" % (start_date, end_date, tech_team_id, code_type)
    where_clause_picasso = "WHERE (LastModifiedDate >= %s AND LastModifiedDate <= %s) AND LastModifiedById != '%s' AND Code_Type__c = '%s'" % (start_date, end_date, tech_team_id, code_type)
    sql_query_all = "select %s from Lead %s" % (select_items, where_clause_all)
    sql_query_picasso = "select %s from Lead %s" % (select_items, where_clause_picasso)
    try:
        all_leads = sf.query_all(sql_query_all)
        picasso_leads = sf.query_all(sql_query_picasso)
        logging.info("Updating Leads count: %s " % (len(all_leads['records'])))
        logging.info("Updating PICASSO Leads count: %s " % (len(picasso_leads['records'])))
        create_or_update_leads(all_leads['records'], sf)
        update_sfdc_leads(all_leads['records'], sf)
        create_or_update_picasso_leads(picasso_leads['records'], sf)
    except Exception as e:
        print e
        logging.info("Fail to get updated leads from %s to %s" % (start_date, end_date))
        logging.info("%s" % (e))


@kronos.register('43 0 * * *')
def get_last_day_leads():
    """ Get Previous Day Leads from SFDC """
    end_date = datetime.now(pytz.UTC)    # we need to use UTC as salesforce API requires this
    start_date = end_date - timedelta(days=1)
    start_date = SalesforceApi.convert_date_to_salesforce_format(start_date)
    end_date = SalesforceApi.convert_date_to_salesforce_format(end_date)
    logging.info("prev Month Updated Leads from %s to %s" % (start_date, end_date))
    logging.info("Connecting to SFDC %s" % (datetime.utcnow()))
    sf = SalesforceApi.connect_salesforce()
    logging.info("Connect Successfully")
    select_items = settings.SFDC_FIELDS
    code_type = 'Picasso'
    where_clause = "WHERE (CreatedDate >= %s AND CreatedDate <= %s) AND Code_Type__c != '%s'" % (start_date, end_date, code_type)
    where_clause_picasso = "WHERE (CreatedDate >= %s AND CreatedDate <= %s) AND Code_Type__c = '%s'" % (start_date, end_date, code_type)
    sql_query_all = "select %s from Lead %s" % (select_items, where_clause)
    sql_query_picasso = "select %s from Lead %s" % (select_items, where_clause_picasso)
    try:
        all_leads = sf.query_all(sql_query_all)
        picasso_leads = sf.query_all(sql_query_picasso)
        logging.info("Updating Leads count: %s " % (len(all_leads['records'])))
        logging.info("Updating PICASSO Leads count: %s " % (len(picasso_leads['records'])))
        create_or_update_leads(all_leads['records'], sf)
        create_or_update_picasso_leads(picasso_leads['records'], sf)
    except Exception as e:
        print e
        logging.info("Fail to get updated leads from %s to %s" % (start_date, end_date))
        logging.info("%s" % (e))


@kronos.register('1 * * * *')
def get_reschedule_leads():
    """ Get Current Quarter updated Leads from SFDC """
    end_date = datetime.now(pytz.UTC)    # we need to use UTC as salesforce API requires this
    start_date = end_date - timedelta(minutes=419)
    end_date = end_date + timedelta(days=1)
    start_date = SalesforceApi.convert_date_to_salesforce_format(start_date)
    end_date = SalesforceApi.convert_date_to_salesforce_format(end_date)
    logging.info("Current Quarted Updated Leads from %s to %s" % (start_date, end_date))
    logging.info("Connecting to SFDC %s" % (datetime.utcnow()))
    sf = SalesforceApi.connect_salesforce()
    logging.info("Connect Successfully")
    select_items = settings.SFDC_FIELDS
    tech_team_id = settings.TECH_TEAM_ID
    where_clause = "WHERE (Rescheduled_Appointments__c >= %s AND Rescheduled_Appointments__c <= %s) AND Rescheduled_Appointments__c != null AND LastModifiedById != '%s'" % (start_date, end_date, tech_team_id)
    sql_query = "select %s from Lead %s" % (select_items, where_clause)
    try:
        all_leads = sf.query_all(sql_query)
        logging.info("Updating Leads count: %s " % (len(all_leads['records'])))
        create_or_update_leads(all_leads['records'], sf)
        update_sfdc_leads(all_leads['records'], sf)
    except Exception as e:
        print e
        logging.info("Fail to get updated leads from %s to %s" % (start_date, end_date))
        logging.info("%s" % (e))


@kronos.register('55 0 * * *')
def get_deleted_leads():
    """ Get Current Quarter updated Leads from SFDC """
    end_date = datetime.now(pytz.UTC)    # we need to use UTC as salesforce API requires this
    start_date = end_date - timedelta(days=29)
    logging.info("Current Quarted Deleted Leads from %s to %s" % (start_date, end_date))
    logging.info("Connecting to SFDC %s" % (datetime.utcnow()))
    sf = SalesforceApi.connect_salesforce()
    if sf:
        logging.info("Connect Successfully")
        logging.info("Get Deleted leads form %s to %s" % (start_date, end_date))
        leads = sf.Lead.deleted(start_date, end_date)
        if leads:
            ids = [str(lid.get('id')) for lid in leads['deletedRecords']]
            ids = tuple(ids)
            logging.info("Deleted Lead Id's %s, Total = %s" % (ids, len(ids)))
            Leads.objects.filter(sf_lead_id__in=ids).delete()
            WPPLeads.objects.filter(sf_lead_id__in=ids).delete()
            PicassoLeads.objects.filter(sf_lead_id__in=ids).delete()
            logging.info("Deleted Successfully")
        # start_date, end_date = get_quarter_date_slots(datetime.utcnow())
        # start_date = datetime(start_date.year, start_date.month, start_date.day, 0, 0, 0)
        # end_date = end_date = datetime(end_date.year, end_date.month, end_date.day, 23, 59, 59)
        # portal_lead_ids = list(Leads.objects.filter(created_date__gte=start_date, created_date__lte=end_date).values_list(
        #     'sf_lead_id', flat=True).distinct())
        # logging.info("No of Portal Leads on Current Quarter %s" % (len(portal_lead_ids)))
        # start_date = SalesforceApi.convert_date_to_salesforce_format(start_date)
        # end_date = SalesforceApi.convert_date_to_salesforce_format(end_date)
        # where_clause = "WHERE CreatedDate >= %s AND CreatedDate <= %s" % (start_date, end_date)
        # sql_query = "select Id from Lead %s" % (where_clause)
        # try:
        #     all_leads = sf.query_all(sql_query)
        #     logging.info("No of Lead Ids from %s to %s is: %s" % (start_date, end_date, len(all_leads['records'])))
        #     sf_lead_ids = [sf_id.get('Id') for sf_id in all_leads['records']]
        #     logging.info("No of Salesforce Leads on Current Quarter %s" % (len(sf_lead_ids)))
        #     if len(portal_lead_ids) > len(sf_lead_ids):
        #         extra_leads = set(portal_lead_ids) - set(sf_lead_ids)
        #         logging.info("No of Current Quarter leads deleted on portal %s" % (len(extra_leads)))
        #         Leads.objects.filter(sf_lead_id__in=list(extra_leads)).delete()
        # except Exception as e:
        #     print e
        #     logging.info("Fail to get leads from %s to %s" % (start_date, end_date))
        #     logging.info("%s" % (e))


@kronos.register('0 */2 * * *')
def implemented_leads_count_report():
    # Leads based on Region based
    logging.info("Implemeted Leads Count Mail Details")
    specific_date_time = datetime.today()
    specific_date = datetime(specific_date_time.year, specific_date_time.month, specific_date_time.day)
    total_count_tag = list()
    total_count_shopping = list()
    final_dict = {'TAG': 0, 'SHOPPING': 0}
    all_regions = Region.objects.all()
    for region in all_regions:
        each_region_tag = {region.name: 0}
        each_region_shopping = {region.name: 0}
        location_list = [loc.location_name for loc in region.location.all()]
        leads_count_tag = Leads.objects.exclude(type_1__in=['Google Shopping Setup', 'Google Shopping Troubleshooting', 'Google Shopping Migration']).filter(country__in=location_list, lead_status__in=['Pending QC - WIN', 'Implemented'], date_of_installation=specific_date).count()
        each_region_tag[region.name] = leads_count_tag
        total_count_tag.append(each_region_tag)
        final_dict['TAG'] = total_count_tag
        leads_count_shopping = Leads.objects.filter(type_1__in=['Google Shopping Setup', 'Google Shopping Troubleshooting', 'Google Shopping Migration'], country__in=location_list, lead_status__in=['Pending QC - WIN', 'Implemented'], date_of_installation=specific_date).count()
        each_region_shopping[region.name] = leads_count_shopping
        total_count_shopping.append(each_region_shopping)
        final_dict['SHOPPING'] = total_count_shopping
    specific_time = datetime.strftime(specific_date_time, '%H:%M:%S')
    specific_date = specific_date.date()
    logging.info("Implemeted Leads Count Mail Details sending")
    mail_subject = "Wins Count Regionwise @ %s - %s " % (specific_date, specific_time)
    mail_body = get_template('leads/email_templates/lead_status_summary.html').render(
        Context({
            'final_dict': final_dict,
            'specific_date': specific_date,
        })
    )
    mail_from = 'basavaraju@regalix-inc.com'
    mail_to = ['g-crew@regalix-inc.com', 'portalsupport@regalix-inc.com']
    bcc = set([])
    attachments = list()
    send_mail(mail_subject, mail_body, mail_from, mail_to, list(bcc), attachments, template_added=True)
    logging.info("Implemeted Leads Count Mail Details sent")


def get_leads_from_sfdc(start_date, end_date):
    """ Get Leads from SFDC """
    # get SFDC Connection
    logging.info("Connecting to SFDC %s" % (datetime.utcnow()))
    sf = SalesforceApi.connect_salesforce()
    logging.info("Connect Successfully")
    start_date = SalesforceApi.convert_date_to_salesforce_format(start_date)
    end_date = SalesforceApi.convert_date_to_salesforce_format(end_date)
    select_items = settings.SFDC_FIELDS
    where_clause = "WHERE CreatedDate >= %s AND CreatedDate <= %s" % (start_date, end_date)
    sql_query = "select %s from Lead %s" % (select_items, where_clause)
    try:
        all_leads = sf.query_all(sql_query)
        logging.info("No of Leads from %s to %s is: %s" % (start_date, end_date, len(all_leads['records'])))
        create_or_update_leads(all_leads['records'], sf)
    except Exception as e:
        print e
        logging.info("Fail to get leads from %s to %s" % (start_date, end_date))
        logging.info("%s" % (e))


def create_or_update_leads(records, sf):
    """ Create a new leads or update existing lead """
    logging.info("Start saving leads to our DB")
    total_leads = 0
    new_lead_saved = 0
    new_lead_failed = 0
    exist_lead_saved = 0
    exist_lead_failed = 0
    total_wpp_leads = 0
    existing_wpp_leads = 0
    new_wpp_leads = 0
    is_new_lead = True
    owners_list = {u.user_id: {'name': u.full_name, 'email': u.email} for u in SfdcUsers.objects.all()}
    for rec in records:
        total_leads += 1
        sf_lead_id = rec.get('Id')

        sf_lead_id = rec.get('Id')
        type_1 = rec.get('Code_Type__c')
        # if type_1 == 'WPP':
        if type_1 in ['WPP', 'WPP - Nomination']:
            total_wpp_leads += 1
            try:
                lead = WPPLeads.objects.get(sf_lead_id=sf_lead_id)
                existing_wpp_leads += 1
            except ObjectDoesNotExist:
                lead = WPPLeads()
                new_wpp_leads += 1
            lead.lead_status = rec.get('WPP_Lead_Status__c')
            lead.is_ab_test = rec.get('AB_Testing__c')

            # New Additional fields for lead History
            additional_notes = rec.get('Additional_Notes_if_any__c') if rec.get('Additional_Notes_if_any__c') else ''
            lead.additional_notes = additional_notes
            lead.mockup_url = rec.get('Mockup_URL__c')
            lead.mockup_password = rec.get('Mockup_URL_Password__c')
            lead.stage_url = rec.get('Stage_URL__c')
            lead.stage_password = rec.get('Stage_URL_Credentials__c')
            # Storing obectives and pod name in comment5 & url5 fields
            lead.comment_5 = (rec.get('Picasso_Objective__c')).replace(';', ',') if rec.get('Picasso_Objective__c') else ''
            lead.url_5 = rec.get('POD_Name__c') if rec.get('POD_Name__c') else ''
            if type_1 == 'WPP':
                lead.treatment_type = rec.get('Treatment_Type__c') if rec.get('Treatment_Type__c') else 'Full Desktop/Mobile Optimization'
            else:
                lead.treatment_type = rec.get('Treatment_Type__c') if rec.get('Treatment_Type__c') else 'NA'
            lead.ref_uuid = rec.get('Picasso_Reference_Id__c') if rec.get('Picasso_Reference_Id__c') else ''
            if rec.get('PICASSO_build_eligible__c'):
                if rec.get('PICASSO_build_eligible__c') == 'Yes':
                    lead.is_nominated = True
                elif rec.get('PICASSO_build_eligible__c') == 'No':
                    lead.is_nominated = False
        else:
            try:
                # check for existing lead
                lead = Leads.objects.get(sf_lead_id=sf_lead_id)
                is_new_lead = False
            except ObjectDoesNotExist:
                # create new lead
                is_new_lead = True
                lead = Leads()
            lead.lead_status = rec.get('Status')
            lead.language = rec.get('Language__c')
            lead.gcss = rec.get('GCSS_Status__c')

        # Google Representative email and name
        rep_email = rec.get('Email')
        rep_name = rec.get('Google_Rep__c')

        # Lead owner name
        owner_id = rec.get('OwnerId')
        if owner_id and owner_id in owners_list:
            details = owners_list.get(owner_id)
            lead_owner_name = details.get('name')
            lead_owner_email = details.get('email')
        else:
            try:
                user_details = sf.User.get(owner_id)
                lead_owner_name = user_details.get('Name')
                lead_owner_email = user_details.get('Email')
            except ObjectDoesNotExist:
                lead_owner_name = "%s %s" % (settings.DEFAULT_LEAD_OWNER_FNAME, settings.DEFAULT_LEAD_OWNER_LNAME)
                lead_owner_email = settings.DEFAULT_LEAD_OWNER_EMAIL

        # Team
        team = rec.get('Team__c') if rec.get('Team__c') else ''

        # Below information will be created if its a new lead or else the information will be updated
        lead.google_rep_name = rep_name
        lead.google_rep_email = rep_email if rep_email else settings.DEFAULT_LEAD_OWNER_EMAIL

        if rep_email and rep_name:
            # Save Google representatives information to Database
            try:
                GoogeRepresentatives.objects.get(email=rep_email)
            except ObjectDoesNotExist:
                google_rep = GoogeRepresentatives()
                rep_name = rep_name.split(' ')
                google_rep.first_name = unicode(rep_name[0])
                google_rep.last_name = unicode((' ').join(rep_name[1:]))
                google_rep.email = unicode(rep_email)
                google_rep.team = team
                google_rep.save()

        # Save Regalix representatives information to Database
        if lead_owner_email and lead_owner_name:
            try:
                RegalixRepresentatives.objects.get(email=lead_owner_email)
            except ObjectDoesNotExist:
                regalix_rep = RegalixRepresentatives()
                regalix_rep.name = lead_owner_name
                regalix_rep.email = lead_owner_email
                regalix_rep.team = team
                regalix_rep.save()

        # check if column is formatted to date type
        # if it is of date type, convert to datetime object
        created_date = rec.get('CreatedDate')
        created_date = SalesforceApi.salesforce_date_to_datetime_format(created_date)
        if not created_date:
            created_date = datetime.utcnow()

        lead.created_date = created_date

        try:
            lead.ecommerce = int(rec.get('E-commerce'))
        except Exception:
            lead.ecommerce = 0

        lead.lead_owner_name = lead_owner_name if lead_owner_name else "%s %s" % (settings.DEFAULT_LEAD_OWNER_FNAME,
                                                                                  settings.DEFAULT_LEAD_OWNER_LNAME)
        lead.lead_owner_email = lead_owner_email if lead_owner_email else settings.DEFAULT_LEAD_OWNER_EMAIL
        lead.company = unicode(rec.get('Company'))
        lead.country = rec.get('Location__c')

        cid = rec.get('Customer_ID__c')
        if type(cid) is float:
            lead.customer_id = int(cid)
        else:
            lead.customer_id = cid

        lead.first_name = unicode(rec.get('FirstName'))
        lead.last_name = unicode(rec.get('LastName'))
        lead.phone = unicode(rec.get('Phone'))

        lead.first_name_optional = unicode(rec.get('First_Name_optional__c'))
        lead.last_name_optional = unicode(rec.get('Last_Name_optional__c'))
        lead.phone_optional = unicode(rec.get('Phone_optional__c'))
        lead.email_optional = unicode(rec.get('Email_optional__c'))

        # check if column is formatted to date type
        # if it is of date type, convert to datetime object
        date_of_installation = rec.get('Date_of_installation__c')
        date_of_installation = SalesforceApi.salesforce_date_to_datetime_format(date_of_installation)
        lead.date_of_installation = date_of_installation

        appointment_date = rec.get('Appointment_Date__c')
        appointment_date = SalesforceApi.salesforce_date_to_datetime_format(appointment_date)
        lead.appointment_date = appointment_date

        if rec.get('IST_TIME_N__c'):
            appointment_date_in_ist = rec.get('IST_TIME_N__c')
            appointment_date_in_ist = SalesforceApi.salesforce_date_to_datetime_format(appointment_date_in_ist)
            lead.appointment_date_in_ist = appointment_date_in_ist

        first_contacted_on = rec.get('X1st_Contact_on__c')
        first_contacted_on = SalesforceApi.salesforce_date_to_datetime_format(first_contacted_on)
        lead.first_contacted_on = first_contacted_on

        # Rescheduled Appointments
        rescheduled_appointment = rec.get('Rescheduled_Appointments__c')
        rescheduled_appointment = SalesforceApi.salesforce_date_to_datetime_format(rescheduled_appointment)
        lead.rescheduled_appointment = rescheduled_appointment

        # Rescheduled Appointments in IST
        rescheduled_appointment_in_ist = rec.get('Reschedule_IST__c')
        rescheduled_appointment_in_ist = SalesforceApi.salesforce_date_to_datetime_format(rescheduled_appointment_in_ist)
        lead.rescheduled_appointment_in_ist = rescheduled_appointment_in_ist

        time_zone = rec.get('Time_Zone__c') if rec.get('Time_Zone__c') else ''
        lead.time_zone = time_zone

        try:
            lead.dials = int(rec.get('qbdialer__Dials__c'))
        except Exception:
            lead.dials = 0

        lead.lead_sub_status = rec.get('Lead_Sub_Status__c')

        all_regalix_comment = unicode(rec.get('All_Regalix_Comments__c')).encode('unicode_escape')
        # all_regalix_comment = all_regalix_comment.replace('-', '').replace('\\n', ' ').replace('\\r', '')

        lead.regalix_comment = all_regalix_comment
        lead.google_comment = unicode(rec.get('Google_Comment__c')).encode('unicode_escape')

        lead.code_1 = rec.get('Code__c') if rec.get('Code__c') else ''
        lead.url_1 = rec.get('URL__c') if rec.get('URL__c') else ''
        lead.type_1 = rec.get('Code_Type__c') if rec.get('Code_Type__c') else ''
        lead.comment_1 = rec.get('Comment_1__c') if rec.get('Comment_1__c') else ''

        lead.team = team
        lead.sf_lead_id = sf_lead_id

        # Calculate TAT for each lead
        tat = 0
        if lead.lead_status == 'Implemented':
            if lead.team in settings.SERVICES:
                tat = ReportService.get_tat_by_implemented_for_service(
                    lead.date_of_installation, lead.created_date)
            else:
                tat = ReportService.get_tat_by_implemented(
                    lead.date_of_installation, lead.appointment_date, lead.created_date)
        else:
            if lead.type_1 in ['WPP', 'WPP - Nomination']:
                tat = ReportService.get_tat_by_implemented(
                    lead.date_of_installation, lead.appointment_date, lead.created_date)
            else:
                tat = ReportService.get_tat_by_first_contacted_on(
                    lead.first_contacted_on, lead.appointment_date, lead.created_date)
        lead.tat = tat
        # to store values in leads report model
        update_leads_reports(lead)
        try:
            lead.save()
            if is_new_lead:
                new_lead_saved += 1
            else:
                exist_lead_saved += 1
        except Exception as e:
            print lead.sf_lead_id, e
            if is_new_lead:
                new_lead_failed += 1
            else:
                exist_lead_failed += 1

    logging.info("**********************************************************")
    logging.info("Total leads saved to our DB: %s" % (total_leads))
    logging.info("New Leads count: %s" % (new_lead_saved))
    logging.info("New Leads Failed Count: %s" % (new_lead_failed))
    logging.info("Exist leads updated Count: %s" % (exist_lead_saved))
    logging.info("Exist lead failed to update: %s" % (exist_lead_failed))

    logging.info("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    logging.info("Total WPP leads saved to our DB: %s" % (total_wpp_leads))
    logging.info("New WPP leads saved to our DB: %s" % (new_wpp_leads))
    logging.info("Exist WPP leads updated Count: %s" % (existing_wpp_leads))
    logging.info("**********************************************************")


@kronos.register('30 * * * *')
def get_salesforce_users():
    """ Get all Users from SFDC """

    logging.info("Connecting to SFDC %s" % (datetime.utcnow()))
    sf = SalesforceApi.connect_salesforce()
    logging.info("Connect Successfully")
    user_details = sf.query_all("Select Id, Email, Name, Username from User")
    users = user_details.get('records')
    for user in users:
        details = {
            'user_id': user.get('Id'),
            'full_name': user.get('Name'),
            'email': user.get('Email'),
            'username': user.get('Username')
        }

        create_sfdc_user(details)


def create_sfdc_user(details):
    """ Create users in to db """

    try:
        user = SfdcUsers.objects.get(user_id=details.get('user_id'))
    except ObjectDoesNotExist:
        user = SfdcUsers()
    user.user_id = details.get('user_id')
    user.full_name = details.get('full_name')
    user.email = details.get('email')
    user.username = details.get('username')
    user.save()


# @kronos.register('*/30 * * * *')
# def get_appointment_and_rescheduled_leads():
#     """ Get appointment and rescheduled leads from SFDC """
#     end_date = datetime.now(pytz.UTC)    # we need to use UTC as salesforce API requires this
#     start_date = end_date - timedelta(days=20)
#     end_date = end_date + timedelta(days=7)
#     start_date = SalesforceApi.convert_date_to_salesforce_format(start_date)
#     end_date = SalesforceApi.convert_date_to_salesforce_format(end_date)
#     logging.info("Connecting to SFDC %s" % (datetime.utcnow()))
#     sf = SalesforceApi.connect_salesforce()
#     if sf:
#         logging.info("Connect Successfully")
#         logging.info("Get Appointment and Rescheduled leads form %s to %s" % (start_date, end_date))
#         select_items = settings.SFDC_FIELDS
#         # select_items = "Id, Location__c, Time_Zone__c, Rescheduled_Appointments__c, Date_of_installation__c, Status"
#         where_clause = "WHERE (Rescheduled_Appointments__c != null OR Appointment_Date__c != null) AND (CreatedDate >= %s AND CreatedDate <= %s)"\
#             % (start_date, end_date)
#         sql_query = "select %s from Lead %s" % (select_items, where_clause)
#         try:
#             all_leads = sf.query_all(sql_query)
#             logging.info("No of Leads from %s to %s is: %s" % (start_date, end_date, len(all_leads['records'])))
#             update_sfdc_leads(all_leads['records'], sf)
#         except Exception as e:
#             print e
#             logging.info("Fail to get leads from %s to %s" % (start_date, end_date))
#             logging.info("%s" % (e))


def update_sfdc_leads(records, sf):
    """ Update Appointment and Rescheduled Appointment IN IST Time """
    sf.headers.update({"Sforce-Auto-Assign": 'FALSE'})
    logging.info("Updating Leads count on SFDC - %s: %s" % (datetime.strftime(datetime.now(), '%d/%b/%Y'), len(records)))
    for lead in records:
        location = lead.get('Location__c')
        time_zone = lead.get('Time_Zone__c')
        type_1 = lead.get('Code_Type__c')
        rescheduled_appointment = lead.get('Rescheduled_Appointments__c')
        appointment_date = lead.get('Appointment_Date__c')
        appointment_in_ist = lead.get('IST_TIME_N__c')
        # appointment_in_pst = lead.get('Appointment_Time_in_PST__c')
        if rescheduled_appointment:
            sf_lead_id = lead.get('Id')
            rescheduled_appointment = SalesforceApi.salesforce_date_to_datetime_format(rescheduled_appointment)
            timezone = SalesforceApi.get_current_timezone_by_location(rescheduled_appointment, location, time_zone)
            reschedule_in_ist = SalesforceApi.convert_appointment_to_timezone(rescheduled_appointment, timezone, 'IST')

            try:
                sf.Lead.update(sf_lead_id, {'Reschedule_IST__c': reschedule_in_ist})
            except Exception as e:
                print e
                logging.info("Failed to update the Reschedule Appointment because of this reason: %s" % (e))
        if type_1 == 'WPP' and appointment_date:
            appointment_date = SalesforceApi.salesforce_date_to_datetime_format(appointment_date)
            timezone = SalesforceApi.get_current_timezone_by_location(appointment_date, location, time_zone)
            appointment_in_ist = SalesforceApi.convert_appointment_to_timezone(appointment_date, timezone, 'IST')
            # tz = SalesforceApi.get_current_timezone_of_salesforce()
            # appointment_in_pst = SalesforceApi.convert_appointment_to_timezone(appointment_date, timezone, tz.zone_name)
            try:
                sf.Lead.update(sf_lead_id, {'IST_TIME_N__c': appointment_in_ist})
            except Exception as e:
                print e
                logging.info("Failed to update the WPP Appointment because of this reason: %s" % (e))


def create_or_update_picasso_leads(records, sf):
    """ Create a new leads or update existing lead for picasso"""
    logging.info("Start saving leads to our PICASSO DB")
    total_leads = 0
    new_lead_saved = 0
    new_lead_failed = 0
    exist_lead_saved = 0
    exist_lead_failed = 0
    is_new_lead = True
    owners_list = {u.user_id: {'name': u.full_name, 'email': u.email} for u in SfdcUsers.objects.all()}
    for rec in records:
        total_leads += 1
        sf_lead_id = rec.get('Id')
        type_1 = rec.get('Code_Type__c')
        try:
            # check for existing lead
            lead = PicassoLeads.objects.get(sf_lead_id=sf_lead_id)
            is_new_lead = False
        except ObjectDoesNotExist:
            # create new lead
            is_new_lead = True
            lead = PicassoLeads()
        lead.lead_status = rec.get('Picasso_Lead_Stage__c') if rec.get('Picasso_Lead_Stage__c') else 'In Queue'
        lead.type_1 = type_1

        # Google Representative email and name
        rep_email = rec.get('Email')
        rep_name = rec.get('Google_Rep__c')

        # Lead owner name
        owner_id = rec.get('OwnerId')
        if owner_id and owner_id in owners_list:
            details = owners_list.get(owner_id)
            lead_owner_name = details.get('name')
            lead_owner_email = details.get('email')
        else:
            try:
                user_details = sf.User.get(owner_id)
                lead_owner_name = user_details.get('Name')
                lead_owner_email = user_details.get('Email')
            except ObjectDoesNotExist:
                lead_owner_name = "%s %s" % (settings.DEFAULT_LEAD_OWNER_FNAME, settings.DEFAULT_LEAD_OWNER_LNAME)
                lead_owner_email = settings.DEFAULT_LEAD_OWNER_EMAIL

        # Team
        team = rec.get('Team__c') if rec.get('Team__c') else ''

        # Below information will be created if its a new lead or else the information will be updated
        lead.google_rep_name = rep_name
        lead.google_rep_email = rep_email if rep_email else settings.DEFAULT_LEAD_OWNER_EMAIL

        if rep_email and rep_name:
            # Save Google representatives information to Database
            try:
                GoogeRepresentatives.objects.get(email=rep_email)
            except ObjectDoesNotExist:
                google_rep = GoogeRepresentatives()
                rep_name = rep_name.split(' ')
                google_rep.first_name = unicode(rep_name[0])
                google_rep.last_name = unicode((' ').join(rep_name[1:]))
                google_rep.email = unicode(rep_email)
                google_rep.team = team
                google_rep.save()

        # Save Regalix representatives information to Database
        if lead_owner_email and lead_owner_name:
            try:
                RegalixRepresentatives.objects.get(email=lead_owner_email)
            except ObjectDoesNotExist:
                regalix_rep = RegalixRepresentatives()
                regalix_rep.name = lead_owner_name
                regalix_rep.email = lead_owner_email
                regalix_rep.team = team
                regalix_rep.save()

        # check if column is formatted to date type
        # if it is of date type, convert to datetime object
        created_date = rec.get('CreatedDate')
        created_date = SalesforceApi.salesforce_date_to_datetime_format(created_date)
        if not created_date:
            created_date = datetime.utcnow()

        lead.created_date = created_date

        lead.lead_owner_name = lead_owner_name if lead_owner_name else "%s %s" % (settings.DEFAULT_LEAD_OWNER_FNAME,
                                                                                  settings.DEFAULT_LEAD_OWNER_LNAME)
        lead.lead_owner_email = lead_owner_email if lead_owner_email else settings.DEFAULT_LEAD_OWNER_EMAIL
        lead.company = unicode(rec.get('Company'))
        lead.country = rec.get('Location__c')

        cid = rec.get('Customer_ID__c')
        internal_cid = rec.get('Internal_CID_1__c')  # for live we have to change
        if type(cid) is float:
            lead.customer_id = int(cid)
        else:
            lead.customer_id = cid

        lead.internal_cid = internal_cid
        lead.first_name = unicode(rec.get('FirstName'))
        lead.last_name = unicode(rec.get('LastName'))
        lead.phone = unicode(rec.get('Phone'))

        # check if column is formatted to date type
        # if it is of date type, convert to datetime object
        date_of_installation = rec.get('Delivery_Date__c')
        date_of_installation = SalesforceApi.salesforce_date_to_datetime_format(date_of_installation)
        lead.date_of_installation = date_of_installation

        # estimated TAT for Lead
        estimated_tat = rec.get('Picasso_TAT__c')
        estimated_tat = SalesforceApi.salesforce_date_to_datetime_format(estimated_tat)
        lead.estimated_tat = estimated_tat

        lead.regalix_comment = unicode(rec.get('All_Regalix_Comments__c')).encode('unicode_escape')
        lead.google_comment = unicode(rec.get('Google_Comment__c')).encode('unicode_escape')

        lead.code_1 = rec.get('Code__c') if rec.get('Code__c') else ''
        lead.url_1 = rec.get('URL__c') if rec.get('URL__c') else ''
        lead.type_1 = rec.get('Code_Type__c') if rec.get('Code_Type__c') else ''
        lead.comment_1 = rec.get('Comment_1__c') if rec.get('Comment_1__c') else ''
        lead.additional_notes = rec.get('Additional_Notes_if_any__c') if rec.get('Additional_Notes_if_any__c') else ''
        lead.ref_uuid = rec.get('Picasso_Reference_Id__c') if rec.get('Picasso_Reference_Id__c') else ''

        lead.team = team
        lead.sf_lead_id = sf_lead_id
        lead.picasso_objective = (rec.get('Picasso_Objective__c')).replace(';', ',') if rec.get('Picasso_Objective__c') else ''
        # lead.picasso_multiple_objectives = (rec.get('Picasso_Objective__c')).replace(';', ',') if rec.get('Picasso_Objective__c') else ''
        lead.pod_name = rec.get('POD_Name__c') if rec.get('POD_Name__c') else ''
        lead.treatment_type = rec.get('Treatment_Type__c') if rec.get('Treatment_Type__c') else ''
        if rec.get('PICASSO_build_eligible__c'):
            if rec.get('PICASSO_build_eligible__c') == 'Yes':
                lead.is_build_eligible = True
            elif rec.get('PICASSO_build_eligible__c') == 'No':
                lead.is_build_eligible = False

        try:
            lead.save()
            if is_new_lead:
                new_lead_saved += 1
            else:
                exist_lead_saved += 1
        except Exception as e:
            print lead.sf_lead_id, e
            if is_new_lead:
                new_lead_failed += 1
            else:
                exist_lead_failed += 1

    logging.info("**********************************************************")
    logging.info("Total Picasso leads saved to our DB: %s" % (total_leads))
    logging.info("New Picasso Leads count: %s" % (new_lead_saved))
    logging.info("New Picasso Leads Failed Count: %s" % (new_lead_failed))
    logging.info("Exist Picasso leads updated Count: %s" % (exist_lead_saved))
    logging.info("Exist Picasso lead failed to update: %s" % (exist_lead_failed))


# @kronos.register('*/10 * * * *')
# def get_call_log_response_from_spreadsheet():
#     """ Get Current Quarter updated Leads from SFDC """

#     json_file = settings.MEDIA_ROOT + '/gtrack-test-0e3eb2372302.json'

#     json_key = json.load(open(json_file))
#     scope = ['https://spreadsheets.google.com/feeds']

#     credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'], scope)

#     gc = gspread.authorize(credentials)

#     sheet_url = settings.SPREADSHEET_URL

#     worksheet = gc.open_by_url(sheet_url).sheet1

#     db_total_records = CallLogAccountManager.objects.all().count()
#     sheet_total_records = worksheet.row_count

#     spreadsheet_records = list()
#     if db_total_records == 0:
#         for i in range(2, sheet_total_records + 1):
#             spreadsheet_records.append(worksheet.row_values(i))
#     else:
#         sheet_row_start = CallLogAccountManager.objects.all().order_by('-id')[0].sheet_row_count
#         for i in range(sheet_row_start + 1, sheet_total_records + 1):
#             spreadsheet_records.append(worksheet.row_values(i))

#     objects_list = list()
#     for record in spreadsheet_records:
#         if record[6]:
#             log_details = CallLogAccountManager()
#             log_details.username = record[8]  # record['Username']
#             log_details.seller_name = record[1]  # record['Seller Name']
#             log_details.seller_id = record[2]  # record['Seller ID']
#             log_details.phone_number = record[3]  # record['Phone Number']
#             log_details.alternate_number = record[4]  # record['Alternate Number']
#             meeting_time_in_cst = datetime.strptime(record[6], "%m/%d/%Y %H:%M:%S")

#             log_details.meeting_time = meeting_time_in_cst  # record['Meeting Time']
#             log_details.call_status = record[5]  # record['Call Status']
#             log_details.log_time_stamp = datetime.strptime(record[0], "%m/%d/%Y %H:%M:%S")  # record['Timestamp']
#             log_details.sheet_row_count = sheet_total_records
#             objects_list.append(log_details)

#     # # total records - 1 saved
#     CallLogAccountManager.objects.bulk_create(objects_list)


def update_leads_reports(lead):

    """ Create a new leads or update existing lead to generate reports """
    try:
        report_lead = LeadsReport.objects.get(sf_lead_id=lead.sf_lead_id)
    except ObjectDoesNotExist:
        report_lead = LeadsReport()

    report_lead.google_rep_name = lead.google_rep_name
    report_lead.google_rep_email = lead.google_rep_name
    report_lead.lead_owner_name = lead.lead_owner_name
    report_lead.lead_owner_email = lead.lead_owner_email
    report_lead.customer_id = lead.customer_id
    report_lead.program = lead.team
    report_lead.location = lead.country
    report_lead.tat = lead.tat
    report_lead.sf_lead_id = lead.sf_lead_id
    report_lead.language = lead.language
    report_lead.date_of_installation = lead.date_of_installation
    if lead.type_1 not in ['WPP', 'WPP - Nomination']:
        if lead.type_1 in settings.CODE_TYPE_MAPPING:
            report_lead.code_type = settings.CODE_TYPE_MAPPING[lead.type_1]
        else:
            report_lead.code_type = lead.type_1

        if lead.lead_status in settings.LEAD_STATUS_MAPPING:
            report_lead.lead_status = settings.LEAD_STATUS_MAPPING[lead.lead_status]
        elif lead.lead_status == 'Rework Required' and lead.lead_sub_status != 'RR - Inactive':
            report_lead.lead_status = 'Implemented'
        else:
            report_lead.lead_status = lead.lead_status

    report_lead.created_date = lead.created_date

    try:
        report_lead.save()
    except Exception as e:
        print e
