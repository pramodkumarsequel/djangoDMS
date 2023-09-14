
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

  // Create Role
  $(".role-create").click(loadForm);
  $("#modal-book").on("submit", ".role-create-form", saveForm);

  // Update Role
  $("#example").on("click", ".role-update", loadForm);
  $("#modal-book").on("submit", ".role-update-form", saveForm);

  $("#example").on("click", ".js-delete-book", loadForm);
  $("#modal-book").on("submit", ".js-role-delete-form", saveForm);

});