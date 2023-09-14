
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

  // Create Distributor
  $(".item-create").click(loadForm);
  $("#modal-book").on("submit", ".item-create-form", saveForm);

  // Update Distributor
  $("#example").on("click", ".item-update", loadForm);
  $("#modal-book").on("submit", ".item-update-form", saveForm);

//Delete Distributor
  $("#example").on("click", ".js-delete-item", loadForm);
  $("#modal-book").on("submit", ".js-item-delete-form", saveForm);

});