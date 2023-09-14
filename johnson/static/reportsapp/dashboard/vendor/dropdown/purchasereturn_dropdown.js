 $("#id_Distributors").change(function () {
      var url = $("#disform").attr("data-dis-url");  // get the url of the `
      var distributorId = $(this).val();

      $.ajax({                  // initialize an AJAX request
        url: url,                    // set the url of the request
        data: {
          'Distributors': distributorId      // add the country id to the GET parameters
        },
        success: function (data) {   // `data` is the return of the  view function
          $("#id_distributor_name").val(data.distributor_name);  // replace the contents of the with the data that came from the server
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
    $('#id_Total_Invoice_Amount').val(sum);
}


$("#id_gst_type").change(function () {
  var url = $("#disform").attr("data-gst-url");  // get the url of the `
  var id_gst_type = $(this).val();
  var inv_amount = $('#id_Total_Inventory_Amount').val();
  //var $tr = $(this).closest('tr');

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
      $('#id_Total_GST').val(new_num.toFixed(2));
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
  $('#id_total_discount_amount').val(total_discount);
}

$("#id_pi_no").change(function () {
  var url = $("#disform").attr("data-pidate-url");  // get the url of the `
  var pid = $(this).val();
    $.ajax({                  // initialize an AJAX request
      url: url,                    // set the url of the request
      data: {
        'pid': pid      // add the country id to the GET parameters
      },
      success: function (data) {   // `data` is the return of the  view function
        $("#id_pi_date").val(data.piDate);
        $("#id_Supplier_Invoice_No").val(data.sup); 
        $("#id_SAP_Order_Date").val(data.supdate); 
        $("#id_Distributors").val(data.dcode);
        $("#id_distributor_name").val(data.dname);
       $("#id_CGST_AMOUNT").val(data.cgst.toFixed(2));
       $("#id_SGST_AMOUNT").val(data.cgst.toFixed(2));
       $("#id_Total_GST").val(data.tgst.toFixed(2));
       $("#id_total_discount_amount").val(data.td.toFixed(2));
       $("#id_Total_Inventory_Amount").val(data.tinv.toFixed(2));
       $("#id_Total_Invoice_Amount").val(data.tinvoice.toFixed(2));
      }
    });

  }); 

  $("#id_pi_no").change(function () {
    var url = $("#disform").attr("data-all-popup");  // get the url of the `
    var pid = $(this).val();
      $.ajax({                  // initialize an AJAX request
        url: url,                    // set the url of the request
        data: {
          'pid': pid      // add the country id to the GET parameters
        },
        success: function (data) {   // `data` is the return of the  view function
         $("#id_Distributors").html(data);
        }
      });
  
    });   


    $("#id_pi_no").change(function () {
      var url = $("#disform").attr("data-gst-popup");  // get the url of the `
      var pid = $(this).val();
        $.ajax({                  // initialize an AJAX request
          url: url,                    // set the url of the request
          data: {
            'pid': pid      // add the country id to the GET parameters
          },
          success: function (data) {   // `data` is the return of the  view function
           $("#id_gst_type").html(data);
          }
        });
    
      });    
      
      $("#id_pi_no").change(function () {
        var url = $("#disform").attr("pur-line-item");  
        var $tr = $(this).closest('tr');
        var pid = $(this).val();
          $.ajax({                
            url: url,              
            data: {
              'pid': pid    
            },
            success: function (data) {  
             $(".Item_Code").html(data);
            
            }
          });

          $(".Item_Code").change(function () {
            var url = $("#itemname").attr("data-line-code"); 
            var distributorId = $(this).val();
            var $tr = $(this).closest('tr');
            $.ajax({               
              url: url,                 
              data: {
                'items': distributorId,
                'pid': pid   
              },
              success: function (data) {  
                $(".ItemName", $tr).val(data.itmname); 
                $('.UOM', $tr).val(data.uom);
                $('.Quantity', $tr).val(data.qyn);
                $('.Rate', $tr).val(data.rate);
                $('.Discount', $tr).val(data.dis);
                $('.Amount', $tr).val(data.tamunt);
              }
            });
        
          });
      
        });      

        
        $("#id_pi_no").change(function () {
          var url = $("#disform").attr("data_vendor_load");  // get the url of the `
          var pid = $(this).val();
            $.ajax({                  // initialize an AJAX request
              url: url,                    // set the url of the request
              data: {
                'pid': pid      // add the country id to the GET parameters
              },
              success: function (data) { 
                $("#id_Vendor_Name").html(data);
              }
            });
        
          });         