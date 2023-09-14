

$(document).ready(function(){




    jQuery('.clear-region-filter').click(function(){
        window.location.href = "/city-list/";
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

$("#id_sale_return_order").change(function () {
    var url = $("#disform").attr("data-orderwise-url");  // get the url of the `
    var orderid = $(this).val();
    console.log(orderid);
    var $tr = $(this).closest('tr');
         console.log(distributorId)
    $.ajax({                  // initialize an AJAX request
      url: url,                    // set the url of the request
      data: {
        'orderid': orderid      // add the country id to the GET parameters
      },
      success: function (data) {   // `data` is the return of the  view function
        $(".ItemName", $tr).val(data.item_name);  // replace the contents of the with the data that came from the server
        $('.UOM', $tr).val(data.uom);
      }
    });

  });



  $("#id_sales_order_no").change(function () {
    var url = $("#disform").attr("data-so_url");  // get the url of the `
    var soid = $(this).val();

    $.ajax({                  // initialize an AJAX request
      url: url,                    // set the url of the request
      data: {
        'soid': soid      // add the country id to the GET parameters
      },
      success: function (data) {   // `data` is the return of the  view function
        $("#id_sales_order_date").val(data.s_date);  // replace the contents of the with the data that came from the server
      }
    });

  });  


  $("#id_sale_invoice_no").change(function () {
    var url = $("#disform").attr("data-si-url");  // get the url of the `
    var si_id = $(this).val();

    $.ajax({                  // initialize an AJAX request
      url: url,                    // set the url of the request
      data: {
        'si_id': si_id      // add the country id to the GET parameters
      },
      success: function (data) {   // `data` is the return of the  view function
        $("#id_Bill_Date").val(data.si_id);  // replace the contents of the with the data that came from the server
      }
    });

  }); 


  $("#id_sales_order_no").change(function () {
    var url = $("#disform").attr("filter-data-sorederwise");  // get the url of the `
    var soid = $(this).val();

    $.ajax({                  // initialize an AJAX request
      url: url,                    // set the url of the request
      data: {
        'soid': soid      // add the country id to the GET parameters
      },
      success: function (data) { 
        $("#id_Customers").val(data.cust_code); 
        $("#id_Customer_Name").val(data.cust_name); 
        $("#id_sales_order_date").val(data.bill_date);  
        $("#id_cust_po_no").val(data.cust_po_no);
        $("#id_cust_po_date").val(data.cust_po_date);
        $("#id_SGST_AMOUNT").val(data.sgst_amunt);
        $("#id_CGST_AMOUNT").val(data.cgst_amunt);
        $("#id_Total_GST").val(data.tgst);
        $("#id_Cash_Discount_Amount").val(data.c_dis);
        $("#id_Total_Inventory_Amount").val(data.total_invent);
        $("#id_Total_Amount").val(data.inv_mount);
      }
    });

  }); 
  


  $("#id_sales_order_no").change(function () {
    var url = $("#disform").attr("load_item_dropdown");  // get the url of the `
    var soid = $(this).val();

    $.ajax({                  // initialize an AJAX request
      url: url,                    // set the url of the request
      data: {
        'soid': soid      // add the country id to the GET parameters
      },
      success: function (data) { 
        $(".Item_Code").html(data);
    
      }
    });
  });

  $(".Item_Code").change(function () {
    var url = $("#itemname").attr("all_item_data");  // get the url of the `
    var soid = $(this).val();
    var $tr = $(this).closest('tr');
    $.ajax({                  // initialize an AJAX request
      url: url,                    // set the url of the request
      data: {
        'soid': soid      // add the country id to the GET parameters
      },
      success: function (data) { 
        $('.ItemName',$tr).val(data.sale_itm_nm);
        $('.Quantity',$tr).val(data.sale_qyn);
        $('.UOM',$tr).val(data.sale_um);
        $('.Rate',$tr).val(data.sale_rate);
        $('.Discount',$tr).val(data.sale_dis);
        $('.SRL',$tr).val(data.sale_serial);
        $('.Amount',$tr).val(data.sale_total);
    
      }
    });
  });


  
  $("#id_sales_order_no").change(function () {
    var url = $("#disform").attr("data-cust-code");  // get the url of the `
    var soid = $(this).val();

    $.ajax({                  // initialize an AJAX request
      url: url,                    // set the url of the request
      data: {
        'soid': soid      // add the country id to the GET parameters
      },
      success: function (data) { 
        $("#id_Customers").html(data);
    
      }
    });
  });

  $("#id_sales_order_no").change(function () {
    var url = $("#disform").attr("data-gst-code");  // get the url of the `
    var soid = $(this).val();

    $.ajax({                  // initialize an AJAX request
      url: url,                    // set the url of the request
      data: {
        'soid': soid      // add the country id to the GET parameters
      },
      success: function (data) { 
        $("#id_gst_type").html(data);
    
      }
    });
  });




});

