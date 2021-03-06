    window.shoppingLeads = {'Dynamic Remarketing - Extension (non retail)': 'Dynamic Remarketing - Extension (non retail)',
                            'Google Shopping Setup': 'Google Shopping Setup',
                            'Dynamic Remarketing - Retail': 'Dynamic Remarketing - Retail'}

    // lead form controls
    $("#appointmentCheck" ).click(function() {
      $( "#tag_appointment" ).animate({
      height: "toggle"
      }, 300, function() {
      });
    });
  
  $("#webmasterCheck" ).click(function() {
    /* this line for uncheck other check box*/ 
    $("#web_access").prop("checked", false);
    $('#tag_contact_person_name').val('');
    $('#webmaster_name').val('')
    $("#webmasterCheck").val(1);
    $( "#webmaster" ).animate({
    height: "toggle"
    }, 300, function() {
    });
    $( "#web-dum1, #web-dum2" ).toggle(500);
  });

  /* this line for uncheck webmasterCheck box*/ 
  $("#web_access").on('click', function() {
    $("#webmasterCheck").prop("checked", false);
    $("#web_access").prop("checked", true);
    $('#tag_contact_person_name').val('');
    advertiserName = $('#advertiser_name').val();
    $('#tag_contact_person_name').val(advertiserName);
    $( "#webmaster").hide();

  });

  $("#webmaster_name").focusout(function(){
  if($("#webmasterCheck").is(":checked")){
    $("#webmasterCheck").val(1);
    var webmaster_name = $("#webmaster_name").val();
    $("#tag_contact_person_name").val(webmaster_name);
  }else{
    $("#webmasterCheck").val(0);
    $("#tag_contact_person_name").val('');
  }
});

   $("#advertiser_name").focusout(function(){
    if($("#web_access").is(":checked")){
      $("#web_access").val(1);
      var advertiser_name = $("#advertiser_name").val();
      $("#tag_contact_person_name").val(advertiser_name);
    }else{
      $("#web_access").val(0);
      $("#tag_contact_person_name").val('');
  }
});



    $("#is_campaign_created1").click(function(){
      if(document.getElementById('is_campaign_created1').checked == false){
          $(this).val(0);
          $("#rbid_campaign1").show();
          $("#rbudget_campaign1").show();
      }else{
          $(this).val(1);
          $("#rbid_campaign1").hide().val('');
          $("#rbudget_campaign1").hide().val('');
      }
    });


    $("#is_campaign_created2").click(function(){
      if(document.getElementById('is_campaign_created2').checked == false){
          $(this).val(0);
          $("#rbid_campaign2").show();
          $("#rbudget_campaign2").show();
      }else{
          $(this).val(1);
          $("#rbid_campaign2").hide().val('');
          $("#rbudget_campaign2").hide().val('');
      }
    });


    $("#is_campaign_created3").click(function(){
      if(document.getElementById('is_campaign_created3').checked == false){
        $(this).val(0);
          $("#rbid_campaign3").show();
          $("#rbudget_campaign3").show();
      }else{
        $(this).val(1);
          $("#rbid_campaign3").hide().val('');
          $("#rbudget_campaign3").hide().val('');
      }
    });
    
  $('#team').change(function(){
    $('#g_cases_id').val('')
    var selectedTeam = $(this).val();
    if (selectedTeam.indexOf('Services') != -1){
      // if(selectedTeam == 'Services/GCE'){
      //   alert("Only Pinnacle and HiPo Newbie customers are eligible for Regalix support");
      // }
      $(".tr_service_segment").show();
      $('label[for="g_cases_id"]').show();
      $('label[for="service_segment"]').hide();
      $('#g_cases_id').show();
      $('#GCaseId').show();
      $("#service_segment").hide();
    }else if(selectedTeam == 'ETO' || selectedTeam == 'ETO: Agency' || selectedTeam == 'ETO: Inbound' || selectedTeam == 'ETO: Outbound' || selectedTeam == 'ETO: CS'){
      if (window.is_loc_changed){
        setLocations(window.locations);
        window.is_loc_changed = false;
      }
      $("#service_segment").show();
      $("#service_segment").val('');
      $(".tr_service_segment").show();
      $('#g_cases_id').hide();
      $('label[for="g_cases_id"]').hide();
      $('label[for="service_segment"]').show();
    }else{
      if (window.is_loc_changed){
        setLocations(window.locations);
        window.is_loc_changed = false;
      }
      $(".tr_service_segment").hide();
      $('#g_cases_id').hide();
      $('#GCaseId').hide();

      $('label[for="g_cases_id"]').hide();
      $('label[for="service_segment"]').hide();
    }
  });

  $('#team').trigger("change");
  
  $('#setup_lead_check').click(function() {
    $('#setup_lead_form').toggle();
  })

  function submitbtn(ths){
      $(ths).submit().attr('disabled', true);
  }

  function setLocations(newLocations){
    $("#country option").remove()
    $("#country").append('<option value="0">Program Location</option>');
    for(i=0; i<newLocations.length; i++){
      $("#country").append('<option value="' + newLocations[i]['name'] + '" location_id="' + newLocations[i]['id']+ '">'+ newLocations[i]['name'] +'</option>');
    }
  }
  
   // sshopping check 
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
    $('.shopping-policy').removeClass('error-box');
    $('.web-access').removeClass('error-box');
    $('.error-box').removeClass('error-box');
    // var check = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    var check = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    var cidFormat = /^\d{3}-\d{3}-\d{4}$/;
    var phoneFormat = /^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$/;
    var numericExpression = /^[0-9]+$/;
    window.failedFields = new Array();
    var fix_slots = new Array();

    window.is_error = false;
    if(window.is_reset == true){
      window.is_reset = false;
      return false;
    }

    
    // Google Rep Name Validation
    grefElem = document.getElementById('gref');
    validateField(grefElem);

    // Google Rep Email Validation
    emailrefElem = document.getElementById('emailref');
    validateField(emailrefElem);

    validateEmailField(emailrefElem)

    // Programs Validation
    teamElem = document.getElementById('team');
    validateField(teamElem);

    // Service Segment Validation
    if ($(frm.service_segment).is(":visible")) {
      service_segmentElem = document.getElementById('service_segment');
      validateField(service_segmentElem);
    }

    // GcaseId validation
    if ($(frm.g_cases_id).is(":visible")) {
      gCasesIdElem = document.getElementById('g_cases_id');
      validateField(gCasesIdElem);
    }

    // Google Manager details validation
    teamElem = document.getElementById('team');
    validateField(teamElem);

    if (document.getElementById("manager_name").value == "") {
      //alert("Please Update Google Manager details");
      managerElem = document.getElementById("manager_name");
      validateField(managerElem);
    }

    if (document.getElementById("manager_email").value == "") {
      //alert("Please Update Google Manager details");
      emailElem = document.getElementById("manager_email");
      validateField(emailElem);
    }
    // Email Validation
    emailElem = document.getElementById("manager_email");
    validateEmailField(emailElem);

    // Advertiser Info
    // Advertiser Name Validation
    advertiserNameElem = document.getElementById('advertiser_name');
    validateField(advertiserNameElem);

    // Advertiser Email Validation
    aemailElem = document.getElementById('aemail');
    validateField(aemailElem);

    // Email Validation
    validateEmailField(aemailElem);

    // Advertiser Phone Validation
    phoneElem = document.getElementById('phone');
    validateField(phoneElem);

    // Advertiser Company Validation
    companyElem = document.getElementById('company');
    validateField(companyElem);
    
    // Customer Id validation
    cidElem = document.getElementById('cid');
    validateField(cidElem);

    if(!frm.cid.value.match(cidFormat)){
      //alert("Please enter a valid Customer ID (nnn-nnn-nnnn)");
      $(frm.cid).addClass('error-box');
      //$(frm.cid).after('<span class="error-txt">Please enter a valid Customer ID (nnn-nnn-nnnn)</span>')
      /*frm.cid.focus();*/
      window.is_error = true;
    }

    // Location/Country Validation
    countryElem = document.getElementById('country');
    validateField(countryElem);

    // Advertiser Location validation
    // advertiserLocationElem = document.getElementById('advertiser_location');
    // validateField(advertiserLocationElem);

    // Language validation
    languageElem = document.getElementById('language');
    validateField(languageElem);

    // Timezone Validation
    tzoneElem = document.getElementById('tzone');
    validateField(tzoneElem);

    // Does the advertiser have edit access for the website or has a webmaster validation for selection
    if(document.getElementById("web_access").checked == false && document.getElementById("webmasterCheck").checked == false){
      $('.web-access').addClass('error-box');
      window.is_error = true;
    }

    // Webmaster Validation
    if(document.getElementById("webmasterCheck").checked == true){

      // Contact Person Name
      webMasterNameElem = document.getElementById('webmaster_name');
      validateField(webMasterNameElem);

      // Contact Person Role
      webMasterEmailElem = document.getElementById('web_master_email');
      validateField(webMasterEmailElem);

      // Contact Person Name
      poptElem = document.getElementById('popt');
      validateField(poptElem);

    }


    // ####################### Bundle Code Types Validations #####################################
    // Code Type / Task 1
    ctype1Elem = document.getElementById('ctype1');
    validateField(ctype1Elem);

    // Check all related fields for Code Type 1
    task1 = ctype1Elem.value;
    if(task1){
      if(task1 == 'Google Shopping Setup'){
          
          // Validate Shopping related fields
          rbidElem = document.getElementById('rbid1');
          validateField(rbidElem);

          rbidmodifierElem = document.getElementById('rbidmodifier1');
          validateField(rbidmodifierElem);

          rbudgetElem = document.getElementById('rbudget1');
          validateField(rbudgetElem);

          shoppingUrlElem = document.getElementById('url1');
          validateField(shoppingUrlElem);


          shoppingMCIDElem = document.getElementById('is-mc_id1');
          if(shoppingMCIDElem.checked == true){
              shoppingMCElem = document.getElementById('mc_id1');
              validateField(shoppingMCElem);
          }
          
          // Hava an appointment for Google Shopping No Appointments
          // if (document.getElementById("appointmentCheck").checked == true) {
          //   // Contact Person Name Validation
          //   contactElem = document.getElementById('shop_contact_person_name1');
          //   validateField(contactElem);

          //   // Contact Person Role Validation
          //   roleElem = document.getElementById('shop_primary_role');
          //   validateField(roleElem);

          //   // Appointments Date and Time Validation
          //   setupDateElem = document.getElementById('setup_datepick1');
          //   validateField(setupDateElem);

          //   if(setupDateElem.value){
          //       var slot = {
          //       'type' : 'SHOPPING',
          //       'time' : setupDateElem.value
          //       }
          //       fix_slots.push(slot)
          //     }
          //   }

      }else{
          if (task1.indexOf('Dynamic') != -1){
            if(document.getElementById('is_campaign_created1').checked == false){
                rbidElem = document.getElementById('rbid_campaign1');
                validateField(rbidElem);

                rbudgetElem = document.getElementById('rbudget_campaign1');
                validateField(rbudgetElem);
            }
          } else if(task1.indexOf('RLSA') != -1){
                  if($('#rlsa_bulk1').is(":visible")){

                        rlsaUserListEle = document.getElementById('user_list_id1');
                        validateField(rlsaUserListEle);

                        rlsaBidAdjustment = document.getElementById('rsla_bid_adjustment1');
                        validateField(rlsaBidAdjustment);

                        campaignIds = document.getElementById('campaign_ids1');
                        validateField(campaignIds);

                        existingBid = document.getElementById('overwrite_existing_bid_modifiers1');
                        validateField(existingBid);

                        newBid = document.getElementById('create_new_bid_modifiers1');
                        validateField(newBid);

                        rlsaPolicies = document.getElementById('rsla_policies1');
                        if(!$(rlsaPolicies).is(":checked")){
                           $(rlsaPolicies).parent().addClass('error-box');
                            window.failedFields.push(rlsaPolicies);
                            window.is_error = true;
                            return false;
                        }
                    }

          } else{
            $("#rbid_campaign1").val('');
            $("#rbudget_campaign1").val('');
          }

          // Validate Tag related fields
          tagUrlElem = document.getElementById('url1');
          validateField(tagUrlElem);

          if($('#analyticscode1').is(':visible')){
            validateField($('#analytics_code1'));
          }

          }
      }

    // Code Type / Task 2
    // Check all related fields for Code Type 1
    ctype2Elem = document.getElementById('ctype2');
    task2 = ctype2Elem.value;
    if(task2){
      if(task2 == 'Google Shopping Setup'){
          
          // Validate Shopping related fields
          rbidElem = document.getElementById('rbid2');
          validateField(rbidElem);

          rbidmodifierElem = document.getElementById('rbidmodifier2');
          validateField(rbidmodifierElem);

          rbudgetElem = document.getElementById('rbudget2');
          validateField(rbudgetElem);

          shoppingUrlElem = document.getElementById('url2');
          validateField(shoppingUrlElem);

          shoppingMCIDElem = document.getElementById('is-mc_id2');
          if(shoppingMCIDElem.checked == true){
              shoppingMCElem = document.getElementById('mc_id2');
              validateField(shoppingMCElem);
          } 

      }else{
          // Validate Tag related fields

          if (task2.indexOf('Dynamic') != -1){
            if(document.getElementById('is_campaign_created2').checked == false){
                rbidElem = document.getElementById('rbid_campaign2');
                validateField(rbidElem);

                rbudgetElem = document.getElementById('rbudget_campaign2');
                validateField(rbudgetElem);
            }
          } else if(task2.indexOf('RLSA') != -1){
             if($('#rlsa_bulk2').is(":visible")){

                    rlsaUserListEle = document.getElementById('user_list_id2');
                    validateField(rlsaUserListEle);

                    rlsaBidAdjustment = document.getElementById('rsla_bid_adjustment2');
                    validateField(rlsaBidAdjustment);

                    campaignIds = document.getElementById('campaign_ids2');
                    validateField(campaignIds);

                    existingBid = document.getElementById('overwrite_existing_bid_modifiers2');
                    validateField(existingBid);

                    newBid = document.getElementById('create_new_bid_modifiers2');
                    validateField(newBid);

                    rlsaPolicies = document.getElementById('rsla_policies2');
                    if(!$(rlsaPolicies).is(":checked")){
                       $(rlsaPolicies).parent().addClass('error-box');
                        window.failedFields.push(rlsaPolicies);
                        window.is_error = true;
                        return false;
                    }
                }

          } else{
            $("#rbid_campaign2").val('');
            $("#rbudget_campaign2").val('');
          }

          tagUrlElem = document.getElementById('url2');
          validateField(tagUrlElem);

          if($('#analyticscode2').is(':visible')){
            validateField($('#analytics_code2'));
          }
      }
    }

    // Code Type / Task 3
    // Check all related fields for Code Type 3
    ctype3Elem = document.getElementById('ctype3');
    task3 = ctype3Elem.value;
    if(task3){
      if(task3 == 'Google Shopping Setup'){
          
          // Validate Shopping related fields
          rbidElem = document.getElementById('rbid3');
          validateField(rbidElem);

          rbidmodifierElem = document.getElementById('rbidmodifier3');
          validateField(rbidmodifierElem);

          rbudgetElem = document.getElementById('rbudget3');
          validateField(rbudgetElem);

          shoppingUrlElem = document.getElementById('url3');
          validateField(shoppingUrlElem);

          shoppingMCIDElem = document.getElementById('is-mc_id3');
          if(shoppingMCIDElem.checked == true){
              shoppingMCElem = document.getElementById('mc_id3');
              validateField(shoppingMCElem);
          }
          
      }else{
          // Validate Tag related fields

          if (task3.indexOf('Dynamic') != -1){
            if(document.getElementById('is_campaign_created3').checked == false){
                rbidElem = document.getElementById('rbid_campaign3');
                validateField(rbidElem);

                rbudgetElem = document.getElementById('rbudget_campaign3');
                validateField(rbudgetElem);
            }
          } else if(task3.indexOf('RLSA') != -1){
             if($('#rlsa_bulk3').is(":visible")){

                    rlsaUserListEle = document.getElementById('user_list_id3');
                    validateField(rlsaUserListEle);

                    rlsaBidAdjustment = document.getElementById('rsla_bid_adjustment3');
                    validateField(rlsaBidAdjustment);

                    campaignIds = document.getElementById('campaign_ids3');
                    validateField(campaignIds);

                    existingBid = document.getElementById('overwrite_existing_bid_modifiers3');
                    validateField(existingBid);

                    newBid = document.getElementById('create_new_bid_modifiers3');
                    validateField(newBid);

                    rlsaPolicies = document.getElementById('rsla_policies3');
                    if(!$(rlsaPolicies).is(":checked")){
                       $(rlsaPolicies).parent().addClass('error-box');
                        window.failedFields.push(rlsaPolicies);
                        window.is_error = true;
                        return false;
                    }
                }

          } else{
            $("#rbid_campaign3").val('');
            $("#rbudget_campaign3").val('');
          }

          tagUrlElem = document.getElementById('url3');
          validateField(tagUrlElem);

          if($('#analyticscode3').is(':visible')){
            validateField($('#analytics_code3'));
          }
          
      }

    }

    // Hava an appointment 
    if ($("#appointmentCheck").is(":visible") && document.getElementById("appointmentCheck").checked == true) {
      // Contact Person Name Validation
      contactElem = document.getElementById('tag_contact_person_name');
      validateField(contactElem);

      // Contact Person Role Validation
      roleElem = document.getElementById('tag_primary_role');
      validateField(roleElem);

      // Appointments Date and Time Validation
      tagDateElem = document.getElementById('tag_datepick');
      if ($(tagDateElem).val() == "" || $(tagDateElem).val() == "0" || !$(tagDateElem).val()) {
          $(tagDateElem).addClass('error-box');
          window.failedFields.push(tagDateElem);
          window.is_error = true;
        }
      // validateField(tagDateElem);

      if(tagDateElem.value){
          var slot = {
          'type' : 'TAG',
          'time' : tagDateElem.value
          }
          fix_slots.push(slot)
        }
      }else{
        document.getElementById('tag_datepick').value = '';
      }

    if($("#is_shopping_policies").is(":visible")){
        if($("#is_shopping_policies").is(":checked")){
          $("#is_shopping_policies").val(1);
          $(".shopping-policy").removeClass('error-box');
        }else{
            $(".shopping-policy").addClass('error-box');
            $("#is_shopping_policies").val(0);
            window.failedFields.push($("#is_shopping_policies"));
            window.is_error = true;
        }
        isAgree = ensureAllPolicies()
    }

      // Analytics setup check box
      $('.is_ga_setup').each(function(){
        if(!$(this).is(":visible")){
          $(this).val(0);
        }
      });

      // Check If Error in Form
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
        return status;  
      }  
   } 

    // Check Box Options
    if($("#tag_via_gtm").is(":checked")){
      $("#tag_via_gtm").val(1);
    }else{
      $("#tag_via_gtm").val(0);
    }

    if($("#web_access").is(":checked")){
        $("#web_access").val(1);
    }else{
      $("#web_access").val(0);
    }


function validateField(elem){
    // Validate Form Field
    if ($(elem).val() == "" || $(elem).val() == "0" || !$(elem).val()) {
      $(elem).addClass('error-box');
      window.failedFields.push(elem);
      window.is_error = true;
      return false;
    }
}

function validateEmailField(elem) {
  var check = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  // Validate Email Field
  if (!$(elem).val().trim().match(check)) {
      $(elem).addClass('error-box');
      /*$(elem).focus();*/
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
    
function resetBtn(elem){
  elemId = $(elem).attr('id');
  if(elemId == 'formReset'){
    window.is_reset = true;
    window.location.reload();
  }
}

function uncheckAllBehaviourCheckBoxs(selectedindex){
  $('#product_behaviour'+selectedindex).prop('checked', false);
  $('#cartpage_behaviour'+selectedindex).prop('checked', false);
  $('#checkout_process'+selectedindex).prop('checked', false);
  $('#transaction_behaviour'+selectedindex).prop('checked', false);
}

$(".ctype").change(function(){
    window.lead_type = '';
    $("#ctype2 option").show();
    $("#ctype3 option").show();
    var selectedId = $(this).attr('id');
    var indx = selectedId[selectedId.length - 1];
    $('#analytics_code'+indx).val('');
    $('#analyticscode'+indx).hide();
    $('#callextension'+indx).hide();
    $('#call_extension'+indx).prop('checked', false);
    $('#codebehaviour'+indx).hide();
    
    $('#url'+indx).val('');
    $('#comment'+indx).val('');
    $('#rbudget_campaign'+indx).val('');
    $('#rbid_campaign'+indx).val('');

    $('#rlsa_bulk'+indx).hide();
    $("#user_list_id"+ indx).val('');
    $("#internal_cid"+ indx).val('');
    $("#rsla_bid_adjustment"+ indx).val('');
    $("#campaign_ids"+ indx).val('');
    $("#rsla_policies"+indx).prop('checked', false);
    $("#rsla_policies"+indx).val(0);
    $("#overwrite_existing_bid_modifiers"+indx).val('');
    $("#create_new_bid_modifiers"+indx).val('');
    $('#comment'+indx).attr("placeholder", "Special Instructions (Optional)");

    uncheckAllBehaviourCheckBoxs(indx);

    var selectedId1 = $("#ctype1 option:selected").attr('id');
    if(selectedId1){
        id1 = selectedId1.split('_')[1];

        if($("#ctype2 option:selected").attr('id') && id1 == $("#ctype2 option:selected").attr('id').split('_')[1]){
          $("#ctype2").val('');
        }else{
          $("#ctype2_" + id1).hide();
        }

        if($("#ctype3 option:selected").attr('id') && id1 == $("#ctype3 option:selected").attr('id').split('_')[1]){
          $("#ctype3").val('');
        }else{
          $("#ctype3_" + id1).hide();
        } 

    }

    var selectedId2 = $("#ctype2 option:selected").attr('id');
    
    if(selectedId2){
        id2 = selectedId2.split('_')[1];
        if($("#ctype3 option:selected").attr('id') && id2 == $("#ctype3 option:selected").attr('id').split('_')[1]){
            $("#ctype3").val('');
        }else{
            $("#ctype3_" + id2).hide();
        }
    }

    curId = $(this).attr('id');
    $("#" + curId + '_campaign').hide();
    if($(this).val()){
        $("#" + curId + '_name').text($(this).val());
        $("#" + curId + '_appointment').show();
    }else{
        $("#" + curId + '_name').text('');
        $("#" + curId + '_appointment').hide();
    }
    
    if($(this).val() == 'Google Shopping Setup'){
        $("#" + curId + '_shopping').show();
        window.lead_type = 'SHOPPING';
        updateComment(indx, false);
    }else{
        $("#" + curId + '_shopping').hide();
        window.lead_type = 'TAG';
    }

    if($(this).val().indexOf('Dynamic') != -1){
        $("#" + curId + '_campaign').show();
        $("#ga_setup" + indx).attr('checked', false);
        $("#gasetup" + indx).hide();
    }else if($(this).val().indexOf('Analytics') != -1){
      $("#gasetup" + indx).show();   
    }
    else if($(this).val().indexOf('Website Call Conversion') != -1){
        $('#callextension'+indx).show();
    } else if($(this).val().indexOf('RLSA Bulk Implementation') != -1){
        $('#rlsa_bulk'+indx).show();
        $('#comment'+indx).attr("placeholder", "Special Instructions (Optional, if there is an issue with applying RLSA to a campaign, please provide the Campaign ID for the campaign you wish to exclude).");
    } else{
      $("#ga_setup" + indx).attr('checked', false);
      $("#gasetup" + indx).hide();
    }

    if($(this).val().indexOf('Analytics Enhanced E-Commerce Tracking') != -1){
      $('#gasetup'+indx).hide();
      $("#ga_setup" + indx).attr('checked', false);
      $('#codebehaviour'+indx).show();
    } 
    
    if($("#call_extension"+indx).is(":checked")){
        $("#call_extension"+indx).val(1);
      }else{
        $("#call_extension"+indx).val(0);
     }

    var ctype1 = $("#ctype1").val()
    var ctype2 = $("#ctype2").val()
    var ctype3 = $("#ctype3").val()

    if(ctype1 && ctype1 != 'Google Shopping Setup'){
        $(".appointment").show();
    }else if(ctype2 && ctype2 != 'Google Shopping Setup'){
        $(".appointment").show();
    }else if(ctype3 && ctype3 != 'Google Shopping Setup'){
        $(".appointment").show();
    }else{
      $(".appointment").hide();
    }

    tagCheck(indx);

    showHeadsUp();

});


function showHeadsUp(){

  $(".tag-policies").hide();
  $(".shopping-policy").hide();

  type1 = $("#ctype1").val();
  type2 = $("#ctype2").val();
  type3 = $("#ctype3").val();

  if(type1 || type2 || type3){
    // Type 1
    if(type1 && type1 == 'Google Shopping Setup'){
      $("#heads_up").show();
      $(".shopping-policy").show();
    }else if(type1){
      $("#heads_up").show();
      $(".tag-policies").show();
    }

    // Type 2
    if(type2 && type2 == 'Google Shopping Setup'){
      $("#heads_up").show();
      $(".shopping-policy").show();
    }else if(type2){
      $("#heads_up").show();
      $(".tag-policies").show();
    }

    // Type 3
    if(type3 && type3 == 'Google Shopping Setup'){
      $("#heads_up").show();
      $(".shopping-policy").show();
    }else if(type3){
      $("#heads_up").show();
      $(".tag-policies").show();
    }
  }else{
    $("#heads_up").hide();
  }
}

$(".is_mc_id").click(function(){
  var thisId = $(this).attr('id');
  elem = thisId.split('-')[1];
  if($(this).is(':checked')){
      $("#" + elem).show();
  }else{
      $("#" + elem).hide().val('');
  }
})


$("#keep_url").click(function(){
    if($(this).is(":checked")){
      var tagUrl = $("#url1").val();
      if(!tagUrl){
        $("#url1").addClass('error-box');
        $("#url1").focus();
        return false;
      }
      $("#url2, #url3").val(tagUrl);
    }else{
      $("#url2, #url3").val('');
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

$('#region').change(function(){
  var regionId = $('option:selected', this).attr('region_id');
  countryList = regionWiseLocations[regionId];
  console.log(countryList);
  setLocationsForRegion(window.locations, countryList);
});

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

  $(".is_ga_setup").click(function(){
    thisId = $(this).attr('id');
    selectedindex = thisId[thisId.length-1]
    $('#analyticscode'+selectedindex).hide();
    $('#analytics_code'+selectedindex).val('');
    if($(this).is(":checked")){
      $('#analyticscode'+selectedindex).show();
      $(this).val(1);
    }else{
      $('#analyticscode'+selectedindex).hide();
      $(this).val(0);
    }
});


$("#tagCheck").click(function(){
    tagCheck(1);
    tagCheck(3);
    tagCheck(2);
});

function updateComment(indx, isCheck){
  if($("#ctype" + indx).val() && $("#ctype" + indx).val() != 'Google Shopping Setup'){
      if(isCheck){
          $("#comment" + indx).val('implement via GTM');
      }else{
          if ($("#comment" + indx).val() == 'implement via GTM'){
              $("#comment" + indx).val('');
          }
      }
  }else{
    if ($("#comment" + indx).val() == 'implement via GTM'){
        $("#comment" + indx).val('');
    }
  }
}

function tagCheck(indx){

  var elem = document.getElementById('tag_via_gtm'); 
    if(elem.checked == true){
      updateComment(indx, true);
    }else{
      updateComment(indx, false);
    }

}
