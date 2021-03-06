 $(document).ready(function(){
        $(".jquery-filterable-filter").hide()
        $("#form-filter").show()
    })

    $('#all').click(function(){
      showAll();
    })

    $('#InSelfDevelopment').click(function(){
      hideAll();
      $('.inselfdevelopment').show();
    })

    $('#InUIUXReview').click(function(){
      hideAll();
      $('.inuiuxreview').show()
    })

    $('#InDesign').click(function(){
      hideAll();
      $('.indesign').show()
    })
    $('#InDevelopment').click(function(){
      hideAll();
      $('.indevelopment').show()
    })

    $('#InStage').click(function(){
      hideAll();
      $('.instage').show()
    })
    $('#InTesting').click(function(){
      hideAll();
      $('.intest').show()
    })
    $('#Implemented').click(function(){
      hideAll();
      $('.inimplement').show()
    })

    function showAll(){
      $('.indevelopment').show()
      $('.indesign').show()
      $('.inuiuxreview').show()
      $('.instage').show()
      $('.inimplement').show()
      $('.intest').show()
      $('.inselfdevelopment').show()
    }

    function hideAll(){
      $('.indevelopment').hide()
      $('.indesign').hide()
      $('.inuiuxreview').hide()
      $('.instage').hide()
      $('.inimplement').hide()
      $('.intest').hide()
      $('.inselfdevelopment').hide()
    }



    $('#CID').click(function(){
      $('#CIDText').toggle()
    })

  
  function filter(phrase, _id){
    var words = phrase.value.toLowerCase().split(" ");
    var _table = document.getElementById(_id);
    var ele;
    for (var r = 1; r < _table.rows.length; r++){
      ele = _table.rows[r].innerHTML.replace(/<[^>]+>/g,"");
            var displayStyle = 'none';
            for (var i = 0; i < words.length; i++) {
          if (ele.toLowerCase().indexOf(words[i])>=0)
        displayStyle = '';
          else {
        displayStyle = 'none';
        break;
          }
            }
      _table.rows[r].style.display = displayStyle;
    }
  }

 $(document).ready(function(){
     $('.pop_up').mouseover(function(){     
        $(this).find('.popover').show();
      })
      $('.pop_up').mouseout(function(){
          $(this).find('.popover').hide();
      })

      /* sorting function start here*/
        $("#Leads").tablesorter({ 
          // pass the headers argument and assing a object 
          headers: { 
              // assign the secound column (we start counting zero) 
              0: { 
                  // disable it by setting the property sorter to false 
                  sorter: false 
              }, 
              1: { 
                  // disable it by setting the property sorter to false 
                  sorter: false 
              }, 
              2: { 
                  // disable it by setting the property sorter to false 
                  sorter: false 
              },
              3: { 
                  // disable it by setting the property sorter to false 
                  sorter: false 
              }, 
              4: { 
                  // disable it by setting the property sorter to false 
                  sorter: false 
              }, 
              6: { 
                  // disable it by setting the property sorter to false 
                  sorter: false 
              },
              7: { 
                  // disable it by setting the property sorter to false 
                  sorter: false 
              },
              8: { 
                  // disable it by setting the property sorter to false 
                  sorter: false 
              },
              10: { 
                  // disable it by setting the property sorter to false 
                  sorter: false 
              }
          } 
      });
    /*end sorting function*/
    /*comment popup*/
    $('[data-toggle="tooltip"]').tooltip({
          'placement': 'right'
      });
    /*comment popup*/
  })


$('.pingchat').click(function(){
  $('.popup_overlay').show()
})

$('.close').click(function(){
  $('.popup_overlay').hide()
})

$('#habla_panel_div').click(function(){
  $('.popup_overlay').hide()
  $('#habla_panel_div').hide()
})


// sorting function statrt here


 $("#statusHeader").click(function(){

      $('#sortBy').text($("#statusHeader").text());
      $("#StatusRow").trigger("click");
      
   })

   $("#CodeTypeHeader").click(function(){
      $('#sortBy').text($("#CodeTypeHeader").text());
      $("#CodeTypeRow").trigger("click");

   })

   $("#RecentHeader").click(function(){
      $('#sortBy').text($("#RecentHeader").text());
      $("#RecentRow").trigger("click");
   })

   $('#Leads thead>tr>th').unbind('click');

/* sorting function end here*/

/* */

$('#SubmitFeedback').click(function(){
    $(".error-box").removeClass('error-box');
    var feedbackTitle = $('#feedbackTitle').val();
    var feedbackType = $('#feedbackType').val();
    var comments = $('#comments').val();
    var lead_type = 'wpp'
    if (feedbackTitle === '' ){
      $('#feedbackTitle').addClass('error-box');
    }else if(feedbackType === 'Feedback Type'){
      $('#feedbackType').addClass('error-box');
    }else if(comments === ''){
      $('#comments').addClass('error-box');
    }else{
      $('#closeFeedbcak').trigger('click');
      $('#preloaderOverlay').show();
      dataString = {'title': feedbackTitle, 'type': feedbackType, 'comment': comments, 'lead_id': window.lead_id, 'lead_type': lead_type}
      $.ajax({
          url: "/main/create-feedback-from-lead-status",
          data: dataString,
          type: 'GET',
          dataType: "json",
          success: function(data) {
            if(data === 'SUCCESS'){
              alert('feedback succesfully created ')
              $('#preloaderOverlay').hide();
              $('#closeFeedbcak').trigger('click');
              $('#feedbackTitle').val('');
              $('#feedbackType').prop('selectedIndex', 0);
              $('#comments').val('');
            }
          },
          error: function(jqXHR, textStatus, errorThrown) {
              alert('failure');
              $('#preloaderOverlay').hide();
          }
        }); 
    }
    
    })


/*search functionality for the wpp-leads table*/

$('input[name="wppleadSearch"]').on('keyup', function(){
    searchLeads($(this).val());
  });

$('input[name="wppleadSearch"]').on('focusout', function(){
    $('#searchError').hide();
  });


$('.fa-search').on('click', function(){
    searchLeads($('#wppleadSearch').val());
})

$('#wppleadSearch').keypress(function (e) {
  var key = e.which;
  if(key == 13)  // the enter key code
   {
     searchLeads($('#wppleadSearch').val());
   }
});

function searchLeads(searchText){
  $('#searchError').hide();
    if((!searchText) || (searchText.length <=3)){
        //clearLeadDetails();
        $('#searchError').show();

    }else{
        $.ajax({
            'method': 'GET',
            'dataType': 'json',
            'data': {'search-text':searchText, 'lead-type': 'WPP'},
            'url': "/leads/searh-leads/",
            success: function(response){
              // console.log(response);
              $('#searchError').hide();
              if(response['lead_list'].length != 0){
                $('.pre-load-img').hide();
                // $('.services_action').hide();
                setWppLeadSummary(response['lead_status_dict'])
                setWppLeadSummaryTable(response['lead_list'])
              }else{
                $('.services_action').show();
                $('#tableBody').html('');
                $('.pre-load-img').show();
              }
            },
            error:function(xhr, status, error){
                alert('No Leads found for the search');
            }
        })
    }
}

treatment_type = $('#treatment_type').val()

$('#reset').click(function(event){
  event.preventDefault();
  $.ajax({
    'method': 'GET',
    'dataType': 'json',
    'data': {'treatment_type': treatment_type},
    'url': "/leads/get-wpp-lead-summary-by-treatment/",
    success: function(data){
      $('#wppleadSearch').val('');
      setWppLeadSummary(data['status_count'])
      setWppLeadSummaryTable(data['leads_list'])
    },
    error:function(xhr, status, error){
      console.log('failure');
    }
  });
});