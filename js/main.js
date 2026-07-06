/* Krzysztof Miotk — interakcje i animacje strony */
(function () {
  "use strict";

  /* =========================================================================
     KONFIGURACJA — uzupełnij dwoma linkami i strona w pełni działa.
     ========================================================================= */
  var CONFIG = {
    // 1) Endpoint formularza Formspree (https://formspree.io/f/XXXXXXXX). Pusty = tryb mailto.
    formEndpoint: "",
    // 2) Link do kalendarza (Calendly/Cal.com). Pusty = box zastępczy.
    calendarUrl: "",
    contactEmail: "krzysiek@quale.agency"
  };

  var REDUCE = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ------------------------------------------------------------ Mobilne menu */
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

  /* ------------------------------------------------------------ Filtr artykułów */
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

  /* =========================================================================
     ANIMACJE — rysowane ikony, count-up, marker, glow, ripple, parallax, roller
     ========================================================================= */

  /* --- rysowane liniowo ikony (stroke-draw) --- */
  function strokes(svg) { return svg.querySelectorAll("path, circle, rect, line, polyline"); }
  function prep(svg) {
    strokes(svg).forEach(function (p) {
      try {
        var L = p.getTotalLength();
        p.dataset.len = L;
        p.style.transition = "none";
        p.style.strokeDasharray = L;
        p.style.strokeDashoffset = L;
      } catch (e) {}
    });
  }
  function draw(svg, dur) {
    dur = dur || 900;
    var need = false;
    strokes(svg).forEach(function (p) { if (!p.dataset.len) need = true; });
    if (need) { prep(svg); void svg.getBoundingClientRect(); }
    strokes(svg).forEach(function (p, i) {
      if (!p.dataset.len) return;
      void p.getBoundingClientRect();
      p.style.transition = "stroke-dashoffset " + dur + "ms cubic-bezier(.22,.61,.36,1) " + (i * 110) + "ms";
      p.style.strokeDashoffset = 0;
    });
  }
  function resetSvg(svg) {
    strokes(svg).forEach(function (p) {
      if (!p.dataset.len) { try { p.dataset.len = p.getTotalLength(); } catch (e) { return; } }
      p.style.transition = "none";
      p.style.strokeDashoffset = p.dataset.len;
    });
  }

  /* --- liczniki count-up --- */
  function countUp(el) {
    var target = parseInt(el.getAttribute("data-count"), 10);
    if (!target) return;
    var suffix = el.getAttribute("data-suffix") || "";
    var start = null, dur = 1300;
    function tick(now) {
      if (start === null) start = now;
      var t = Math.min(1, (now - start) / dur);
      var eased = 1 - Math.pow(1 - t, 3);
      el.textContent = Math.round(target * eased) + suffix;
      if (t < 1) requestAnimationFrame(tick);
    }
    requestAnimationFrame(tick);
  }

  /* --- reveal on scroll (+ stagger, + uruchomienie animacji wewnątrz) --- */
  var ICON_SEL = "[data-ico], [data-check], .card .ico svg, .checklist li svg";
  var revealEls = document.querySelectorAll(".reveal");
  function revealInner(root) {
    if (!REDUCE) {
      root.querySelectorAll(ICON_SEL).forEach(function (svg) { draw(svg, 900); });
    }
    root.querySelectorAll("[data-count]").forEach(function (el) { countUp(el); });
  }
  if ("IntersectionObserver" in window && revealEls.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        io.unobserve(e.target);
        var el = e.target;
        var d = parseInt(el.getAttribute("data-delay") || "0", 10);
        if (d) el.style.transitionDelay = d + "ms";
        el.classList.add("in");
        setTimeout(function () { revealInner(el); }, d + 150);
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -8% 0px" });
    revealEls.forEach(function (el) { io.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add("in"); revealInner(el); });
  }

  /* --- ikony/liczniki poza blokami .reveal: własny obserwator --- */
  if ("IntersectionObserver" in window) {
    var io2 = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        io2.unobserve(e.target);
        var el = e.target;
        if (el.hasAttribute("data-count")) countUp(el);
        else if (!REDUCE) { prep(el); draw(el, 900); }
      });
    }, { threshold: 0.3 });
    document.querySelectorAll(ICON_SEL + ", [data-count]").forEach(function (el) {
      if (el.closest(".reveal")) return;               // te obsłuży revealInner
      if (!REDUCE && !el.hasAttribute("data-count")) prep(el);
      io2.observe(el);
    });
  }

  /* --- marker (scaleX in) --- */
  var marks = document.querySelectorAll(".mark");
  if (marks.length && !REDUCE && "IntersectionObserver" in window) {
    marks.forEach(function (m) { m.classList.add("mark-hidden"); });
    var io3 = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        io3.unobserve(e.target);
        e.target.classList.remove("mark-hidden");
        e.target.classList.add("mark-in");
      });
    }, { threshold: 0.6 });
    marks.forEach(function (m) { io3.observe(m); });
  }

  /* --- glow + subtelny lift na kartach (podąża za kursorem) --- */
  if (!REDUCE) {
    document.querySelectorAll(".card").forEach(function (card) {
      if (!card.querySelector(".card-glow")) {
        var g = document.createElement("div");
        g.className = "card-glow";
        card.insertBefore(g, card.firstChild);
      }
      card.addEventListener("mousemove", function (e) {
        var r = card.getBoundingClientRect();
        var px = e.clientX - r.left, py = e.clientY - r.top;
        card.style.transform = "translateY(-4px)";
        card.style.borderColor = "var(--line-strong)";
        card.style.boxShadow = "var(--shadow)";
        var gl = card.querySelector(".card-glow");
        if (gl) {
          gl.style.opacity = "1";
          gl.style.background = "radial-gradient(240px circle at " + px + "px " + py + "px, oklch(57.2% 0.21 280 / .14), transparent 70%)";
        }
      });
      card.addEventListener("mouseenter", function () {
        var svg = card.querySelector("[data-ico], .ico svg");
        if (svg) { resetSvg(svg); draw(svg, 750); }
      });
      card.addEventListener("mouseleave", function () {
        card.style.transform = "";
        card.style.borderColor = "";
        card.style.boxShadow = "";
        var gl = card.querySelector(".card-glow");
        if (gl) gl.style.opacity = "0";
      });
    });
  }

  /* --- ripple na przyciskach --- */
  if (!REDUCE) {
    document.querySelectorAll(".btn").forEach(function (btn) {
      btn.addEventListener("click", function (e) {
        var r = btn.getBoundingClientRect();
        var d = Math.max(r.width, r.height);
        var s = document.createElement("span");
        s.className = "km-ripple";
        s.style.width = s.style.height = d + "px";
        s.style.left = (e.clientX - r.left - d / 2) + "px";
        s.style.top = (e.clientY - r.top - d / 2) + "px";
        s.style.animation = "km-ripple .6s cubic-bezier(.22,.61,.36,1) forwards";
        btn.appendChild(s);
        setTimeout(function () { s.remove(); }, 650);
      });
    });
  }

  /* --- parallax (zdjęcie hero + poświaty CTA) --- */
  var pxEls = Array.prototype.slice.call(document.querySelectorAll("[data-parallax]"));
  if (pxEls.length && !REDUCE) {
    var ticking = false;
    function updatePx() {
      ticking = false;
      var vh = window.innerHeight;
      pxEls.forEach(function (el) {
        var f = parseFloat(el.getAttribute("data-parallax"));
        var r = el.getBoundingClientRect();
        var off = (r.top + r.height / 2 - vh / 2) * f;
        el.style.translate = "0 " + off.toFixed(1) + "px";
      });
    }
    window.addEventListener("scroll", function () {
      if (!ticking) { ticking = true; requestAnimationFrame(updatePx); }
    }, { passive: true });
    updatePx();
  }

  /* --- cylinder z nazwami usług (hero) --- */
  var word = document.querySelector("[data-svc-word]");
  if (word && !REDUCE) {
    var names = ["Badania UX", "Zewnętrzny Dyrektor UX", "Segmentacja klientów", "Audyt UX", "Konsultacje i mentoring", "Wystąpienia i szkolenia"];
    var idx = 0;
    setInterval(function () {
      word.style.transition = "transform .32s cubic-bezier(.55,0,1,.45), opacity .32s cubic-bezier(.55,0,1,.45)";
      word.style.transform = "rotateX(-88deg) translateY(-.45em)";
      word.style.opacity = "0";
      setTimeout(function () {
        idx = (idx + 1) % names.length;
        word.textContent = "„" + names[idx] + "”";
        word.style.transition = "none";
        word.style.transform = "rotateX(88deg) translateY(.45em)";
        void word.offsetWidth;
        word.style.transition = "transform .38s cubic-bezier(0,.55,.45,1), opacity .38s cubic-bezier(0,.55,.45,1)";
        word.style.transform = "rotateX(0deg) translateY(0)";
        word.style.opacity = "1";
      }, 320);
    }, 2800);
  }

  /* ------------------------------------------------------------ Rok w stopce */
  var y = document.querySelector("[data-year]");
  if (y) { y.textContent = new Date().getFullYear(); }

  /* =========================================================================
     FORMULARZE — Formspree (AJAX) lub awaryjnie mailto.
     ========================================================================= */
  function fieldLabel(form, el) {
    if (el.getAttribute("aria-label")) return el.getAttribute("aria-label");
    var lab = el.id && form.querySelector('label[for="' + el.id + '"]');
    return lab ? lab.textContent.replace("*", "").trim() : (el.name || el.placeholder || "Pole");
  }
  function collect(form) {
    var data = {};
    form.querySelectorAll("input, textarea, select").forEach(function (el) {
      if (!el.name || el.type === "submit" || (el.type === "checkbox" && !el.checked)) return;
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
      fetch(CONFIG.formEndpoint, { method: "POST", headers: { "Accept": "application/json" }, body: new FormData(form) })
        .then(function (r) {
          if (r.ok) { showSuccess(form, "Odezwę się najszybciej, jak to możliwe."); }
          else { note(form, "Coś poszło nie tak. Napisz proszę bezpośrednio na " + CONFIG.contactEmail, false); if (btn) { btn.disabled = false; btn.textContent = btn.dataset.label; } }
        })
        .catch(function () { mailtoFallback(form); if (btn) { btn.disabled = false; btn.textContent = btn.dataset.label; } });
    });
  });

  /* =========================================================================
     KALENDARZ rezerwacji — Calendly inline
     ========================================================================= */
  var calBox = document.getElementById("calendar-embed");
  if (calBox) {
    if (CONFIG.calendarUrl) {
      var w = document.createElement("div");
      w.className = "calendly-inline-widget";
      w.setAttribute("data-url", CONFIG.calendarUrl);
      w.style.minWidth = "320px"; w.style.height = "680px";
      calBox.appendChild(w);
      var s = document.createElement("script");
      s.src = "https://assets.calendly.com/assets/external/widget.js"; s.async = true;
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
     Baner zgody na cookies
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
  } catch (e) { /* localStorage niedostępny */ }
})();
