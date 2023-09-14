
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

  // Create Hierachy1
  $(".hierarchy-create").click(loadForm);
  $("#modal-book").on("submit", ".hierarchy-create-form", saveForm);

  // Update Hierarchy1
  $("#example").on("click", ".hierarchy-update", loadForm);
  $("#modal-book").on("submit", ".hierarchy-update-form", saveForm);

//Delete Hierarchy1
  $("#example").on("click", ".js-delete-hierarchy", loadForm);
  $("#modal-book").on("submit", ".js-hierarchy-delete-form", saveForm);

});