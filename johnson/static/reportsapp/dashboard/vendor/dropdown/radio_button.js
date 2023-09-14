
$(document).ready(function(){




    jQuery('.clear-region-filter').click(function(){
        window.location.href = "/city-list/";
    });
    




$('.change-data').on('click', function (event) {
 
    if(id.length!=0){

        Swal.fire({
            title: 'Are you sure you want to delete this record?',
            text: "You won't be able to revert this!",
            type: "warning",
            icon: 'question',
            showCancelButton: true,
            confirmButtonText: "Yes, delete it !!",
            confirmButtonText: 'Delete',
            confirmButtonColor: "#DD6B55"
            
        }).then((result) => {
            if (result.value) {



                $.ajax({
                    url:"/dashboard/delete-multiple-user/",
                    method:"POST",
                    dataType:'json',
                    data:{
                        id,
                        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                    },
                    success:function(res){
                        if(res.warning){
                            document.getElementById("message").innerHTML += '<div class="alert alert-warning alert-dismissible alert-alt solid fade show">\
                                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="btn-close">\
                                </button>'+res.warning+'</div>';
    
                        }
                        if(res.success){
    
                            for(var i=0; i < id.length; i++){
                                if(id[i]!=''){
                                    $('tr#'+id[i]+'').css('background-color','#ccc');
                                    // $('tr#'+id[i]+'').fadeOut('slow');
                                     $('tr#'+id[i]+'').remove(); 
                                }
    
                            }
                            document.getElementById("message").innerHTML += '<div class="alert alert-success alert-dismissible alert-alt solid fade show">\
                                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="btn-close">\
                                </button>'+res.success+'</div>';
    
                        }
                        
                    }
                })


               
            } else if (result.dismiss === Swal.DismissReason.cancel) {
                event.preventDefault();
            }
        });

    
        
    }else{
        Swal.fire({
            type: 'info',
            title: 'Oops...',
            text: 'Please Select Items To Delete',
            confirmButtonColor:"var(--primary)"
        });
    }


});

$(function() {
    $('input[name="Field_selection"]').on('click', function() {


        if ($(this).val() == '1') {
            $('#div_id_prfx').hide();
            $('#div_id_seqnum').hide();
        }
        else {
            
            $('#div_id_prfx').show();
            $('#div_id_seqnum').show();
            $('#div_id_sufx').show();
        }

    });
})


$(document).ready(function () {
    if ($('#id_Field_selection_0').val() == "0"){
        $('.dom1').hide();
    }

    if ($('#id_Field_selection_0').val() == "1"){
        $('.dom').hide()
    }

    $('input[name="Field_selection"]').on('click', function() {
        if ($(this).val() == '1') {
            $('.dom1').show();
        }

        else {
            $('.dom1').hide();
        }

    });
});





});