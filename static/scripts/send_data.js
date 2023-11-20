document.getElementById('execute').addEventListener('click', function() {
    var texto = document.getElementById('Texto').value;

    fetch('/guardar_texto', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ texto: texto }),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Respuesta del servidor:', data);
    })
    .catch(error => {
        console.error('Error al enviar datos al servidor:', error);
    });
});
