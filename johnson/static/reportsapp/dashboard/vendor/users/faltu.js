$("#id_order_no").change(function () {
    var url = $("#disform").attr("data-item");
    var order_id = $(this).val();
         console.log(order_id);

    $.ajax({                  // initialize an AJAX request
      url: url,                    // set the url of the request
      data: {
        'order_id':order_id,     // add the country id to the GET parameters
      },
      success: function (data) {   // `data` is the return of the  view function
       debugger;
        $("#fruit-name").val(data.order);  // replace the contents of the with the data that came from the server
      }
    });

  });