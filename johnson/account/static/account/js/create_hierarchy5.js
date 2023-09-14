
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

  // Create Hierarchy5
  $(".hierarchy5-create").click(loadForm);
  $("#modal-book").on("submit", ".hierarchy5-create-form", saveForm);

  // Update Hierarchy5
  $("#example").on("click", ".hierarchy5-update", loadForm);
  $("#modal-book").on("submit", ".hierarchy5-update-form", saveForm);
   // Delete Hierarchy5
  $("#example").on("click", ".js-delete-hierarchy5", loadForm);
  $("#modal-book").on("submit", ".js-hierarchy5-delete-form", saveForm);

});