if ("speechSynthesis" in window) {
  const speech = new SpeechSynthesisUtterance();
  let messages;

  fetch('/static/languages/speech.json')
    .then(response => response.json())
    .then(data => {
      messages = data;

      document.addEventListener("languageChange", function (event) {
        const lang = event.detail;
        setSpeechLanguage(lang);
      });

      function setSpeechLanguage(lang) {
        switch (lang) {
          case "en":
            speech.lang = "en-US";
            break;
          case "es":
            speech.lang = "es-ES";
            break;
          case "jp":
            speech.lang = "ja-JP";
            break;
          default:
            speech.lang = "en-US";
            break;
        }
      }

      function speak(text) {
        speech.text = text;
        speechSynthesis.speak(speech);
      }

      document.getElementById("send").addEventListener("click", function () {
        const lang = document.documentElement.lang;
        const Message = messages[lang].send || messages["en"].send;
        speak(Message);
      });

      document.getElementById("execute").addEventListener("click", function () {
        const lang = document.documentElement.lang;
        const executingMessage = messages[lang].execute || messages["en"].execute;
        speak(executingMessage);
      });

      document.getElementById("validate").addEventListener("click", function () {
        const lang = document.documentElement.lang;
        const executingMessage = messages[lang].validate || messages["en"].validate;
        speak(executingMessage);
      });

    })  
    .catch(error => console.error('Error loading messages:', error));
} else {
  console.log("La síntesis de voz no es compatible con este navegador.");
}