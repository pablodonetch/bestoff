function buscador(){
    if(document.getElementById('Comuna').value==0)
    {
        return false;
    }
    window.location="/propiedades/buscador?buscar="+document.getElementById('Comuna').value+"-"+document.getElementById('precio').value+"-"+document.getElementById('rentabilidad').value+"-"+document.getElementById('plusvalia').value+"-"+document.getElementById('bancaria').value;
}

function soloNumeros(evt) {
    key = (document.all) ? evt.keyCode : evt.which;
    //alert(key);
    if (key == 17) return false;
    /* digitos,del, sup,tab,arrows*/
    return ((key >= 48 && key <= 57) || key == 8 || key == 127 || key == 9 || key == 0);
}

function validaCorreo(valor) {
    if (/^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i.test(valor)){
     return true;
    } else {
     return false;
    }
  }
  function carga_ajax_get(ruta, valor1, div) {
       $.get(ruta, { valor1: valor1 }, function(resp) {
           $("#" + div + "").html(resp);
       });
       return false;
  
   }
   function confirmaAlert(pregunta, ruta) {
       jCustomConfirm(pregunta, 'Tamila', 'Aceptar', 'Cancelar', function(r) {
           if (r) {
               window.location = ruta;
           }
       });
   }
  
   function alertAlert(mensaje) {
       jAlert(mensaje);
   }