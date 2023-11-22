document.addEventListener("DOMContentLoaded", function () {
  let currentLanguage = "en";

  function changeLanguage(lang) {
    currentLanguage = lang;
    fetch("/static/languages/" + lang + ".json")
      .then((response) => response.json())
      .then((data) => {
        document.title = data.title;
        document.querySelector("#languages a").textContent = data.languages;
        document.querySelector("#interpreter").textContent = data.interpreter;
        document.querySelector("#web").textContent = data.web;
        document.querySelector("#execute").textContent = data.execute;
        document.querySelector("#validate").textContent = data.validate;
        document.querySelector("#send").textContent = data.send;

        const languageOptions = data["languages-option"];
        document.querySelectorAll(".language-list a").forEach((link) => {
          const newLang = link.getAttribute("data-lang");
          link.textContent = languageOptions[newLang];
        });

        const languageChangeEvent = new CustomEvent("languageChange", {
          detail: lang,
        });
        document.dispatchEvent(languageChangeEvent);
        document.documentElement.lang = lang;
      });
  }

  document.querySelectorAll(".language-list a").forEach((link) => {
    link.addEventListener("click", function (event) {
      event.preventDefault();
      const lang = this.getAttribute("data-lang");
      changeLanguage(lang);
    });
  });
});