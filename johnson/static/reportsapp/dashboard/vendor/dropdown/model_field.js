 $("#id_documentType").change(function () {
      debugger;
      var url = $("#mfield").attr("data-modelfield-url");
      var DocType = $(this).val();
          console.log(DocType)

      $.ajax({
        url: url,
        data: {
          'fields': DocType
        },
        success: function (data) {
          $("#id_fields").html(data);
        }
      });

});

$("#id_fields").change(function () {
    debugger;
    var url = $("#mfield").attr("data-field-url");
    var DocType = $(this).val();
        console.log(DocType)

    $.ajax({
      url: url,
      data: {
        'fields': DocType
      },
      success: function (data) {
        $("#id_field").html(data);
      }
    });

});

