(function () {
  var outputDiv = document.querySelector(".console");

  console.log = function (message) {
    outputDiv.innerHTML +=
      (JSON && JSON.stringify ? JSON.stringify(message) : message) + "<br>";
  };
})();

function executeCode() {
  // Realizar una solicitud al servidor Flask cuando se hace clic en el botón
  fetch('/execute_code')
    .then(response => response.json())
    .then(data => {
      console.log(data.mensaje);
      // Agregar el mensaje al div de la consola
      document.querySelector(".console").innerHTML += data.mensaje + "<br>";
    })
    .catch(error => {
      console.error('Error:', error);
      // Manejar errores y mostrarlos en la consola
      document.querySelector(".console").innerHTML += 'Error: ' + error + "<br>";
    });
}