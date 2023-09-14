
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
  $(".dbprice-create").click(loadForm);
  $("#modal-book").on("submit", ".dbprice-create-form", saveForm);

  // Update Distributor
  $("#example").on("click", ".dbprice-update", loadForm);
  $("#modal-book").on("submit", ".dbprice-update-form", saveForm);

//Delete Distributor
  $("#example").on("click", ".js-delete-dbprice", loadForm);
  $("#modal-book").on("submit", ".js-dbprice-delete-form", saveForm);

});