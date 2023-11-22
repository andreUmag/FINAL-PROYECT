// (function () {
//   var outputDiv = document.querySelector(".console");

//   console.log = function (message) {
//     outputDiv.innerHTML +=
//       (JSON && JSON.stringify ? JSON.stringify(message) : message) + "<br>";
//   };
// })();

function executeCode() {
  fetch('/execute_code')
    .then(response => response.json())
    .then(data => {
      console.log(data.mensaje);
      document.querySelector(".console").innerHTML += data.mensaje + "<br>";
    })
    .catch(error => {
      console.error('Error:', error);
      document.querySelector(".console").innerHTML += 'Error: ' + error + "<br>";
    });
}

function validateCode() {
  fetch('/validate_code')
    .then(response => response.json())
    .then(data => {
      console.log(data.mensaje);
      document.querySelector(".console").innerHTML += data.mensaje + "<br>";
    })
    .catch(error => {
      console.error('Error:', error);
      document.querySelector(".console").innerHTML += 'Error: ' + error + "<br>";
    });
}