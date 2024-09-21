/* mi solucion */

function mostrarOcultarContrasena(e) {
    e.preventDefault();
   
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

// Escucha el evento 'input' en el campo 'repetirPassword'
document.getElementById('repetirPassword').addEventListener('input',() => {
    coincidenciaContraseña();
});

function coincidenciaContraseña() {
    let password = document.getElementById('password').value;
    let repetirPassword = document.getElementById('repetirPassword').value;
    let midiv = document.getElementById('miDiv'); // Seleccionando el div para el mensaje

    // Limpia el mensaje anterior antes de añadir uno nuevo
    midiv.innerHTML = '';

    if (repetirPassword !== password) {
        let mensaje = document.createElement('p');
        mensaje.textContent = "Las contraseñas no coinciden";
        midiv.appendChild(mensaje); // Añadir el mensaje al div
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