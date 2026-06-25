/* Krzysztof Miotk — interakcje strony */
(function () {
  "use strict";

  /* =========================================================================
     KONFIGURACJA — uzupełnij dwoma linkami i strona w pełni działa.
     ========================================================================= */
  var CONFIG = {
    // 1) Endpoint formularza Formspree (https://formspree.io/f/XXXXXXXX).
    //    Pozostaw pusty ("") aby używać awaryjnego trybu e-mail (mailto:).
    formEndpoint: "",
    // 2) Link do kalendarza rezerwacji (Calendly lub Cal.com),
    //    np. "https://calendly.com/krzysiek-miotk/30min". Pusty = box zastępczy.
    calendarUrl: "",
    contactEmail: "krzysiek@quale.agency"
  };

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

  /* --- Filtr artykułów (jeśli obecny) --- */
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

  /* =========================================================================
     FORMULARZE — Formspree (AJAX) lub awaryjnie mailto. (P1.1)
     ========================================================================= */
  function fieldLabel(form, el) {
    if (el.getAttribute("aria-label")) return el.getAttribute("aria-label");
    var lab = el.id && form.querySelector('label[for="' + el.id + '"]');
    return lab ? lab.textContent.replace("*", "").trim() : (el.name || el.placeholder || "Pole");
  }

  function collect(form) {
    var data = {};
    form.querySelectorAll("input, textarea, select").forEach(function (el) {
      if (!el.name || el.type === "submit" || el.type === "checkbox" && !el.checked) return;
      data[fieldLabel(form, el)] = el.value;
    });
    return data;
  }

  function showSuccess(form, msg) {
    var panel = document.createElement("div");
    panel.className = "form-success";
    panel.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6L9 17l-5-5"/></svg><div><strong>Dziękuję!</strong><br>' + msg + "</div>";
    form.parentNode.replaceChild(panel, form);
  }

  function note(form, msg, ok) {
    var n = form.querySelector("[data-note]");
    if (n) { n.textContent = msg; n.style.color = ok ? "var(--brand-deep)" : "#b00"; }
  }

  function mailtoFallback(form) {
    var data = collect(form);
    var subj = form.getAttribute("data-subject") || "Wiadomość ze strony krzysztofmiotk.pl";
    var body = Object.keys(data).map(function (k) { return k + ": " + data[k]; }).join("\n");
    window.location.href = "mailto:" + CONFIG.contactEmail +
      "?subject=" + encodeURIComponent(subj) + "&body=" + encodeURIComponent(body);
    note(form, "Otworzyłem Twój program pocztowy z gotową wiadomością — wyślij ją, aby do mnie dotarła.", true);
  }

  document.querySelectorAll("form[data-form]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!form.checkValidity()) { form.reportValidity(); return; }

      if (!CONFIG.formEndpoint) { mailtoFallback(form); return; }

      var btn = form.querySelector('[type="submit"]');
      if (btn) { btn.disabled = true; btn.dataset.label = btn.textContent; btn.textContent = "Wysyłam…"; }

      fetch(CONFIG.formEndpoint, {
        method: "POST",
        headers: { "Accept": "application/json" },
        body: new FormData(form)
      }).then(function (r) {
        if (r.ok) {
          showSuccess(form, "Odezwę się najszybciej, jak to możliwe.");
        } else {
          note(form, "Coś poszło nie tak. Napisz proszę bezpośrednio na " + CONFIG.contactEmail, false);
          if (btn) { btn.disabled = false; btn.textContent = btn.dataset.label; }
        }
      }).catch(function () {
        mailtoFallback(form);
        if (btn) { btn.disabled = false; btn.textContent = btn.dataset.label; }
      });
    });
  });

  /* =========================================================================
     KALENDARZ rezerwacji — Calendly inline (P1.2)
     ========================================================================= */
  var calBox = document.getElementById("calendar-embed");
  if (calBox) {
    if (CONFIG.calendarUrl) {
      var w = document.createElement("div");
      w.className = "calendly-inline-widget";
      w.setAttribute("data-url", CONFIG.calendarUrl);
      w.style.minWidth = "320px";
      w.style.height = "680px";
      calBox.appendChild(w);
      var s = document.createElement("script");
      s.src = "https://assets.calendly.com/assets/external/widget.js";
      s.async = true;
      document.body.appendChild(s);
    } else {
      calBox.innerHTML =
        '<div class="cal-fallback">' +
        '<p class="eyebrow" style="justify-content:center">Kalendarz rezerwacji</p>' +
        '<p>Tu pojawi się widżet rezerwacji terminu. Wklej swój link Calendly lub Cal.com ' +
        'w pliku <code>js/main.js</code> (<code>CONFIG.calendarUrl</code>).</p>' +
        '<a href="#kontakt" class="btn btn--primary">Napisz do mnie zamiast tego ' +
        '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>' +
        "</div>";
    }
  }

  /* =========================================================================
     Baner zgody na cookies (P1.3)
     ========================================================================= */
  try {
    if (!localStorage.getItem("km-cookie-consent")) {
      var bar = document.createElement("div");
      bar.className = "cookie-banner";
      bar.setAttribute("role", "dialog");
      bar.setAttribute("aria-label", "Informacja o plikach cookies");
      bar.innerHTML =
        '<p>Ta strona używa niezbędnych plików cookies, aby działać poprawnie. ' +
        'Korzystając z niej, akceptujesz <a href="polityka-prywatnosci.html">politykę prywatności</a>.</p>' +
        '<div class="cookie-actions">' +
        '<a href="polityka-prywatnosci.html" class="btn btn--ghost">Dowiedz się więcej</a>' +
        '<button type="button" class="btn btn--primary" data-accept>Akceptuję</button>' +
        "</div>";
      document.body.appendChild(bar);
      bar.querySelector("[data-accept]").addEventListener("click", function () {
        try { localStorage.setItem("km-cookie-consent", "1"); } catch (e) {}
        bar.remove();
      });
    }
  } catch (e) { /* localStorage niedostępny — pomijamy baner */ }
})();
