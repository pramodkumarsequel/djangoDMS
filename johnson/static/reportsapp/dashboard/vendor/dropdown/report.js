$(document).ready(function(){
    $("#id_Document_Type").change(function () {
        debugger;
        var url = $("#personForm").attr("data-cities-url");
        var DocType = $(this).val();
  
        $.ajax({
          url: url,
          data: {
            'fields': DocType
          },
          success: function (data) {

            $("#id_fields").html(data);
          }
        });
  
    });

});

$(document).ready(function(){
  $("#id_Document_Type").change(function () {
      var url = $("#personForm").attr("data-load-date-fields");
      var DocType = $(this).val();

      $.ajax({
        url: url,
        data: {
          'fields': DocType
        },
        success: function (data) {
        debugger;
          $("#id_Date_Type").html(data);
        }
      });

  });

});


// $(document).ready(function() {
//   $('#example4').DataTable( {
//     "searching": false,
//     "info": false,
//     "pageLength": 12,
//     "paging": false,
//     'scrollX': 400,
//       dom: 'Bfrtip',
//       buttons: [

//                     {
//                       "extend": 'excelHtml5',
//                       "filename": "Document Reports",
//                       "text": '<i class="fa fa-file-excel-o" style="color: green;">Export to Excel</i>',
//                       "titleAttr": 'ExportExcel',                               
//                       "action": newExportAction
//                    },
//       ]
      
//   });
//   var newExportAction = function (e, dt, button, config) {
//     var self = this;
//     var oldStart = dt.settings()[0]._iDisplayStart;

//     dt.one('preXhr', function (e, s, data) {
//         // Just this once, load all data from the server...
//         data.start = 0;
//         data.length = 2147483647;

//         dt.one('preDraw', function (e, settings) {
//             // Call the original action function 
//             oldExportAction(self, e, dt, button, config);

//             dt.one('preXhr', function (e, s, data) {
//                 // DataTables thinks the first item displayed is index 0, but we're not drawing that.
//                 // Set the property to what it was before exporting.
//                 settings._iDisplayStart = oldStart;
//                 data.start = oldStart;
//             });

//             // Reload the grid with the original page. Otherwise, API functions like table.cell(this) don't work properly.
//             setTimeout(dt.ajax.reload, 0);

//             // Prevent rendering of the full data to the DOM
//             return false;
//         });
//     });

//     // Requery the server with the new one-time export settings
//     dt.ajax.reload();
// };
// } );