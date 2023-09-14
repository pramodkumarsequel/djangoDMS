
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
    $(".state-create").click(loadForm);
    $("#modal-book").on("submit", ".state-create-form", saveForm);
  
    // Update book
    $("#example").on("click", ".state-update", loadForm);
    $("#modal-book").on("submit", ".state-update-form", saveForm);
  
    $("#example").on("click", ".js-delete-state", loadForm);
    $("#modal-book").on("submit", ".js-state-delete-form", saveForm);
  
  });