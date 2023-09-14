$("#id_zone").change(function () {
  debugger;
  var url = $("#retailForm").attr("data-cities-url");  // get the url of the `load_cities` view
  var zoneid = $(this).val();  // get the selected country ID from the HTML input

  $.ajax({                       // initialize an AJAX request
    url: url,                    // set the url of the request (= localhost:8000/hr/ajax/load-cities/)
    data: {
      'Zone': zoneid     // add the country id to the GET parameters
    },
    success: function (data) {   // `data` is the return of the `load_cities` view function
      $("#id_Region").html(data);  // replace the contents of the city input with the data that came from the server
    }
  });

});
$("#id_Region").change(function () {
  debugger;
  var url = $("#retailForm").attr("data-cities-url");  // get the url of the `load_cities` view
  var regionid = $(this).val();  // get the selected country ID from the HTML input

  $.ajax({                       // initialize an AJAX request
    url: url,                    // set the url of the request (= localhost:8000/hr/ajax/load-cities/)
    data: {
      'Region': regionid       // add the country id to the GET parameters
    },
    success: function (data) {   // `data` is the return of the `load_cities` view function
      $("#id_State").html(data);  // replace the contents of the city input with the data that came from the server
    }
  });

});
$("#id_State").change(function () {
        debugger;
        var url = $("#retailForm").attr("data-cities-url");  // get the url of the `load_cities` view
        var stateId = $(this).val();  // get the selected country ID from the HTML input
    
        $.ajax({                       // initialize an AJAX request
          url: url,                    // set the url of the request (= localhost:8000/hr/ajax/load-cities/)
          data: {
            'State': stateId       // add the country id to the GET parameters
          },
          success: function (data) {   // `data` is the return of the `load_cities` view function
            $("#id_City").html(data);  // replace the contents of the city input with the data that came from the server
          }
        });
    
});
 