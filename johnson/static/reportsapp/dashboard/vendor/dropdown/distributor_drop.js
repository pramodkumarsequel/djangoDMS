$("#id_State").change(function () {
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
$("#id_zones").change(function () {
    var url = $("#retailForm").attr("data-region-url");  // get the url of the `load_cities` view
    var stateId = $(this).val();  // get the selected country ID from the HTML input

    $.ajax({                       // initialize an AJAX request
      url: url,                    // set the url of the request (= localhost:8000/hr/ajax/load-cities/)
      data: {
        'zone': stateId       // add the country id to the GET parameters
      },
      success: function (data) {   // `data` is the return of the `load_cities` view function
        $("#id_region").html(data); 
      }
    });

});
$("#id_zones").change(function () {
  var url = $("#retailForm").attr("data-state-url"); 
  var stateId = $(this).val(); 

  $.ajax({                       // initialize an AJAX request
    url: url,                   // set the url of the request (= localhost:8000/hr/ajax/load-cities/)
    data: {
      'zone': stateId       // add the country id to the GET parameters
    },
    success: function (data) {   // `data` is the return of the `load_cities` view function
      $("#id_State").html(data);
    }
  });    
});


$(document).ready(function() {
  $('#excel_file_form').submit(function(event) {
    event.preventDefault();
    var form = $(this);
    var formData = new FormData(form[0]);
    
    $.ajax({
      url: "/export/distributor/",
      type: form.attr('method'),
      data: formData,
      processData: false,
      contentType: false,
      success: function(response) {
        if (response.status === 'success') {
          alert('Data imported successfully.');
          window.location.href="/distributor-list/"
        } else {
          alert(response.message);
          window.location.href="/distributor-list/"
        }
      },
      error: function(xhr, errmsg, err) {
        console.log(xhr.status + ": " + xhr.responseText);
        alert('Error occurred during import.');
        window.location.href="/distributor-list/"
      }
    });
  });
});