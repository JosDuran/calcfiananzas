function enviardata(e) {
    
    
        var exptoeval = $('.w3-input').val();
      
          // ajax the JSON to the server
      $.ajax({
          type: 'POST',
          contentType: "application/json; charset=utf-8",
          url: '/replaceandeval',       
          data: JSON.stringify({'expr':exptoeval}),
          dataType: 'json',        
          success: function (response) {       
              $('.w3-input').val(response.resnf)              
           }
          
      });
      
      
      // stop link reloading the page
      event.preventDefault();
     
  
      }
  
  window.onload = function(){
  var button = document.getElementById('boton');  
  button.onclick = enviardata;

  }