
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

  // Create book
  $(".hierarchy1-create").click(loadForm);
  $("#modal-book").on("submit", ".hierarchy1-create-form", saveForm);

  // Update book
  $("#example").on("click", ".hierarchy1-update", loadForm);
  $("#modal-book").on("submit", ".hierarchy1-update-form", saveForm);

  $("#example").on("click", ".js-delete-hierarchy1", loadForm);
  $("#modal-book").on("submit", ".js-hierarchy1-delete-form", saveForm);

});