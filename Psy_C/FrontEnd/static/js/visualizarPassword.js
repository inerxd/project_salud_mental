/* mi solucion */

function mostrarOcultarContrasena() {

   
    let contrasenaInput = document.getElementById("password");
    let iconoMostrarOcultar = document.getElementById("iconoMostrarOcultar");
    
    
    if (contrasenaInput.type === "password" ) {
      
        contrasenaInput.type = "text";
   
        iconoMostrarOcultar.innerHTML = '<i class="fas fa-eye-slash"></i>';
    
    } else {
   
        contrasenaInput.type = "password";

        iconoMostrarOcultar.innerHTML = '<i class="fas fa-eye"></i>';
     
    }
}

function mostrarOcultarContrasena2(e) {
    e.preventDefault();
   
    let iconoMostrarOcultar2 = document.getElementById("iconoMostrarOcultar2");
    let repetirPassword = document.getElementById("repetirPassword")

    if (repetirPassword.type === "password") {
      
        repetirPassword.type = "text";
        iconoMostrarOcultar2.innerHTML = '<i class="fas fa-eye-slash"></i>';
    } else {
   
        repetirPassword.type = "password";
        iconoMostrarOcultar2.innerHTML = '<i class="fas fa-eye"></i>';
    }
}



/* otra solucion
function mostrarOcultarContrasena(e, inputId, iconId) {
    e.preventDefault();
   
    let contrasenaInput = document.getElementById(inputId);
    let iconoMostrarOcultar = document.getElementById(iconId);

    if (contrasenaInput.type === "password") {
        contrasenaInput.type = "text";
        iconoMostrarOcultar.innerHTML = '<i class="fas fa-eye-slash"></i>';
    } else {
        contrasenaInput.type = "password";
        iconoMostrarOcultar.innerHTML = '<i class="fas fa-eye"></i>';
    }
}*/