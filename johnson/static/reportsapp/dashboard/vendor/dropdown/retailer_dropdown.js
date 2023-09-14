$("#id_state").change(function () {
    var url = $("#retailForm").attr("data-cities-url");  // get the url of the `load_cities` view
    var stateId = $(this).val();  // get the selected country ID from the HTML input

    $.ajax({                       // initialize an AJAX request
      url: url,                    // set the url of the request (= localhost:8000/hr/ajax/load-cities/)
      data: {
        'State': stateId       // add the country id to the GET parameters
      },
      success: function (data) {   // `data` is the return of the `load_cities` view function
        $("#id_city").html(data);  // replace the contents of the city input with the data that came from the server
      }
    });

  });
  $("#id_zone").change(function () {
    var url = $("#retailForm").attr("data-region-url"); 
    var stateId = $(this).val(); 

    $.ajax({                       // initialize an AJAX request
      url: url,                   // set the url of the request (= localhost:8000/hr/ajax/load-cities/)
      data: {
        'zone': stateId       // add the country id to the GET parameters
      },
      success: function (data) {   // `data` is the return of the `load_cities` view function
        $("#id_region").html(data);
        $("#id_state").html(data);
      }
    });    
  });

  $("#id_zone").change(function () {
    debugger;
    var url = $("#retailForm").attr("data-state-url"); 
    var stateId = $(this).val(); 

    $.ajax({                       // initialize an AJAX request
      url: url,                   // set the url of the request (= localhost:8000/hr/ajax/load-cities/)
      data: {
        'zone': stateId       // add the country id to the GET parameters
      },
      success: function (data) {   // `data` is the return of the `load_cities` view function
        $("#id_state").html(data);
      }
    });    
  });