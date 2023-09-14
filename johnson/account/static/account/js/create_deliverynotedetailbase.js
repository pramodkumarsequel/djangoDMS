
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
  $(".deliverynotedetail-create").click(loadForm);
  $("#modal-book").on("submit", ".deliverynotedetail-create-form", saveForm);
  debugger;

  // Update book
  $("#example").on("click", ".deliverynotedetail-update", loadForm);
  $("#modal-book").on("submit", ".deliverynotedetail-update-form", saveForm);

  $("#example").on("click", ".delete-deliverynotedetail", loadForm);
  $("#modal-book").on("submit", ".js-deliverynotedetail-delete-form", saveForm);

});