if ("speechSynthesis" in window) {
    const speech = new SpeechSynthesisUtterance();

    document.addEventListener('languageChange', function (event) {
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

    // prueba
    document.getElementById("execute").addEventListener("click", function () {
        speak("Reproduciendo mensaje al hacer clic.");
    });
} else {
    console.log("La síntesis de voz no es compatible con este navegador.");
}