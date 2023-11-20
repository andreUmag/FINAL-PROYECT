(function () {
  var outputDiv = document.querySelector(".console");

  console.log = function (message) {
    outputDiv.innerHTML +=
      (JSON && JSON.stringify ? JSON.stringify(message) : message) + "<br>";
  };
})();
