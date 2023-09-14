$(".Item_Code").change(function () {
    var url = $("#itemname").attr("load_item_data"); 
    var distributorId = $(this).val();
    var $tr = $(this).closest('tr');
         console.log(distributorId)
    $.ajax({           
      url: url,                 
      data: {
        'items': distributorId     
      },
      success: function (data) {   
        $(".ItemName", $tr).val(data.item_name);  
        $('.UOM', $tr).val(data.uom);
        $('.Rate', $tr).val(data.p_price);
      }
    });

  });

  $('.table-responsive input').on("input", function () {
    var total = []
    var $tr = $(this).closest('tr');
    var textValue1 = $("input.Rate", $tr).val();
    var textValue2 = $('input.Quantity', $tr).val();
    var textValue3 = $('input.Discount', $tr).val();
    amt = textValue1 * textValue2;
    dis = amt*textValue3/100;
    amt=amt-dis
    console.log(amt);
    $('.Amount', $tr).val(amt);
    calc_total();
    calc_total_gst();
    calc_gst_type();
});

function calc_total() {
    var sum = 0;
    var total_invoice = 0;
    $(".Amount").each(function () {
        sum += parseFloat($(this).val());
    });
    
    $('#id_Total_Inventory_Amount').val(sum);
    $('#id_Total_Invoice_Amount').val(sum);
}

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
  $('#id_total_discount_amount').val(total_discount.toFixed(2));
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

$("#id_Distributors").change(function () {
  var url = $("#disform").attr("data-dis-url");  
  var distributorId = $(this).val();
       console.log(distributorId)

  $.ajax({                
    url: url,                 
    data: {
      'Distributors': distributorId      // add the country id to the GET parameters
    },
    success: function (data) {   // `data` is the return of the  view function
     debugger;
      $("#id_Distributor_Name").val(data.distributor_name);  // replace the contents of the with the data that came from the server
    }
  });

});

