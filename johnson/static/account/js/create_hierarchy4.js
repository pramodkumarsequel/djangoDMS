
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

  // Create Hierarchy4
  $(".hierarchy4-create").click(loadForm);
  $("#modal-book").on("submit", ".hierarchy4-create-form", saveForm);

  // Update Hierarchy4
  $("#example").on("click", ".hierarchy4-update", loadForm);
  $("#modal-book").on("submit", ".hierarchy4-update-form", saveForm);
   // Delete Hierarchy4
  $("#example").on("click", ".js-delete-hierarchy4", loadForm);
  $("#modal-book").on("submit", ".js-hierarchy4-delete-form", saveForm);

});