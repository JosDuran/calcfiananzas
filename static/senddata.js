function enviardata(e) {    
        var exptoeval = $('#exptextid').val();      
          // ajax the JSON to the server
      $.ajax({
          type: 'POST',
          contentType: "application/json; charset=utf-8",
          url: '/replaceandeval',       
          data: JSON.stringify({'expr':exptoeval}),
          dataType: 'json',        
          success: function (response) {       
              $('#exptextid').val(response.resnf)              
           }          
      });
             
      // stop link reloading the page
      event.preventDefault();
      var txt = $('#historybox');
      txt.val(  txt.val() +'\n' + exptoeval );      
      }
  
  window.onload = function(){
  var button = document.getElementById('boton');  
  button.onclick = enviardata;

  }