$(document).ready(function(){
    debugger;
    $("#id_document_type").change(function () {
        debugger;
        var url = $("#warehousewiseitemform").attr("data-fields-url");
        var DocType = $(this).val();
  
        $.ajax({
          url: url,
          data: {
            'fields': DocType
          },
          success: function (data) {
          debugger;
            $("#id_groups").html(data);
          }
        });
  
    });

});