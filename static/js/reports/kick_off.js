 /* Success Metrics multiple add code start here */
 $('.add-succes').click(function () {
      id = $(this).attr('id');
      indx = id.split('_')[1];
      next_id = parseInt(indx) + 1
      if(next_id <= 5 )
      {
          $(".remove-succes").show();
          $new_row = $("#succes_row_1").clone().attr('id', 'succes_row_'+next_id).show();
          $(".succes-mat-onebox", $new_row).attr('id', 'succes_metrices_one_'+next_id);        
          $(".succes-mat-twobox", $new_row).attr('id', 'succes_metrices_two_'+next_id);  
          $(".succes-mat-threebox", $new_row).attr('id', 'succes_metrices_three_'+next_id); 
          $(".succes-mat-onebox", $new_row).attr('name', 'succes_metrices_one_'+next_id);        
          $(".succes-mat-twobox", $new_row).attr('name', 'succes_metrices_two_'+next_id);  
          $(".succes-mat-threebox", $new_row).attr('name', 'succes_metrices_three_'+next_id);  
          $new_row.appendTo(".succes-matrics");
          $("#succes_metrices_one_"+next_id).val('');    
          $("#succes_metrices_two_"+next_id).val('');  
          $("#succes_metrices_three_"+next_id).val('');  
          $('.remove-succes').attr('id',"#removeSuccesMat_" + next_id);
          $('.add-succes').attr('id',"#addSuccesMat_" + next_id);
        }
        if(next_id == 5 )
        {
          $(".add-succes").hide();
        }
  });

  $('.remove-succes').click(function () {
    id = $(this).attr('id');
    indx = id.split('_')[1];
    if(("#removeSuccesMat_"+indx) != "#removeTestimony_1" )
    {
        $(".add-succes").show();
        $("#succes_row_"+indx).remove();
        $('.remove-succes').attr('id',"#removeSuccesMat_" + (indx-1));
        $('.add-succes').attr('id',"#addSuccesMat_" + (indx-1));
    }
    if(("#removeSuccesMat_"+(indx-1)) == "#removeSuccesMat_1" )
    {
      $('.remove-succes').hide();
    }
  });
/*Success Metrics multiple add code Ends here */

 /* start bootsrap selector plugg in fetching multiple selected values id's */
    $('.region-ul').children().on('click', function(){
        selectProcessRegionData(this);
    });
    //adding locations based on region selected
    $('#locationTypeBtn').on('click', function(){
        var loc_elements = $('.location-ul li a .tickMarkShow');
        var elements = $('.region-ul li a .tickMarkShow');
        $(".location-ul").html('');
        $("#locationTypeList").empty();
        if(elements.length > 0)
        {
            for (var i=0;i<elements.length;i++)
            {
                var element_id = $(elements[i]).parent().parent().attr('id');
                for (var j=0;j<window.regionWiseLocations[element_id].length;j++)
                {
                    $(".location-ul").append('<li id="'+ window.regionWiseLocations[element_id][j]+'">'+
                                                 '<a href="#" class="smallLoc">'+
                                                 '<input type="checkbox" class="hiddenCheckbox"/>'+
                                                 '<span class="glyphicon glyphicon-ok tickMark">'+
                                                 '</span>&nbsp;'+ window.regionWiseLocations[element_id][j]+'</a></li>');
                }
                $(".location-ul").css('height','auto');
                $(".location-ul").css('overflow-x','hidden');
            }
            var final_elements = $(".location-ul li");
            for(var k=0;k<loc_elements.length;k++)
            {
              for(var i=0;i<final_elements.length;i++)
              {
                if($(loc_elements[k]).parent().parent().attr('id') == $(final_elements[i]).attr('id'))
                {
                  $(final_elements[i]).children().children("span").addClass("tickMarkShow");
                }
              }
            }
            $('.location-ul').children().on('click', function(){
                selectTeams(this.className, this);
            });
        }
        else
        {
          $(".location-ul").html('');
          $(".location-ul").append('<li id=""><a href="#" class="smallLoc"></span>&nbsp;Please Select Region</a></li>')
        }
    });
 // checking & unchecking also adding removing selected regions to empty selector oprtins
    function selectProcessRegionData(regionElement){
       if($(regionElement).attr('id')){
        var regionSpacereplace = $(regionElement).attr('id').replace(" ", "");
       }
        var OptionElement = "<option class='"+regionSpacereplace+"' value='"+ regionSpacereplace+"' selected></option>";
        $( "#regionTypeList" ).append( OptionElement ); 
        var selectedProcessElement = $(regionElement).children("a").children('span');
        if(selectedProcessElement.hasClass('tickMarkShow')){
            selectedProcessElement.removeClass('tickMarkShow');     // UnSelect the Process Element.
            $('#regionTypeList .'+regionSpacereplace+'').remove();   
        }
        else{
            selectedProcessElement.addClass('tickMarkShow');
        }
    }
    // checking & unchecking also adding removing selected locations to to empty selector data base
    function selectTeams(parentElementId, selectedElement){
       if($(selectedElement).attr('id')){
       }
        var locationSpacereplace = $(selectedElement).attr('id').replace(/[^\w\s]/gi, "");
        var selectedTeamsElement = $(selectedElement).children("a").children('span');
        var optionElement = "<option class ='"+parentElementId+"' value='"+ $(selectedElement).attr('id')+"' selected></option>";
        var optionElementToDatabase = "<option class ='"+parentElementId+"' id='removing"+locationSpacereplace+"' value='"+ $(selectedElement).attr('id')+"' selected></option>";
        $( "#locationTypeList" ).append(optionElementToDatabase);
        if(selectedTeamsElement.hasClass('tickMarkShow')){
            selectedTeamsElement.removeClass('tickMarkShow');
            $(' #removing'+locationSpacereplace+' ').remove();
        }
        else{
            selectedTeamsElement.addClass('tickMarkShow');
        }
    }
/* end of regions selection and location selection codes */

/* To select multiple code type selector plugg in fetching multiple selected values id and also checking and unchecking codetype selected */
$('.code-type-ul').children().on('click', function(){
        selectProcessPopulateCodeType(this);
    });
    function selectProcessPopulateCodeType(codeTypeElement){
       if($(codeTypeElement).attr('val')){
        var codeTypereplace = $(codeTypeElement).attr('val').replace(/ /g, "_");
       }
        var OptionElement = "<option id='"+codeTypereplace+"' value='"+codeTypereplace+"' selected></option>";

        var selectedProcessElement = $(codeTypeElement).children("a").children('span');
        // UnSelect Process Items.
        if(selectedProcessElement.hasClass('tickMarkShow')){
            selectedProcessElement.removeClass('tickMarkShow');     // UnSelect the Process Element.
            $('#codeTypeList  #'+codeTypereplace+' ').remove();
        }
        else{
            selectedProcessElement.addClass('tickMarkShow');
            $( "#codeTypeList" ).append(OptionElement);
        }
    }
/* end of multiple code type selector plugg in fetching multiple selected values id  */

/* To select multiple advertize type selector plugg in fetching multiple selected values id and also checking and unchecking codetype selected */
$('.advertizer-prg-ul').children().on('click', function(){
        selectingAdvertizeProgramType(this);
    });
    function selectingAdvertizeProgramType(advertizeTypeElement){
      
       if($(advertizeTypeElement).attr('id')){
        var advertizeTypeProgram = $(advertizeTypeElement).attr('id')
        console.log(advertizeTypeProgram);
       }
        var OptionElement = "<option class='"+advertizeTypeProgram+"' value='"+advertizeTypeProgram+"' selected></option>";

        var selectedProcessElement = $(advertizeTypeElement).children("a").children('span');
        // UnSelect Process Items.
        if(selectedProcessElement.hasClass('tickMarkShow')){
            selectedProcessElement.removeClass('tickMarkShow');     // UnSelect the Process Element.
            $('#advertiser_type  .'+advertizeTypeProgram+' ').remove();
        }
        else{
            selectedProcessElement.addClass('tickMarkShow');
            $( "#advertiser_type" ).append(OptionElement);
        }
    }
/* end of multiple advertize type selector plugg in fetching multiple selected values id  */

$(function(){
  $(':input[type=number]').on('mousewheel',function(e){ $(this).blur(); });
});



/* validating all feilds of kick-off-programm  page */
function validatethis() {
    $(".error-txt").remove();
    $(".lead-form .form-control").removeClass('error-box');
    // var check = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    var numericExpression = /^[0-9]+$/;
    window.is_error = false;
    window.failedFields = new Array();
    if(window.is_reset == true){
      window.is_reset = false;
      return false;
    }else if(window.is_error){
      return false;
    }
// Program Name and all field Validation
  programName = document.getElementById('program_name');
  validateField(programName);
  
  googlePocElem = document.getElementById('google_poc'); 
  validateField(googlePocElem);
  
  validateRegionField();
   
  googlePocEmail = document.getElementById('google_poc_email');
  validateField(googlePocEmail);
   
  validateLocationField();
  
  googlePoc = document.getElementById('google_poc_location'); 
  validateField(googlePoc);

  advertizerType();

  programStartDate = $('#program_start_date');
  checkDate(programStartDate);

  codeType();

  programEndDate = $('#program_end_date');
  checkDate(programEndDate);
  
  estimatedleadNomber = document.getElementById('estimated_lead_no');
  validateField(estimatedleadNomber);

  subjectEstimatedDay();
  
  progOverView = document.getElementById('program_overview');
  validateField(progOverView);

  succesElementOne = document.getElementsByClassName('succes-mat-onebox');
  validateField(succesElementOne);
  
  succesElementTwo = document.getElementsByClassName('succes-mat-twobox');
  validateField(succesElementTwo);
      
  succesElementThree = document.getElementsByClassName('succes-mat-threebox');
  validateField(succesElementThree);
    
  expectations = document.getElementById('expectations'); 
  validateField(expectations);
  
  explainWorkFlow = document.getElementById('explain_workflow');
  validateField(explainWorkFlow);

  winCriteriaq = document.getElementById('win_criteria');
  validateField(winCriteriaq);
 
  leadSubbmission();

  checkChat();

  validateConnectDayType();

  validateConnectDay();

  tag_meeting_time = document.getElementById('tag_meeting_time');
  validateField(tag_meeting_time);
   
    // Check If Error in Form
      if(window.is_error || window.failedFields > 0 ){
        focusElem = failedFields[0];
        $(focusElem).focus();
        return false;
      }else if (window.is_error == false && window.failedFields == 0 ){
        $('#preloaderOverlay').show();
        return true;
      }  
      else{
        return false;
      }
    }

function checkDate(elem){
  if($(elem).val() == ""){
      $(elem).addClass('error-box');
      window.failedFields.push($(elem));
      window.is_error = true;
      return false;
  }
  else
  {
    $(elem).removeClass('error-box');
     window.is_error = false;
     return true;
  } 
}

function leadSubbmission(){
  if(document.getElementById('lead_submission_portal').checked == false && document.getElementById('lead_submission_other').checked == false){
      $('.radio-validate').addClass('error-box');
        window.is_error = true;
        return false;
    }
    else if(document.getElementById('lead_submission_other').checked == true && document.getElementById('lead_sub_other').value == ""){
        $('#lead_sub_other').addClass('error-box');
         $('#lead_submission_other').addClass('error-box');
        window.is_error = true;
        return false;
    }
    else{
      $('.radio-validate').removeClass('error-box');
       $('#lead_sub_other').removeClass('error-box');
         $('#lead_submission_other').removeClass('error-box');
         return true;
      }
}

function codeType(){
      var codeElement = $('.code-type-ul li a .tickMarkShow');
      if(codeElement.length == 0)
        {
          $('#codeTypeBtn').addClass('error-box');
          window.failedFields.push($('#code_type_opt'));
          window.failedFields.push($('#code_type'));
          window.is_error = true;
          return false;
        }
        else
        {
          $("#codeTypeBtn").removeClass('error-box');
           window.is_error = false;
           return true;
        } 
}
function advertizerType(){
    if (document.getElementById('advertiser_type').value == ""){
        $('.add-type').addClass('error-box');
        $('#advertizeTypeBtn').addClass('error-box');
        window.failedFields.push($('.add-type'));
        window.is_error = true;
        return false;
    }
   else{
       $('.add-type').removeClass('error-box');
       $('#advertizeTypeBtn').removeClass('error-box');
       window.is_error = false;
       return true;
    }
}
function checkChat(){
   if(document.getElementById('real_time_live_trans').checked == false && document.getElementById('real_time_chat').checked == false){
      $('.real-chat').addClass('error-box');
       $('.live-trans').addClass('error-box');
        window.is_error = true;
        return false;
          }
       else{
       $('.real-chat').removeClass('error-box');
        $('.live-trans').removeClass('error-box');
        window.is_error = false;
        return true;
          }
}
function subjectEstimatedDay(){
  if(document.getElementById('subject-estimated-day').value == "choose"){
    window.failedFields.push($('#subject-estimated-day')); 
    $('#subject-estimated-day').addClass('error-box'); 
      window.is_error = true;
        return false;
  }
   else{
    $('#subject-estimated-day').removeClass('error-box');
        window.is_error = false;
        return true;
        }
}
 // Validate Region Field
 function validateRegionField(){
  regionElements = $('.region-ul li a .tickMarkShow');
  if(regionElements.length==0)
  {
    $('#regionTypeBtn').addClass('error-box');
    window.failedFields.push($('#regionTypeBtn')); 
    window.failedFields.push($('#regionTypesDiv'));
    window.is_error = true;
    return false;
  }
  else
  {
    $("#regionTypeBtn").removeClass('error-box');
    window.is_error = false;
    return true;
  }
}
// Validate Location Field
function validateLocationField(){
  locationElements = $('.location-ul li a .tickMarkShow');
  if(locationElements.length==0)
  {
    $('#locationTypeBtn').addClass('error-box'); 
    window.failedFields.push($('#locationTypeBtn'));
    window.failedFields.push($('.target-locations-main'));
    window.is_error = true;
    return false;
  }
  else
  {
    $("#locationTypeBtn").removeClass('error-box');
    window.is_error = false;
    return true;
  }
}

function validateConnectDayType(){
  var valofday = document.getElementById('connect').value;
  if (valofday == 'choose'){
    $('#connect').addClass('error-box');
    window.failedFields.push($('#connect'));
    window.is_error = true;
    return false;
  }
  else{
    $('#connect').removeClass('error-box');
    return true;
  }
}

function validateConnectDay(){
  var valofday = document.getElementById('tagteam-connect-day').value;
  if (valofday == 'choose'){
    $('#tagteam-connect-day').addClass('error-box');
    window.failedFields.push($('#tagteam-connect-day'));
    window.is_error = true;
    return false;
  }
  else{
    $('#tagteam-connect-day').removeClass('error-box');
    return true;
  }
}

// Validate Form Field
function validateField(elem) {
  console.log($(elem).val());
  if ($(elem).val() == "" || $(elem).val() == "0" || !$(elem).val() ) {
      $(elem).addClass('error-box');
      window.failedFields.push(elem);
      window.is_error = true;
      return false;
  } else {
      $(elem).removeClass('error-box');
      return true;
  }
}
/*End of validation of kick off program page*/