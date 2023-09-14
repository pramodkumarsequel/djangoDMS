$(document).ready(function(){
  $("#id_Distributors").change(function () {
      var url = $("#disform").attr("data-dis-url");  // get the url of the `
      var distributorId = $(this).val();
           console.log(distributorId)

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

$("#id_purchase_invoice").change(function () {
    var url = $("#disform").attr("data-orderno-url");  // get the url of the `
    var orderid = $(this).val();
        console.log(orderid)
  
      $.ajax({                  // initialize an AJAX request
        url: url,                    // set the url of the request
        data: {
          'orderid': orderid      // add the country id to the GET parameters
        },
        success: function (data) {   // `data` is the return of the  view function
          //$("#id_Bill_Date").val(data.odate);
          $("#id_mrn_no").html(data);
        }
      });
  
    });
  

    $("#id_mrn_no").change(function () {
      var url = $("#disform").attr("data-mrn-url");  // get the url of the `
      var mrnid = $(this).val();
        $.ajax({                  // initialize an AJAX request
          url: url,                    // set the url of the request
          data: {
            'mrnid': mrnid      // add the country id to the GET parameters
          },
          success: function (data) {   // `data` is the return of the  view function
            $("#id_mrn_date").val(data.mrndate); 
            $('#id_Supplier_Invoice_No').val(data.sup_no);
            $('#id_SAP_Order_Date').val(data.sup_date);
            $('#id_gst_type').val(data.gtype);
            $('#id_SGST_AMOUNT').val(data.msgst);
            $('#id_CGST_AMOUNT').val(data.mcgst);
            $('#id_Total_GST').val(data.tgst);
            $('#id_total_discount_amount').val(data.mcdis);
            $('#id_Total_Inventory_Amount').val(data.t_inv);
            $('#id_Total_Invoice_Amount').val(data.mtamount);
            //$('#id_Vendor_Name').val(data.bill_ent);
            

          }
        });
    
      });    


      $("#id_purchase_invoice").change(function () {
        var url = $("#disform").attr("data-pi_date");  // get the url of the `
        var orderid = $(this).val();
            console.log(orderid)
      
          $.ajax({                  // initialize an AJAX request
            url: url,                    // set the url of the request
            data: {
              'orderid': orderid      // add the country id to the GET parameters
            },
            success: function (data) {   // `data` is the return of the  view function
              $("#id_Bill_Date").val(data.final_date);
            }
          });
      
        });
      

        $("#id_mrn_no").change(function () {
          var url = $("#disform").attr("data-ds-url");
          var orderid = $(this).val();
              console.log(orderid)
        
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


          $("#id_mrn_no").change(function () {
            var url = $("#disform").attr("data-gst-drop");
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


            
          $("#id_mrn_no").change(function () {
            var url = $("#disform").attr("data-item-drop");
            var orderid = $(this).val();   
              $.ajax({                  
                url: url,                   
                data: {
                  'orderid': orderid
                },
                success: function (data) {
                  $(".Item_Code").html(data);
                }
              });

              $(".Item_Code").change(function () {
                var url = $("#itemname").attr("data-itm-line");  // get the url of the `
                var distributorId = $(this).val();
                var $tr = $(this).closest('tr');
                $.ajax({                  // initialize an AJAX request
                  url: url,                    // set the url of the request
                  data: {
                    'items': distributorId,
                    'orderid':orderid

                  },
                  success: function (data) {   // `data` is the return of the  view function
                    $(".ItemName", $tr).val(data.itmname);  // replace the contents of the with the data that came from the server
                    $('.UOM', $tr).val(data.uom);
                    $('.bal_qty', $tr).val(data.qyan);
                    $('.Rate', $tr).val(data.rate);
                    $('.Discount', $tr).val(data.dis);
                    $('.SRL', $tr).val(data.srl);
                    $('.Amount', $tr).val(data.amt);
                  }
                });
            
              });
            



          
            });    

});



$('#id_mrn_no').change(function () {
  debugger;
  var url =$('#disform').attr("data_load_vendor");
  var mrnid = $(this).val();
  $.ajax({
    url:url,
    data: {
      'mrn_id': mrnid
    },
    success: function (data) {
      $('#id_Vendor_Name').html(data);
    }
  });
});
