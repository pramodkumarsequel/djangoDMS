$("#id_warehouseCode").change(function () {
    debugger;
    var url = $("#whform").attr("data-whf-url");  // get the url of the `
    var wh_id = $(this).val();
    console.log(wh_id);
    $.ajax({                  // initialize an AJAX request
      url: url,                    // set the url of the request
      data: {
        'wh_id': wh_id,     // add the country id to the GET parameters
      },
      success: function (data) {   // `data` is the return of the  view function
        $("#id_warehouseName").val(data.whName);  // replace the contents of the with the data that came from the server
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

$(".Item_Code").change(function () {
    var url = $("#whform").attr("data-itm-url");  // get the url of the `
    var distributorId = $(this).val();
    var $tr = $(this).closest('tr');
    $.ajax({                  // initialize an AJAX request
      url: url,                    // set the url of the request
      data: {
        'items': distributorId      // add the country id to the GET parameters
      },
      success: function (data) {   // `data` is the return of the  view function
        $(".ItemName", $tr).val(data.item_name);  // replace the contents of the with the data that came from the server
        $('.UOM', $tr).val(data.um);
        $('.Rate', $tr).val(data.pr);
        $('.Amount', $tr).val(0);
        $('.Quantity', $tr).val(0);
        $('.Discount', $tr).val();
      }
    });

  });