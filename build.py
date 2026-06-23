#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generator spójnych podstron krzysztofmiotk.pl (branding QUALE)."""
import os

BASE = os.path.dirname(os.path.abspath(__file__))

ARROW = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" '
         'stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>')
CHECK = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
         'stroke-linecap="round" stroke-linejoin="round"><path d="M20 6L9 17l-5-5"/></svg>')

NAV = [("uslugi.html", "Usługi"), ("insights.html", "Insights"),
       ("o-mnie.html", "O mnie"), ("kontakt.html", "Kontakt")]


def head(title, desc):
    return f'''<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{title}</title>
<meta name="description" content="{desc}" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@400;500;600;700;800;900&family=Inter:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="css/styles.css" />
</head>
<body>'''


def header(active):
    links = ""
    for href, label in NAV:
        cur = ' aria-current="page"' if href == active else ""
        links += f'      <a href="{href}"{cur}>{label}</a>\n'
    return f'''
<header class="site-header">
  <div class="wrap nav">
    <a href="index.html" class="brand" aria-label="Krzysztof Miotk — strona główna">
      <img src="assets/logo.svg" alt="Krzysztof Miotk" class="brand-logo" width="280" height="42" />
    </a>
    <nav class="nav-links" aria-label="Główna nawigacja">
{links}    </nav>
    <div class="nav-cta">
      <a href="kontakt.html" class="btn btn--primary nav-desk">Umów konsultację</a>
      <button class="nav-toggle" aria-label="Menu" aria-expanded="false"><span></span></button>
    </div>
  </div>
</header>
'''


FOOTER = '''
<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <div class="brand"><img src="assets/logo-white.svg" alt="Krzysztof Miotk" class="brand-logo" width="280" height="42" /></div>
        <p class="footer-about">UX Researcher i konsultant. Zamieniam wiedzę o użytkownikach w wartość dla biznesu. Decision Guy w Quale UX.</p>
        <div class="socials">
          <a href="https://www.linkedin.com/" aria-label="LinkedIn" target="_blank" rel="noopener"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M4.98 3.5A2.5 2.5 0 1 1 0 3.5a2.5 2.5 0 0 1 4.98 0zM.5 8h4V24h-4V8zM8 8h3.8v2.2h.05c.53-1 1.83-2.2 3.77-2.2 4.03 0 4.78 2.65 4.78 6.1V24h-4v-7.1c0-1.7-.03-3.9-2.38-3.9-2.38 0-2.75 1.86-2.75 3.78V24H8V8z"/></svg></a>
          <a href="https://www.facebook.com/" aria-label="Facebook" target="_blank" rel="noopener"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M13 22v-9h3l.5-3.5H13V7.3c0-1 .3-1.7 1.8-1.7H17V2.4c-.4-.05-1.5-.16-2.8-.16-2.8 0-4.7 1.7-4.7 4.8v2.66H6.5V13H9.5v9H13z"/></svg></a>
          <a href="https://www.instagram.com/" aria-label="Instagram" target="_blank" rel="noopener"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor" stroke="none"/></svg></a>
        </div>
      </div>
      <div class="footer-col">
        <h4>Usługi</h4>
        <ul>
          <li><a href="badania-ux.html">Badania UX</a></li>
          <li><a href="zewnetrzny-dyrektor-ux.html">Zewnętrzny Dyrektor UX</a></li>
          <li><a href="segmentacja-klientow.html">Segmentacja klientów</a></li>
          <li><a href="audyt-ux.html">Audyt UX</a></li>
          <li><a href="konsultacje-i-mentoring.html">Konsultacje i mentoring</a></li>
          <li><a href="wystapienia-i-szkolenia.html">Wystąpienia i szkolenia</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Serwis</h4>
        <ul>
          <li><a href="index.html">Strona główna</a></li>
          <li><a href="uslugi.html">Usługi</a></li>
          <li><a href="insights.html">Insights</a></li>
          <li><a href="o-mnie.html">O mnie</a></li>
          <li><a href="kontakt.html">Kontakt</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Kontakt</h4>
        <ul>
          <li><a href="mailto:krzysiek@quale.agency">krzysiek@quale.agency</a></li>
          <li><a href="kontakt.html">Umów konsultację</a></li>
          <li><a href="https://quale.agency" target="_blank" rel="noopener">quale.agency</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© <span data-year>2025</span> Krzysztof Miotk. Wszelkie prawa zastrzeżone.</span>
      <a href="#">Polityka prywatności</a>
    </div>
  </div>
</footer>

<script src="js/main.js"></script>
</body>
</html>
'''


def cta_band():
    return f'''
<section class="section section--tight">
  <div class="wrap">
    <div class="cta-band reveal">
      <p class="eyebrow" style="justify-content:center; color:#fff">Zacznijmy</p>
      <h2>Porozmawiajmy o Twoim produkcie</h2>
      <p>Umów bezpłatną konsultację — opowiesz mi o wyzwaniu, a ja podpowiem, od czego zacząć, żeby badania realnie wsparły biznes.</p>
      <a href="kontakt.html" class="btn btn--light btn--lg">Umów konsultację {ARROW}</a>
    </div>
  </div>
</section>
'''


def write(name, title, desc, active, body):
    html = head(title, desc) + header(active) + "<main>\n" + body + "</main>\n" + FOOTER
    with open(os.path.join(BASE, name), "w", encoding="utf-8") as f:
        f.write(html)
    print("✓", name)


def checklist(items):
    lis = "".join(f"        <li>{CHECK} {it}</li>\n" for it in items)
    return f'<ul class="checklist">\n{lis}      </ul>'


# ===========================================================================
#  SERWIS — dane usług
# ===========================================================================
SERVICES = [
    {
        "slug": "badania-ux",
        "name": "Badania UX",
        "tag": "Research",
        "lead": "Pozyskaj wiedzę o użytkownikach i przekuj ją w biznes — z moją pomocą.",
        "for_whom": "Dla zespołów produktowych i marketingowych, które chcą podejmować decyzje na podstawie zachowań realnych użytkowników, a nie wewnętrznych opinii.",
        "what": [
            "Wywiady pogłębione i testy użyteczności (moderowane i niemoderowane).",
            "Badania ilościowe: ankiety, analiza ścieżek, dane z analityki.",
            "Mapy podróży klienta i identyfikacja punktów tarcia.",
            "Rekomendacje powiązane z konkretnymi metrykami biznesowymi.",
        ],
        "steps": [
            ("Brief i cel", "Ustalamy, którą decyzję lub metrykę badanie ma wesprzeć."),
            ("Plan badania", "Dobieram metody i rekrutuję właściwych uczestników."),
            ("Realizacja", "Prowadzę badania i zbieram dane jakościowe oraz ilościowe."),
            ("Insighty i rekomendacje", "Dostajesz wnioski gotowe do wdrożenia, nie surowy raport."),
        ],
        "price": "Wycena indywidualna",
        "price_note": "zależnie od zakresu i metod",
    },
    {
        "slug": "zewnetrzny-dyrektor-ux",
        "name": "Zewnętrzny Dyrektor UX",
        "tag": "Leadership",
        "lead": "Oddeleguj zarządzanie doświadczeniami klientów bez kosztów etatu.",
        "for_whom": "Dla firm, które potrzebują strategicznego przywództwa w obszarze UX, ale nie są jeszcze gotowe (lub nie chcą) zatrudniać dyrektora na pełen etat.",
        "what": [
            "Strategia UX spięta z celami biznesowymi firmy.",
            "Budowanie i rozwój kultury badawczej w zespole.",
            "Priorytetyzacja inicjatyw i nadzór nad jakością doświadczeń.",
            "Wsparcie w rekrutacji i rozwoju zespołu UX.",
        ],
        "steps": [
            ("Diagnoza", "Poznaję organizację, zespół i obecną dojrzałość UX."),
            ("Strategia", "Tworzymy plan działania i mierzalne cele na kwartały."),
            ("Prowadzenie", "Regularnie wspieram zespół i nadzoruję realizację."),
            ("Samodzielność", "Zostawiam organizację silniejszą, niż ją zastałem."),
        ],
        "price": "Współpraca abonamentowa",
        "price_note": "elastyczny wymiar godzin w miesiącu",
    },
    {
        "slug": "segmentacja-klientow",
        "name": "Segmentacja klientów",
        "tag": "Strategia",
        "lead": "Zrozum, którzy klienci przynoszą największy zysk i jak o nich zadbać.",
        "for_whom": "Dla zespołów, które chcą przestać traktować wszystkich klientów tak samo i skierować zasoby tam, gdzie zwracają się najszybciej.",
        "what": [
            "Segmentacja oparta na danych behawioralnych i wartości klienta.",
            "Profile i persony zakorzenione w realnych zachowaniach, nie w domysłach.",
            "Wskazanie segmentów o najwyższym potencjale LTV.",
            "Rekomendacje, jak komunikować się i projektować dla każdego segmentu.",
        ],
        "steps": [
            ("Dane", "Łączymy analitykę, transakcje i wiedzę o klientach."),
            ("Analiza", "Wyodrębniam segmenty i opisuję ich potrzeby oraz wartość."),
            ("Priorytety", "Pokazuję, które segmenty rozwijać, a które utrzymywać."),
            ("Aktywacja", "Przekładam segmenty na konkretne działania produktu i marketingu."),
        ],
        "price": "Wycena indywidualna",
        "price_note": "zależnie od dostępności danych",
    },
    {
        "slug": "audyt-ux",
        "name": "Audyt UX",
        "tag": "Audyt",
        "lead": "Zacznij od przeglądu UX w produkcie na bazie wiedzy i analityki.",
        "for_whom": "Dla firm, które chcą szybko dowiedzieć się, gdzie tracą użytkowników i pieniądze — zanim zainwestują w większy projekt.",
        "what": [
            "Przegląd kluczowych ścieżek na bazie heurystyk i dobrych praktyk.",
            "Analiza danych ilościowych i miejsc porzuceń w lejku.",
            "Lista problemów uszeregowana według wpływu na biznes.",
            "Konkretne, priorytetyzowane rekomendacje napraw (quick wins + długofalowe).",
        ],
        "steps": [
            ("Zakres", "Wybieramy ścieżki i ekrany o największym znaczeniu biznesowym."),
            ("Przegląd", "Analizuję produkt heurystycznie i w oparciu o dane."),
            ("Priorytety", "Porządkuję znaleziska według wpływu i kosztu naprawy."),
            ("Raport decyzyjny", "Dostajesz mapę drogową napraw gotową do wdrożenia."),
        ],
        "price": "Pakiet stały",
        "price_note": "od przeglądu pojedynczej ścieżki",
    },
    {
        "slug": "konsultacje-i-mentoring",
        "name": "Konsultacje i mentoring",
        "tag": "Mentoring",
        "lead": "Indywidualnie przedyskutuj wyzwania lub podnieś swoje kompetencje w UX.",
        "for_whom": "Dla badaczy, projektantów i product managerów, którzy potrzebują sparingpartnera albo chcą świadomie rozwijać warsztat UX research.",
        "what": [
            "Sesje 1:1 dopasowane do Twojego aktualnego wyzwania.",
            "Przegląd planów badawczych, narzędzi i wniosków.",
            "Indywidualna ścieżka rozwoju kompetencji.",
            "Wsparcie w trudnych rozmowach o roli badań w organizacji.",
        ],
        "steps": [
            ("Cel", "Określamy, co chcesz osiągnąć lub rozwiązać."),
            ("Sesje", "Pracujemy regularnie lub doraźnie — jak potrzebujesz."),
            ("Praktyka", "Dostajesz konkretne zadania i materiały między spotkaniami."),
            ("Efekt", "Rośniesz w roli i podejmujesz lepsze decyzje badawcze."),
        ],
        "price": "Stawka godzinowa",
        "price_note": "pojedyncze sesje lub pakiety",
    },
    {
        "slug": "wystapienia-i-szkolenia",
        "name": "Wystąpienia i szkolenia",
        "tag": "Edukacja",
        "lead": "Zaproś mnie na konferencję lub podnieś kompetencje całego zespołu.",
        "for_whom": "Dla organizatorów konferencji i liderów zespołów, którzy chcą energetycznych, konkretnych wystąpień i szkoleń osadzonych w praktyce.",
        "what": [
            "Prelekcje konferencyjne o UX research i wartości badań dla biznesu.",
            "Warsztaty szyte na miarę potrzeb i poziomu zespołu.",
            "Szkolenia z metod badawczych i demokratyzacji badań.",
            "Materiały, które zespół wykorzysta długo po szkoleniu.",
        ],
        "steps": [
            ("Temat", "Ustalamy temat, cele i poziom zaawansowania odbiorców."),
            ("Program", "Przygotowuję autorski program lub wystąpienie."),
            ("Realizacja", "Prowadzę energetycznie i angażująco — online lub na żywo."),
            ("Kontynuacja", "Zostawiam materiały i wskazówki do dalszej pracy."),
        ],
        "price": "Wycena indywidualna",
        "price_note": "wystąpienie, warsztat lub cykl",
    },
]

OTHER_ICONS = {
    "badania-ux": '<circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3"/>',
    "zewnetrzny-dyrektor-ux": '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/>',
    "segmentacja-klientow": '<path d="M21 21H4a1 1 0 0 1-1-1V3"/><path d="M7 16l4-5 3 3 5-7"/>',
    "audyt-ux": '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M9 15l2 2 4-4"/>',
    "konsultacje-i-mentoring": '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>',
    "wystapienia-i-szkolenia": '<path d="M3 11l18-5v12L3 14v-3zM11.6 16.8a3 3 0 1 1-5.8-1.6"/>',
}


def service_page(s):
    steps_html = ""
    for t, d in s["steps"]:
        steps_html += f'''        <div class="step stack" style="margin-bottom:1.4rem">
          <h4>{t}</h4>
          <p class="muted" style="font-size:.97rem">{d}</p>
        </div>
'''
    body = f'''
<section class="page-hero">
  <div class="wrap">
    <p class="breadcrumbs"><a href="index.html">Start</a><span>/</span><a href="uslugi.html">Usługi</a><span>/</span>{s["name"]}</p>
    <p class="eyebrow">{s["tag"]}</p>
    <h1 style="max-width:16ch; margin-top:.6rem">{s["name"]}</h1>
    <p class="lead">{s["lead"]}</p>
    <div class="hero-cta" style="margin-top:1.6rem">
      <a href="kontakt.html" class="btn btn--primary btn--lg">Umów konsultację {ARROW}</a>
      <a href="uslugi.html" class="btn btn--ghost btn--lg">Wszystkie usługi</a>
    </div>
  </div>
</section>

<section class="section--tight">
  <div class="wrap split">
    <div class="prose reveal">
      <h2>Dla kogo</h2>
      <p>{s["for_whom"]}</p>

      <h2>Co dostajesz</h2>
      {checklist(s["what"])}

      <h2>Jak przebiega współpraca</h2>
      <div class="steps" style="margin-top:1.2rem">
{steps_html}      </div>
    </div>

    <aside class="reveal">
      <div class="sidecard">
        <span class="pill">{s["tag"]}</span>
        <h4 style="margin-top:1rem">{s["name"]}</h4>
        <div class="price">{s["price"]} <small>· {s["price_note"]}</small></div>
        <p class="muted" style="font-size:.95rem; margin:.6rem 0 1.2rem">Najlepiej zacznijmy od krótkiej rozmowy — dopasuję zakres do Twojej sytuacji i celu biznesowego.</p>
        <a href="kontakt.html" class="btn btn--primary btn--block">Porozmawiajmy {ARROW}</a>
        <a href="mailto:krzysiek@quale.agency" class="btn btn--ghost btn--block" style="margin-top:.6rem">krzysiek@quale.agency</a>
      </div>
    </aside>
  </div>
</section>
{cta_band()}'''
    write(s["slug"] + ".html",
          f'{s["name"]} — Krzysztof Miotk',
          s["lead"],
          "uslugi.html",
          body)


for s in SERVICES:
    service_page(s)


# ===========================================================================
#  USŁUGI — hub
# ===========================================================================
def services_cards():
    cards = ""
    for s in SERVICES:
        ico = OTHER_ICONS[s["slug"]]
        cards += f'''      <a href="{s["slug"]}.html" class="card">
        <div class="ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{ico}</svg></div>
        <h3>{s["name"]}</h3>
        <p>{s["lead"]}</p>
        <span class="card-foot link-arrow">Dowiedz się więcej {ARROW}</span>
      </a>
'''
    return cards


uslugi_body = f'''
<section class="page-hero">
  <div class="wrap">
    <p class="breadcrumbs"><a href="index.html">Start</a><span>/</span>Usługi</p>
    <p class="eyebrow">Usługi</p>
    <h1 style="max-width:18ch; margin-top:.6rem">Wsparcie UX dopasowane do <span class="uline">etapu Twojego produktu</span></h1>
    <p class="lead">Od pojedynczych badań, przez audyty i segmentację, po stałe przywództwo UX. Wybierz format, który najlepiej odpowiada na Twoje wyzwanie.</p>
  </div>
</section>

<section class="section--tight">
  <div class="wrap">
    <div class="grid grid-3 reveal">
{services_cards()}    </div>
  </div>
</section>

<section class="section section--tint">
  <div class="wrap">
    <div class="section-head center reveal">
      <p class="eyebrow" style="justify-content:center">Jak pracuję</p>
      <h2>Każda usługa prowadzi do decyzji</h2>
      <p class="lead">Niezależnie od formatu, pracuję tak samo: zaczynam od celu biznesowego i kończę na rekomendacjach, które da się wdrożyć.</p>
    </div>
    <div class="grid grid-4 reveal">
      <div class="step stack"><h4>Zrozumienie celu</h4><p class="muted" style="font-size:.95rem">Zaczynamy od metryki, którą chcesz poprawić.</p></div>
      <div class="step stack"><h4>Badanie</h4><p class="muted" style="font-size:.95rem">Dobieram metody do pytania, nie odwrotnie.</p></div>
      <div class="step stack"><h4>Synteza i decyzje</h4><p class="muted" style="font-size:.95rem">Insighty zamieniam w priorytety i rekomendacje.</p></div>
      <div class="step stack"><h4>Wdrożenie i efekt</h4><p class="muted" style="font-size:.95rem">Wspieram wdrożenie i mierzę realny wpływ.</p></div>
    </div>
  </div>
</section>
{cta_band()}'''

write("uslugi.html", "Usługi — Krzysztof Miotk",
      "Usługi UX: badania, zewnętrzny dyrektor UX, segmentacja klientów, audyt UX, konsultacje i szkolenia.",
      "uslugi.html", uslugi_body)


# ===========================================================================
#  INSIGHTS
# ===========================================================================
ARTICLES = [
    ("strategia", "Know How", "Audyt DOSE+K: hormony szczęścia (i stresu) w interfejsie",
     "Framework do audytu UX oparty na neurochemii. Jak dopamina, oksytocyna, serotonina, endorfiny i kortyzol wpływają na decyzje użytkowników.",
     "Zespół Quale", "ZQ", "15 min czytania", False),
    ("product", "UX Design", "Szybkość to nie zawsze dobry UX — historia platformy XTB",
     "Jak przez nadmierną szybkość interfejsu straciłem kilka tysięcy złotych i czego to uczy o projektowaniu pod decyzje.",
     "Krzysztof Miotk", "KM", "10 min czytania", True),
    ("research", "User Research", "Demokratyzacja badań — kompletny poradnik UX",
     "Jak rozłożyć badania na cały zespół, zachowując jakość i wiarygodność wniosków.",
     "Zespół Quale", "ZQ", "35 min czytania", False),
    ("strategia", "Strategia", "Jak zatrzymać klientów i sprawić, żeby chcieli wracać?",
     "O tym, jak dbamy o EX-perience klientów i co realnie buduje ich lojalność.",
     "Agata Łapińska", "AŁ", "6 min czytania", True),
    ("research", "Eventy UX", "UX w Lesie 2025: charytatywny plenerowy barcamp UX",
     "Relacja z plenerowego barcampu UX w Polsce — społeczność, wiedza i dobra sprawa.",
     "Krzysztof Miotk", "KM", "8 min czytania", False),
    ("product", "Product Design", "Od insightu do decyzji produktowej — bez przepaści",
     "Jak projektować proces, w którym wnioski z badań nie giną między researchem a roadmapą.",
     "Krzysztof Miotk", "KM", "12 min czytania", True),
]

FILTERS = [("all", "Wszystkie"), ("research", "User Research"),
           ("product", "Product Design"), ("strategia", "Strategia")]


ARTICLE_IMG = {
    "Od insightu do decyzji produktowej — bez przepaści": "krzysztof-prelekcja.jpg",
    "Demokratyzacja badań — kompletny poradnik UX": "warsztaty.jpg",
}


def article_card(a):
    cat, tag, title, desc, author, initials, rt, alt = a
    altc = " alt" if alt else ""
    img = ARTICLE_IMG.get(title)
    thumb = (f'<div class="thumb has-img"><img src="assets/img/{img}" alt="{title}" /></div>'
             if img else f'<div class="thumb{altc}"></div>')
    return f'''      <a href="#" class="article reveal" data-cat="{cat}">
        {thumb}
        <div class="meta"><span class="tag">{tag}</span></div>
        <h3>{title}</h3>
        <p>{desc}</p>
        <div class="byline"><span class="avatar">{initials}</span> {author} <span class="dot"></span> {rt}</div>
      </a>
'''


feat = ARTICLES[0]
filt_html = "".join(
    f'      <button class="filter{" is-active" if f[0]=="all" else ""}" data-filter="{f[0]}">{f[1]}</button>\n'
    for f in FILTERS)
cards_html = "".join(article_card(a) for a in ARTICLES[1:])

insights_body = f'''
<section class="page-hero">
  <div class="wrap">
    <p class="breadcrumbs"><a href="index.html">Start</a><span>/</span>Insights</p>
    <p class="eyebrow">Insights</p>
    <h1 style="max-width:16ch; margin-top:.6rem">Wiedza, którą możesz <span class="uline">wdrożyć</span></h1>
    <p class="lead">Artykuły, frameworki i case studies o UX research, projektowaniu produktów i strategii doświadczeń klienta.</p>
  </div>
</section>

<section class="section--tight">
  <div class="wrap">
    <a href="#" class="featured reveal">
      <div class="feat-body">
        <span class="tag">{feat[1]}</span>
        <h2>{feat[2]}</h2>
        <p>{feat[3]}</p>
        <div class="byline"><span class="avatar">{feat[5]}</span> {feat[4]} <span class="dot"></span> {feat[6]}</div>
      </div>
      <div class="feat-media has-img"><img src="assets/img/panel.jpg" alt="Zespół Quale podczas panelu dyskusyjnego na wydarzeniu UX" /></div>
    </a>
  </div>
</section>

<section class="section--tight">
  <div class="wrap">
    <div class="filters reveal">
{filt_html}    </div>
    <div class="grid grid-3">
{cards_html}    </div>
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <div class="newsletter reveal">
      <div class="grid grid-2" style="align-items:center; gap:clamp(24px,4vw,56px)">
        <div>
          <p class="eyebrow">Newsletter</p>
          <h2 style="margin:.6rem 0 1rem">Raporty i artykuły co 2 tygodnie</h2>
          <p>Tylko treści merytoryczne. Zero spamu. Możesz wypisać się w każdej chwili.</p>
        </div>
        <div>
          <form data-demo>
            <div style="display:flex; gap:.75rem; flex-wrap:wrap;">
              <input type="email" required placeholder="Twój adres e-mail" aria-label="Twój adres e-mail" />
              <button type="submit" class="btn btn--dark">Zapisz się</button>
            </div>
            <p class="small" data-note>Zapisując się, akceptujesz politykę prywatności.</p>
          </form>
        </div>
      </div>
    </div>
  </div>
</section>
'''

write("insights.html", "Insights — Krzysztof Miotk",
      "Artykuły o UX research, projektowaniu produktów i strategii doświadczeń klienta.",
      "insights.html", insights_body)


# ===========================================================================
#  O MNIE
# ===========================================================================
o_mnie_body = f'''
<section class="page-hero">
  <div class="wrap split" style="align-items:center">
    <div class="reveal">
      <p class="breadcrumbs"><a href="index.html">Start</a><span>/</span>O mnie</p>
      <p class="eyebrow">O mnie</p>
      <h1 style="margin-top:.6rem">Krzysztof <span class="mark mark--text">Miotk</span></h1>
      <p class="lead" style="margin-top:1rem">UX Researcher i konsultant. Zamieniam wiedzę o użytkownikach w wartość dla biznesu — i uczę zespoły robić to samodzielnie.</p>
      <div class="hero-cta" style="margin-top:1.6rem">
        <a href="kontakt.html" class="btn btn--primary btn--lg">Porozmawiajmy {ARROW}</a>
        <a href="insights.html" class="btn btn--ghost btn--lg">Czytaj insights</a>
      </div>
    </div>
    <figure class="figure reveal" style="max-width:380px; margin-inline:auto">
      <img class="portrait-photo" src="assets/img/krzysztof-portret.jpg" alt="Krzysztof Miotk — Decision Guy w Quale UX, inaczej Wiedźmin UX" width="280" height="316" />
    </figure>
  </div>
</section>

<section class="section--tight">
  <div class="wrap split">
    <div class="prose reveal maxw-prose">
      <h2>Badania w służbie biznesu</h2>
      <p>Wierzę, że badania są przydatne tylko wtedy, gdy służą biznesowi. Dlatego nie dostarczam raportów do szuflady — pracuję na decyzjach. Pokazuję markom, gdzie tracą pieniądze w doświadczeniu klienta i co konkretnie zrobić, żeby je odzyskać.</p>
      <p>Pomagam silnym markom zwiększać konwersję i wartość klienta w czasie dzięki User Experience opartemu na danych, a nie na opiniach.</p>

      <h2>Praktyk i nauczyciel</h2>
      <p>Od 2017 roku wykładam i prowadzę zajęcia z UX research — odpowiadam m.in. za jedyny w Polsce kierunek studiów poświęcony badaniom UX. Łączę praktykę konsultanta z dydaktyką, dzięki czemu wiedza, którą przekazuję, jest świeża i osadzona w realnych projektach.</p>
      <p>Po wystąpieniach konferencyjnych w 2023 roku przylgnął do mnie przydomek „UX Wiedźmin”. Współtworzę też „UX po Godzinach” — najstarszy aktywny podcast o UX w Polsce.</p>

      <h2>Poza ekranem</h2>
      <p>Jestem instruktorem harcerskim w stopniu podharcmistrza. Po godzinach działam w ratownictwie i pływam pod żaglami — to tam ćwiczę spokój, decyzyjność i pracę zespołową, które przenoszę do projektów.</p>
    </div>

    <aside class="reveal">
      <figure class="figure" style="margin-bottom:1.2rem">
        <img src="assets/img/krzysztof-prelekcja.jpg" alt="Krzysztof Miotk podczas wystąpienia na konferencji INFOSHARE 2025" width="248" height="212" />
      </figure>
      <div class="sidecard">
        <h4>W skrócie</h4>
        <ul class="checklist" style="margin-top:.6rem">
          <li>{CHECK} UX Researcher i konsultant</li>
          <li>{CHECK} Decision Guy w Quale UX</li>
          <li>{CHECK} Wykładowca UX research od 2017</li>
          <li>{CHECK} „UX Wiedźmin” (od 2023)</li>
          <li>{CHECK} Współtwórca podcastu „UX po Godzinach”</li>
          <li>{CHECK} Podharcmistrz, ratownik, żeglarz</li>
        </ul>
        <a href="kontakt.html" class="btn btn--primary btn--block" style="margin-top:1.2rem">Umów konsultację {ARROW}</a>
      </div>
    </aside>
  </div>
</section>

<section class="section section--soft">
  <div class="wrap center reveal" style="max-width:62ch">
    <p class="quote">„Badania są przydatne tylko wtedy, gdy <span class="mark">służą biznesowi</span>.”</p>
    <p class="mt-3 muted">— Krzysztof Miotk</p>
  </div>
</section>
{cta_band()}'''

write("o-mnie.html", "O mnie — Krzysztof Miotk",
      "Krzysztof Miotk — UX Researcher i konsultant, wykładowca, „UX Wiedźmin”, współtwórca podcastu „UX po Godzinach”.",
      "o-mnie.html", o_mnie_body)


# ===========================================================================
#  KONTAKT
# ===========================================================================
kontakt_body = f'''
<section class="page-hero">
  <div class="wrap">
    <p class="breadcrumbs"><a href="index.html">Start</a><span>/</span>Kontakt</p>
    <p class="eyebrow">Kontakt</p>
    <h1 style="max-width:16ch; margin-top:.6rem">Porozmawiajmy o <span class="uline">Twoim produkcie</span></h1>
    <p class="lead">Opisz krótko swoje wyzwanie. Odezwę się i podpowiem, od czego zacząć, żeby badania realnie wsparły biznes.</p>
  </div>
</section>

<section class="section--tight">
  <div class="wrap split">
    <div class="reveal">
      <form data-demo class="card" style="padding:clamp(24px,3vw,36px)">
        <div class="field">
          <label for="name">Imię i nazwisko</label>
          <input id="name" name="name" type="text" required placeholder="Jan Kowalski" />
        </div>
        <div class="field">
          <label for="email">E-mail</label>
          <input id="email" name="email" type="email" required placeholder="jan@firma.pl" />
        </div>
        <div class="field">
          <label for="topic">Temat</label>
          <select id="topic" name="topic">
            <option>Badania UX</option>
            <option>Zewnętrzny Dyrektor UX</option>
            <option>Segmentacja klientów</option>
            <option>Audyt UX</option>
            <option>Konsultacje i mentoring</option>
            <option>Wystąpienia i szkolenia</option>
            <option>Inny temat</option>
          </select>
        </div>
        <div class="field">
          <label for="msg">Wiadomość</label>
          <textarea id="msg" name="msg" required placeholder="Opisz krótko swoje wyzwanie i cel biznesowy..."></textarea>
        </div>
        <button type="submit" class="btn btn--primary btn--lg btn--block">Wyślij wiadomość {ARROW}</button>
        <p class="small muted" data-note style="margin-top:.9rem; font-size:.85rem">Wysyłając formularz, akceptujesz politykę prywatności.</p>
      </form>
    </div>

    <aside class="reveal">
      <div class="sidecard">
        <h4>Bezpośredni kontakt</h4>
        <p class="muted" style="font-size:.95rem; margin:.5rem 0 1.2rem">Wolisz napisać od razu? Śmiało — odpowiadam na każdą wiadomość.</p>
        <ul class="checklist">
          <li>{CHECK} <a href="mailto:krzysiek@quale.agency" style="color:var(--brand);font-weight:600">krzysiek@quale.agency</a></li>
          <li>{CHECK} Bezpłatna konsultacja wstępna</li>
          <li>{CHECK} Odpowiedź zwykle w 1–2 dni robocze</li>
        </ul>
        <div class="socials" style="margin-top:1rem">
          <a href="https://www.linkedin.com/" aria-label="LinkedIn" target="_blank" rel="noopener" style="border-color:var(--line-strong)"><svg viewBox="0 0 24 24" fill="var(--brand)"><path d="M4.98 3.5A2.5 2.5 0 1 1 0 3.5a2.5 2.5 0 0 1 4.98 0zM.5 8h4V24h-4V8zM8 8h3.8v2.2h.05c.53-1 1.83-2.2 3.77-2.2 4.03 0 4.78 2.65 4.78 6.1V24h-4v-7.1c0-1.7-.03-3.9-2.38-3.9-2.38 0-2.75 1.86-2.75 3.78V24H8V8z"/></svg></a>
        </div>
      </div>
      <div class="sidecard" style="margin-top:1rem; background:var(--brand-light); border-color:transparent">
        <span class="pill" style="background:#fff">Quale UX</span>
        <p style="margin-top:.8rem; color:var(--brand-deep); font-weight:600">Działam w ramach Quale — agencji UX research &amp; strategy.</p>
        <a href="https://quale.agency" target="_blank" rel="noopener" class="link-arrow" style="margin-top:.6rem">quale.agency {ARROW}</a>
      </div>
    </aside>
  </div>
</section>
'''

write("kontakt.html", "Kontakt — Krzysztof Miotk",
      "Skontaktuj się z Krzysztofem Miotkiem — bezpłatna konsultacja wstępna. krzysiek@quale.agency",
      "kontakt.html", kontakt_body)

print("\\nGotowe — wszystkie podstrony wygenerowane.")
