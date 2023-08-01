function buscador(){
    /*if(document.getElementById('Comuna').value==0)
    {
        return false;
    }*/
    var contrato = document.getElementById('id_contrato_vigente');
    var contrato_vigente= false;
    if (contrato.checked==true){
        contrato_vigente=true;
    }
    /*window.location="/propiedades/buscador?buscar="+document.getElementById('Comuna').value+"-"+document.getElementById('precio').value+"-"+document.getElementById('rentabilidad').value+"-"+document.getElementById('plusvalia').value+"-"+document.getElementById('bancaria').value;*/
    window.location="/propiedades/buscador?buscar="+document.getElementById('Comuna').value+'&&contrato='+contrato_vigente+'&&rentabilidad=false&&plusvalia=false';
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
    jCustomConfirm(pregunta, 'Tienda', 'Aceptar', 'Cancelar', function(r) {
        if (r) {
            window.location = ruta;
        }
    });
}


function alertAlert(mensaje) {
    jAlert(mensaje);
}


function sendLogin()
{
   var form=document.Formulario_Login;
   console.log(form.correo)
   if(form.correo.value==0)
   {
       alertAlert('El campo E-Mail es obligatorio');
       form.correo.value='';
       return false;
   }
   if(validaCorreo(form.correo.value)==false)
   {
       alertAlert('El E-Mail no es válido');
       form.correo.value='';
       return false;
   }
   if(form.password.value==0)
   {
       alertAlert('El campo Contraseña es obligatorio');
       form.password.value='';
       return false;
   }
   form.submit();
}


function sendRegistro()
{
   form=document.form_registro;
   if(form.nombre.value==0)
   {
       alertAlert('El campo Nombre es obligatorio');
       form.nombre.value='';
       return false;
   }
  
       if(form.apellido.value==0)
       {
           alertAlert('El campo Apellido es obligatorio');
           form.apellido.value='';
           return false;
       }
   
   
   if(form.correo.value==0)
   {
       alertAlert('El campo E-Mail es obligatorio');
       form.correo.value='';
       return false;
   }
   if(validaCorreo(form.correo.value)==false)
   {
       alertAlert('El E-Mail no es válido');
       form.correo.value='';
       return false;
   }
   if(form.password.value==0)
   {
       alertAlert('El campo Contraseña es obligatorio');
       form.password.value='';
       return false;
   }
   if(form.password2.value==0)
   {
       alertAlert('El campo Repetir Contraseña es obligatorio');
       form.password2.value='';
       return false;
   }
   if(form.password.value!=form.password2.value)
   {
       alertAlert('Las contraseñas ingresadas no coinciden');
       form.password.value='';
       form.password2.value='';
       return false;
   }
   form.submit();
}
function sendRestore()
{
   var form=document.form_restore;
   
   if(form.password1.value==0)
   {
       alertAlert('El campo Contraseña es obligatorio');
       form.password1.value='';
       return false;
   }
   if(form.password2.value==0)
   {
       alertAlert('El campo Repetir Contraseña es obligatorio');
       form.password2.value='';
       return false;
   }
   if(form.password1.value!=form.password2.value)
   {
       alertAlert('Las contraseñas ingresadas no coinciden');
       form.password1.value='';
       form.password2.value='';
       return false;
   }
   form.submit();
}

function sendReset()
{
   var form=document.form_reset;
   
   
   if(form.correo.value==0)
   {
       alertAlert('El campo E-Mail es obligatorio');
       form.correo.value='';
       return false;
   }
  
   form.submit();
}

function salir(ruta)
{
   jCustomConfirm('¿Realmente desea cerrar sesión?', 'Tienda', 'Aceptar', 'Cancelar', function(r) {
        if (r) {
            window.location = ruta;
        }
    });
}

