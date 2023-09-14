
  $("#id_Distributors").change(function () {
      var url = $("#disform").attr("data-dis-url");  // get the url of the `
      var distributorId = $(this).val();


      $.ajax({                  // initialize an AJAX request
        url: url,                    // set the url of the request
        data: {
          'Distributors': distributorId      // add the country id to the GET parameters
        },
        success: function (data) {   // `data` is the return of the  view function
 
          $("#id_Distributor_Name").val(data.distributor_name);  // replace the contents of the with the data that came from the server
        }
      });

    });

    function myFunction(e) {
    document.getElementById("myText").value = e.target.value
}

$('.table-responsive input').on("input", function () {
    var total = []
    var $tr = $(this).closest('tr');
    var textValue1 = $("input.Rate", $tr).val();
    var textValue2 = $('input.Quantity', $tr).val();
    var textValue3 = $('input.Discount', $tr).val();
    amt = textValue1 * textValue2;
    dis = amt*textValue3/100;
    amt=amt-dis
    $('.Amount', $tr).val(amt);
    calc_total();
    calc_total_gst();
});

function calc_total() {
    var sum = 0;
    $(".Amount").each(function () {
        sum += parseFloat($(this).val());
    });
    
    $('#id_Total_Inventory_Amount').val(sum);
    $('#id_Total_Invoice_Amount').val(sum);
}


$("#id_gst_type").change(function () {
  var url = $("#disform").attr("data-gst-url");  // get the url of the `
  var id_gst_type = $(this).val();
  var inv_amount = $('#id_Total_Inventory_Amount').val();
  console.log(inv_amount);
  //var $tr = $(this).closest('tr');

  console.log(id_gst_type)
  $.ajax({                  // initialize an AJAX request
    url: url,                    // set the url of the request
    data: {
      'id_gst_type': id_gst_type      // add the country id to the GET parameters
    },
    success: function (data) {   // `data` is the return of the  view function
      sgst = data.SGST_AMOUNT;
      cgst = data.CGST_AMOUNT;
      total_sgst = inv_amount*sgst/100;
      total_cgst = inv_amount*cgst/100;
      total_gst_amount = total_sgst+total_cgst;
      var new_num = total_gst_amount.toFixed(2);

      $("#id_SGST_AMOUNT").val(total_sgst.toFixed(2));  // replace the contents of the with the data that came from the server
      $('#id_CGST_AMOUNT').val(total_cgst.toFixed(2));
      $('#id_Total_GST').val(new_num);
    }
  });

});
function calc_total_gst() {
  var total_discount = 0;
  $(".Discount").each(function () {
    var $tr = $(this).closest('tr');
    var rate = $("input.Rate", $tr).val();
    var qyn = $('input.Quantity', $tr).val();
    var dis = $('input.Discount', $tr).val();
    amt = rate*qyn;
    dis = amt*dis/100;
    total_discount+= dis;
  });
  $('#id_Cash_Discount_Amount').val(total_discount);
}



$("#id_Customers").change(function () {
    var url = $("#disform").attr("data-cust-url");  // get the url of the `
    var custid = $(this).val();

    $.ajax({                  // initialize an AJAX request
      url: url,                    // set the url of the request
      data: {
        'custid': custid      // add the country id to the GET parameters
      },
      success: function (data) {   // `data` is the return of the  view function
        $("#id_Customer_Name").val(data.customer_name);  // replace the contents of the with the data that came from the server
      }
    });

  });


  $("#id_dl_note_no").change(function () {
    var url = $("#disform").attr("data-di-url");  // get the url of the `
    var dlid = $(this).val();

    $.ajax({                  // initialize an AJAX request
      url: url,                    // set the url of the request
      data: {
        'dlid': dlid      // add the country id to the GET parameters
      },
      success: function (data) {   // `data` is the return of the  view function
        $("#id_dl_note_date").val(data.d_date);  // replace the contents of the with the data that came from the server
      }
    });

  });  



  $("#id_sale_order").change(function () {
    var url = $("#disform").attr("data-so_url");  // get the url of the `
    var soid = $(this).val();

    $.ajax({                  // initialize an AJAX request
      url: url,                    // set the url of the request
      data: {
        'soid': soid      // add the country id to the GET parameters
      },
      success: function (data) {   // `data` is the return of the  view function
        $("#id_sale_order_date").val(data.s_date);  // replace the contents of the with the data that came from the server
      }
    });

  });   



  $("#id_dl_note_no").change(function () {
    var url = $("#disform").attr("dl-full-data");  // get the url of the `
    var dlid = $(this).val();

    $.ajax({                  // initialize an AJAX request
      url: url,                    // set the url of the request
      data: {
        'dlid': dlid      // add the country id to the GET parameters
      },
      success: function (data) {   // `data` is the return of the  view function
        // $("#id_dl_note_date").val(data.bill_date); 
        $("#id_SGST_AMOUNT").val(data.sgst);
        $("#id_CGST_AMOUNT").val(data.cgst);
        $("#id_Total_GST").val(data.total_gst);
        $("#id_Cash_Discount_Amount").val(data.cash_dis);
        $('#id_Total_Inventory_Amount').val(data.total_inventory);
        $("#id_Total_Invoice_Amount").val(data.total_amount);
      }
    });

  });   

  $("#id_dl_note_no").change(function () {
    var url = $("#disform").attr("dl-item-load"); 
    var dlid = $(this).val();

    $.ajax({            
      url: url,             
      data: {
        'dlid': dlid  
      },
      success: function (data) { 
        $(".Item_Code").html(data); 

   
      }
    });


    $(".Item_Code").change(function () {
      var url = $("#itemname").attr("data-item-load"); 
      var dl = $(this).val();
      var $tr = $(this).closest('tr');
  
      $.ajax({           
        url: url,             
        data: {
          'dlid': dl,
          'delivery_order': dlid  
        },
        success: function (data) {  
          $(".ItemName", $tr).val(data.itm_name);
          $(".bal_qty",$tr).val(data.qyt); 
          $(".Rate",$tr).val(data.rate); 
          $(".UOM",$tr).val(data.uom); 
          $(".Discount",$tr).val(data.discount); 
          $(".SRL",$tr).val(data.srl); 
          $(".Amount",$tr).val(data.amount); 
        }
      });
  
    });
    

  }); 

  $("#id_dl_note_no").change(function () {
    var url = $("#disform").attr("dl-gst-dropdown");  // get the url of the `
    var dlid = $(this).val();

    $.ajax({                  // initialize an AJAX request
      url: url,                    // set the url of the request
      data: {
        'dlid': dlid      // add the country id to the GET parameters
      },
      success: function (data) {   // `data` is the return of the  view function
        $("#id_gst_type").html(data); 
   
      }
    });

  }); 

  $("#id_dl_note_no").change(function () {
    var url = $("#disform").attr("dl-cust-dropdwon");  // get the url of the `
    var dlid = $(this).val();

    $.ajax({                  // initialize an AJAX request
      url: url,                    // set the url of the request
      data: {
        'dlid': dlid      // add the country id to the GET parameters
      },
      success: function (data) {   // `data` is the return of the  view function
        $("#id_Customers").html(data); 
   
      }
    });

  }); 

  
  $("#id_dl_note_no").change(function () {
    var url = $("#disform").attr("dl-so-dropdown");  // get the url of the `
    var dlid = $(this).val();

    $.ajax({                  // initialize an AJAX request
      url: url,                    // set the url of the request
      data: {
        'dlid': dlid      // add the country id to the GET parameters
      },
      success: function (data) {   // `data` is the return of the  view function
        $("#id_sale_order").html(data); 
   
      }
    });

  });
  