 // lead form controls
    $("#appointmentCheck1" ).click(function() {
      $( "#tag_appointment" ).animate({
      height: "toggle"
      }, 300, function() {
      });
    });
  
    $("#appointmentCheck2" ).click(function() {
      $( "#shopping_appointment" ).animate({
      height: "toggle"
      }, 300, function() {
      });
    });

    $("#appointmentCheck" ).click(function() {
      $( "#appointment" ).animate({
      height: "toggle"
      }, 300, function() {
      });
      if($(this).is(":checked")){
        $("#setup_datepick").val('');
        $("#setup_datepick").hide();
        $("#tag_datepick").val('');
        $("#tag_datepick").hide();
      }else{
        $("#setup_datepick").show();
        $("#tag_datepick").show();
      }

    });
    
    $("#webmasterCheck" ).click(function() {
      /* this line for uncheck other check box*/ 
      $("#tag_contact_person_name, #shop_contact_person_name").val(''); 
      $("#web_access").prop("checked", false);
      $('#webaccess-inline').hide();

      $( "#webmaster" ).animate({
      height: "toggle"
      }, 300, function() {
      });
      $( "#web-dum1, #web-dum2" ).toggle(500);
    });

    /* this line for uncheck webmasterCheck box*/ 
    $("#web_access").on('click', function() {
      $("#webmasterCheck").prop("checked", false);
      $( "#webmaster").hide();

      if($("#web_access").is(":checked")){
          $("#web_access").val(1);
          var advertiser_name = $("#advertiser_name").val();
          $("#tag_contact_person_name, #shop_contact_person_name").val(advertiser_name);
          // clear webmaster fields
          $('#webmaster_name').val('');
          $('#web_master_email').val('');
          $('#popt').val('');
      }else{
        $("#web_access").val(0);
        $("#tag_contact_person_name, #shop_contact_person_name").val('');
      }


    });
    
    $("#tagImplementation" ).click(function() {

      if($(this).children().is(':visible')){
        if($( "#shoppingSetup .check-icon" ).is(":visible") || $('#rlsaSetup .check-icon').is(":visible")){
          $("#submit_buttons").show();
          //$("#heads_up").show();
        }else{
          $("#submit_buttons").hide();
          //$("#heads_up").hide();
        }
      }else{
        $("#submit_buttons").show();
        //$("#heads_up").show();
      }

      $( "#tasks" ).animate({
      height: "toggle"
      }, 300, function() {
      });
      //$( "#tagImplementation .check-icon" ).toggle();
      $( "#tagImplementation .check-icon" ).animate({
      opacity: "toggle"
      }, 200, function() {
        if($(".tag-policies").is(":visible")){
            $(".tag-policies").hide();
            $('#tagCheckBoxs').hide();
            $("#is_tag_lead").val('no');
          }else{
            $(".tag-policies").show();
            selectedTeam = $('#team').val()
            if((selectedTeam.indexOf('ETO') != -1) || (selectedTeam.indexOf('UMM') != -1)){
              $('#tagCheckBoxs').show();
            }else{
              $('#tagCheckBoxs').hide();
            }
            $("#heads_up").show();
            $("#is_tag_lead").val('yes'); 
          }

          // Hide Heads Up section
          if($("#is_tag_lead").val() == 'no' && $("#is_shopping_lead").val() == 'no' && $("#is_rlsa_lead").val() == 'no'){
            $("#heads_up").hide();
          }

      });
    });
    
    $("#shoppingSetup" ).click(function() {
      $('#Shopping_Campaign_Setup').attr('checked', true);
      if($(this).children().is(':visible')){
        if($( "#tagImplementation .check-icon" ).is(":visible") || $('#rlsaSetup .check-icon').is(":visible")){
          $("#submit_buttons").show();
          //$("#heads_up").show();
        }else{
          $("#submit_buttons").hide();
          //$("#heads_up").hide();
        }
      }else{
        $("#submit_buttons").show();
        //$("#heads_up").show();
      }
      $( "#shoppingInfo" ).animate({
      height: "toggle"
      }, 300, function() {
      });

      $( "#shoppingSetup .check-icon" ).animate({
      opacity: "toggle"
      }, 200, function() {
          if($(".shopping-policy").is(":visible")){
            $(".shopping-policy").hide();
            $("#shoppingTerms").hide();
            $("#is_shopping_policies").attr('checked', false);
            $("#is_shopping_lead").val('no'); 
          }else{
            $(".shopping-policy").show();
            $("#heads_up").show();
            $("#is_shopping_lead").val('yes'); 
          }

        // Hide Heads Up section
        if($("#is_tag_lead").val() == 'no' && $("#is_shopping_lead").val() == 'no' && $("#is_rlsa_lead").val() == 'no'){
          $("#heads_up").hide();
        }

      });
    });

 /* start RLSA bulk implimentation code */
  $("#rlsaSetup" ).click(function() {

      if($(this).children().is(':visible')){
        if($( "#tagImplementation .check-icon" ).is(":visible") || $( "#shoppingSetup .check-icon" ).is(":visible")){
          $("#submit_buttons").show();
          $('#tagCheckBoxs').show();
          //$("#heads_up").show();
        }else{
          $("#submit_buttons").hide();
          //$("#heads_up").hide();
        }
      }else{
        $("#submit_buttons").show();
        //$("#heads_up").show();
      }

      $( "#rlsa-impl-initial1" ).animate({
      height: "toggle"
      }, 300, function() {
      });
      //$( "#tagImplementation .check-icon" ).toggle();
      $( "#rlsaSetup .check-icon").animate({opacity: "toggle"}, 200, function(){ 
        if($('.rlsa-policy').is(':visible')){
          //for closing RLSA Fields am making '' as value
          $('#internal_cid1, #user_list_id1, #rsla_bid_adjustment1, #authEmail').val('');
          $('#rlsa-impl-initial2, #rlsa-impl-initial3, #rlsa-impl-initial4, #rlsa-impl-initial5').remove();
          $('#removeRlsa_1').hide();
          $('#add_rlsa1').show();
          $(".rlsa-policy").hide();
          if($( "#tagImplementation .check-icon" ).is(":visible")){
            selectedTeam = $('#team').val()
            if((selectedTeam.indexOf('ETO') != -1) || (selectedTeam.indexOf('UMM') != -1)){
              $('#tagCheckBoxs').show();
            }else{
              $('#tagCheckBoxs').hide();
            }
          }
          $("#is_rlsa_lead").val('no');
        }else{
          var cid = $('#cid').val()
          if(cid){
          $('#internal_cid1').val($('#cid').val());
          $('#internal_cid1').attr('readonly', true);
          }
          $('#removeRlsa_1').hide();
          $('#add_rlsa1').show();
          $(".rlsa-policy").show();
          $("#heads_up").show();
          if($( "#tagImplementation .check-icon" ).is(":visible")){
            selectedTeam = $('#team').val()
            if((selectedTeam.indexOf('ETO') != -1) || (selectedTeam.indexOf('UMM') != -1)){
              $('#tagCheckBoxs').show();
            }else{
              $('#tagCheckBoxs').hide();
            }
          }
          $('#is_rlsa_lead').val('yes')
        }

        // Hide Heads Up section
        if($("#is_tag_lead").val() == 'no' && $("#is_shopping_lead").val() == 'no' && $("#is_rlsa_lead").val() == 'no'){
          $("#heads_up").hide();
        }

      });
    });
/* end of RLSA bulk implimentation code*/

    /*Shopping Comapaign changes code starts here*/

    $('#Shopping_Campaign_Setup').click(function(){
      $('#description').val('');
      $('#shopping_url').val('');
      $('#Shopping_Trobleshoot').prop('checked', false);
      $('#shopping_campaing_issues, #issues_description').val();
      $( "#shopping_trobleshooting" ).hide();
      $( ".shoppingInfo" ).animate({
      height: "toggle"
      }, 300, function() {
      });
    });

    $('#Shopping_Trobleshoot').click(function(){
      $('#issues_description').val('');
      $('#rbid, #rbidmodifier, #rbudget, #shopping_url, #mc_id, #description').val('');
      $('#Shopping_Campaign_Setup').prop('checked', false);
      $('#shopping_trobleshooting_url').val('');
      $('#mcIdCheck').prop('checked', true);
      $( ".shoppingInfo" ).hide();
      $( "#shopping_trobleshooting" ).animate({
      height: "toggle"
      }, 300, function() {
      });
    });

    $('#shopping_trobleshooting_url').focusout(function(){
      if($('#Shopping_Trobleshoot').prop('checked', true)){
        $('#shopping_url').val($('#shopping_trobleshooting_url').val());
      }else if($('#Shopping_Campaign_Setup').prop('checked', true)){
        $('#shopping_url').val('');
      }else{
        $('#shopping_url').val('');
      }
    });

    /*Shopping Comapaign changes code starts here*/

    $(".add" ).click(function() { 
      $( ".add" ).hide();
      $( ".remove" ).hide();
      id = $(this).attr('id');
      indx = id.split('_')[1];
      next_id = parseInt(indx) + 1
      $( "#task_" + indx ).animate({
      height: "toggle"
      }, 300, function() {
      });
      setTimeout(function() {
        $( "#removeTask_" + indx).show();
      }, 300); 

       setTimeout(function() {
        $("#addTask_" + next_id).show();
      }, 300); 
    });
    
    $(".remove" ).click(function() {    
      $( ".add" ).hide();
      $( ".remove" ).hide();
      id = $(this).attr('id');
      indx = id.split('_')[1];
      $('#code_type_avg_time_'+indx).html('');
      $('#code_type_avg_time_'+indx).hide('');
      next_id = parseInt(indx) + 1
      prev_id = parseInt(indx) - 1
      $("#ctype" + indx).val('');
      $("#url" + indx).val('');
      $("#code" + indx).val('');
      $("#comment" + indx).val('');
      $("#ga_setup" + indx).val('0');

      $('#ctype_campaign'+indx).hide();
      $('#is_campaign_created'+indx).prop('checked', false);
      $('#product_expectations'+indx).prop('checked', false);
      $('#campaign_implemented'+indx).prop('checked', false);

      $( "#task_" + indx).animate({
      height: "toggle"
      }, 300, function() {
      });

      setTimeout(function() {
        $("#removeTask_" + prev_id ).show();
      }, 300); 

      setTimeout(function() {
        $("#addTask_" + indx).show();
      }, 300); 
      
    });
    
    // media query for team page
    if ($(window).width() <= 767){  
      $("div.team-slider").removeClass('slider1');
    }

  $('#team').change(function(){
    var selectedTeam = $(this).val();
    $("#team_service_gce").hide();
    $('#g_cases_id').val('');
    $('#ldap').val('');
    $("#service_segment").val('');
    $('#tagCheckBoxs').hide();
    $('#tag_appointment_aware, #tag_admin_access, #tag_admin_code').prop('checked', false);
    if (selectedTeam.indexOf('Services') != -1){
      if(selectedTeam == 'Services/GCE'){
        $("#team_service_gce").show();
      }
      $(".tr_service_segment").show();
      $('label[for="g_cases_id"]').hide();
      $('label[for="service_segment"]').hide();
      $('#g_cases_id').show();
      $('#GCaseId').show();
      $("#service_segment").hide();
      //$('#ldap').hide();
      $('#tagCheckBoxs').hide();
    }else if(selectedTeam =='GCE Kickstart Reactive'){
      if (window.is_loc_changed){
        setLocations(window.locations);
        window.is_loc_changed = false;
      }
      $("#service_segment").hide();
      $("#service_segment").val('');
      $(".tr_service_segment").show();
      $('#g_cases_id').show();
      $('label[for="g_cases_id"]').show();
      $('label[for="service_segment"]').hide();
      $('#tagCheckBoxs').hide();
      //$('#ldap').hide();
    }
    else if(['ETO', 'ETO: Agency', 'ETO: Inbound', 'ETO: Outbound', 'ETO: CS'].indexOf(selectedTeam) != -1 && $('#tasks').is(':visible')){
      if (window.is_loc_changed){
        setLocations(window.locations);
        window.is_loc_changed = false;
      }
      //$('#ldap').show();
      $('#tagCheckBoxs').show();
      $("#service_segment").show();
      $("#service_segment").val('');
      $(".tr_service_segment").show();
      $('#g_cases_id').hide();

      $('label[for="g_cases_id"]').hide();
      $('label[for="service_segment"]').show();
    }else if(selectedTeam == 'UMM'){
      $("#team_service_gce").hide();
      $('#g_cases_id').val('')
      $("#service_segment").val('');
      $('#tagCheckBoxs').show();
    }else if(['ETO', 'ETO: Agency', 'ETO: Inbound', 'ETO: Outbound', 'ETO: CS'].indexOf(selectedTeam) != -1 ){
      //$('#ldap').show();
      $('#g_cases_id').hide();
      }
    else{
      if (window.is_loc_changed){
        setLocations(window.locations);
        window.is_loc_changed = false;
      }
      $(".tr_service_segment").hide();
      $('#g_cases_id').hide();
      $('#GCaseId').hide();

      $('label[for="g_cases_id"]').hide();
      $('label[for="service_segment"]').hide();
      $('#tagCheckBoxs').hide();
      //$('#ldap').hide();
    }
  });

  $('#team').trigger("change");
  
  $('#setup_lead_check').click(function() {
    $('#setup_lead_form').toggle();
  })

  function submitbtn(ths){
      $(ths).submit().attr('disabled', true);
  }

  $("#tag_contact_person_name").change(function(){
      var tag_name = $(this).val();
      $("#shop_contact_person_name").val(tag_name);
  });

  $("#shop_contact_person_name").change(function(){
    var shop_name = $(this).val();
      $("#tag_contact_person_name").val(shop_name);
  });

  $("#tag_primary_role").change(function(){
      var tag_role = $(this).val();
      $("#shop_primary_role").val(tag_role);
  });

  $("#shop_primary_role").change(function(){
      var shop_role = $(this).val();
      $("#tag_primary_role").val(shop_role);
  });

  function setLocations(newLocations){
    $("#country option").remove()
    $("#country").append('<option value="0">Market Served</option>');
    for(i=0; i<newLocations.length; i++){
      $("#country").append('<option value="' + newLocations[i]['name'] + '" location_id="' + newLocations[i]['id']+ '">'+ newLocations[i]['name'] +'</option>');
    }
    $("#country").val('0');
  }
  

function setLocationsForRegion(newLocations, countryIds){
    $("#country option").remove()
    $("#country").append('<option value="0">Market Served</option>');
    if(countryIds && countryIds.length > 0){
        for(i=0; i<newLocations.length; i++){
          if(countryIds.indexOf(newLocations[i]['id']) != -1){
           $("#country").append('<option value="' + newLocations[i]['name'] + '" location_id="' + newLocations[i]['id']+ '">'+ newLocations[i]['name'] +'</option>');
         }
        }
    }else{
        for(i=0; i<newLocations.length; i++){
          $("#country").append('<option value="' + newLocations[i]['name'] + '" location_id="' + newLocations[i]['id']+ '">'+ newLocations[i]['name'] +'</option>');
        }
    }
    
   $("#country").val('0');
  }

   //shopping check 
    $("#is_shopping_policies" ).click(function() {
        $(".shopping-policy").removeClass('error-box');
        $( "#shoppingTerms" ).animate({
        height: "toggle"
        }, 300, function() {
        });
    }); 


function validatethis(frm) {
    $(".error-txt").remove();
    $(".lead-form .form-control").removeClass('error-box');
    $('.web-access').removeClass('error-box');
    $('.error-box').removeClass('error-box');
    var check = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    var cidFormat = /^\d{3}-\d{3}-\d{4}$/;
    var phoneFormat = /^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$/;
    var numericExpression = /^[0-9]+$/;
    var emailFormat = /^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$/i; 
    var ct = 0;
    var rc = 0;
    var fix_slots = new Array();
    window.failedFields = new Array();
    window.is_error = false;

    if(window.is_reset == true){
      window.is_reset = false;
      return false;
    }
    
    grefElem = document.getElementById('gref');
    validateFiled(grefElem);
    
    emailrefElem = document.getElementById('emailref');
    validateFiled(emailrefElem);
    validateFormatField(emailrefElem, emailFormat);
    
    teamElem = document.getElementById('team');
    validateFiled(teamElem);
    // Service Segment Validation
    if ($(frm.service_segment).is(":visible")) {
      service_segmentElem = document.getElementById('service_segment');
      validateFiled(service_segmentElem);
    }
    // GcaseId validation
    if ($(frm.g_cases_id).is(":visible")) {
      gCasesIdElem = document.getElementById('g_cases_id');
      validateFiled(gCasesIdElem);
    }

    // Google Manager details validation
    teamElem = document.getElementById('team');
    validateFiled(teamElem);
    
    managerElem = document.getElementById("manager_name");
    validateFiled(managerElem);

    emailElem = document.getElementById("manager_email");
    validateFiled(emailElem);
    validateFormatField(emailElem, emailFormat)

    // Advertiser Info
    // Advertiser Name Validation
    advertiserNameElem = document.getElementById('advertiser_name');
    validateFiled(advertiserNameElem);

    aemailElem = document.getElementById('aemail');
    validateFiled(aemailElem);
    // Email Validation
    validateFormatField(aemailElem, emailFormat);

    // Advertiser Phone Validation
    phoneElem = document.getElementById('phone');
    validateFiled(phoneElem);

    // Advertiser Company Validation
    companyElem = document.getElementById('company');
    validateFiled(companyElem);

    // Customer Id validation
    cidElem = document.getElementById('cid');
    validateFiled(cidElem);
    validateFormatField(cidElem, cidFormat);

    // Advertiser Email Validation
    countryElem = document.getElementById('country');
    validateFiled(countryElem);

    // Language validation
    languageElem = document.getElementById('language');
    validateFiled(languageElem);

    // Timezone Validation
    tzoneElem = document.getElementById('tzone');
    validateFiled(tzoneElem);

    // Does the advertiser have edit access for the website or has a webmaster validation for selection
    if(document.getElementById("web_access").checked == false && document.getElementById("webmasterCheck").checked == false){
      $('.web-access').addClass('error-box');
      window.is_error = true;
    }

    // Webmaster Validation
    if(document.getElementById("webmasterCheck").checked == true){

      // Contact Person Name
      webMasterNameElem = document.getElementById('webmaster_name');
      validateFiled(webMasterNameElem);

      // Contact Person Role
      webMasterEmailElem = document.getElementById('web_master_email');
      validateFiled(webMasterEmailElem);

      // Contact Person Name
      poptElem = document.getElementById('popt');
      validateFiled(poptElem);

    }

    if($("#rlsaSetupBtn").is(":visible")){
      authEmail = document.getElementById('authEmail');
      validateFiled(authEmail);
      for( i=1; i <= $(".rlsa-codes").length; i++){
        if($("#rlsa-impl-initial" + i).is(":visible")){
            validateRLSAFields(i);
        }
      }

      if($('.rlsa-policy').is(':visible') && $('#rsla_policies1').is(':checked')==false){
         $('.rlsa-policy').addClass('error-box');
          window.is_error = true;
      }
    }

    // Tag Implementation lead form related Validation
    // validate Tag Implementation fields
    if($("#tagImplementationBtn").is(":visible")){
      // Hava an appointment 

      for( i=1; i <= $(".task").length; i++){
        if($("#task_" + i).is(":visible")){
          validateTaskFields(i);
        }
      }

      if (document.getElementById("appointmentCheck1").checked == true) {

        // Contact Person Name Validation 
        contactElem = document.getElementById('tag_contact_person_name');
        validateFiled(contactElem);

        // Contact Person Role Validation 
        roleElem = document.getElementById('tag_primary_role');
        validateFiled(roleElem);

        // Appointments Date and Time Validation
        setupDateElem = document.getElementById('tag_datepick');
        validateFiled(setupDateElem);

        if(frm.tag_datepick.value != ''){
            var slot = {
              'type' : 'TAG',
              'time' : frm.tag_datepick.value
            }
          fix_slots.push(slot)  
        }

      }else{
          frm.tag_datepick.value = '';  
      }

    }else{
      frm.tag_datepick.value = '';
    }
    
    // Check If Shopping related lead fields
    if ($('#shoppingSetupBtn').is(':visible')) {
        
       if($('.shoppingInfo').is(':visible')){
        
            rbidElem = document.getElementById('rbid');
            validateFiled(rbidElem);

            bidmodifiercontrolerElem = document.getElementById('bidmodifiercontroler');
            validateFiled(bidmodifiercontrolerElem);


            rbidinpercentageElem = document.getElementById('rbidinpercentage');
            validateFiled(rbidinpercentageElem);


            // rbidmodifierElem = document.getElementById('rbidmodifier');
            // validateFiledAllowZero(rbidmodifierElem);

            rbudgetElem = document.getElementById('rbudget');
            validateFiled(rbudgetElem);

            shoppingElem = document.getElementById('shopping_url');
            validateFiled(shoppingElem);
            
            // MC-ID Validation
            MCIDElem = document.getElementById('mcIdCheck');
            if(MCIDElem.checked == true){
                MCElem = document.getElementById('mc_id');
                validateFiled(MCElem);
            }
        }

        if($('#shopping_trobleshooting').is(':visible')){

          shoppingCampaingIssuesElem = document.getElementById('shopping_campaign_issues');
          validateFiled(shoppingCampaingIssuesElem);

          issuesDiscriptionEle = document.getElementById('issues_description');
          validateFiled(issuesDiscriptionEle);

          shoppingElem = document.getElementById('shopping_trobleshooting_url');
          validateFiled(shoppingElem);
        }

    // Hava an appointment 
    if (document.getElementById("appointmentCheck2").checked == true) {

      // Contact Person Name Validation 
      shopcontactElem = document.getElementById('shop_contact_person_name');
      validateFiled(shopcontactElem);

      // Contact Person Role Validation 
      shoproleElem = document.getElementById('shop_primary_role');
      validateFiled(shoproleElem);

      // Appointments Date and Time Validation
      setupdateElem = document.getElementById('setup_datepick');
      validateFiled(setupdateElem);

        // If Setup Date Slot Selected
        if(frm.setup_datepick.value != ''){
            var slot = {
              'type' : 'SHOPPING',
              'time' : frm.setup_datepick.value
            }
          fix_slots.push(slot)
        }
    }else{
      frm.setup_datepick.value = '';
    }

      if($("#is_shopping_policies").is(":checked")){
          $("#is_shopping_policies").val(1);
          $(".shopping-policy").removeClass('error-box');
      }else{
          $(".shopping-policy").addClass('error-box');
          window.failedFields.push($("#is_shopping_policies"));
          window.is_error = true;
          $("#is_shopping_policies").val(0);
      }

      isAgree = ensureAllPolicies()

      }else{
        // If Setup Date Slot Not Selected
        frm.setup_datepick.value = '';
      }

      // Check Box Options
      // if($("#tag_via_gtm").is(":checked")){
      //   $("#tag_via_gtm").val(1);
      // }else{
      //   $("#tag_via_gtm").val(0);
      // }

      if($("#web_access").is(":checked")){
          $("#web_access").val(1);
      }else{
        $("#web_access").val(0);
      }

      // Analytics setup check box
      $('.is_ga_setup').each(function(){
        if(!$(this).is(":visible")){
          $(this).val(0);
        }
      });

      if($('.tag-policies-aware').is(':visible')){
        if($('#tag_appointment_aware').is(':checked')){

        }else{
           window.failedFields.push($("#tag_appointment_aware"));
           window.is_error = true;
           $('.tag-policies-aware').addClass('error-box');
          
        }
      }
      if($('.tag-policies-access').is(':visible')){
        if($('#tag_admin_access').is(':checked')){
          
        }else{
           window.failedFields.push($("#tag_admin_access"));
           window.is_error = true;
           $('.tag-policies-access').addClass('error-box');
          
        }
      }
      if($('.tag-policies-code').is(':visible')){
        if($('#tag_admin_code').is(':checked')){
          
        }else{
           window.failedFields.push($("#tag_admin_code"));
           window.is_error = true;
           $('.tag-policies-code').addClass('error-box');
          
        }
      }

      // For Adwords Conversion Code code type we are validating dynamic conversion value tracking
      if($('.tag-add-policies').is(':visible')){
       if($("#add_tracking_yes[type='radio']").is(':checked') || $("#add_tracking_no[type='radio']").is(':checked') ){
        // Nothoing to do here
       }
       else{
          window.failedFields.push($("#tagAddwordsCheck"));
          window.is_error = true;
          $('#tagAddwordsCheck').addClass('error-box');
        }
      }

    if(window.is_error){
      focusElem = failedFields[0];
      $(focusElem).focus();
      return false;
    }else{
      var status = true;
      if (fix_slots.length) {
        status = check_and_create_appointment(fix_slots);
      }
      
      if (status) {
        if(window.tz_name){
            console.log(window.tz_name);
            $("#tzone").append("<option value=" + window.tz_name + "></option>").val(window.tz_name)
        }
        $('#preloaderOverlay').show();
        $('form input[type=submit]').attr('disabled', 'disabled');
      }
      //to workon picasso modal
      if(status && isBoth != 'both'){
        $("#myModal").modal();
      }
      return status;  
    $('.lead-form').delay(15000).submit();
    }
  }

function validateFiled(elem){
      // Validate Form Field
      if ($(elem).val() == "" || $(elem).val() == "0" || !$(elem).val()) {
        $(elem).addClass('error-box');
        window.failedFields.push(elem);
        window.is_error = true;
        return false;
      }
  }

function validateFiledAllowZero(elem){
  if ($(elem).val() == "" || !$(elem).val()) {
        $(elem).addClass('error-box');
        window.failedFields.push(elem);
        window.is_error = true;
        return false;
      }
}

function validateFormatField(elem, check) {
  // Validate Email Field
  if (!$(elem).val().trim().match(check)) {
      $(elem).addClass('error-box');
      window.failedFields.push(elem);
      window.is_error = true;
      return false;
    }
}

function ensureAllPolicies(){
  var isAgree = false;
  if($("#shoppingTerms").is(":visible")){
      $(".shopping-group").each(function(){
        if($(this).is(":checked")){
          isAgree = true;
        }else{
          isAgree = false;
          window.failedFields.push($(this));
          $(this).parent().addClass('error-box');
          window.is_error = true;
          return isAgree;
        }
      });
    }
    return isAgree
}

function validateTaskFields(indx){
  ctypeElem = document.getElementById('ctype' + indx);
  validateFiled(ctypeElem)

  urlElem = document.getElementById('url' + indx);
  validateFiled(urlElem)

  if($('#analyticscode' + indx).is(":visible")){
      var analyticsCodeElem = document.getElementById('analytics_code' + indx)
      validateFiled(analyticsCodeElem)
  }
  var isCampaign = document.getElementById('ctype_campaign' + indx)
  if($(isCampaign).is(':visible')){
    validateDynamicFields($('#is_campaign_created'+indx))
    validateDynamicFields($('#product_expectations'+indx))
    validateDynamicFields($('#campaign_implemented'+indx))
  }
}

function validateRLSAFields(indx){
  if($('.rlsa-impl-section').is(':visible')){

    rlsaUserListEle = document.getElementById('user_list_id' + indx);
    validateFiled(rlsaUserListEle);

    rlsaBidAdjustment = document.getElementById('rsla_bid_adjustment' + indx);
    validateFiled(rlsaBidAdjustment);

  }
}


function resetBtn(elem){
  elemId = $(elem).attr('id');
  if(elemId == 'formReset'){
    window.is_reset = true;
    window.location.reload();
  }
}

$("#mcIdCheck").click(function(){
  if($(this).is(':checked')){
      $("#mc_id").show();
  }else{
      $("#mc_id").hide();
  }
});

$("#keep_url").click(function(){
    if($(this).is(":checked")){
      var tagUrl = $("#url1").val();
      if(!tagUrl){
        $("#url1").addClass('error-box');
      }
      $("#url2, #url3, #url4, #url5").val(tagUrl);
    }else{
      $("#url2, #url3, #url4, #url5").val('');
    }
});
  
$("#webmaster_name").change(function(){
    var webmasterName = $(this).val();
    $("#tag_contact_person_name, #shop_contact_person_name").val(webmasterName);
});

$('.code_type').change(function(){

  conversionTracking()
  var selectedCodeType = $(this).val();
  selectedId = $(this).attr('id')
  selectedindex = selectedId[selectedId.length-1]

  $('#ga_setup'+selectedindex).prop('checked', false);
  $('#analytics_code'+selectedindex).val('');
  $('#analyticscode'+selectedindex).hide();
  $('#callextension'+selectedindex).hide();
  $('#call_extension'+selectedindex).prop('checked', false);
  $('#codebehaviour'+selectedindex).hide();

  $('#is_campaign_created'+selectedindex).prop('checked', false);
  $('#product_expectations'+selectedindex).prop('checked', false);
  $('#campaign_implemented'+selectedindex).prop('checked', false);
    
  $('#ctype_campaign'+selectedindex).hide();
  $('#gasetup'+selectedindex).hide();

  if (selectedCodeType.indexOf('Analytics') != -1){
    $('#gasetup'+selectedindex).show();
  }
   if(['Google Analytics Dynamic Remarketing (Retail)', 'Google Analytics Dynamic Remarketing (Non-Retail)', 'Dynamic Remarketing - Extension (non retail)', 'Dynamic Remarketing - Retail'].indexOf(selectedCodeType) != -1){
      $('#ctype_campaign'+selectedindex).show();
      $('#gasetup'+selectedindex).hide();
  }

  if(['GA Smart Goals'].indexOf(selectedCodeType) != -1){
    $("#smart-goal-messsage").show();   
  }
  if(['GA Smart Goals'].indexOf(selectedCodeType) == -1){
    $("#smart-goal-messsage").hide();   
  }

  else if(selectedCodeType.indexOf('Website Call Conversion') != -1){
      $('#callextension'+selectedindex).show();
  } else if(selectedCodeType.indexOf('RLSA Bulk Implementation') != -1){
      $('#rlsa_bulk'+selectedindex).show();
      $('#comment'+selectedindex).attr("placeholder", "Special Instructions (Optional, if there is an issue with applying RLSA to a campaign, please provide the Campaign ID for the campaign you wish to exclude)");

  }
  if(selectedCodeType.indexOf('Analytics Enhanced E-Commerce Tracking') != -1){
      $('#gasetup'+selectedindex).hide();
      $('#codebehaviour'+selectedindex).show();
  }
});

$(document).on('click', '.is_campaign_created', function() {
    thisId = $(this).attr('id');
    if($(this).is(":checked")){
        $("."+ thisId).hide().val('');
    }else{
      $("."+ thisId).show().val('');
    }
});

$(document).on('click', '.headsup-policies', function() {
    thisId = $(this).attr('id');
    if($(this).is(":checked")){
        $("#"+ thisId).val(1);
    }else{
        $("#"+ thisId).val(0);
    }
    
});

$(document).on('click', '#is_campaign_created', function() {
    thisId = $(this).attr('id');
    if($(this).is(":checked")){
        $("#"+ thisId).val(1);
    }else{
        $("#"+ thisId).val(0);
    }
    
});

// $("#tagCheck").click(function(){
//     var elem = document.getElementById('tag_via_gtm'); 
//     if(elem.checked == true){
//       for( i=1; i <= $(".task").length; i++){
//         if($("#comment" + i).is(":visible")){
//          $("#comment"+i).val('implement via GTM');
//         }
//       }
//     }else{
//       $("#comment1, #comment2, #comment3, #comment4, #comment5").val('');
//     }
// });

$(".is_ga_setup").click(function(){
    thisId = $(this).attr('id');
    selectedindex = thisId[thisId.length-1]
    $('#analyticscode'+selectedindex).hide();
    if($(this).is(":checked")){
      $('#analyticscode'+selectedindex).show();
      $(this).val(1);
    }else{
      $('#analyticscode'+selectedindex).hide();
      $('#analytics_code'+selectedindex).val('');
      $(this).val(0);
    }
});

$('#region').change(function(){
  var regionId = $('option:selected', this).attr('region_id');
  countryList = regionWiseLocations[regionId];
  console.log(countryList);
  setLocationsForRegion(window.locations, countryList);
});


/*function uncheckAllBehaviourCheckBoxs(selectedindex){
  $('#product_behaviour'+selectedindex).prop('checked', false);
  $('#cartpage_behaviour'+selectedindex).prop('checked', false);
  $('#checkout_process'+selectedindex).prop('checked', false);
  $('#transaction_behaviour'+selectedindex).prop('checked', false);
}*/

function conversionTracking(){
  var codeTypeValues = Array()
  for( i=1; i <= 5; i++){
  if($("#ctype" + i).is(":visible")){
      codeTypeValues.push($("#ctype"+i).val());
      }
   }
   console.log(codeTypeValues);
   if(codeTypeValues.indexOf('Adwords Conversion Code') != -1){
      $('.tag-add-policies').show();
   }else{
      $('.tag-add-policies').hide();
   }
}

/*Adding More RLSA Task types*/
function addMoreRLSAs(indx){
  nextIndex = indx + 1;

  rlsa = '<div class="rlsa-codes" id="rlsa-impl-initial'+nextIndex+'">' + 
            '<div class="row">' + 
                '<div class="col-md-4">' + 
                     '<input type="text" class="form-control " id="user_list_id'+nextIndex+'" name="user_list_id'+nextIndex+'" placeholder="User List ID/ Audieance ID">' + 
                '</div>' + 
                '<div class="col-md-4">' + 
                    '<input type="text" class="form-control " id="rsla_bid_adjustment'+nextIndex+'" name="rsla_bid_adjustment'+nextIndex+'" placeholder="RLSA BID Adjustment(%)">'+
                '</div>'+
                '<div class="col-md-4" >'+
                   '<p style="height:80px;text-align:left;font-size:13px;line-height:19px;color:#8c8c8c">'+
                  'Check PitchIQ or <a href="https://goto.google.com/rlsa-bid-dash" target="_blank">go/rlsa-bid-dash</a> for customer  <br> specific recomandations! we recommend at <br>least + 40%'+
                    '</p>'+
                '</div>'+
              '</div>'+
               '<div class="row">'+
                  '<div class="col-md-8 row" >'+
                    '<div class="form-heading" style="font-family:none;margin-left:17px;">&nbsp;</div>'+
                  '</div>'+
                  '<div class="col-md-4" >'
 
      add =     '<a id="add_rlsa'+nextIndex+'" class="btn std-btn task-btn" style="margin-right:10px;background:#109d59 !important;" onclick="addMoreRLSAs('+nextIndex+');"><i class="fa fa-plus-circle" ></i>Add User List</a>'
      remove =  '<a id="removeRlsa_'+nextIndex+'" class="btn std-btn task-btn remove-rlsa" style="display:none" onclick="removeRLSAs('+nextIndex+');"><i class="fa fa-minus-circle"></i>Remove User List</a>'
                  '</div>'+
        '</div>'
    $('#add_rlsa'+indx).hide();
    $('#removeRlsa_'+indx).show();
    prevIndex = indx - 1;
    $('#removeRlsa_'+ prevIndex).hide();
    if((indx=>1) &&(indx<4)){
     $(rlsa+add+remove).insertAfter($('#rlsa-impl-initial'+indx)); 
    }else{
      $(rlsa+remove).insertAfter($('#rlsa-impl-initial'+indx)); 
    }

}

function removeRLSAs(indx){
   prevIndex = indx - 1;
   nextIndex = indx + 1
   $('#rlsa-impl-initial'+nextIndex).remove();
   $('#add_rlsa'+indx).show();
   $('#removeRlsa_'+indx).hide();
   $('#removeRlsa_'+prevIndex).show();
}

function validateDynamicFields(elemId){
  if (elemId.is(':visible')){
    if (elemId.is(':checked')){
      //do nothing
    } 
    else {
       window.failedFields.push(elemId);
       window.is_error = true;
       elemId.parent().addClass('error-box');
       return false;
    }
  }

}

function rlsaInternalCIDPrepopulate(){
  if($('#rlsa-impl-initial1').is(":visible")){
    var cid = $('#cid').val()
    if(cid){
    $('#internal_cid1').val($('#cid').val());
    $('#internal_cid1').attr('readonly', true);
    }else{
      $('#internal_cid1').val('');
    $('#internal_cid1').attr('readonly', false);
    }
  }
}
/*Ends Here*/
 $('#active_campaigns').click(function(){
  if($('#active_campaigns').is(':checked')){
    $('#active_campaigns').val($('#active_campaigns').siblings().text());
    $('#paused_campaigns').val('');
  }else{
    $('#active_campaigns').val('');
  }
 })

  $('#paused_campaigns').click(function(){
  if($('#paused_campaigns').is(':checked')){
    $('#paused_campaigns').val($('#paused_campaigns').siblings().text());
    $('#active_campaigns').val('');
  }else{
    $('#paused_campaigns').val('');
  }
 })


  $("#tagImplementation").click(function(){
    if($("#tagImplementationBtn .check-icon").is(":visible") == false){
      $('#ctype1').prop('selectedIndex',0);
      $('#tagAddwordsCheck').hide();
    }
  });



  //to check whitelist cids for picasso
function checkID()
{
  var cid_to_compare = $('#cid').val().trim();
  var cid_to_compare_with = ['141-438-8038','535-500-0157','291-913-3432','759-650-0311','845-361-1984','816-734-4387','539-378-8691','452-078-8787','877-036-6027','432-061-1453','588-100-0901','503-402-2167','877-178-8841','958-233-3976','409-949-9433','746-784-4227','517-040-0654','755-792-2970','557-698-8888','659-099-9730','157-783-3226','973-969-9007','762-036-6593','693-270-0524','190-060-0082','466-193-3485','425-772-2231','868-822-2430','597-860-0811','683-499-9563','329-838-8967','472-953-3897','997-381-1253','804-003-3552','782-338-8418','801-447-7151','400-092-2301','561-356-6842','564-923-3355','134-076-6962','173-683-3119','681-282-2837','509-686-6725','815-203-3850','623-103-3242','733-957-7405','484-646-6923','795-969-9437','697-637-7295','269-646-6281','579-564-4692','604-758-8746','555-740-0042','495-388-8379','868-398-8491','715-747-7866','641-051-1033','595-839-9177','341-066-6434','386-919-9545','261-583-3028','638-411-1789','917-273-3027','444-037-7708','200-679-9542','585-529-9985','511-211-1165','785-379-9398','161-643-3483','780-660-0743','774-054-4530','629-008-8007','936-332-2862','837-189-9115','869-137-7432','223-901-1308','474-999-9659','549-850-0408','936-264-4107','824-366-6752','892-223-3684','837-358-8900','347-447-7348','678-142-2246','427-882-2119','889-774-4422','370-367-7990','875-023-3008','362-264-4028','951-044-4937','690-514-4388','545-046-6532','648-780-0812','425-363-3057','846-213-3842','557-142-2041','621-366-6105','381-936-6370','226-964-4437','375-497-7493','531-078-8820','419-222-2972','852-900-0511','520-139-9242','687-332-2848','132-083-3833','537-821-1492','851-529-9559','768-624-4057','675-955-5408','801-954-4704','872-461-1505','305-313-3735','314-325-5782','311-529-9843','571-561-1735','463-053-3731','582-387-7164','545-096-6937','292-320-0953','712-661-1638','797-358-8133','270-810-0223','521-676-6316','348-543-3426','855-009-9737','769-377-7572','177-635-5092','670-629-9628','256-416-6499','615-431-1906','573-601-1230','543-403-3188','886-601-1310','633-378-8472','540-198-8126','717-177-7168','374-421-1082','467-950-0948','302-603-3356','403-481-1154','329-855-5046','900-122-2087','227-649-9707','557-152-2282','387-593-3267','658-787-7096','299-571-1650','940-129-9007','534-656-6998','996-465-5348','234-216-6746','173-362-2591','913-372-2224','539-810-0497','511-297-7602','163-865-5488','686-251-1155','998-027-7537','991-813-3615','173-567-7080','577-768-8461','884-528-8077','514-934-4400','533-627-7481','554-587-7611','393-049-9887','634-417-7977','803-133-3037','276-566-6157','909-689-9177','810-745-5927','726-799-9677','106-170-0313','504-243-3166','625-095-5192','589-482-2563','127-299-9903','661-659-9996','174-058-8562','372-488-8922','420-154-4118','189-376-6142','699-684-4168','547-867-7673','461-015-5293','159-180-0502','689-669-9608','407-069-9871','529-880-0542','666-311-1183','832-826-6987','970-061-1640','238-489-9687','826-488-8072','429-058-8351','322-920-0320','577-580-0543','131-915-5676','426-000-0932','287-086-6293','699-706-6871','240-992-2295','825-060-0330','546-716-6574','495-276-6330','796-972-2570','739-392-2460','447-833-3938','898-338-8012','837-315-5395','460-666-6708','335-389-9182','519-137-7487','895-934-4143','642-051-1952','731-783-3702','946-172-2334','766-639-9858','180-399-9942','478-711-1883','762-189-9894','479-925-5813','393-391-1848','385-655-5065','670-588-8182','366-949-9952','952-437-7884','613-937-7156','603-129-9472','271-006-6655','268-301-1843','447-626-6992','794-505-5048','821-244-4057','918-641-1356','474-723-3402','768-973-3573','299-739-9795','585-565-5182','158-885-5933','233-710-0039','192-570-0630','297-817-7469','512-577-7919','263-086-6421','968-757-7051','272-379-9450','728-794-4373','742-206-6959','187-126-6898','932-425-5035','612-593-3397','160-003-3561','722-265-5438','162-570-0268','141-263-3178','207-175-5563','423-826-6264','993-460-0944','608-277-7687','339-461-1486','512-683-3632','658-464-4133','568-745-5238','484-455-5531','395-328-8735','653-415-5878','787-247-7176','622-061-1843','228-785-5465','222-963-3005','648-368-8581','523-782-2457','284-705-5615','862-285-5200','735-905-5753','910-496-6148','324-454-4637','338-921-1491','427-609-9373','265-566-6907','274-460-0245','145-175-5450','893-108-8984','524-475-5560','482-761-1497','864-895-5217','964-393-3402','834-084-4482','667-381-1120','471-556-6537','601-815-5702','981-111-1993','552-101-1299','302-898-8037','842-443-3931','731-494-4898','416-836-6037','626-422-2651','436-579-9331','602-262-2482','677-367-7653','497-759-9726','687-589-9038','103-864-4605','783-743-3342','204-841-1208','885-528-8232','949-080-0638','217-966-6752','287-219-9571','935-259-9698','332-648-8659','804-685-5877','972-729-9298','352-183-3876','140-693-3472','705-945-5772','577-554-4320','181-467-7081','743-130-0892','246-348-8192','456-569-9092','937-951-1146','891-609-9103','280-399-9651','144-380-0086','819-078-8982','386-355-5274','328-581-1092','224-188-8142','643-580-0958','680-525-5601','245-878-8728','953-874-4303','888-240-0035','462-699-9572','914-511-1128','624-038-8917','396-727-7227','864-019-9143','241-112-2198','218-999-9087','306-710-0343','990-174-4425','475-006-6538','954-447-7482','638-609-9128','812-565-5062','315-363-3117','944-479-9717','381-338-8308','354-459-9892','266-189-9368','353-172-2132','226-029-9344','419-738-8313','257-415-5797','507-476-6886','589-372-2857','913-741-1221','441-847-7640','230-821-1192','970-536-6575','957-771-1522','793-344-4275','439-955-5942','414-982-2827','653-810-0037','988-016-6554','931-250-0028','823-860-0816','480-410-0463','472-316-6897','611-892-2551','330-961-1143','900-251-1000','363-792-2176','255-627-7689','230-583-3267','885-944-4818','715-455-5805','637-816-6273','996-920-0609','873-813-3006','696-736-6618','185-771-1801','812-307-7462','481-511-1660','253-597-7743','531-786-6777','771-813-3246','815-618-8272','150-799-9880','470-628-8052','965-444-4647','499-806-6013','853-506-6908','517-168-8539','568-665-5337','781-878-8125','706-837-7572','583-714-4432','339-771-1960','484-533-3710','250-942-2093','514-325-5182','321-731-1863','848-481-1820','599-813-3685','724-100-0862','878-486-6912','507-956-6756','104-521-1953','424-763-3008','862-552-2258','778-509-9848','260-819-9295','854-514-4172','398-315-5151','271-995-5567','972-670-0011','427-710-0736','432-193-3266','797-763-3057','556-426-6160','313-459-9137','494-649-9787','955-234-4582','546-009-9474','959-278-8788','491-507-7335','273-080-0292','714-009-9090','873-881-1637','351-194-4574','399-887-7208','659-877-7395','683-213-3878','773-896-6623','598-856-6512','152-574-4328','236-862-2787','297-044-4453','446-198-8162','982-567-7405','736-312-2192','180-094-4668','172-354-4598','647-448-8600','978-821-1509','562-134-4212','669-890-0727','543-373-3617','220-345-5655','835-107-7157','753-707-7422','713-922-2067','576-893-3688','680-316-6441','628-639-9753','908-964-4788','282-545-5147','226-415-5941','712-874-4923','349-196-6592','650-090-0121','415-374-4552','930-602-2036','426-298-8908','777-527-7265','462-483-3689','995-364-4903','442-578-8116','758-305-5117','729-656-6662','206-914-4072','994-261-1750','853-410-0936','612-229-9947','824-658-8597','292-642-2765','526-631-1095','512-388-8402','295-049-9783','523-451-1585','112-284-4156','616-804-4043','257-569-9848','854-216-6578','163-067-7127','973-006-6203','692-008-8703','470-783-3327','574-890-0486','572-373-3239','479-053-3309','630-422-2767','439-383-3538','957-092-2412','800-179-9316','598-535-5353','969-747-7956','306-608-8123','517-757-7613','175-015-5866','684-708-8245','580-598-8358','428-884-4548','834-971-1452','987-661-1998','412-571-1973','519-617-7526','881-437-7118','350-231-1660','224-994-4352','817-139-9042','660-422-2655','678-549-9275','422-275-5047','120-046-6959','562-496-6439','180-433-3425','315-932-2900','186-883-3098','153-104-4552','652-736-6191','555-352-2144','663-956-6926','434-742-2797','564-686-6751','251-480-0413','742-622-2778','274-765-5453','816-122-2060','126-704-4188','462-862-2428','773-561-1447','854-239-9743','421-855-5897','370-913-3091','193-465-5915','241-796-6414','105-999-9966','109-443-3386','472-034-4762','432-796-6734','550-475-5516','808-926-6602','722-592-2912','727-788-8810','605-196-6678','805-494-4631','405-323-3378','765-906-6944','519-909-9343','974-226-6824','273-630-0112','585-957-7158','896-524-4760','215-925-5831','782-482-2522','741-984-4973','482-523-3549','284-949-9008','974-179-9527','485-762-2757','483-537-7321','704-166-6905','835-182-2462','478-981-1532','996-269-9654','536-154-4487','250-067-7538','603-680-0276','171-294-4816','506-805-5365','476-501-1686','502-190-0332','475-610-0087','623-788-8991','615-127-7224','306-948-8746','811-307-7658','691-843-3087','237-296-6106','451-559-9881','657-930-0858','190-376-6783','933-812-2123','877-325-5337','876-607-7057','144-252-2717','828-094-4818','916-539-9442','574-716-6190','865-029-9411','192-722-2232','241-020-0399','473-859-9618','953-288-8068','202-905-5628','314-793-3993','536-203-3869','975-332-2977','485-382-2885','535-459-9687','535-322-2367','688-766-6637','679-772-2379','187-759-9393','560-793-3799','454-872-2504','320-932-2281','544-570-0496','706-993-3771','911-178-8075','866-660-0562','864-757-7607','144-316-6754','871-094-4374','850-832-2768','321-814-4993','148-084-4597','660-469-9402','190-954-4705','631-684-4833','263-678-8603','583-517-7560','747-896-6104','143-907-7076','221-338-8291','484-140-0044','218-995-5886','477-665-5097','466-505-5932','975-477-7134','274-464-4612','938-624-4788','605-517-7678','490-910-0975','628-324-4664','789-838-8204','444-802-2951','417-818-8730','386-835-5093','508-774-4029','104-231-1047','522-904-4577','882-521-1394','429-313-3880','202-540-0318','836-799-9872','597-410-0094','567-832-2997','879-181-1369','480-429-9773','773-581-1111','774-010-0868','722-712-2842','890-905-5756','216-998-8732','153-554-4068','962-861-1743','359-349-9379','186-875-5063','223-500-0158','607-874-4713','821-046-6481','123-966-6415','191-857-7751','955-357-7261','431-692-2251','997-038-8065','165-762-2107','787-941-1763','784-243-3441','558-436-6047','339-197-7133','354-200-0606','359-285-5247','693-730-0983','709-417-7248','984-804-4767','331-463-3783','922-103-3282','962-231-1932','363-141-1165','463-531-1056','240-236-6290','922-126-6098','811-686-6534','907-384-4212','842-690-0743','130-376-6748','386-900-0822','465-398-8598','606-971-1855','467-227-7107','330-437-7876','704-613-3161','230-126-6373','884-274-4344','551-436-6823','731-869-9688','702-457-7537','639-277-7011','949-613-3631','397-146-6848','819-414-4233','865-645-5653','641-221-1844','157-111-1972','639-478-8918','804-535-5519','135-569-9481','228-221-1667','736-562-2058','993-093-3343','905-507-7497','422-336-6982','440-733-3337','523-233-3492','409-070-0525','703-976-6798','765-462-2492','840-759-9538','421-702-2533','376-267-7961','631-520-0547','684-116-6992','953-217-7491','267-800-0542','655-758-8108','222-934-4522','808-730-0648','369-772-2213','748-785-5607','837-445-5875','380-171-1055','902-887-7213','882-033-3492','243-361-1271','143-930-0608','296-596-6541','247-460-0418','674-257-7903','831-008-8317','866-745-5124','138-853-3517','748-851-1063','123-842-2695','130-879-9832','722-694-4672','828-726-6706','109-729-9052','312-157-7031','663-170-0786','349-211-1457','340-568-8776','608-350-0210','533-602-2704','906-303-3303','433-484-4608','499-736-6237','575-545-5588','907-833-3982','454-442-2589','948-007-7531','851-021-1042','857-643-3782','479-661-1190','148-176-6536','286-179-9092','435-973-3721','370-296-6021','295-827-7898','171-429-9674','568-026-6502','678-698-8725','373-937-7935','369-599-9142','771-258-8760','573-378-8988','638-976-6373','370-481-1102','919-602-2861','992-010-0787','338-041-1883','124-629-9037','414-712-2661','536-020-0010','246-752-2067','949-189-9182','229-694-4690','493-700-0487','979-670-0559','791-892-2646','539-326-6019','745-199-9042','882-567-7723','177-177-7008','248-339-9996','315-552-2843','748-094-4600','788-459-9155','926-321-1483','619-410-0951','528-681-1282','792-916-6067','319-466-6510','224-399-9022','484-535-5600','917-830-0795','651-249-9832','662-762-2607','298-625-5731','315-931-1606','556-016-6188','621-225-5451','363-039-9092','785-446-6933','262-176-6082','634-648-8062','543-416-6626','301-523-3569','393-340-0282','504-670-0635','719-438-8743','745-360-0747','370-803-3607','597-041-1907','485-717-7925','795-395-5709','949-660-0338','121-144-4982','357-849-9666','445-297-7353','289-280-0158','126-263-3127','108-786-6572','374-424-4665','239-304-4113','185-203-3425','581-671-1448','240-484-4278','560-793-3202','794-988-8555','745-290-0292','915-728-8992','688-483-3012','665-224-4737','677-495-5772','825-989-9197','785-581-1957','191-726-6961','765-129-9978','656-362-2505','751-941-1025','872-522-2853','502-050-0354','238-919-9586','888-953-3075','149-017-7992','344-415-5696','243-484-4611','285-284-4737','207-299-9445','924-871-1746','830-970-0786','548-135-5208','387-871-1968','569-846-6107','925-076-6478','871-299-9239','810-956-6141','725-745-5418','531-176-6415','436-805-5068','769-672-2626','133-686-6601','583-225-5054','944-195-5820','576-852-2265','113-223-3795','774-619-9976','360-659-9617','959-844-4500','769-533-3891','921-032-2488','900-735-5965','404-941-1682','691-695-5096','813-752-2962','711-175-5878','407-259-9133','377-496-6205','412-254-4298','175-315-5018','290-468-8147','275-804-4181','310-135-5311','329-152-2689','756-645-5603','154-440-0182','319-116-6128','732-442-2577','645-762-2123','108-605-5372','274-090-0396','488-898-8212','150-295-5561','783-245-5159','832-689-9001','978-111-1660','266-559-9308','665-283-3963','140-961-1676','417-147-7075','503-293-3034','920-593-3492','984-406-6249','597-135-5811','389-051-1162','740-355-5533','371-318-8068','724-406-6294','770-466-6636','400-141-1410','257-782-2722','573-120-0787','367-173-3035','792-789-9823','460-967-7516','151-075-5281','197-173-3547','117-396-6412','753-746-6268','669-964-4328','786-100-0387','721-418-8557','305-145-5962','724-504-4676','133-285-5418','601-812-2774','891-989-9455','820-784-4617','395-140-0425','105-751-1530','847-688-8188','627-443-3523','647-544-4042','513-177-7684','228-689-9506','690-590-0131','429-001-1430','735-957-7554','969-333-3272','664-957-7507','273-968-8026','198-406-6160','200-912-2545','729-415-5858','485-183-3027','422-095-5063','182-553-3576','640-194-4973','627-924-4508','303-385-5350','574-994-4880','451-717-7270','544-467-7196','493-267-7915','417-741-1246','216-128-8318','672-289-9400','816-686-6518','708-435-5586','988-813-3018','175-696-6865','723-343-3702','702-325-5505','168-849-9136','977-728-8823','442-739-9421','822-380-0676','955-956-6522','386-913-3870','212-246-6576','423-065-5068','265-119-9465','777-756-6008','233-324-4667','619-633-3298','412-082-2299','258-481-1590','940-190-0368','349-685-5897','746-067-7403','108-495-5204','643-464-4642','357-894-4673','841-487-7892','796-647-7808','985-974-4570','400-064-4687','994-616-6127','448-718-8358','514-885-5305','560-077-7714','494-553-3415','944-155-5503','948-604-4435','824-368-8921','494-372-2777','114-635-5818','981-741-1423','298-627-7556','772-062-2316','931-587-7900','503-730-0603','486-710-0047','205-171-1349','317-071-1068','873-580-0148','705-828-8878','484-216-6731','148-244-4030','697-604-4792','183-122-2912','473-664-4880','142-902-2176','300-218-8385','484-892-2983','211-379-9498','138-696-6646','537-253-3582','712-486-6117','694-341-1532','127-274-4727','907-204-4431','990-184-4263','461-722-2468','217-112-2020','652-768-8627','640-193-3082','813-505-5567','750-253-3895','224-168-8489','220-542-2296','972-008-8656','411-573-3482','359-597-7434','157-684-4514','809-613-3748','989-607-7483','200-761-1048','334-568-8053','799-832-2447','587-212-2508','164-406-6062','913-662-2905','367-936-6223','896-332-2873','606-643-3978','447-476-6435','398-556-6688','436-995-5645','224-479-9152','996-682-2358','295-671-1958','850-500-0608','139-875-5459','778-532-2416','563-437-7677','223-143-3127','912-610-0447','323-383-3248','635-197-7165','664-458-8905','581-192-2057','768-533-3842','795-299-9985','648-847-7385','814-041-1127','731-945-5068','978-047-7927','472-409-9927','384-921-1953','904-728-8123','183-220-0957','332-815-5573','437-179-9569','974-938-8340','597-829-9322','539-739-9557','437-080-0545','245-423-3291','639-299-9235','656-450-0743','913-475-5941','992-805-5677','907-437-7097','345-287-7917','793-156-6842','434-158-8230','876-579-9274','803-471-1773','652-110-0918','543-916-6544','175-858-8958','197-319-9557','338-403-3312','365-312-2752','343-157-7088','751-038-8005','628-946-6812','478-929-9896','749-808-8012','327-652-2050','943-939-9042','577-985-5103','473-851-1946','779-758-8531','303-126-6632','113-703-3673','712-459-9853','451-288-8657','474-146-6527','317-923-3316','508-763-3059','381-319-9202','390-476-6982','736-417-7948','948-212-2209','992-902-2297','669-401-1711','888-008-8821','677-436-6298','433-086-6572','310-196-6470','852-702-2028','304-100-0682','542-153-3445','722-236-6303','498-367-7610','414-919-9208','257-366-6265','118-844-4311','129-955-5629','472-469-9882','646-388-8394','723-049-9023','850-085-5543','189-196-6668','617-262-2048','752-364-4823','561-349-9588','866-849-9718','557-401-1855','819-821-1817','694-624-4294','170-739-9814','151-723-3196','475-780-0510','640-323-3712','140-842-2534','604-863-3037','878-130-0772','377-199-9558','581-778-8391','831-119-9262','762-991-1913','630-252-2462','117-921-1665','222-227-7693','375-715-5481','142-551-1320','502-761-1550','124-169-9715','775-595-5736','208-410-0537','745-444-4185','740-914-4263','160-098-8604','640-997-7713','968-363-3481','355-421-1971','495-700-0082','795-367-7308','956-075-5017','827-041-1752','769-783-3366','402-339-9286','445-360-0252','960-487-7941','964-296-6287','517-491-1562','429-894-4834','770-684-4933','924-485-5122','973-874-4425','898-948-8470','622-341-1376','252-608-8242','690-056-6116','733-724-4201','644-705-5411','921-095-5950','662-797-7328','193-123-3970','409-172-2822','559-599-9851','537-381-1564','161-933-3924','899-057-7223','135-364-4448','355-534-4203','809-789-9923','463-686-6718','419-061-1271','162-165-5780','779-751-1081','739-075-5177','503-800-0845','284-640-0732','655-702-2878','863-934-4095','643-590-0730','841-378-8410','542-866-6882','929-197-7573','400-755-5078','869-642-2751','639-896-6525','444-759-9657','165-071-1570','904-376-6031','730-234-4847','618-708-8971','724-010-0830','888-350-0772','576-707-7668','145-333-3921','582-394-4421','217-432-2526','258-497-7117','288-372-2172','511-884-4531','171-416-6434','718-821-1772','351-026-6807','597-786-6548','961-226-6089','433-008-8920','167-309-9948','397-888-8830','630-685-5293','737-676-6842','851-833-3772','926-121-1955','811-900-0423','534-214-4308','547-107-7685','493-054-4755','929-115-5563','104-687-7243','761-074-4535','989-548-8118','968-673-3552','118-231-1961','817-375-5937','508-376-6723','981-601-1490','759-399-9598','560-929-9697','924-918-8260','351-006-6472','931-227-7141','772-940-0305','430-779-9242','990-643-3144','436-593-3805','401-565-5528','340-694-4867','241-401-1676','200-693-3461','802-049-9374','907-068-8635','958-568-8832','571-853-3955','807-955-5245','486-759-9428','160-447-7171','964-003-3130','124-720-0972','201-706-6873','646-587-7340','639-841-1102','652-239-9252','924-295-5037','294-777-7231','818-088-8443','440-740-0241','564-655-5284','622-077-7555','444-269-9028','257-482-2019','861-106-6166','526-525-5177','970-177-7523','484-687-7955','882-677-7240','305-994-4357','615-711-1745','748-399-9595','719-183-3677','462-440-0848','180-135-5728','418-089-9561','721-559-9365','710-726-6277','751-936-6698','353-250-0335','392-260-0388','741-920-0977','681-187-7401','180-320-0045','192-943-3603','742-174-4398','380-639-9917','442-221-1587','451-574-4346','970-334-4313','487-324-4007','653-818-8640','332-082-2633','790-133-3045','642-954-4247','944-570-0129','246-936-6677','629-684-4741','754-314-4181','818-306-6250','545-170-0070','361-598-8442','185-726-6319','169-130-0407','206-929-9018','730-491-1613','807-257-7602','817-196-6536','821-412-2308','324-536-6603','687-046-6603','608-145-5396','448-683-3527','877-086-6532','289-855-5144','769-135-5213','908-419-9771','650-601-1464','219-879-9253','285-689-9777','127-747-7295','611-769-9486','478-949-9467','894-339-9402','832-510-0456','883-799-9952','361-410-0502','397-921-1570','183-177-7563','303-776-6492','101-750-0751','595-160-0155','285-398-8243','846-505-5043','401-790-0132','373-560-0768','878-304-4497','397-289-9438','118-951-1901','880-780-0923','283-233-3723','688-359-9057','964-753-3079','670-974-4885','149-561-1295','655-948-8765','706-382-2023','296-265-5735','707-604-4706','846-179-9037','745-167-7732','792-744-4240','446-837-7550','864-633-3942','607-983-3753','521-686-6909','610-459-9908','188-032-2138','657-865-5765','656-697-7855','527-621-1243','873-168-8511','480-736-6827','641-573-3833','299-402-2435','534-469-9448','358-805-5601','521-944-4592','514-695-5345','731-690-0462','360-536-6233','395-445-5723','530-345-5618','910-767-7087','263-697-7141','628-493-3178','762-090-0662','632-000-0590','791-623-3192','634-235-5467','964-649-9976','219-487-7627','897-144-4950','269-861-1043','432-308-8437','212-850-0345','456-697-7015','992-747-7392','309-934-4348','903-575-5888','874-322-2447','851-647-7461','745-790-0296','223-519-9738','315-830-0031','510-598-8161','496-731-1668','373-236-6695','360-379-9026','873-596-6327','710-595-5691','277-779-9282','491-891-1652','118-249-9446','805-168-8925','486-881-1813','834-112-2848','705-086-6698','817-277-7513','570-848-8267','612-555-5009','471-428-8957','687-896-6230','537-989-9916','743-225-5842','780-208-8704','323-337-7640','796-435-5572','572-905-5467','547-489-9778','976-293-3841','449-360-0010','198-554-4167','405-770-0601','969-149-9263','139-515-5811','364-735-5426','339-888-8913','584-234-4499','755-421-1968','756-334-4578','937-639-9450','468-778-8257','898-852-2667','472-766-6736','640-968-8678','263-386-6868','235-212-2663','400-463-3987','479-564-4553','714-031-1978','397-484-4437','920-613-3236','893-322-2144','652-229-9988','567-078-8829','359-584-4849','517-011-1068','306-685-5941','302-490-0061','564-069-9983','306-150-0402','697-485-5137','251-017-7304','452-316-6343','362-887-7215','248-259-9422','155-534-4056','798-669-9798','933-531-1693','781-311-1014','842-911-1456','828-265-5401','873-135-5313','226-697-7670','783-727-7153','531-926-6473','247-815-5243','289-648-8668','514-810-0814','998-753-3566','946-428-8023','970-124-4156','732-047-7837','713-351-1840','913-977-7737','825-583-3392','230-339-9632','366-476-6353','691-531-1207','385-332-2683','989-208-8422','256-584-4826','838-164-4257','413-280-0001','357-738-8844','627-662-2657','397-909-9257','915-835-5840','665-580-0913','709-471-1441','808-057-7190','111-837-7806','836-807-7907','144-623-3232','640-953-3075','364-556-6395','212-848-8141','156-476-6545','936-109-9113','447-963-3880','909-970-0810','943-128-8960','689-780-0793','552-484-4955','844-107-7197','378-927-7052','457-029-9358','964-292-2043','401-752-2981','650-071-1331','745-179-9674','260-922-2289','788-588-8350','774-923-3280','739-516-6535','516-062-2797','397-387-7418','785-260-0160','728-421-1466','155-289-9412','446-284-4301','337-696-6714','329-404-4877','171-471-1598','645-642-2501','991-880-0280','388-285-5439','705-328-8888','403-103-3251','303-182-2026','449-985-5588','967-102-2379','614-141-1321','151-588-8908','884-157-7929','435-459-9420','900-257-7534','990-139-9831','672-046-6165','111-122-2461','415-464-4203','562-622-2216','690-728-8192','401-103-3943','226-149-9135','951-845-5587','238-542-2732','263-071-1953','994-145-5717','630-870-0568','894-634-4938','519-311-1754','438-686-6150','915-581-1177','941-748-8223','411-306-6986','716-246-6990','633-469-9080','968-121-1759','749-497-7364','111-065-5237','212-030-0323','516-337-7618','211-615-5638','667-892-2008','546-646-6118','699-213-3427','877-642-2685','592-173-3465','913-479-9817','792-817-7162','989-298-8527','555-049-9883','175-872-2007','312-859-9001','553-334-4863','237-502-2268','240-494-4091','931-603-3031','380-683-3436','887-031-1528','434-212-2247','271-577-7751','194-759-9275','827-937-7641','742-254-4026','644-735-5657','856-049-9411','980-208-8663','670-427-7790','829-289-9521','836-936-6454','921-566-6978','352-681-1338','487-488-8959','222-145-5541','342-393-3441','146-342-2915','812-529-9718','192-222-2915','943-728-8142','216-202-2931','835-393-3734','288-802-2566','840-430-0225','896-090-0842','887-588-8806','167-163-3742','606-365-5108','573-846-6055','786-543-3257','118-371-1447','330-858-8812','695-084-4848','301-763-3107','591-288-8096','795-847-7658','556-576-6796','601-098-8777','690-837-7803','553-970-0758','130-949-9928','539-179-9530','389-431-1041','778-664-4565','990-052-2931','361-393-3698','682-479-9629','412-428-8613','685-852-2937','321-377-7108','440-532-2754','712-777-7517','127-120-0228','564-042-2452','404-042-2694','348-715-5165','164-275-5167','397-108-8237','695-614-4918','574-945-5627','833-571-1180','774-966-6682','403-918-8446','368-757-7842','427-938-8646','714-075-5272','290-071-1112','688-667-7426','790-311-1122','721-402-2085','805-309-9476','263-391-1677','514-559-9418','205-209-9086','623-188-8281','348-321-1250','545-267-7183','455-118-8763','697-617-7085','596-372-2536','594-405-5508','124-060-0292','237-224-4891','382-812-2156','525-356-6097','305-472-2408','138-676-6766','345-275-5523','455-266-6267','395-205-5866','822-460-0975','593-569-9212','229-557-7823','481-752-2313','519-957-7381','108-234-4663','860-848-8182','342-004-4172','211-236-6675','758-601-1138','475-864-4858','905-513-3810','105-106-6971','145-223-3745','777-903-3070','459-068-8484','914-174-4442','982-074-4970','966-441-1233','716-210-0288','753-099-9697','606-654-4761','154-066-6807','105-366-6450','377-937-7574','477-140-0615','627-553-3510','173-139-9340','944-192-2210','830-982-2876','957-317-7390','699-607-7000','928-046-6822','519-016-6696','787-822-2137','362-809-9572','968-401-1857','569-525-5328','353-074-4733','615-459-9136','297-651-1186','547-851-1108','661-390-0872','596-996-6335','152-006-6791','579-286-6405','731-719-9867','801-003-3212','898-234-4857','410-137-7923','548-251-1351','345-214-4720','656-712-2513','908-591-1212','895-205-5857','594-824-4330','925-474-4621','196-010-0612','142-106-6247','216-906-6048','722-250-0408','332-046-6123','744-346-6227','880-353-3548','686-683-3245','965-342-2325','913-354-4617','240-641-1926','883-735-5847','795-728-8567','789-389-9536','151-815-5751','790-202-2463','846-671-1561','900-558-8810','555-377-7751','361-301-1492','513-718-8785','967-826-6700','787-902-2231','899-177-7421','985-185-5572','523-365-5972','464-145-5550','455-376-6537','830-130-0698','693-882-2112','437-801-1541','872-795-5214','694-637-7545','141-079-9227','697-988-8085','347-715-5341','814-071-1093','247-197-7217','751-452-2773','301-409-9901','767-170-0597','504-286-6276','991-122-2681','378-329-9188','982-132-2283','470-869-9953','218-367-7086','312-049-9316','658-225-5237','805-164-4782','639-489-9290','217-664-4702','845-078-8358','786-034-4662','542-038-8267','195-195-5137','524-985-5511','427-080-0042','388-688-8218','400-299-9249','509-526-6397','735-979-9585','319-009-9388','450-387-7423','748-935-5778','343-972-2541','867-292-2765','543-584-4480','164-546-6487','307-131-1011','570-245-5195','956-362-2067','454-101-1842','185-316-6912','822-893-3938','558-934-4522','850-610-0037','163-573-3362','471-387-7433','709-272-2368','967-223-3976','755-158-8985','831-263-3845','408-779-9702','857-215-5175','698-090-0568','964-513-3708','220-426-6038','704-965-5441','792-527-7385','310-827-7547','914-188-8822','911-558-8447','615-906-6387','163-215-5035','641-354-4028','238-289-9470','183-794-4736','613-556-6103','817-978-8252','493-325-5143','556-972-2034','675-852-2168','886-160-0141','909-838-8203','202-608-8853','460-666-6215','654-711-1103','889-424-4629','817-981-1685','796-669-9932','860-837-7882','729-654-4658','498-547-7981','410-511-1198','716-310-0649','584-283-3458','240-315-5565','268-493-3065','692-236-6021','760-603-3743','948-309-9427','606-242-2085','799-142-2357','636-825-5172','618-161-1789','277-001-1077','937-742-2360','339-079-9487','466-445-5108','197-131-1953','977-668-8889','760-667-7386','764-834-4437','953-582-2643','335-320-0057','244-283-3617','484-047-7258','790-290-0032','597-093-3448','156-566-6128','866-547-7093','727-211-1063','175-456-6497','385-959-9282','913-714-4357','768-721-1376','806-660-0386','773-162-2262','326-266-6884','953-460-0447','102-834-4808','719-317-7963','260-349-9446','741-441-1982','709-422-2617','351-789-9622','163-794-4092','706-274-4766','536-343-3917','887-141-1798','162-811-1897','452-160-0228','229-772-2787','301-998-8192','482-795-5894','963-608-8280','846-686-6893','708-199-9730','404-708-8170','264-589-9602','530-138-8063','115-158-8533','711-669-9433','491-437-7527','562-525-5064','868-001-1078','617-774-4993','539-681-1387','886-942-2232','551-799-9307','765-465-5982','176-345-5638','128-689-9053','857-918-8967','732-618-8123','574-264-4427','727-239-9540','424-076-6892','951-749-9018','333-544-4899','470-300-0474','402-501-1503','340-407-7441','859-610-0853','626-904-4789','455-750-0843','353-766-6596','699-107-7102','726-760-0236','658-144-4851','239-484-4367','997-455-5658','864-541-1157','666-380-0504','639-437-7662','343-278-8966','230-842-2752','276-245-5175','856-932-2701','180-759-9513','742-772-2109','310-791-1316','692-720-0528','321-475-5775','142-308-8464','504-422-2925','774-637-7961','423-230-0682','717-645-5387','563-364-4969','794-070-0877','446-806-6808','725-959-9700','110-144-4505','689-630-0645','516-137-7047','689-900-0169','601-600-0397','141-355-5657','178-349-9272','873-910-0313','670-517-7648','722-632-2566','992-884-4066','693-788-8690','809-098-8897','944-368-8475','805-617-7691','329-950-0546','462-798-8327','697-210-0225','875-328-8366','360-804-4147','974-204-4487','743-043-3417','902-864-4517','141-443-3970','618-256-6342','499-664-4541','268-729-9395','984-852-2715','483-100-0247','721-969-9063','978-174-4257','964-259-9516','744-444-4563','914-629-9724','320-803-3362','581-957-7630','960-498-8737','724-862-2123','480-924-4663','420-963-3438','336-967-7291','308-984-4490','776-431-1008','396-303-3545','420-224-4858','304-570-0036','222-325-5952','264-720-0695','365-386-6997','961-990-0391','906-207-7758','161-965-5413','925-875-5521','288-828-8586','630-966-6838','831-478-8610','889-591-1722','432-191-1108','918-247-7944','341-481-1028','719-659-9946','128-433-3874','218-732-2224','607-889-9008','901-319-9532','550-587-7581','660-953-3317','832-464-4303','690-082-2973','541-006-6332','358-710-0145','692-419-9495','706-399-9871','751-490-0032','404-421-1733','861-259-9368','744-190-0631','791-835-5808','891-605-5103','564-761-1473','727-795-5806','611-918-8916','294-867-7167','788-967-7388','723-829-9700','870-292-2162','259-728-8608','752-227-7487','437-055-5390','557-061-1388','186-902-2972','930-084-4526','331-378-8299','421-594-4036','686-211-1071','309-023-3073','729-194-4375','610-343-3182','153-850-0542','597-349-9916','804-589-9808','340-538-8610','572-967-7046','837-892-2167','530-898-8107','247-431-1871','853-914-4333','390-247-7670','104-195-5783','751-493-3137','972-525-5101','677-382-2288','482-591-1082','865-189-9068','406-806-6415','647-465-5454','335-632-2696','466-530-0976','936-500-0928','381-800-0288','368-796-6047','748-380-0113','696-789-9190','270-497-7952','829-986-6691','262-456-6577','531-854-4293','339-947-7263','848-920-0910','954-929-9962','500-931-1524','636-413-3147','404-584-4582','161-591-1856','415-837-7080','234-297-7982','844-755-5110','386-096-6247','819-844-4597','513-181-1922','417-546-6085','633-666-6808','192-468-8202','440-550-0249','540-773-3406','739-281-1434','984-287-7657','562-591-1653','572-969-9867','915-958-8230','305-486-6242','817-516-6560','405-336-6598','996-940-0911','371-169-9767','720-380-0825','448-138-8718','722-556-6602','341-741-1446','645-989-9943','723-393-3836','482-363-3801','249-911-1591','583-330-0663','567-835-5579','842-538-8595','239-332-2105','770-748-8958','378-337-7597','321-161-1235','818-266-6042','828-507-7898','827-528-8417','377-012-2782','820-392-2275','324-423-3985','895-812-2537','374-651-1826','728-869-9054','170-332-2473','665-557-7272','497-176-6131','835-025-5384','765-483-3547','827-070-0697','920-804-4078','299-565-5212','165-080-0146','182-891-1310','585-512-2236','488-900-0482','421-906-6320','217-914-4543','545-692-2563','994-453-3530','787-381-1654','388-886-6536','231-120-0613','595-204-4598','816-634-4882','635-881-1661','687-875-5782','475-501-1353','981-251-1581','697-740-0868','359-211-1655','435-495-5386','423-254-4128','364-842-2562','949-701-1943','221-824-4842','728-972-2895','464-828-8526','222-955-5132','586-174-4385','947-800-0642','412-886-6967','567-797-7625','957-507-7500','254-778-8422','932-405-5743','820-718-8354','200-589-9140','792-548-8087','951-062-2141','849-641-1090','542-441-1033','761-299-9895','118-598-8988','438-920-0316','166-257-7946','208-071-1985','142-884-4752','191-812-2860','678-292-2706','741-008-8648','487-050-0315','127-082-2847','153-224-4970','900-806-6040','781-511-1946','204-212-2587','191-013-3647','606-934-4698','847-594-4216','208-304-4806','158-822-2843','286-302-2336','826-568-8738','560-358-8494','246-564-4076','345-725-5236','212-077-7117','396-718-8331','846-627-7971','950-308-8332','597-313-3893','802-089-9631','254-571-1792','514-702-2125','496-463-3658','590-800-0658','897-461-1552','635-085-5462','603-831-1683','218-739-9033','574-828-8533','103-454-4057','282-046-6011','871-752-2863','357-810-0155','625-435-5332','874-593-3966','342-037-7379','795-485-5173','930-636-6152','317-150-0331','879-464-4133','569-810-0486','634-147-7721','868-550-0637','999-742-2001','293-262-2219','166-126-6498','395-350-0751','318-780-0803','687-772-2782','736-711-1566','686-321-1230','614-292-2235','189-640-0565','943-769-9575','635-187-7491','493-606-6789','824-827-7225','378-952-2225','280-777-7457','576-805-5927','241-665-5716','511-292-2885','389-654-4324','590-829-9342','375-326-6499','512-765-5614','613-943-3274','799-264-4474','455-512-2720','794-901-1203','216-104-4578','172-679-9257','138-698-8612','642-226-6906','648-952-2253','210-177-7117','354-786-6278','560-628-8869','700-214-4907','253-731-1276','320-450-0342','248-810-0878','753-829-9211','801-970-0762','975-032-2549','665-071-1347','454-221-1377','727-907-7211','265-339-9273','716-544-4118','749-809-9445','356-710-0567','679-627-7182','616-458-8388','816-396-6755','926-720-0685','988-859-9820','570-847-7440','159-483-3520','117-094-4576','237-191-1707','307-295-5533','695-967-7783','791-034-4217','166-873-3947','403-874-4566','990-318-8935','221-729-9875','546-813-3224','678-706-6466','878-377-7131','143-404-4597','235-970-0628','810-551-1978','278-741-1148','966-047-7635','641-191-1837','906-222-2635','743-018-8182','660-945-5091','686-305-5813','445-542-2887','564-005-5588','216-135-5412','884-622-2833','970-630-0483','815-302-2772','538-522-2257','768-148-8562','232-338-8464','614-993-3778','325-592-2096','751-788-8113','184-090-0457','897-181-1265','961-475-5536','602-814-4932','680-658-8943','887-760-0574','406-547-7763','938-097-7536','619-240-0927','172-492-2175','390-848-8458','996-802-2008','100-029-9768','656-817-7951','828-457-7843','531-563-3778','412-414-4792','644-340-0081','932-202-2321','399-733-3249','470-024-4688','769-024-4094','249-343-3007','295-285-5516','464-595-5232','849-135-5868','418-157-7192','219-871-1101','807-165-5993','998-651-1336','265-238-8939','178-724-4522','819-107-7636','503-133-3943','260-732-2187','479-538-8547','790-746-6427','288-447-7927','940-045-5792','254-680-0853','281-517-7063','906-211-1381','443-591-1903','477-429-9985','352-701-1198','326-186-6658','409-407-7098','129-656-6665','855-932-2347','893-469-9666','643-861-1737','974-424-4728','969-906-6363','662-309-9264','489-948-8892','435-529-9407','823-753-3377','823-793-3109','914-079-9968','623-802-2577','438-647-7688','698-894-4047','224-619-9210','764-553-3642','156-639-9609','279-351-1421','724-532-2460','276-391-1558','529-060-0792','445-666-6774','694-065-5976','941-196-6610','148-933-3747','321-044-4346','707-139-9712','870-712-2621','623-730-0717','224-124-4987','741-206-6662','800-601-1582','457-187-7842','625-620-0339','718-612-2083','206-936-6493','657-940-0410','761-267-7912','915-560-0072','341-334-4427','350-998-8180','920-984-4611','427-718-8598','354-583-3692','507-793-3028','318-010-0886','136-546-6186','733-617-7445','578-767-7187','515-766-6603','620-171-1572','216-060-0591','234-821-1515','843-242-2733','724-548-8815','950-389-9096','496-821-1402','688-351-1377','292-383-3066','485-480-0272','285-008-8892','432-896-6385','385-107-7105','844-158-8528','297-809-9021','644-592-2695','890-462-2612','141-879-9757','895-171-1720','379-183-3145','508-973-3742','664-632-2547','432-020-0314','724-060-0543','143-232-2112','254-235-5032','701-898-8822','560-832-2932','907-654-4023','551-968-8122','324-457-7286','139-431-1613','462-821-1583','623-511-1564','652-579-9498','560-035-5725','846-952-2433','219-694-4362','480-052-2415','754-450-0268','590-456-6420','978-998-8050','900-166-6245','207-689-9178','657-198-8112','836-049-9543','323-374-4622','739-051-1612','347-723-3283','132-706-6842','622-938-8960','214-062-2337','683-319-9685','138-935-5972','547-061-1927','641-524-4911','790-772-2906','976-398-8785','475-735-5764','158-702-2721','621-526-6750','788-458-8683','131-226-6055','159-822-2271','577-399-9053','982-695-5736','754-498-8484','521-577-7097','712-235-5411','294-336-6600','408-751-1608','268-817-7251','116-401-1158','521-774-4262','823-717-7622','746-328-8321','659-426-6573','190-816-6565','656-272-2267','901-652-2065','797-806-6394','497-682-2759','870-979-9213','481-019-9392','334-874-4903','313-121-1907','278-096-6486','773-521-1089','171-475-5571','931-914-4765','183-275-5347','790-592-2211','436-469-9828','941-061-1933','435-054-4968','826-133-3317','699-083-3838','950-929-9556','972-535-5522','517-266-6296','271-493-3301','642-049-9397','424-033-3779','615-192-2100','352-165-5807','607-983-3762','103-821-1735','911-345-5843','370-992-2455','614-084-4560','654-941-1753','348-411-1186','209-484-4771','827-758-8516','802-554-4567','893-184-4800','370-532-2635','384-327-7403','566-063-3884','997-950-0553','704-429-9610','368-927-7497','842-391-1335','144-892-2947','251-841-1926','370-566-6332','833-043-3638','379-812-2153','884-568-8065','319-571-1956','600-740-0448','557-615-5383','847-558-8912','285-427-7737','486-474-4582','486-503-3628','874-682-2453','827-249-9615','654-760-0846','431-515-5012','721-027-7020','313-793-3566','923-775-5295','776-867-7734','932-316-6013','907-879-9577','392-939-9576','304-365-5497','432-867-7347','835-962-2557','145-369-9668','158-596-6451','663-000-0742','861-547-7459','951-444-4206','223-713-3201','219-247-7886','833-912-2276','870-800-0068','719-140-0738','974-098-8461','308-893-3325','124-469-9782','440-641-1385','999-003-3295','539-641-1570','696-879-9152','464-431-1740','509-439-9236','531-542-2496','632-216-6475','981-657-7161','487-744-4458','218-866-6768','230-620-0057','264-711-1965','945-535-5783','414-030-0602','395-953-3443','402-188-8949','257-344-4223','602-483-3558','254-407-7801','271-260-0752','710-276-6866','892-846-6361','756-592-2748','260-412-2738','134-783-3791','532-983-3744','146-452-2023','406-419-9717','906-964-4413','323-011-1215','689-211-1576','561-604-4897','420-163-3093','452-344-4903','153-543-3736','836-140-0997','610-518-8240','247-067-7201','478-791-1348','843-389-9726','630-532-2402','644-639-9775','184-026-6687','538-230-0396','106-524-4765','783-631-1848','805-048-8161','637-364-4021','105-483-3518','802-491-1841','353-214-4217','985-966-6347','593-238-8672','139-973-3624','539-378-8601','447-961-1016','396-019-9547','377-268-8985','479-454-4080','194-127-7365','350-914-4578','392-670-0001','630-123-3745','663-224-4123','875-282-2592','605-651-1653','428-919-9433','147-102-2032','532-412-2948','842-370-0143','226-196-6797','312-993-3976','146-079-9701','734-784-4992','566-903-3400','702-299-9507','901-174-4012','565-550-0193','706-262-2850','967-384-4281','947-998-8753','915-868-8938','609-086-6818','964-693-3500','310-191-1741','239-782-2383','421-738-8063','894-979-9107','778-020-0893','889-903-3341','852-719-9251','345-685-5497','302-343-3005','403-635-5097','312-097-7707','255-621-1257','158-873-3515','962-510-0237','536-413-3353','798-352-2820','207-631-1757','224-491-1133','324-747-7112','412-047-7468','695-665-5437','820-326-6824','730-852-2471','689-066-6724','212-354-4486','532-944-4598','751-737-7401','313-834-4312','577-396-6487','207-577-7091','195-717-7920','507-720-0773','233-121-1026','580-623-3507','608-429-9745','795-816-6147','850-834-4441','305-823-3078','409-300-0513','727-137-7382','185-346-6443','628-375-5135','846-189-9472','478-380-0321','721-546-6402','878-444-4923','442-769-9401','674-285-5301','465-480-0603','683-289-9617','962-491-1218','115-475-5705','628-327-7567','140-005-5177','651-657-7147','862-999-9852','925-392-2712','642-331-1623','621-379-9718','583-677-7262','545-861-1188','448-341-1562','996-829-9992','272-036-6806','420-074-4575','503-922-2770','573-532-2077','583-926-6266','776-546-6102','683-300-0665','741-375-5280','502-257-7571','811-540-0868','962-223-3396','946-106-6295','500-070-0167','177-765-5202','615-722-2907','698-618-8187','914-160-0158','134-728-8173','627-027-7802','645-961-1392','526-432-2055','881-146-6998','574-525-5273','180-925-5652','741-697-7572','429-259-9133','586-117-7291','161-198-8543','994-226-6576','630-506-6177','133-028-8590','993-296-6183','220-898-8510','104-445-5548','463-653-3872','853-209-9660','758-952-2357','191-222-2618','258-078-8821','238-863-3343','339-491-1151','592-982-2011','330-883-3195','735-899-9595','787-068-8785','354-555-5972','445-538-8245','144-550-0342','741-020-0008','345-896-6683','404-509-9007','954-457-7396','253-542-2893','434-154-4268','124-760-0872','907-528-8616','107-867-7448','361-485-5809','237-175-5718','497-758-8581','608-440-0243','379-780-0103','593-686-6852','754-271-1993','862-709-9913','732-202-2866','223-836-6712','549-278-8571','424-433-3498','917-978-8919','266-855-5138','191-915-5261','884-314-4321','698-401-1450','733-628-8764','423-480-0240','446-480-0832','348-704-4290','637-787-7983','724-039-9389','773-341-1023','951-804-4423','337-247-7384','949-666-6878','547-517-7863','677-750-0443','421-206-6862','820-784-4062','439-129-9122','124-293-3787','231-808-8111','980-605-5931','296-475-5048','556-073-3117','319-147-7062','595-358-8111','251-628-8577','236-650-0193','576-543-3371','645-465-5288','562-230-0508','750-816-6401','974-624-4462','880-253-3576','236-564-4142','297-523-3617','725-487-7703','122-472-2461','690-625-5587','496-780-0466','957-645-5857','393-049-9226','391-654-4675','249-730-0093','931-133-3804','280-947-7387','812-132-2792','665-006-6778','696-132-2592','246-572-2770','912-918-8479','698-574-4588','715-737-7743','721-798-8807','805-406-6676','319-639-9603','800-229-9278','978-580-0733','191-752-2397','252-886-6925','749-556-6631','965-198-8567','823-947-7617','237-175-5912','636-840-0102','167-034-4531','792-184-4648','586-354-4837','172-633-3937','316-474-4313','284-488-8104','108-741-1658','464-105-5852','313-547-7758','652-096-6517','553-693-3762','402-987-7853','407-058-8898','158-159-9705','958-160-0288','403-723-3159','206-491-1898','102-274-4096','967-085-5461','271-156-6345','742-539-9460','772-491-1957','335-935-5222','446-401-1458','713-948-8546','371-306-6716','181-630-0567','448-612-2631','375-022-2472','931-565-5801','699-026-6933','993-512-2937','255-481-1927','312-646-6686','914-995-5490','472-500-0068','808-080-0862','661-922-2377','584-806-6817','306-764-4641','827-735-5061','917-542-2373','198-897-7451','659-716-6435','811-375-5747','583-675-5856','219-213-3755','789-425-5012','796-625-5762','959-914-4373','133-436-6062','872-454-4857','137-243-3008','637-630-0342','759-544-4362','908-439-9517','650-047-7757','671-957-7393','460-181-1479','907-658-8002','566-328-8387','311-312-2597','896-316-6866','289-528-8404','958-255-5252','233-548-8117','823-395-5791','633-859-9632','127-256-6193','699-738-8935','761-072-2426','294-285-5089','874-466-6267','507-516-6055','352-284-4018','133-122-2497','364-163-3448','650-545-5193','529-697-7646','528-301-1611','592-782-2183','237-999-9047','205-072-2903','374-516-6023','347-657-7087','201-246-6317','400-462-2542','953-077-7431','570-135-5885','805-723-3496','980-210-0242','721-246-6141','291-090-0797','214-033-3198','791-761-1362','875-032-2173','694-207-7523','335-421-1518','626-078-8908','855-604-4866','134-397-7301','649-265-5689','668-084-4543','925-573-3056','774-913-3537','945-013-3566','911-737-7837','895-518-8610','637-771-1263','627-717-7240','364-985-5928','486-329-9312','905-537-7378','379-827-7198','250-159-9244','789-664-4948','518-621-1228','683-511-1585','839-304-4189','409-091-1328','890-511-1775','567-172-2739','633-404-4662','690-656-6606','271-291-1787','618-505-5633','865-366-6741','868-237-7344','925-529-9848','409-503-3157','252-615-5143','819-285-5887','109-516-6088','478-292-2370','271-880-0941','649-645-5955','126-311-1724','139-618-8763','947-030-0150','158-024-4558','546-069-9431','499-061-1466','587-868-8797','952-669-9662','203-985-5255','744-462-2142','905-834-4962','766-657-7570','735-255-5844','962-948-8087','875-954-4232','216-942-2268','859-516-6757','573-732-2182','496-511-1302','344-175-5413','177-498-8057','182-792-2769','407-639-9082','491-867-7805','234-865-5957','928-098-8265','789-119-9753','948-802-2129','928-721-1387','854-786-6622','260-614-4053','787-396-6870','823-263-3989','485-999-9360','670-701-1190','142-390-0835','885-453-3987','140-132-2974','515-012-2721','803-160-0478','800-233-3232','617-202-2843','357-090-0748','583-994-4652','171-278-8462','984-281-1108','667-692-2067','704-048-8984','156-954-4875','137-218-8223','960-490-0967','304-047-7833','303-194-4315','765-761-1492','529-651-1295','666-356-6270','370-419-9637','812-497-7743','284-280-0115','520-364-4629','154-546-6462','423-712-2495','644-679-9513','410-236-6268','247-517-7616','526-181-1038','588-925-5163','365-164-4272','632-958-8292','760-165-5418','793-269-9272','567-173-3748','100-268-8199','351-757-7003','649-591-1357','985-252-2433','323-008-8268','113-399-9813','378-379-9520','574-748-8437','799-384-4578','959-111-1030','457-417-7270','299-117-7241','339-597-7193','831-520-0965','153-524-4567','736-540-0402','928-222-2152','819-270-0646','345-104-4758','473-953-3795','523-810-0071','775-071-1631','729-322-2057','473-635-5364','827-256-6045','493-908-8272','887-725-5773','974-758-8950','629-954-4862','967-012-2896','994-438-8872','508-649-9935','542-672-2917','366-182-2727','900-170-0033','568-709-9595','402-846-6844','821-660-0363','853-508-8340','904-881-1142','527-885-5030','534-037-7837','628-851-1603','831-186-6974','688-005-5553','349-944-4831','232-141-1850','867-227-7432','856-611-1630','394-853-3120','942-107-7590','634-729-9397','674-697-7743','499-724-4592','946-175-5425','480-585-5104','772-492-2425','564-343-3013','122-643-3852','748-594-4032','873-304-4472','891-895-5437','494-572-2332','194-708-8216','390-831-1548','777-167-7311','625-180-0210','746-174-4333','615-644-4965','899-804-4047','792-913-3605','541-799-9594','600-449-9658','264-955-5689','845-109-9368','119-546-6494','799-200-0517','912-501-1315','405-274-4937','549-305-5051','475-448-8283','728-479-9353','301-569-9536','505-386-6692','365-932-2287','427-511-1657','500-340-0255','655-118-8317','672-063-3283','819-968-8300','673-065-5536','756-327-7562','280-750-0100','759-109-9553','435-458-8001','793-069-9234','633-782-2198','326-282-2842','402-159-9992','775-650-0021','277-615-5291','140-899-9938','210-845-5342','280-821-1972','898-786-6941','333-976-6513','643-198-8068','364-902-2137','374-387-7235','712-763-3032','616-939-9187','907-651-1382','763-421-1072','365-345-5847','217-386-6587','121-422-2652','702-049-9206','627-789-9001','300-739-9466','970-360-0107','109-447-7926','130-201-1890','104-107-7622','387-595-5939','176-994-4678','465-839-9783','889-997-7629','538-412-2538','187-178-8549','970-569-9960','938-175-5273','381-756-6887','488-982-2386','745-408-8507','760-817-7654','689-376-6158','422-409-9815','634-048-8706','598-460-0671','612-952-2108','698-337-7143','995-992-2121','836-735-5091','758-253-3795','495-758-8142','465-243-3888','386-826-6203','994-041-1211','196-732-2379','498-183-3195','614-910-0376','332-798-8712','828-662-2221','769-931-1937','158-395-5862','279-791-1915','878-211-1523','846-662-2978','289-533-3028','833-317-7037','524-028-8905','224-629-9677','227-949-9372','993-603-3631','536-748-8768','907-367-7215','317-176-6607','923-825-5523','953-434-4652','631-862-2312','722-301-1547','902-902-2752','582-511-1432','188-832-2390','983-298-8266','806-025-5478','525-629-9126','698-140-0814','358-862-2690','828-225-5957','218-560-0673','141-951-1622','607-282-2992','266-120-0038','561-002-2296','900-732-2722','537-989-9736','251-275-5481','498-226-6057','818-031-1967','974-838-8303','990-669-9623','640-845-5535','443-163-3772','108-080-0047','856-349-9215','321-289-9188','489-111-1012','134-848-8370','253-415-5315','724-325-5261','244-821-1265','610-596-6278','268-945-5595','830-669-9483','691-753-3446','109-041-1622','412-421-1239','915-985-5737','911-525-5745','753-754-4327','713-993-3215','237-232-2393','671-876-6821','796-900-0761','293-846-6852','639-263-3363','483-408-8902','135-537-7785','843-582-2358','527-423-3597','383-162-2087','648-375-5297','210-887-7820','436-186-6408','708-150-0658','395-288-8812','985-441-1412','417-230-0878','784-690-0569','692-496-6665','813-636-6663','128-945-5038','314-629-9726','769-404-4707','917-728-8375','606-154-4503','164-414-4847','499-380-0925','978-650-0982','505-103-3756','817-335-5188','871-241-1438','573-841-1346','758-257-7644','259-981-1471','892-938-8556','281-063-3338','701-209-9140','986-411-1224','330-908-8382','162-981-1381','370-449-9890','677-630-0935','899-160-0508','127-268-8416','835-329-9419','727-161-1317','468-913-3007','709-938-8997','968-026-6498','787-196-6581','621-423-3006','162-337-7740','767-107-7034','536-810-0052','139-082-2585','439-920-0302','944-123-3066','270-879-9002','563-673-3527','348-598-8727','724-226-6731','128-818-8587','671-431-1491','665-443-3031','602-773-3047','585-800-0295','329-667-7122','226-999-9233','341-353-3454','208-038-8054','360-393-3526','860-040-0008','362-491-1347','284-467-7016','286-974-4128','146-630-0688','943-415-5682','134-566-6175','850-153-3282','172-422-2594','853-681-1282','700-093-3754','478-592-2173','318-293-3085','827-253-3315','739-979-9431','269-397-7656','970-555-5222','361-308-8083','824-106-6862','824-090-0326','324-420-0767','711-193-3273','909-916-6253','596-835-5391','857-387-7701','656-653-3502','588-815-5095','407-647-7030','150-233-3517','874-187-7380','312-297-7469','925-766-6292','474-034-4479','699-356-6393','801-066-6412','127-101-1287','815-318-8285','965-276-6975','619-507-7792','420-950-0965','547-532-2507','450-960-0235','595-906-6405','398-636-6516','630-491-1330','101-979-9917','806-517-7620','725-554-4008','400-938-8137','845-492-2760','629-719-9194','208-270-0492','249-332-2533','306-316-6007','298-482-2958','464-058-8082','292-153-3277','269-761-1346','524-241-1120','801-534-4628','114-807-7370','631-843-3994','717-558-8776','434-733-3151','752-924-4278','828-656-6440','629-686-6160','697-075-5075','364-360-0425','346-791-1865','880-425-5628','693-915-5867','539-377-7152','361-038-8087','975-064-4618','758-480-0745','293-393-3009','638-014-4218','998-323-3242','478-243-3125','990-770-0246','974-779-9586','876-709-9498','954-182-2587','323-265-5861','304-541-1585','463-601-1321','285-135-5618','251-866-6233','541-549-9171','705-948-8046','400-345-5086','269-677-7467','274-621-1327','132-696-6816','246-237-7734','695-414-4237','711-888-8906','866-352-2186','165-672-2452','280-082-2262','741-746-6013','386-927-7139','689-584-4396','359-139-9622','990-479-9697','628-894-4828','820-337-7519','254-489-9320','375-170-0376','187-772-2353','873-542-2980','845-460-0597','271-332-2643','430-702-2842','281-869-9838','866-255-5505','714-858-8592','916-555-5238','590-519-9685','528-987-7214','333-085-5762','479-988-8766','700-539-9001','467-583-3348','820-392-2738','370-570-0747','200-644-4000','615-802-2047','618-937-7736','524-434-4073','997-400-0552','134-975-5566','643-736-6807','112-249-9938','809-319-9257','546-595-5335','284-319-9852','254-647-7376','700-595-5286','166-980-0750','891-978-8965','678-770-0482','191-013-3837','678-955-5077','597-097-7633','760-615-5587','274-094-4565','383-259-9140','223-671-1306','342-956-6037','846-812-2755','388-894-4077','939-094-4223','201-189-9003','252-973-3959','665-552-2071','555-642-2160','408-519-9468','578-086-6773','655-967-7112','499-326-6576','709-919-9688','319-461-1322','970-212-2324','102-561-1882','318-770-0220','187-210-0508','855-189-9503','190-761-1328','443-716-6072','746-917-7841','403-947-7006','858-937-7586','311-528-8487','850-970-0073','210-565-5708','124-326-6980','416-012-2898','780-958-8143','781-462-2976','902-401-1154','826-329-9288','436-477-7660','427-869-9053','241-803-3787','274-454-4857','109-939-9680','608-706-6198','366-570-0643','252-334-4257','841-749-9976','802-369-9771','204-797-7866','886-944-4314','646-543-3938','687-079-9028','388-937-7226','146-349-9607','746-981-1233','903-907-7560','849-748-8974','423-401-1853','199-115-5625','806-159-9847','143-771-1057','402-401-1731','126-181-1402','697-466-6311','960-523-3998','641-572-2128','427-654-4673','263-019-9352','742-854-4168','773-662-2362','925-593-3478','655-260-0673','544-158-8262','388-713-3637','121-762-2175','338-290-0231','565-724-4747','701-898-8346','796-974-4632','136-602-2363','491-342-2957','857-616-6254','871-140-0447','826-035-5542','914-389-9592','737-234-4371','871-894-4936','958-223-3933','677-203-3175','396-374-4280','205-923-3818','103-972-2397','111-198-8322','303-715-5407','730-349-9282','359-656-6249','783-343-3115','918-044-4735','443-099-9087','249-347-7758','739-914-4361','328-040-0823','291-776-6871','941-639-9278','910-480-0463','792-105-5901','288-079-9943','323-262-2647','323-013-3201','674-848-8183','906-759-9698','733-125-5019','928-703-3513','597-918-8010','621-441-1937','124-499-9411','515-928-8966','392-722-2927','636-888-8627','644-546-6265','432-585-5748','996-078-8643','696-799-9244','874-647-7841','175-017-7191','810-434-4696','515-082-2687','805-306-6537','325-792-2962','802-176-6648','946-251-1951','187-912-2210','539-579-9248','922-343-3395','765-870-0083','189-756-6215','771-030-0018','322-189-9969','242-159-9022','847-447-7443','879-134-4747','534-916-6786','106-824-4641','690-030-0662','115-317-7772','565-586-6772','946-481-1832','118-939-9152','780-280-0767','411-077-7190','925-970-0452','815-779-9023','580-108-8001','481-306-6916','898-534-4533','992-518-8373','637-739-9492','472-255-5785','338-615-5337','346-432-2797','297-317-7288','719-256-6588','621-681-1944','300-010-0171','751-122-2616','314-270-0453','227-586-6315','993-905-5027','440-006-6938','643-687-7569','205-025-5513','601-198-8474','347-150-0976','593-896-6027','803-398-8672','660-995-5686','354-486-6587','423-217-7812','356-784-4159','539-953-3368','765-691-1538','636-272-2983','853-426-6794','746-496-6183','391-097-7381','636-550-0268','377-984-4756','196-285-5638','562-545-5518','212-808-8897','714-813-3703','424-389-9055','619-801-1322','573-226-6538','207-252-2447','516-979-9305','381-472-2407','996-291-1983','254-100-0177','913-863-3212','687-005-5569','784-957-7635','223-738-8101','250-528-8273','752-708-8578','759-389-9383','741-353-3245','280-129-9560','943-886-6926','930-439-9933','845-677-7457','649-577-7375','763-894-4585','933-740-0047','307-281-1647','465-928-8566','269-232-2915','233-695-5565','376-469-9172','687-057-7382','564-205-5224','868-926-6442','683-702-2492','529-808-8394','956-011-1762','618-931-1086','700-683-3307','107-460-0897','767-584-4803','999-732-2818','407-467-7442','807-309-9803','522-735-5298','213-920-0500','459-085-5962','945-006-6853','402-995-5148','701-024-4350','343-985-5608','472-253-3802','184-111-1057','361-794-4372','916-355-5598','384-630-0884','428-254-4315','214-976-6814','932-277-7136','446-647-7653','137-871-1975','748-680-0738','619-614-4638','963-112-2271','184-857-7133','915-425-5530','816-193-3177','302-883-3097','462-736-6070','966-424-4392','729-317-7048','921-100-0192','657-808-8081','318-992-2638','663-456-6842','116-428-8709','855-953-3161','480-677-7522','163-989-9107','316-670-0861','910-159-9673','877-060-0353','529-553-3812','725-323-3343','753-829-9887','480-131-1693','351-821-1130','181-572-2786','328-395-5173','770-990-0847','961-586-6874','639-359-9730','748-437-7234','870-577-7355','602-314-4211','673-572-2084','449-345-5712','369-556-6039','823-678-8082','138-317-7415','922-384-4941','319-411-1501','921-254-4166','800-131-1287','349-212-2888','161-428-8731','687-127-7943','568-645-5178','461-356-6036','177-655-5724','117-730-0052','915-046-6768','204-169-9825','350-554-4428','768-018-8676','739-469-9061','729-429-9575','689-104-4922','673-644-4882','840-752-2436','706-832-2937','702-503-3018','534-468-8712','437-377-7709','752-945-5466','987-199-9452','446-649-9713','390-308-8847','853-639-9592','728-104-4294','414-904-4713','663-512-2362','248-715-5535','332-512-2452','913-060-0518','304-072-2899','514-755-5870','210-696-6229','813-828-8423','968-227-7300','793-134-4726','622-024-4880','854-155-5769','507-553-3667','197-299-9328','104-129-9856','755-489-9038','643-354-4382','838-957-7605','296-115-5396','960-403-3883','523-735-5769','486-519-9017','773-369-9370','236-184-4179','472-082-2145','163-213-3445','645-651-1947','572-988-8862','478-879-9490','421-271-1092','240-334-4076','845-782-2718','462-430-0238','708-518-8807','162-596-6286','739-046-6212','524-584-4912','674-029-9592','899-701-1268','872-688-8266','771-862-2964','481-832-2724','199-886-6947','925-888-8192','773-328-8057','357-030-0494','390-223-3562','654-976-6552','343-574-4132','554-247-7562','272-246-6296','710-488-8797','686-055-5498','642-583-3177','664-042-2332','492-607-7438','533-040-0862','973-713-3592','383-193-3230','666-943-3189','805-237-7115','376-044-4462','699-507-7798','425-876-6089','358-437-7052','274-035-5845','208-270-0384','506-343-3957','920-346-6947','539-365-5549','655-390-0513','523-980-0326','897-741-1000','668-090-0512','241-976-6598','647-870-0108','429-141-1034','837-189-9241','133-892-2282','565-846-6394','594-770-0171','295-576-6064','626-577-7955','527-852-2941','182-917-7002','710-144-4024','413-354-4079','305-606-6253','647-111-1165','666-317-7047','938-488-8802','442-670-0408','544-166-6682','108-411-1533','482-791-1164','422-439-9680','431-291-1936','275-739-9615','689-788-8847','923-331-1857','683-409-9260','865-662-2835','957-288-8083','522-996-6040','477-566-6087','939-485-5559','172-362-2533','966-623-3452','146-480-0867','540-390-0213','955-091-1698','603-379-9260','349-131-1840','305-599-9543','250-607-7132','727-143-3274','784-201-1073','189-147-7969','451-821-1937','232-999-9346','112-124-4892','393-999-9173','331-037-7822','431-106-6832','578-579-9472','600-308-8257','124-662-2142','765-542-2475','893-811-1356','595-000-0987','181-240-0372','220-007-7665','600-905-5685','921-804-4922','513-144-4181','837-081-1998','302-477-7947','259-192-2008','740-282-2147','281-014-4920','952-362-2967','667-407-7322','130-496-6948','241-798-8020','835-747-7395','387-502-2883','378-378-8858','863-208-8103','572-927-7323','922-667-7705','216-356-6032','221-293-3922','393-951-1395','145-290-0163','806-012-2994','312-328-8187','308-948-8727','307-001-1828','934-082-2404','411-531-1893','349-036-6042','205-341-1842','318-569-9987','773-282-2298','659-419-9958','580-488-8673','684-628-8427','497-773-3243','963-947-7720','628-688-8837','872-491-1201','689-514-4323','944-048-8828','424-404-4102','369-880-0227','471-318-8602','950-946-6298','969-572-2360','546-439-9453','920-702-2418','275-538-8817','635-560-0125','788-113-3992','897-337-7306','589-561-1132','423-167-7698','635-895-5376','220-029-9914','218-867-7620','459-212-2027','682-074-4287','752-282-2152','249-730-0857','449-791-1131','130-095-5027','759-677-7706','755-019-9877','404-561-1775','588-346-6120','140-511-1445','836-753-3437','828-271-1758','650-244-4383','572-053-3398','550-160-0407','339-324-4801','563-990-0453','565-460-0548','319-983-3177','469-293-3932','714-657-7567','525-933-3103','713-808-8490','562-589-9401','355-799-9662','423-487-7418','168-622-2013','373-121-1330','248-596-6488','459-563-3357','660-193-3259','652-109-9504','420-750-0023','816-814-4378','291-837-7967','897-142-2841','882-723-3103','793-649-9272','577-676-6823','335-512-2429','813-363-3332','519-488-8059','898-233-3065','450-576-6823','399-185-5568','673-919-9693','863-127-7141','262-012-2578','464-105-5285','200-772-2500','467-347-7695','838-749-9263','687-590-0107','964-915-5901','965-810-0062','826-092-2362','315-343-3542','973-125-5440','507-247-7008','985-894-4214','897-120-0552','990-914-4720','566-187-7573','323-250-0730','416-454-4906','118-229-9983','222-824-4051','982-862-2582','680-097-7983','861-912-2846','975-060-0459','949-102-2871','600-506-6385','825-417-7991','709-969-9997','619-575-5323','861-761-1742','306-464-4671','218-698-8167','718-274-4561','585-748-8917','532-570-0588','978-353-3861','295-718-8278','977-046-6032','457-267-7492','340-971-1740','521-715-5458','906-531-1405','930-740-0573','595-661-1843','182-133-3143','128-434-4183','557-569-9717','506-325-5013','846-682-2910','188-268-8342','462-775-5427','719-755-5447','197-684-4242','244-727-7073','464-025-5722','853-458-8403','807-979-9861','935-247-7487','984-652-2387','935-554-4765','212-042-2433','310-353-3273','761-025-5734','886-616-6638','720-278-8122','963-599-9888','356-334-4662','994-161-1717','372-579-9350','176-024-4833','706-686-6607','951-065-5763','148-892-2526','136-296-6995','155-794-4053','580-513-3263','737-854-4533','491-523-3309','150-977-7782','121-730-0306','676-258-8232','555-159-9951','158-378-8157','907-269-9336','908-885-5723','208-455-5567','502-091-1687','716-888-8097','600-311-1487','188-878-8068','130-359-9887','156-607-7259','637-235-5213','922-322-2331','369-851-1753','421-379-9198','692-134-4103','494-930-0658','576-497-7613','774-585-5569','123-630-0187','203-966-6432','466-294-4768','674-925-5555','953-233-3664','458-745-5339','780-261-1261','165-428-8761','440-674-4957','954-093-3606','675-546-6987','638-167-7493','909-699-9029','261-149-9341','308-084-4183','201-211-1891','841-230-0757','316-394-4431','874-192-2987','470-676-6485','903-212-2469','816-247-7917','787-303-3888','453-319-9647','987-679-9980','847-401-1671','636-268-8042','349-417-7981','689-140-0768','170-024-4771','540-264-4880','412-993-3547','421-047-7417','710-617-7913','297-830-0026','999-642-2037','425-142-2396','887-215-5095','629-226-6390','604-383-3310','326-061-1542','665-584-4107','394-763-3687','983-987-7653','951-188-8991','876-412-2263','384-964-4132','625-257-7567','236-937-7692','600-033-3927','163-210-0687','619-279-9701','474-808-8132','515-148-8793','740-661-1276','693-649-9472','267-490-0935','626-923-3798','120-078-8718','443-004-4627','276-415-5196','670-018-8992','670-838-8327','735-327-7632','474-586-6104','831-990-0252','582-531-1954','119-000-0038','901-334-4577','652-662-2047','762-315-5200','222-565-5810','114-111-1717','671-666-6372','182-726-6002','839-441-1112','253-650-0962','581-770-0949','353-909-9425','946-918-8557','766-397-7867','188-034-4787','571-928-8837','694-397-7325','570-976-6137','795-059-9608','750-106-6667','469-588-8615','814-868-8343','280-878-8525','144-371-1793','311-930-0035','335-574-4733','916-773-3881','203-882-2173','383-571-1973','613-128-8486','530-804-4757','659-501-1289','897-793-3038','998-947-7888','848-670-0113','139-737-7483','140-609-9296','341-913-3562','971-970-0853','412-631-1184','273-697-7158','854-656-6423','325-533-3966','389-210-0816','212-175-5197','960-228-8352','823-031-1818','293-722-2858','491-324-4987','484-753-3977','134-044-4744','276-883-3252','760-409-9117','105-220-0360','187-029-9980','677-686-6418','689-314-4957','591-921-1046','365-233-3876','834-045-5827','472-167-7067','298-375-5811','371-199-9952','564-832-2130','379-917-7482','960-163-3943','332-513-3423','292-118-8299','120-832-2905','693-355-5550','595-676-6502','681-221-1537','551-094-4477','664-996-6660','896-169-9822','284-733-3608','426-469-9968','949-391-1472','835-275-5332','416-027-7855','684-781-1173','992-959-9338','812-929-9257','530-891-1672','549-021-1232','910-487-7347','531-504-4694','325-622-2389','557-712-2492','881-450-0288','226-402-2773','356-603-3696','286-304-4698','877-000-0301','740-658-8469','544-203-3748','409-499-9588','751-812-2058','335-344-4733','870-198-8916','916-131-1767','869-198-8632','546-844-4686','561-229-9358','711-206-6122','276-425-5343','463-423-3407','155-045-5513','462-686-6356','238-238-8521','308-994-4107','439-671-1403','430-543-3225','155-523-3022','581-050-0421','256-344-4891','758-135-5960','121-481-1557','584-993-3307','104-817-7092','490-130-0584','410-276-6077','706-664-4788','385-125-5928','365-373-3947','667-811-1131','961-833-3017','190-810-0416','299-046-6378','496-629-9148','232-734-4343','849-392-2939','924-505-5389','953-142-2904','227-530-0539','596-133-3019','309-273-3091','944-747-7343','366-352-2165','498-283-3638','534-396-6258','751-125-5573','683-237-7302','706-441-1602','109-271-1622','959-922-2318','289-527-7334','379-608-8911','717-470-0649','160-930-0992','924-576-6198','553-090-0973','197-273-3808','798-446-6622','856-053-3585','611-034-4611','900-840-0369','665-280-0827','255-051-1837','118-882-2122','266-273-3320','188-161-1038','764-894-4126','476-598-8637','546-238-8603','352-716-6613','663-318-8772','282-926-6730','829-173-3862','877-069-9810','659-984-4533','446-662-2878','637-318-8256','895-874-4779','800-163-3343','188-327-7291','426-921-1192','867-486-6080','759-879-9549','455-113-3935','468-713-3305','948-539-9517','248-107-7663','246-738-8200','119-320-0738','610-685-5268','101-962-2115','565-445-5227','969-103-3868','817-610-0467','990-433-3955','176-896-6672','649-220-0075','319-223-3657','519-183-3450','932-247-7462','320-832-2292','411-835-5083','526-596-6513','509-569-9060','950-144-4813','170-446-6459','245-958-8636','400-804-4725','542-340-0220','985-370-0484','646-720-0619','190-291-1673','401-058-8524','802-474-4437','339-175-5600','119-707-7797','101-734-4290','173-261-1893','531-333-3312','634-032-2346','426-603-3897','339-168-8973','872-072-2917','345-882-2131','144-822-2011','927-193-3353','861-216-6748','620-971-1353','211-673-3800','245-828-8719','511-914-4229','298-864-4141','381-824-4776','986-642-2823','623-640-0301','686-138-8353','237-319-9578','372-084-4182','173-653-3508','864-923-3865','377-136-6392','541-104-4409','340-879-9548','844-507-7703','345-878-8821','603-256-6872','173-689-9252','570-973-3225','291-169-9638','350-342-2148','945-531-1222','720-264-4155','494-008-8117','364-874-4992','754-607-7910','134-856-6345','552-226-6398','100-675-5603','630-967-7773','548-955-5515','576-273-3402','644-892-2842','164-702-2937','618-694-4785','600-733-3284','533-455-5092','959-098-8912','267-812-2190','794-372-2911','945-462-2958','294-546-6659','784-483-3253','396-889-9422','501-388-8646','730-614-4653','188-337-7884','751-666-6880','178-052-2226','126-382-2868','853-172-2990','301-737-7777','451-220-0683','703-621-1877','247-881-1522','626-805-5282','127-075-5185','300-544-4113','634-865-5129','409-153-3458','980-928-8132','284-471-1933','100-079-9987','726-919-9682','505-926-6597','328-553-3556','116-498-8028','409-923-3912','304-203-3947','730-655-5888','872-904-4849','267-105-5273','302-479-9285','277-506-6450','703-542-2458','838-937-7747','298-319-9702','298-488-8350','205-342-2146','937-641-1252','178-030-0867','488-588-8026','444-184-4267','395-398-8151','231-847-7277','141-550-0082','159-725-5713','229-734-4029','498-836-6485','671-770-0428','590-744-4955','189-247-7070','900-747-7028','593-815-5576','384-552-2576','159-379-9209','224-515-5341','122-707-7024','310-932-2057','961-093-3572','545-233-3212','525-124-4502','672-553-3468','591-943-3347','767-429-9076','905-961-1692','474-189-9072','622-518-8725','312-140-0765','548-806-6950','236-184-4182','358-909-9060','708-362-2987','325-102-2791','843-709-9279','672-094-4965','836-888-8667','988-150-0083','580-491-1672','677-784-4228','831-832-2595','263-347-7158','563-949-9223','705-924-4467','660-989-9528','305-892-2500','424-647-7065','485-308-8080','750-665-5561','371-643-3484','703-119-9644','923-298-8835','606-101-1554','899-370-0652','952-790-0318','423-054-4980','485-441-1313','216-880-0418','386-952-2832','268-440-0608','719-555-5997','846-936-6837','323-846-6741','699-109-9768','865-694-4610','748-247-7895','400-199-9070','722-581-1298','232-781-1900','853-187-7555','369-271-1448','505-760-0912','593-011-1168','384-986-6153','927-660-0505','319-202-2974','768-034-4294','263-794-4922','504-923-3894','123-473-3703','654-555-5908','453-480-0312','593-462-2342','102-611-1252','634-875-5702','856-541-1755','122-049-9662','244-034-4696','559-483-3502','860-767-7052','868-282-2622','766-619-9722','876-009-9283','979-674-4988','650-118-8023','850-636-6046','191-178-8932','721-976-6883','521-810-0511','227-379-9310','377-596-6859','123-120-0958','520-275-5923','530-838-8611','571-177-7561','114-134-4982','447-502-2560','380-044-4614','107-674-4718','721-833-3901','213-125-5617','502-024-4447','638-330-0332','185-647-7366','389-898-8047','851-735-5705','396-160-0946','545-720-0911','433-405-5955','368-953-3413','504-746-6103','889-687-7713','769-039-9887','390-325-5598','626-315-5495','211-534-4213','288-588-8633','608-700-0402','350-936-6312','823-117-7027','815-329-9818','823-204-4873','993-425-5268','193-791-1141','213-946-6953','271-102-2092','767-620-0843','953-184-4893','817-728-8519','462-103-3127','280-234-4439','362-571-1728','115-165-5317','259-371-1998','591-210-0155','317-146-6045','107-016-6340','115-390-0027','159-593-3113','309-739-9915','147-738-8842','804-658-8153','855-626-6227','306-262-2764','258-054-4925','762-356-6811','708-123-3900','544-568-8858','616-921-1861','761-095-5897','102-555-5441','404-100-0005','571-502-2601','338-515-5298','918-380-0750','180-298-8473','966-319-9412','707-336-6333','345-490-0893','678-174-4051','286-336-6745','620-516-6287','303-506-6116','989-045-5288','832-806-6932','600-264-4113','913-947-7857','379-736-6878','308-593-3412','110-444-4577','834-191-1530','803-995-5231','686-313-3192','388-668-8822','451-094-4780','729-038-8931','760-971-1073','338-338-8056','152-422-2443','654-643-3018','554-190-0540','584-406-6022','883-042-2352','440-396-6385','463-742-2867','508-133-3491','856-127-7727','644-007-7404','843-882-2227','830-352-2085','669-332-2668','946-463-3863','568-723-3593','620-732-2937','365-939-9483','672-977-7875','180-626-6627','480-851-1637','852-187-7199','489-808-8384','996-180-0297','595-363-3290','608-464-4452','961-340-0518','634-023-3615','154-458-8792','756-345-5058','418-000-0747','558-068-8385','112-148-8827','156-542-2367','603-091-1294','619-676-6584','819-015-5972','113-441-1021','136-747-7526','871-916-6847','797-080-0379','566-910-0684','721-152-2721','171-992-2937','843-123-3413','561-892-2420','954-006-6500','727-730-0271','457-253-3181','189-412-2855','248-629-9192','216-363-3326','840-964-4257','882-072-2158','447-019-9202','923-485-5043','407-840-0546','873-910-0194','219-585-5323','348-663-3602','534-087-7947','590-889-9365','495-825-5572','250-004-4073','189-831-1145','123-594-4254','858-714-4329','530-896-6867','316-598-8608','331-380-0269','542-867-7277','566-446-6702','663-380-0742','962-840-0086','603-859-9959','351-927-7775','994-522-2568','980-463-3311','315-461-1310','593-843-3951','611-341-1286','599-473-3962','212-631-1794','143-433-3346','195-921-1047','668-357-7105','881-601-1672','730-443-3362','819-130-0398','867-250-0601','909-792-2181','761-103-3946','844-211-1067','225-245-5896','689-908-8007','874-751-1300','494-154-4892','227-952-2018','761-030-0553','724-536-6817','459-283-3885','356-226-6562','218-923-3607','680-803-3354','997-221-1327','369-951-1125','895-969-9037','655-441-1768','666-579-9188','950-937-7792','720-744-4286','311-261-1235','352-270-0904','153-274-4900','542-796-6448','416-063-3106','508-328-8978','755-386-6336','997-700-0883','545-851-1616','904-310-0975','904-104-4342','515-305-5037','768-917-7035','177-652-2857','196-659-9542','856-887-7212','549-996-6328','644-483-3822','793-537-7690','197-492-2801','917-489-9993','576-433-3008','445-713-3853','387-355-5804','792-684-4663','100-528-8448','101-777-7535','785-869-9367','541-449-9007','235-780-0621','114-775-5340','269-155-5622','946-035-5557','249-949-9296','125-131-1516','675-133-3623','461-182-2874','576-312-2337','121-502-2172','861-656-6748','803-233-3863','332-420-0258','988-500-0265','784-174-4470','420-044-4518','211-344-4107','289-666-6732','662-940-0403','322-182-2582','883-025-5338','430-269-9983','442-495-5355','185-866-6937','524-908-8217','272-676-6466','355-553-3810','844-299-9017','339-811-1768','568-057-7977','462-917-7455','587-204-4567','258-100-0578','429-290-0906','757-375-5522','802-879-9575','729-424-4304','144-044-4097','322-532-2378','328-862-2157','726-935-5031','484-531-1543','205-911-1807','163-987-7493','594-260-0322','281-651-1837','826-582-2918','928-254-4052','819-264-4423','367-533-3944','727-932-2648','259-187-7087','430-466-6150','504-595-5337','914-781-1212','156-730-0567','952-967-7272','574-743-3136','126-559-9034','749-972-2673','222-597-7274','669-103-3540','775-383-3901','244-559-9377','417-455-5582','712-980-0997','446-086-6546','782-779-9847','261-293-3737','655-657-7470','540-597-7702','283-992-2085','640-459-9799','113-100-0688','913-737-7332','888-049-9770','358-806-6617','659-905-5837','307-104-4707','134-827-7187','875-757-7933','441-642-2787','693-210-0375','206-328-8781','320-156-6145','686-341-1578','999-820-0571','780-617-7246','245-252-2973','595-883-3520','650-139-9958','420-212-2273','413-633-3425','513-756-6358','807-848-8096','333-313-3771','804-440-0093','496-778-8576','707-796-6512','254-619-9194','880-788-8085','771-364-4419','379-255-5231','329-798-8028','561-920-0102','504-968-8312','283-428-8133','413-528-8151','239-389-9712','614-671-1567','204-682-2328','633-200-0602','563-012-2666','531-132-2563','798-188-8458','906-331-1551','669-040-0268','586-235-5693','420-054-4053','121-503-3875','716-406-6612','585-226-6159','983-738-8763','641-105-5115','907-288-8061','599-269-9712','488-336-6561','438-202-2250','901-742-2253','239-494-4305','540-336-6753','741-013-3863','548-068-8926','272-323-3817','774-004-4626','367-085-5840','552-658-8778','796-155-5181','848-287-7415','798-279-9433','786-266-6388','491-186-6932','233-137-7702','596-938-8638','817-269-9260','621-524-4582','935-856-6892','614-594-4983','412-634-4181','671-582-2302','633-717-7208','282-338-8217','707-883-3877','179-859-9573','803-190-0805','254-521-1285','440-699-9671','750-438-8412','631-885-5599','288-559-9321','259-147-7181','652-621-1288','193-477-7932','222-145-5605','716-128-8767','675-408-8998','827-625-5725','814-696-6382','530-395-5361','457-440-0626','694-220-0403','184-618-8886','802-970-0083','997-851-1746','269-911-1453','785-183-3168','405-540-0482','627-707-7375','916-074-4912','803-840-0342','913-978-8863','514-091-1502','750-436-6246','647-288-8230','425-459-9139','412-134-4588','652-603-3066','667-191-1914','900-280-0704','220-927-7285','934-038-8240','823-967-7371','876-616-6993','745-916-6181','165-904-4907','136-929-9129','135-501-1879','147-678-8027','482-389-9146','809-974-4428','764-234-4500','991-621-1637','707-621-1928','484-015-5371','220-188-8224','534-500-0678','765-718-8467','847-802-2243','724-644-4167','800-561-1483','110-650-0758','234-906-6157','771-632-2052','570-574-4486','435-486-6874','579-115-5370','761-206-6822','923-233-3801','270-335-5980','826-556-6983','308-748-8818','490-578-8156','772-946-6293','255-801-1876','573-665-5902','338-622-2649','103-046-6558','889-550-0661','876-507-7591','392-628-8277','795-529-9809','412-215-5622','446-297-7252','442-774-4230','752-672-2553','340-548-8853','309-669-9458','526-695-5999','404-121-1678','437-042-2079','117-808-8362','181-709-9750','715-436-6258','478-332-2007','822-312-2789','612-256-6928','119-721-1259','574-523-3669','291-975-5310','213-828-8862','428-079-9951','122-933-3028','870-315-5144','429-802-2828','538-910-0451','970-104-4592','132-305-5382','719-070-0964','863-833-3217','429-863-3430','879-507-7731','529-530-0549','646-415-5602','936-790-0673','449-924-4950','714-315-5096','580-135-5708','913-537-7155','613-567-7481','384-381-1391','290-958-8658','834-876-6529','997-961-1163','736-637-7063','952-830-0887','821-150-0226','703-011-1268','653-316-6962','818-242-2196','837-232-2364','663-466-6517','590-319-9581','557-236-6733','658-737-7163','215-637-7766','450-439-9707','389-538-8393','437-242-2158','146-603-3522','394-858-8299','997-847-7154','440-844-4521','787-057-7153','295-504-4350','731-561-1587','250-076-6239','185-378-8303','726-523-3620','191-762-2992','685-797-7615','557-021-1085','346-193-3918','753-554-4578','903-259-9443','685-728-8653','709-248-8717','994-615-5735','482-634-4652','317-744-4607','710-667-7165','166-022-2282','341-712-2801','600-238-8583','130-756-6813','794-130-0817','243-674-4197','975-666-6828','589-504-4688','299-399-9975','263-638-8718','118-382-2803','671-685-5492','492-136-6575','674-613-3090','444-175-5687','969-759-9785','466-178-8527','889-545-5186','234-723-3169','330-976-6630','811-721-1899','465-852-2845','299-799-9650','149-089-9117','715-264-4688','317-383-3982','461-285-5206','188-487-7085','463-618-8512','215-246-6180','291-327-7475','879-594-4532','945-407-7053','400-878-8587','859-782-2865','829-248-8382','985-146-6332','355-538-8838','558-336-6396','851-819-9888','786-698-8197','788-535-5664','324-757-7353','707-904-4699','552-366-6188','231-633-3848','339-386-6288','340-678-8005','867-339-9292','816-124-4413','570-065-5607','200-717-7735','866-645-5895','604-211-1382','803-484-4286','644-313-3973','780-777-7354','454-232-2266','733-497-7702','805-397-7603','296-866-6001','761-482-2207','540-360-0048','981-229-9729','435-601-1668','609-346-6897','527-681-1325','571-484-4258','867-672-2358','658-432-2931','157-619-9420','955-244-4125','138-826-6566','869-150-0041','987-104-4513','116-950-0705','685-372-2410','332-476-6807','473-102-2092','828-081-1573','145-549-9067','773-965-5162','314-236-6136','320-529-9976','444-914-4438','464-053-3431','283-204-4854','242-971-1255','142-384-4773','580-396-6469','620-683-3404','651-571-1495','944-719-9715','504-958-8300','560-819-9034','654-032-2113','493-365-5323','434-012-2433','919-745-5556','572-668-8275','437-665-5149','445-577-7026','464-525-5460','652-638-8623','867-380-0824','207-825-5710','918-777-7637','309-162-2728','393-074-4265','810-694-4466','242-386-6076','525-696-6742','414-822-2562','798-048-8748','250-284-4167','905-606-6860','320-244-4347','564-507-7282','838-504-4114','708-539-9817','462-629-9774','419-239-9427','272-130-0249','764-753-3192','234-394-4230','402-155-5446','231-506-6811','974-241-1481','951-382-2524','857-369-9987','889-631-1994','563-179-9107','526-244-4028','820-870-0800','979-686-6417','281-023-3531','503-269-9466','749-318-8721','479-272-2808','658-557-7357','771-666-6257','969-020-0168','329-580-0513','400-179-9698','616-131-1223','218-679-9736','405-830-0718','545-245-5886','988-303-3937','518-930-0272','766-759-9016','215-512-2762','318-120-0993','161-863-3562','848-845-5253','692-164-4744','411-243-3257','773-753-3232','966-901-1032','584-561-1213','937-662-2802','374-314-4500','330-233-3785','565-765-5905','389-443-3933','763-111-1076','232-665-5767','693-835-5135','434-696-6151','984-166-6862','712-637-7931','621-062-2346','201-768-8245','844-203-3780','789-827-7962','948-649-9377','501-160-0258','849-601-1413','672-213-3084','240-987-7366','233-453-3641','800-475-5916','930-801-1572','487-483-3286','820-258-8630','578-866-6797','126-864-4513','691-110-0731','774-402-2387','905-617-7855','828-542-2576','939-243-3040','304-050-0763','840-278-8560','946-642-2235','549-564-4143','134-399-9753','585-969-9452','337-943-3723','553-844-4492','986-697-7561','779-738-8098','738-918-8446','553-982-2267','612-881-1440','358-203-3742','811-398-8157','159-288-8682','239-828-8220','282-768-8803','933-379-9275','432-762-2767','860-891-1871','241-267-7795','615-904-4679','528-486-6182','692-677-7598','884-013-3776','778-690-0557','481-120-0962','334-323-3381','741-248-8557','460-911-1937','982-044-4427','536-787-7068','669-406-6599','863-294-4522','661-454-4323','539-156-6427','483-994-4757','920-716-6200','469-778-8301','101-967-7322','448-184-4008','149-962-2018','811-097-7523','331-922-2633','873-412-2779','386-655-5417','381-697-7590','157-090-0685','832-766-6843','362-624-4238','932-610-0487','967-055-5198','349-755-5418','297-659-9346','830-696-6148','229-108-8705','822-831-1493','465-860-0783','791-550-0582','733-791-1428','510-745-5053','870-273-3517','708-492-2895','560-368-8612','956-665-5826','798-471-1760','913-642-2478','822-081-1740','595-608-8512','406-095-5680','883-169-9372','891-570-0031','373-220-0724','897-064-4915','763-872-2640','975-706-6933','733-494-4570','260-728-8228','276-421-1344','718-589-9691','903-085-5462','217-214-4246','880-702-2972','892-636-6029','237-121-1371','979-702-2807','792-520-0481','616-120-0588','890-091-1611','694-470-0645','417-066-6682','144-263-3216','750-030-0903','898-725-5310','132-895-5216','904-370-0467','341-406-6602','211-309-9485','551-604-4313','793-277-7337','818-487-7510','340-011-1097','282-082-2620','481-130-0702','316-784-4507','332-478-8810','919-882-2127','965-714-4732','725-628-8340','967-756-6221','457-331-1580','337-094-4461','854-775-5741','637-021-1770','668-197-7072','671-581-1452','375-245-5818','532-304-4734','953-634-4265','465-301-1880','121-351-1523','608-963-3131','436-240-0102','114-056-6673','865-371-1843','154-383-3433','515-468-8331','218-138-8390','761-060-0802','100-253-3998','624-792-2160','655-468-8603','773-609-9103','158-821-1995','864-325-5347','491-234-4472','639-745-5967','231-611-1602','731-960-0098','401-665-5378','343-659-9321','543-698-8538','347-918-8852','947-354-4460','188-812-2798','436-918-8825','844-504-4892','676-882-2981','278-386-6132','348-732-2348','812-542-2016','962-507-7482','118-523-3988','731-123-3444','652-015-5752','464-614-4325','606-280-0735','234-104-4457','680-081-1412','590-469-9846','447-885-5292','111-171-1461','538-928-8621','854-708-8626','350-353-3388','842-252-2397','303-436-6916','364-595-5265','945-445-5911','944-536-6143','835-663-3807','169-559-9202','574-065-5642','136-244-4793','345-414-4172','552-801-1778','439-454-4243','102-672-2522','222-129-9256','883-786-6154','243-194-4843','353-831-1576','251-347-7523','418-415-5533','251-931-1767','783-896-6921','315-474-4425','733-157-7730','537-505-5923','503-061-1307','625-723-3610','989-014-4643','604-890-0296','427-401-1780','566-599-9781','934-169-9568','515-619-9265','203-982-2771','416-043-3923','468-328-8595','406-723-3365','410-765-5477','823-195-5113','715-042-2375','136-481-1690','808-213-3043','257-537-7875','133-996-6230','219-502-2958','636-211-1966','571-709-9641','218-215-5864','174-928-8856','399-685-5378','588-157-7536','117-808-8172','974-770-0482','896-519-9747','338-819-9132','278-024-4128','144-113-3334','309-540-0811','357-631-1979','805-906-6198','503-803-3876','758-212-2817','836-811-1338','632-005-5117','714-556-6352','376-510-0785','160-748-8180','681-083-3941','688-990-0277','641-445-5472','498-712-2220','492-966-6517','499-131-1951','352-186-6236','694-115-5222','831-267-7142','248-773-3793','507-439-9216','796-714-4842','624-801-1622','173-629-9753','524-814-4877','369-533-3971','267-308-8116','826-962-2314','383-312-2827','637-361-1488','512-121-1121','289-991-1877','988-474-4244','596-470-0525','921-839-9555','517-373-3823','327-408-8220','983-450-0306','189-260-0195','492-300-0557','841-043-3892','731-256-6112','567-386-6353','749-613-3278','600-083-3465','959-192-2077','893-316-6822','695-196-6836','157-944-4938','744-757-7324','391-004-4591','653-606-6141','664-910-0855','678-769-9528','101-282-2542','763-968-8823','902-565-5772','151-727-7541','797-073-3447','134-603-3922','127-055-5137','172-532-2928','742-886-6133','230-108-8708','320-414-4008','466-814-4505','699-633-3032','783-250-0047','128-907-7478','381-337-7358','802-354-4711','281-959-9842','304-718-8407','643-392-2003','583-487-7533','598-170-0313','296-909-9755','616-926-6508','855-982-2752','108-462-2586','285-770-0161','676-584-4677','323-229-9732','446-644-4992','891-537-7872','316-647-7955','454-550-0653','479-884-4742','115-092-2327','125-891-1553','707-814-4072','679-775-5750','463-241-1845','825-300-0933','322-326-6688','594-742-2807','119-304-4299','766-844-4508','551-476-6938','211-140-0217','623-755-5649','329-519-9990','847-940-0596','373-143-3426','414-657-7821','499-619-9919','378-206-6350','988-137-7297','355-469-9991','203-511-1903','871-189-9508','400-556-6371','697-584-4807','124-923-3978','517-992-2501','893-066-6967','443-925-5521','768-571-1467','464-718-8003','803-994-4869','559-856-6867','254-322-2037','193-578-8955','784-315-5487','365-859-9927','110-750-0788','439-888-8797','524-929-9780','412-311-1413','510-553-3622','866-021-1172','421-297-7463','230-078-8805','866-819-9142','561-394-4680','742-376-6145','223-457-7223','265-607-7615','516-353-3820','696-402-2317','750-892-2651','583-924-4007','990-523-3366','631-110-0385','656-380-0072','599-522-2308','792-201-1033','821-130-0206','122-501-1038','863-692-2854','924-764-4577','468-309-9746','845-516-6765','800-745-5910','712-444-4623','200-830-0272','587-129-9260','903-846-6278','366-877-7149','324-111-1227','422-106-6718','380-472-2069','645-752-2027','974-448-8747','174-177-7530','630-705-5257','796-435-5695','684-537-7947','901-437-7011','562-293-3933','651-971-1593','588-018-8795','623-402-2642','195-423-3632','262-558-8510','619-743-3742','789-346-6631','297-698-8403','188-805-5058','293-111-1647','243-048-8913','785-534-4386','952-154-4543','247-768-8317','196-245-5892','816-713-3196','172-056-6281','945-400-0047','536-565-5615','939-761-1143','698-328-8601','742-794-4233','669-976-6987','912-745-5668','483-303-3747','218-083-3445','698-514-4258','957-139-9308','514-878-8338','879-427-7788','444-247-7626','260-983-3832','129-319-9245','532-270-0402','203-545-5597','359-708-8643','456-177-7068','265-028-8117','517-189-9788','647-338-8825','533-241-1068','527-457-7005','369-039-9215','530-051-1332','799-322-2627','786-239-9531','330-463-3976','899-366-6465','928-599-9133','158-607-7703','291-366-6065','223-790-0178','149-386-6465','246-160-0730','967-124-4045','545-743-3230','235-346-6953','866-457-7991','995-671-1516','780-887-7334','159-394-4783','845-208-8197','791-799-9012','565-633-3123','871-972-2172','247-743-3271','101-048-8561','957-326-6182','850-531-1465','463-484-4592','878-835-5713','318-494-4998','807-543-3893','818-899-9866','289-931-1168','397-043-3173','358-011-1750','373-936-6402','976-877-7036','653-930-0152','630-897-7438','759-504-4548','287-460-0998','427-124-4110','268-245-5130','163-784-4639','318-990-0378','688-394-4977','862-055-5868','547-101-1474','600-890-0930','793-767-7467','529-758-8551','276-487-7478','730-466-6655','547-829-9072','626-790-0359','772-457-7726','885-619-9192','171-654-4781','724-882-2076','234-982-2385','119-952-2461','682-533-3337','497-598-8876','613-000-0883','699-096-6525','535-324-4568','758-191-1543','478-678-8692','812-365-5548','329-090-0082','856-718-8587','389-842-2073','911-015-5898','281-812-2420','612-450-0497','576-521-1067','168-481-1482','136-238-8289','418-741-1262','116-388-8422','569-106-6582','262-546-6215','692-186-6847','866-439-9462','782-182-2362','406-332-2346','258-857-7352','219-486-6179','451-876-6402','589-154-4961','685-465-5567','444-016-6968','640-290-0135','651-950-0607','545-959-9232','459-247-7387','450-939-9687','354-578-8762','958-889-9140','878-959-9318','100-779-9508','762-912-2670','806-475-5533','197-459-9448','278-682-2797','812-344-4902','975-353-3892','281-509-9968','612-028-8920','542-393-3463','388-971-1545','937-063-3978','788-711-1481','714-011-1750','580-428-8025','165-417-7572','338-370-0143','327-108-8078','729-887-7876','926-957-7088','829-152-2110','800-229-9816','844-494-4842','584-673-3272','958-708-8427','581-124-4547','737-442-2107','160-916-6352','490-768-8548','266-691-1345','383-201-1923','603-169-9292','628-022-2210','343-217-7971','395-197-7267','647-933-3732','590-526-6622','833-853-3944','395-303-3479','154-286-6496','395-290-0708','298-785-5383','716-594-4263','584-333-3312','758-511-1214','661-798-8745','729-020-0584','940-758-8170','820-669-9336','279-052-2477','232-752-2976','543-731-1361','857-524-4166','109-510-0437','872-364-4855','203-294-4022','284-929-9257','768-393-3852','921-677-7084','571-063-3067','897-136-6510','309-018-8612','300-870-0913','164-707-7642','997-579-9761','589-892-2693','636-454-4633','389-841-1688','997-104-4801','412-410-0902','852-682-2722','851-561-1587','828-668-8194','474-056-6972','963-864-4186','510-553-3648','106-651-1373','468-073-3256','905-172-2698','883-185-5825','160-027-7865','988-331-1945','369-543-3437','994-978-8206','536-751-1628','140-601-1758','415-415-5232','392-306-6190','251-818-8778','847-277-7667','377-243-3451','120-699-9492','690-407-7723','179-297-7553','359-460-0387','255-165-5896','174-183-3373','697-182-2253','842-118-8022','254-050-0336','536-249-9437','103-564-4628','406-904-4854','494-637-7016','242-679-9438','938-657-7012','771-364-4416','199-370-0211','268-570-0717','903-320-0650','809-927-7502','507-044-4328','781-994-4540','676-949-9274','687-727-7393','252-235-5650','197-780-0514','717-021-1158','552-290-0723','200-690-0339','722-313-3175','745-413-3918','378-229-9507','816-579-9097','498-827-7147','732-832-2419','723-682-2927','782-794-4331','391-446-6358','993-185-5173','614-787-7032','423-347-7957','592-046-6548','483-691-1210','821-018-8015','287-592-2555','778-960-0646','708-833-3085','954-611-1942','388-977-7410','495-857-7550','249-253-3547','460-035-5053','582-455-5607','983-546-6221','756-623-3106','741-208-8677','299-375-5320','945-063-3878','552-162-2456','408-151-1672','100-694-4703','726-611-1477','275-379-9105','459-173-3917','244-999-9781','551-981-1183','340-345-5025','983-140-0508','313-806-6805','145-469-9721','257-485-5502','105-923-3489','784-646-6192','319-057-7406','255-739-9642','543-534-4735','869-609-9621','727-331-1920','655-463-3988','644-637-7808','528-680-0174','403-735-5353','725-428-8808','528-796-6779','525-952-2580','851-360-0268','413-112-2232','626-881-1685','566-188-8990','605-428-8303','160-665-5612','466-112-2143','955-461-1921','491-725-5408','206-822-2057']
  if (cid_to_compare_with.indexOf(cid_to_compare) > -1)
  {
    //In the array!
    window.is_error = true;
    $('#cid_error').show();
    $(".lead-form :input").prop("disabled", true);
    $("#cid").prop("disabled", false);
  
    dataLayer.push({ 'event': 'gTrackEvent', 'category': 'Picasso', 'action': 'ineligible', 'label': cid.value});
    $('#formsubmit').prop('disabled', true);
    return false;
  }
  else {
      //Not in the array
    $('#cid_error').hide();
    $(".lead-form :input").prop("disabled", false);
    $('#formsubmit').prop('disabled', false);
    return true;
  }
}