let inputEmail = document.querySelector("#email");
let errorDiv = document.querySelector('#error')
inputEmail.addEventListener('input',validarMsm);


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