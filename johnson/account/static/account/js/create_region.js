
$(function () {

    /* Functions */
  
    var loadForm = function () {
      var btn = $(this);
      $.ajax({
        url: btn.attr("data-url"),
        type: 'get',
        dataType: 'json',
        beforeSend: function () {
          $("#modal-book").modal("show");
        },
        success: function (data) {
          $("#modal-book .modal-content").html(data.html_form);
        }
      });
    };
  
    var saveForm = function () {
      var form = $(this);
      $.ajax({
        url: form.attr("action"),
        data: form.serialize(),
        type: form.attr("method"),
        dataType: 'json',
        success: function (data) {
          if (data.form_is_valid) {
              alert("Data created!");
            $("#example tbody").html(data.html_user_list);
            $("#modal-book").modal("hide");
          }
          else {
            $("#modal-book .modal-content").html(data.html_form);
          }
        }
      });
      return false;
    };
  
  
    /* Binding */
  
    // Create book
    $(".region-create").click(loadForm);
    $("#modal-book").on("submit", ".region-create-form", saveForm);
  
    // Update book
    $("#example").on("click", ".region-update", loadForm);
    $("#modal-book").on("submit", ".region-update-form", saveForm);
  
    $("#example").on("click", ".js-delete-region", loadForm);
    $("#modal-book").on("submit", ".js-region-delete-form", saveForm);
  
  });