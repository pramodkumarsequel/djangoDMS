
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

  // Create Details of Sales
  $(".purchasereturndetail-create").click(loadForm);
  $("#modal-book").on("submit", ".purchasereturndetail-create-form", saveForm);

  // Update Details Of Sales
  $("#example").on("click", ".purchasereturndetail-update", loadForm);
  $("#modal-book").on("submit", ".purchasereturndetail-update-form", saveForm);

    // Delete Details Of Sales
  $("#example").on("click", ".js-delete-purchasereturndetail", loadForm);
  $("#modal-book").on("submit", ".js-purchasereturndetail-delete-form", saveForm);

});