(function () {
  var oldConsoleLog = console.log;
  var outputDiv = document.querySelector(".console");

  console.log = function (message) {
    if (typeof message == "object") {
      outputDiv.innerHTML +=
        (JSON && JSON.stringify ? JSON.stringify(message) : message) + "<br>";
    } else {
      outputDiv.innerHTML += message + "<br>";
    }
    oldConsoleLog.apply(console, arguments);
  };
})();

console.log("Hola, esto se mostrará en el div.");
console.log(5+5);
