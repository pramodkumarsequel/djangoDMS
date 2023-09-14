$(document).ready(function(){


  $("#id_Distributors").change(function () {
      var url = $("#disform").attr("data-dis-url");  // get the url of the `
      var distributorId = $(this).val();

      $.ajax({                  // initialize an AJAX request
        url: url,                    // set the url of the request
        data: {
          'Distributors': distributorId      // add the country id to the GET parameters
        },
        success: function (data) {   // `data` is the return of the  view function
         debugger;
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
    var total_invoice = 0;
    $(".Amount").each(function () {
        sum += parseFloat($(this).val());
    });
    
    $('#id_Total_Inventory_Amount').val(sum);
    $('#id_Total_Amount').val(sum);
}


$("#id_gst_type").change(function () {
  var url = $("#disform").attr("data-gst-url");  // get the url of the `
  var id_gst_type = $(this).val();
  var inv_amount = $('#id_Total_Inventory_Amount').val();
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
      total_sgst = total_sgst.toFixed(2);
      total_cgst = total_cgst.toFixed(2);
      $("#id_SGST_AMOUNT").val(total_sgst);  // replace the contents of the with the data that came from the server
      $('#id_CGST_AMOUNT').val(total_cgst);
      $('#id_Total_GST').val(new_num);
    }
  });

});
function calc_total_gst() {
  var total_discount = 0;
  $(".Discount").each(function () {
    var $tr = $(this).closest('tr');
    // total_discount += parseFloat($(this).val());
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
       debugger;
        $("#id_Customer_Name").val(data.customer_name);  // replace the contents of the with the data that came from the server
      }
    });

  });

$("#id_p_order_no").change(function () {
    var url = $("#disform").attr("data-orderno-url");  // get the url of the `
    var orderid = $(this).val();
      $.ajax({                
        url: url,                    
        data: {
          'orderid': orderid   
        },
        success: function (data) {  
          $("#id_Bill_Date").val(data.odate);
          $("#id_Distributor_Name").val(data.ordis);
        }
      });

    });

$("#id_p_order_no").change(function () {
  var url = $("#disform").attr("data-ds-url");
  var orderid = $(this).val();

    $.ajax({                  
      url: url,                   
      data: {
        'orderid': orderid
      },
      success: function (data) {
        $("#id_Distributors").html(data);
      }
    });

  });

  function myFunction(e) {
  document.getElementById("myText").value = e.target.value
}  

$("#id_p_order_no").change(function () {
  var url = $("#disform").attr("data-gst-load");
  var orderid = $(this).val();
      console.log(orderid)

    $.ajax({                  
      url: url,                   
      data: {
        'orderid': orderid
      },
      success: function (data) {
        $("#id_gst_type").html(data);
      }
    });

  });

  function myFunction(e) {
  document.getElementById("myText").value = e.target.value
}


$("#id_p_order_no").change(function () {
  var url = $("#disform").attr("data-order-wise");
  var pur_id = $(this).val();
    $.ajax({                  
      url: url,                   
      data: {
        'orderid': pur_id,
      },
      success: function (data) {
        $(".Item_Code").html(data);
      }
    });
  $(".Item_Code").change(function () {
    var url = $("#itemname").attr("data-itm-url");  // get the url of the `
    var distributorId = $(this).val();
    var $tr = $(this).closest('tr');
         console.log(distributorId)
    $.ajax({                  // initialize an AJAX request
      url: url,                    // set the url of the request
      data: {
        'items': distributorId,
        'purchase_order_id':pur_id
      },
      success: function (data) {   
        $(".ItemName", $tr).val(data.item);  
        $('.UOM', $tr).val(data.um);
        $('.bal_qty', $tr).val(data.qty);
        $('.Rate', $tr).val(data.rate);
        $('.Discount', $tr).val(data.dis);
        $('.SRL', $tr).val(data.sr);
        $('.Amount', $tr).val(data.totl);
      }
    });


  });
});

});


$("#id_p_order_no").change(function () {
 //window.location.href = "/receiptnote-create/";
  var url = $("#disform").attr("data-item_id");
  var pur_id = $(this).val();
    $.ajax({                  
      url: url,                   
      data: {
        'orderid': pur_id,
      },
      success: function (data) {
        $("#fruit-name").val(data.or);
      }
    });
  });



  $("#id_p_order_no").change(function () {
    var url = $("#disform").attr("data_vendor_load");  // get the url of the `
    var orderid = $(this).val();
      $.ajax({                
        url: url,                    
        data: {
          'orderid': orderid   
        },
        success: function (data) {  
          $('#id_billing_entity').html(data);
        }
      });

    });

