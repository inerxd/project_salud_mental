let a = 1;
let inputEmail = document.querySelector("#email");
let errorDiv = document.querySelector('#error');
let Div1 = document.querySelector('#campo1');
let Div2 = document.querySelector('#campo2');
let Div3 = document.querySelector('#campo3');
let Div4 = document.querySelector('#campo4');
let password = document.querySelector('#password')
let inputRepetirPass = document.querySelector('#repetirPassword')
inputEmail.addEventListener('input',validarMsm);
inputEmail.addEventListener('input',camposVacios);
inputEmail.addEventListener('input',camposVacios2);
inputEmail.addEventListener('input',camposVacios3);
inputRepetirPass.addEventListener('input',contraseñaCoincida);



function validarEmail(email){
    const regex =  /^\w+([.-_+]?\w+)*@\w+([.-]?\w+)*(\.\w{2,10})+$/;
    const resultado = regex.test(email);
   return resultado;
}

function mensajeError(){
    let error = document.createElement('p');
    error.textContent = "debe ser correo valido";
    errorDiv.appendChild(error);
}

function validarMsm(e){
    errorDiv.innerHTML = '';
    if(e.target.value !== '' && !validarEmail(e.target.value) ){
        mensajeError()
    }
}

function camposVacios(e){
    Div1.innerHTML = '';
    if(e.target.value === ''){
    let noVacio = document.createElement('p');
    noVacio.textContent = "Este campo no debe ir vacio";
    Div1.appendChild(noVacio);

    }
}

function camposVacios2(e){
    Div2.innerHTML = '';
    if(e.target.value === ''){
    let noVacio2 = document.createElement('p');
    noVacio2.textContent = "Este campo no debe ir vacio";
    Div2.appendChild(noVacio2);

    }
}

function camposVacios3(e){
    Div3.innerHTML = '';
    if(e.target.value === ''){
    let noVacio3 = document.createElement('p');
    noVacio3.textContent = "Este campo no debe ir vacio";
    Div3.appendChild(noVacio3);

    }
}

function contraseñaCoincida() {
    Div4.innerHTML = ''; // Limpia el contenido de Div4 al inicio

    // Verifica si el campo de repetir contraseña está vacío


    // Compara las contraseñas
    if (inputRepetirPass.value !== password.value) {
        // Si no coinciden, muestra el mensaje de error
        let vacio4 = document.createElement('p');
        vacio4.textContent = "Las contraseñas no coinciden"; // Mensaje de error
        Div4.appendChild(vacio4); // Muestra el mensaje de error
    } else {
        // Si coinciden, limpia el mensaje de error
        Div4.innerHTML = ''; // Elimina cualquier mensaje de error
    }
}