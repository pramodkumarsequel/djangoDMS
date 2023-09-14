

$(document).ready(function(){




    jQuery('.clear-item-filter').click(function(){
        window.location.href = "/item-list/";
    });

    $(document).ready(function() {
      $('#example4').on('change', '.form-check-input', function() {
          var itemId = $(this).data('item-id');
          var isChecked = $(this).prop('checked');
          $.ajax({
              type: 'GET',
              url: '/item_toggle_active/',
              data: {
                  'toggle_value': isChecked,
                  'row_id': itemId  
              },
              success: function(response) {
              },
              error: function(xhr, status, error) {
                  // Handle error
              }
          });
      });
  
  });
  
    




$('#delete_multiple_btn').on('click', function (event) {
    var id = [];
       
    $(':checkbox:checked').each(function(i){
        id[i]=$(this).val();
    });

    if(id.length!=0){

        Swal.fire({
            title: 'Are you sure you want to delete this record?',
            text: "You won't be able to revert this!",
            type: "warning",
            icon: 'question',
            showCancelButton: true,
            confirmButtonText: "Yes, delete it !!",
            confirmButtonText: 'Delete',
            confirmButtonColor: "#DD6B55"
            
        }).then((result) => {
            if (result.value) {



                $.ajax({
                    url:"/dashboard/delete-multiple-user/",
                    method:"POST",
                    dataType:'json',
                    data:{
                        id,
                        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                    },
                    success:function(res){
                        if(res.warning){
                            document.getElementById("message").innerHTML += '<div class="alert alert-warning alert-dismissible alert-alt solid fade show">\
                                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="btn-close">\
                                </button>'+res.warning+'</div>';
    
                        }
                        if(res.success){
    
                            for(var i=0; i < id.length; i++){
                                if(id[i]!=''){
                                    $('tr#'+id[i]+'').css('background-color','#ccc');
                                    // $('tr#'+id[i]+'').fadeOut('slow');
                                     $('tr#'+id[i]+'').remove(); 
                                }
    
                            }
                            document.getElementById("message").innerHTML += '<div class="alert alert-success alert-dismissible alert-alt solid fade show">\
                                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="btn-close">\
                                </button>'+res.success+'</div>';
    
                        }
                        
                    }
                })


               
            } else if (result.dismiss === Swal.DismissReason.cancel) {
                event.preventDefault();
            }
        });

    
        
    }else{
        Swal.fire({
            type: 'info',
            title: 'Oops...',
            text: 'Please Select Items To Delete',
            confirmButtonColor:"var(--primary)"
        });
    }


});





$('.sweet-success-cancel').on('click', function (event) {
    event.preventDefault();
    const url = $(this).attr('href');

    Swal.fire({
        title: 'Are you sure you want to delete this record?',
        text: "You won't be able to revert this!",
        type: "warning",
        icon: 'question',
        showCancelButton: true,
        confirmButtonText: "Yes, delete it !!",
        confirmButtonText: 'Delete',
        confirmButtonColor: "#DD6B55"
        
    }).then((result) => {
        if (result.value) {
            window.location.href = url;
        } else if (result.dismiss === Swal.DismissReason.cancel) {
            event.preventDefault();
        }
    })
});




$("#id_Hierarchy1").change(function () {
    var url = $("#itmForm").attr("data-itm-url");  // get the url of the `load_cities` view
    var hier1Id = $(this).val();  // get the selected country ID from the HTML input

    $.ajax({                       // initialize an AJAX request
      url: url,                    // set the url of the request (= localhost:8000/hr/ajax/load-cities/)
      data: {
        'hierarchy1': hier1Id       // add the country id to the GET parameters
      },
      success: function (data) {   // `data` is the return of the `load_cities` view function
        $("#id_Hierarchy2").html(data);  // replace the contents of the city input with the data that came from the server
      }
    });

  });
  $("#id_Hierarchy2").change(function () {
    var url = $("#itmForm").attr("data-hier3-url");  // get the url of the `load_cities` view
    var stateId = $(this).val();  // get the selected country ID from the HTML input

    $.ajax({                       // initialize an AJAX request
      url: url,                    // set the url of the request (= localhost:8000/hr/ajax/load-cities/)
      data: {
        'hierarchy2': stateId       // add the country id to the GET parameters
      },
      success: function (data) {   // `data` is the return of the `load_cities` view function
        $("#id_Hierarchy3").html(data);  // replace the contents of the city input with the data that came from the server
      }
    });

  });

  $("#id_Hierarchy3").change(function () {
    var url = $("#itmForm").attr("data-hier-url");  // get the url of the `load_cities` view
    var hier3id = $(this).val();  // get the selected country ID from the HTML input

    $.ajax({                       // initialize an AJAX request
      url: url,                    // set the url of the request (= localhost:8000/hr/ajax/load-cities/)
      data: {
        'hier3id': hier3id       // add the country id to the GET parameters
      },
      success: function (data) {   // `data` is the return of the `load_cities` view function
        $("#id_Hier4").html(data);  // replace the contents of the city input with the data that came from the server
      }
    });

  });

  $("#id_Hier4").change(function () {
    var url = $("#itmForm").attr("data-hier5-url");  // get the url of the `load_cities` view
    var hier4id = $(this).val();  // get the selected country ID from the HTML input

    $.ajax({                       // initialize an AJAX request
      url: url,                    // set the url of the request (= localhost:8000/hr/ajax/load-cities/)
      data: {
        'hier4id': hier4id       // add the country id to the GET parameters
      },
      success: function (data) {   // `data` is the return of the `load_cities` view function
        $("#id_Hier5").html(data);  // replace the contents of the city input with the data that came from the server
      }
    });

  });


 $("#id_base_uom").change(function () {
  debugger;
  var url = $('#itmForm').attr("base-unit-url");
  var base_unit_id  = $(this).val();
  $.ajax({
    url : url,
    data: {
      'base_unit_id':base_unit_id
    },
    success : function (data) {
      $('#id_sale_uom').html(data);

    }
  });
 });

 $("#id_base_uom").change(function () {
  var url = $('#itmForm').attr("purchase-unit-url");
  var base_unit_id  = $(this).val();
  $.ajax({
    url : url,
    data: {
      'base_unit_id':base_unit_id
    },
    success : function (data) {
      $('#id_purchase_uom').html(data);

    }
  });
 });

});

