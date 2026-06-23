/* Krzysztof Miotk — interakcje strony */
(function () {
  "use strict";

  /* --- Mobilne menu --- */
  var toggle = document.querySelector(".nav-toggle");
  if (toggle) {
    toggle.addEventListener("click", function () {
      var open = document.body.classList.toggle("nav-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    document.querySelectorAll(".nav-links a").forEach(function (a) {
      a.addEventListener("click", function () {
        document.body.classList.remove("nav-open");
        toggle.setAttribute("aria-expanded", "false");
      });
    });
  }

  /* --- Filtr artykułów (Insights) --- */
  var filters = document.querySelectorAll(".filter");
  var articles = document.querySelectorAll("[data-cat]");
  if (filters.length) {
    filters.forEach(function (btn) {
      btn.addEventListener("click", function () {
        filters.forEach(function (b) { b.classList.remove("is-active"); });
        btn.classList.add("is-active");
        var cat = btn.getAttribute("data-filter");
        articles.forEach(function (el) {
          var match = cat === "all" || el.getAttribute("data-cat") === cat;
          el.style.display = match ? "" : "none";
        });
      });
    });
  }

  /* --- Reveal on scroll --- */
  var revealEls = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && revealEls.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); }
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -8% 0px" });
    revealEls.forEach(function (el) { io.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add("in"); });
  }

  /* --- Rok w stopce --- */
  var y = document.querySelector("[data-year]");
  if (y) { y.textContent = new Date().getFullYear(); }

  /* --- Demo formularzy (bez backendu) --- */
  document.querySelectorAll("form[data-demo]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var note = form.querySelector("[data-note]");
      if (note) {
        note.textContent = "Dziękuję! To wersja demonstracyjna — formularz nie wysyła jeszcze danych.";
        note.style.color = "var(--brand-deep)";
      }
      form.reset();
    });
  });
})();
