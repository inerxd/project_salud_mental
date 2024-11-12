let why = "";


    // Selecciona el contenedor donde se va a agregar el formulario
    const contenedor = document.querySelector('.conteiner');

    // Función que crea y añade el formulario al contenedor
    function miFuturo() {
        const formulario = document.createElement('form');
        formulario.innerHTML = `<label for="">prueba</label>`;
        contenedor.appendChild(formulario);
       
}