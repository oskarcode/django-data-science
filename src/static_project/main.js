$(document).ready(function(){
          $('.ui.dropdown')
          .dropdown()
          
          $('.ui.message .close')
          .on('click', function() {
          $(this)
          .closest('.ui.message')
          .transition('fade')
          ;
          })
          ;

          $('#model-btn').click(function() {
                    $('.ui.modal')
                    .modal('show')
           ;
          })
;
})




