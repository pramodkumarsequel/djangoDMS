

$(document).ready(function(){
    $("#id_sale_return_order").change(function () {
        const url = $("#disform").attr("data-orderwise-url");  // get the url of the `
        const orderid = $(this).val();
        console.log(orderid);
        const $tr = $(this).closest('tr');
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
        const url = $("#disform").attr("data-so_url");  // get the url of the `
        const soid = $(this).val();
    
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
        const url = $("#disform").attr("data-si-url");  // get the url of the `
        const si_id = $(this).val();
    
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
        const url = $("#disform").attr("filter-data-sorederwise");  // get the url of the `
        const soid = $(this).val();
    
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
      
    
    
      $("#id_sales_order_no").change(function (e) {
        e.preventDefault();
        const url = $("#disform").attr("load_item_dropdown");  // get the url of the `
        const soid = $(this).val();
        $(this).each(function() {
          order_id = $(this).val();
        }); 
        $.ajax({                  // initialize an AJAX request
          url: url,                    // set the url of the request
          data: {
            'soid': soid,
          },
          success: function (data) { 
            $(".Item_Code").html(data);   
          }
        });

        $(".Item_Code").change(function (e) {
          e.preventDefault();
          const url = $("#itemname").attr("all_item_data");  // get the url of the `
          const soid = $(this).val();
          const $tr = $(this).closest('tr');
          $.ajax({                  // initialize an AJAX request
            url: url,                    // set the url of the request
            data: {
              'soid': soid,
              'order_id':order_id

            },
            success: function (data) { 
              $('.ItemName',$tr).val(data.sale_itm_nm);
              $('.bal_qty',$tr).val(data.sale_qyn);
              $('.UOM',$tr).val(data.sale_um);
              $('.Rate',$tr).val(data.sale_rate);
              $('.Discount',$tr).val(data.sale_dis);
              $('.SRL',$tr).val(data.sale_serial);
              $('.Amount',$tr).val(data.sale_total);
          
            }
          });
        });

      });
         
      $("#id_sales_order_no").change(function () {
        const url = $("#disform").attr("data-cust-code");  // get the url of the `
        const soid = $(this).val();
    
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
        const url = $("#disform").attr("data-gst-code"); 
        const soid = $(this).val();
    
        $.ajax({               
          url: url,                  
          data: {
            'soid': soid     
          },
          success: function (data) { 
            $("#id_gst_type").html(data);
        
          }
        });
      });
    
    
    $('.table-responsive input').on("input", function () {
        const total = []
        const $tr = $(this).closest('tr');
        const textValue1 = $("input.Rate", $tr).val();
        const textValue2 = $('input.Quantity', $tr).val();
        const textValue3 = $('input.Discount', $tr).val();
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
      $('#id_Total_Amount').val(sum);
  }
    
    $("#id_gst_type").change(function () {
        const url = $("#disform").attr("data-gst-url");
        var inv_amount = $('#id_Total_Inventory_Amount').val();
        const id_gst_type = $(this).val();

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
          const new_num = total_gst_amount.toFixed(2);
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
        dis = (amt*dis)/100;
        total_discount+= dis;
      });
      $('#id_Cash_Discount_Amount').val(total_discount);
    }
    
    
    
    $("#id_Customers").change(function () {
        const url = $("#disform").attr("data-cust-url");  // get the url of the `
        const custid = $(this).val();
    
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
    
    
      $('#id_sale_invoice_no').change(function() {
        const url = $("#disform").attr("data-si-load");  // get the url of the `
        const si_id = $(this).val();
    
        $.ajax({                  // initialize an AJAX request
          url: url,                    // set the url of the request
          data: {
            'si_id': si_id      // add the country id to the GET parameters
          },
          success: function (data) {   // `data` is the return of the  view function
            $("#id_SGST_AMOUNT").val(data.sgst);
            $("#id_CGST_AMOUNT").val(data.cgst);
            $('#id_Total_GST').val(data.t_gst);
            $('#id_Cash_Discount_Amount').val(data.cash_dis);
            $('#id_Total_Inventory_Amount').val(data.t_inventory);
            $('#id_Total_Invoice_Amount').val(data.t_invoice);
          }
        });
    
      });
    
    
    
    
      $('#id_sale_invoice_no').change(function() {
        const url = $("#disform").attr("data-load-item");  // get the url of the `
        const si_id = $(this).val();
    
        $.ajax({                  // initialize an AJAX request
          url: url,                    // set the url of the request
          data: {
            'si_id': si_id      // add the country id to the GET parameters
          },
          success: function (data) {   // `data` is the return of the  view function
            $(".Item_Code").html(data);
    
          }
        });
    
      });  
      
      $('#id_sale_invoice_no').change(function() {
        const url = $("#disform").attr("data-gst-dropdown");  // get the url of the `
        const si_id = $(this).val();
    
        $.ajax({                  // initialize an AJAX request
          url: url,                    // set the url of the request
          data: {
            'si_id': si_id      // add the country id to the GET parameters
          },
          success: function (data) {   // `data` is the return of the  view function
            $("#id_gst_type").html(data);
    
          }
        });
    
      });  
    
      $('#id_sale_invoice_no').change(function() {
        const url = $("#disform").attr("load-cust-code");  // get the url of the `
        const si_id = $(this).val();
    
        $.ajax({                  // initialize an AJAX request
          url: url,                    // set the url of the request
          data: {
            'si_id': si_id      // add the country id to the GET parameters
          },
          success: function (data) {   // `data` is the return of the  view function
            $("#id_Customers").html(data);
    
          }
        });
    
      }); 
  

    
    });
    
    