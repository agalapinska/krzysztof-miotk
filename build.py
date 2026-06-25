#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generator podstron krzysztofmiotk.pl — treść 1:1 z oryginału, branding QUALE."""
import os, re

BASE = os.path.dirname(os.path.abspath(__file__))

ARROW = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" '
         'stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>')
CHEV = ('<svg class="chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" '
        'stroke-linecap="round" stroke-linejoin="round"><path d="M6 9l6 6 6-6"/></svg>')

MOTTO = "Jeżeli mam wybierać między badaniami słabymi a gorszymi, to wolę nie wybierać wcale."

# Kolejność i etykiety usług (jak w menu oryginału)
SERVICE_NAV = [
    ("badania-ux", "Badania UX"),
    ("zewnetrzny-dyrektor-ux", "Zewnętrzny Dyrektor UX"),
    ("segmentacja-klientow", "Segmentacja klientów"),
    ("audyt-ux", "Audyt UX"),
    ("konsultacje-i-mentoring", "Konsultacje i mentoring"),
    ("wystapienia-i-szkolenia", "Wystąpienia i szkolenia"),
]

# Hasła usług (z sekcji „Potrzebujesz innej usługi?")
TAGLINES = {
    "badania-ux": "Pozyskaj wiedzę o użytkownikach i przekuj je w biznes z moją pomocą.",
    "zewnetrzny-dyrektor-ux": "Oddeleguj zarządzanie doświadczeniami Twoich klientów bez kosztów etatu.",
    "segmentacja-klientow": "Zrozum, którzy klienci przynoszą największy zysk i jak o nich zadbać.",
    "audyt-ux": "Zacznij od przeglądu UX w Twoim produkcie na bazie mojej wiedzy i analityki.",
    "konsultacje-i-mentoring": "Indywidualnie przedyskutuj rzeczy lub podnieś swoje kompetencje w UX.",
    "wystapienia-i-szkolenia": "Zaproś mnie na konferencję lub podnieś kompetencje swojego zespołu.",
}

ICONS = {
    "badania-ux": '<circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3"/>',
    "zewnetrzny-dyrektor-ux": '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/>',
    "segmentacja-klientow": '<path d="M21 21H4a1 1 0 0 1-1-1V3"/><path d="M7 16l4-5 3 3 5-7"/>',
    "audyt-ux": '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M9 15l2 2 4-4"/>',
    "konsultacje-i-mentoring": '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>',
    "wystapienia-i-szkolenia": '<path d="M3 11l18-5v12L3 14v-3zM11.6 16.8a3 3 0 1 1-5.8-1.6"/>',
}


def md(t):
    """**bold** -> <strong>."""
    return re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)


# --------------------------------------------------------------------- szkielet
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


def submenu(active_slug):
    items = ""
    for slug, label in SERVICE_NAV:
        cur = ' aria-current="page"' if slug == active_slug else ""
        items += f'        <a href="{slug}.html"{cur}>{label}</a>\n'
    return items


def header(active):
    """active: 'uslugi' | 'kontakt' | <service-slug>"""
    uslugi_active = (active == "uslugi" or active in TAGLINES)
    kontakt_cur = ' aria-current="page"' if active == "kontakt" else ""
    uslugi_cur = ' aria-current="page"' if active == "uslugi" else ""
    return f'''
<header class="site-header">
  <div class="wrap nav">
    <a href="index.html" class="brand" aria-label="Krzysztof Miotk — strona główna">
      <img src="assets/logo.svg" alt="Krzysztof Miotk" class="brand-logo" width="280" height="42" />
    </a>
    <nav class="nav-links" aria-label="Główna nawigacja">
      <div class="nav-item">
        <a href="uslugi.html" class="nav-top"{uslugi_cur} aria-haspopup="true">Usługi {CHEV}</a>
        <div class="submenu">
{submenu(active if active in TAGLINES else "")}        </div>
      </div>
      <a href="kontakt.html"{kontakt_cur}>Kontakt</a>
    </nav>
    <div class="nav-cta">
      <a href="kontakt.html" class="btn btn--primary nav-desk">Umów rozmowę</a>
      <button class="nav-toggle" aria-label="Menu" aria-expanded="false"><span></span></button>
    </div>
  </div>
</header>
'''


def footer_services():
    return "".join(f'          <li><a href="{slug}.html">{label}</a></li>\n'
                   for slug, label in SERVICE_NAV)


FOOTER = f'''
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
{footer_services()}        </ul>
      </div>
      <div class="footer-col">
        <h4>Serwis</h4>
        <ul>
          <li><a href="index.html">Strona główna</a></li>
          <li><a href="uslugi.html">Usługi</a></li>
          <li><a href="kontakt.html">Kontakt</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Kontakt</h4>
        <ul>
          <li><a href="mailto:krzysiek@quale.agency">krzysiek@quale.agency</a></li>
          <li><a href="kontakt.html">Umów videorozmowę</a></li>
          <li><a href="https://quale.agency" target="_blank" rel="noopener">quale.agency</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© <span data-year>2025</span> Krzysztof Miotk. Wszelkie prawa zastrzeżone.</span>
      <a href="polityka-prywatnosci.html">Polityka prywatności</a>
    </div>
  </div>
</footer>

<script src="js/main.js"></script>
</body>
</html>
'''


def write(name, title, desc, active, body):
    html = head(title, desc) + header(active) + "<main>\n" + body + "</main>\n" + FOOTER
    with open(os.path.join(BASE, name), "w", encoding="utf-8") as f:
        f.write(html)
    print("✓", name)


# --------------------------------------------------------------------- renderery
def process_steps(steps):
    out = '<div class="steps grid grid-2" style="margin-top:1.4rem">\n'
    for title, desc in steps:
        out += f'''      <div class="step stack" style="margin-bottom:.4rem">
        <h4>{md(title)}</h4>
        <p class="muted" style="font-size:.97rem">{md(desc)}</p>
      </div>\n'''
    out += "    </div>"
    return out


def methods_grid(items):
    out = '<div class="grid grid-3 reveal">\n'
    for i, (title, desc) in enumerate(items, 1):
        out += f'''      <div class="card">
        <span class="method-num">{i}</span>
        <h3>{md(title)}</h3>
        <p>{md(desc)}</p>
      </div>\n'''
    out += "    </div>"
    return out


def reasons_block(items):
    out = '<div class="reveal">\n'
    for title, body in items:
        out += f'''      <div class="reason">
        <h3>{md(title)}</h3>
        <p>{md(body)}</p>
      </div>\n'''
    out += "    </div>"
    return out


def casestudy_block(label, title, desc, link=None):
    link_html = ""
    if link:
        txt, url = link
        link_html = f'<a href="{url}" class="link-arrow">{txt} {ARROW}</a>'
    return f'''    <div class="casestudy reveal">
      <span class="pill">{label}</span>
      <h3>{title}</h3>
      <p>{md(desc)}</p>
      {link_html}
    </div>'''


def cross_links(current):
    cards = ""
    for slug, label in SERVICE_NAV:
        if slug == current:
            continue
        ico = ICONS[slug]
        cards += f'''      <a href="{slug}.html" class="card">
        <div class="ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{ico}</svg></div>
        <h3>{label}</h3>
        <p>{TAGLINES[slug]}</p>
        <span class="card-foot link-arrow">Zobacz usługę {ARROW}</span>
      </a>\n'''
    return f'''
<section class="section section--soft">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">Potrzebujesz innej usługi?</p>
      <h2>Kliknij na wybraną usługę</h2>
      <p class="lead">…aby przeczytać przykładowe wdrożenie i moje przemyślenia (artykuły) na ten temat.</p>
    </div>
    <div class="grid grid-3 reveal">
{cards}    </div>
    <div class="center" style="margin-top:2.5rem">
      <a href="kontakt.html" class="btn btn--primary btn--lg">Umów videorozmowę {ARROW}</a>
    </div>
  </div>
</section>'''


def service_hero(s):
    return f'''
<section class="page-hero">
  <div class="wrap">
    <p class="breadcrumbs"><a href="index.html">Start</a><span>/</span><a href="uslugi.html">Usługi</a><span>/</span>{s["name"]}</p>
    <h1 style="max-width:18ch; margin-top:.4rem">{md(s["h1"])}</h1>
    <p class="lead">{md(s["lead"])}</p>
    <div class="hero-cta" style="margin-top:1.6rem">
      <a href="kontakt.html" class="btn btn--primary btn--lg">Wyceń usługę {ARROW}</a>
      <a href="uslugi.html" class="btn btn--ghost btn--lg">Wszystkie usługi</a>
    </div>
  </div>
</section>'''


def section(inner, cls=""):
    return f'\n<section class="section--tight {cls}">\n  <div class="wrap">\n{inner}\n  </div>\n</section>'


def service_page(s):
    body = service_hero(s)

    # intro (czym jest)
    body += f'''
<section class="section--tight">
  <div class="wrap maxw-prose reveal">
    <h2>{md(s["intro_h"])}</h2>
    {s["intro_html"]}
  </div>
</section>'''

    # metody (opcjonalnie)
    if s.get("methods"):
        body += f'''
<section class="section section--soft">
  <div class="wrap">
    <div class="section-head reveal"><h2>{md(s["methods_h"])}</h2></div>
    {methods_grid(s["methods"])}
  </div>
</section>'''

    # proces
    if s.get("process"):
        body += f'''
<section class="section--tight">
  <div class="wrap reveal">
    <h2>{md(s.get("process_h","Jak wygląda proces?"))}</h2>
    {process_steps(s["process"])}
  </div>
</section>'''

    # dlaczego warto (opcjonalnie)
    if s.get("reasons"):
        body += f'''
<section class="section section--soft">
  <div class="wrap">
    <div class="section-head reveal"><h2>{md(s["reasons_h"])}</h2></div>
    {reasons_block(s["reasons"])}
  </div>
</section>'''

    # testimonial (opcjonalnie)
    if s.get("testimonial"):
        t = s["testimonial"]
        body += f'''
<section class="section--tight">
  <div class="wrap maxw-prose reveal">
    <div class="testimonial"><p>{t["quote"]}</p><div class="who">{t["who"]}</div></div>
  </div>
</section>'''

    # case study (opcjonalnie)
    if s.get("casestudy"):
        c = s["casestudy"]
        body += f'''
<section class="section--tight">
  <div class="wrap">
    <p class="eyebrow reveal" style="margin-bottom:1rem">{c.get("label","Przykładowy projekt")}</p>
    {casestudy_block(c.get("tag","Case study"), c["title"], c["desc"], c.get("link"))}
  </div>
</section>'''

    # cross-links + motto
    body += cross_links(s["slug"])
    body += f'''
<section class="section--tight center">
  <div class="wrap"><p class="motto">„{MOTTO}"</p></div>
</section>'''
    write(s["slug"] + ".html", f'{s["name"]} — Krzysztof Miotk', s["lead"], s["slug"], body)


# ===========================================================================
#  TREŚĆ USŁUG (1:1 z krzysztofmiotk.pl)
# ===========================================================================
SERVICES = []

SERVICES.append({
    "slug": "badania-ux", "name": "Badania UX",
    "h1": "Badania UX",
    "lead": "Zbadaj potrzeby klientów lub użyteczność swoich produktów, a następnie przekuj je w rozwiązania z moją pomocą.",
    "intro_h": "Badania UX to most między danymi a decyzjami biznesowymi i projektowymi.",
    "intro_html": (
        "<p>Nie bez powodu jestem jedynym kierownikiem studiów z zakresu badań UX w Polsce. A osoby, które uczyłem pracują w agencjach i produktach.</p>"
        "<p>" + md("Przeprowadzam **badania UX na każdym poziomie skomplikowania i z użyciem najbardziej optymalnych metod do postawionych celów i budżetów.**") + "</p>"
        "<p>" + md("Wskażę Ci, które ścieżki pozwolą spełnić Twój cel biznesowy. Zazwyczaj do postawionego celu są 2-4 sensowne (opłacalne w stosunku cena do jakości) ścieżki. Ja pokażę Ci je wszystkie wraz z zaletami i wadami każdej z nich – **a Ty świadomie podejmiesz decyzję co zrobimy wspólnie.**") + "</p>"
    ),
    "methods_h": "Najczęściej realizowane metody badań UX",
    "methods": [
        ("Testy użyteczności", "**Użyteczność produktów online i offline** to obecnie podstawa. Zbadam Twój produkt lub usługę z Twoją grupą docelową, aby zwiększyć m.in. **konwersję**, **retencję**, oraz **CLV**."),
        ("Product Discovery", "Proces badawczy, który pozwoli na **odkrycie potencjału i popytu na Twój produkt.** Przyda się przy nowym pomyśle na produkt lub stagnacji obecnego."),
        ("Wywiady pogłębione", "Odkryję **ukryte potrzeby** Twoich klientów – również te **niezaspokojone przez Twoją konkurencję**. Przekujemy je w innowacje w Twojej firmie."),
        ("Focusy", "Poprowadzę grupowe wywiady, które wskażą **emocjonalną część zachowań i potrzeb** Twoich klientów. Dzięki temu wskażę Ci **ścieżkę zakupową** Twoich klientów."),
        ("Warsztaty z klientami", "Wraz z Twoimi klientami wypracujemy optymalizacje i innowacje Twojego produktu. Te warsztaty świetnie pokazują **jak klienci postrzegają Twój produkt i czego potrzebują, aby z Tobą pozostać.**"),
        ("Inne metody badań UX", "Eyetracking? Treetesting? Card sorting? A może coś jeszcze innego? Są to rzadsze metody, ale również je realizuję! Po prostu napisz do mnie a opowiem Ci jak to robię 🙂"),
    ],
    "reasons_h": "Dlaczego warto zrobić badania UX ze mną?",
    "reasons": [
        ("Ponad 2500 sesji badawczych w kilkudziesięciu firmach", "Jestem doświadczonym moderatorem, który prowadził badania dla zróżnicowanych branż i grup docelowych – od usług bankowych, przez start-upy, aż po usługi offline dla sektora publicznego."),
        ("Umiejętność przekuwania badań w rozwiązania", "Pracowałem jako Project Manager, a na co dzień jestem konsultantem biznesowym. Nie tylko pozyskuję dane, ale widzę **jak można je przekuć w rozwiązania – zarówno projektowe, jak i strategiczne.**"),
        ("Priorytetyzacja wyników i błędów użyteczności", "Wiem, że nie jest Ci potrzebne 100 wniosków wrzucone w raport. Potrzebne jest pokazanie tych **5-10 najważniejszych**, a pozostałymi 90 zajmiesz się później. Każdy mój raport posiada wskazanie najważniejszych wniosków, które zasilą Twój biznes. Błędy użyteczności dzielę na **3-stopniową skalę, która wskazuje priorytet naprawy**."),
        ("Unikasz błędów, które popełniły (dosłownie) setki badaczy i firm", "Oprócz moich osobistych doświadczeń projektowych otrzymujesz też moje know-how zbudowane na problemach badaczy, **których szkoliłem lub takich, którzy przychodzą do mnie, kiedy skala projektów ich przerasta.** Co roku ta liczba zwiększa się o 50-100 osób."),
    ],
    "casestudy": {"tag": "Case study", "title": "Apteka Gemini — Badania RITE",
                  "desc": "Czyli szybka walidacja 7 koncepcji procesu, aby połączyć ograniczenia prawne, wymogi biznesowe i trendy UX-owe. W 2 tygodnie zbadałem 7 koncepcji designu. Efekty nie wymagają zmian już od kilku lat."},
})

SERVICES.append({
    "slug": "zewnetrzny-dyrektor-ux", "name": "Zewnętrzny Dyrektor UX",
    "h1": "Zewnętrzny Dyrektor UX",
    "lead": "Oddeleguj zarządzanie doświadczeniami Twoich klientów bez kosztów etatowych.",
    "testimonial": {
        "quote": "Współpraca z Krzyśkiem to dla nas comiesięczna oszczędność na designie i wdrożeniach, a także gwarancja zawsze trafionych decyzji UX-owych. Od momentu rozpoczęcia współpracy, zmiany w produkcie są bardziej przemyślane i dopieszczone – a jego działania mają realny i pozytywny wpływ na doświadczenia naszych użytkowników. Krzysiek nie przytakuje. Krzysiek konfrontuje się z nami, pozostając partnerem w dyskusji. Równocześnie potrafi przenieść doświadczenie z różnych branż na nasz produkt, dając nam za każdym razem świeże spojrzenie i pomysły na rozwój.",
        "who": "Jarek Piotrowski, Product Manager @Traffit"},
    "intro_h": "Kim jest zewnętrzny dyrektor UX, którym mogę być w Twoim produkcie?",
    "intro_html": (
        "<p>Zewnętrzny dyrektor UX to osoba, która nie pracuje u Ciebie na pełny etat, ale dba o User Experience Twojej firmy / produktu.</p>"
        "<p>Zewnętrzny dyrektor UX to ekspert, który:</p>"
        "<ul class=\"checklist\">"
        "<li><svg viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'><path d='M20 6L9 17l-5-5'/></svg> " + md("Spojrzy **strategicznie na produkt z perspektywy UX**") + "</li>"
        "<li><svg viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'><path d='M20 6L9 17l-5-5'/></svg> " + md("Podczas rozmów i decyzji wskaże **potencjalne możliwości – przedstawiając ich zalety i ryzyka**") + "</li>"
        "<li><svg viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'><path d='M20 6L9 17l-5-5'/></svg> Wesprze działania operacyjne w odpowiednich momentach – działając z obecnymi pracownikami zgodnie z ich dyspozycyjnością, lub przejmując obowiązki operacyjne do naszej agencji</li>"
        "<li><svg viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'><path d='M20 6L9 17l-5-5'/></svg> " + md("Pomoże **wypracować procesy, które będziecie stosować** nawet po tym, jak Wasza firma stanie się samowystarczalna i nasza współpraca się zakończy") + "</li>"
        "<li><svg viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'><path d='M20 6L9 17l-5-5'/></svg> " + md("**Obiektywnie oceni sytuację** dzięki brakowi emocjonalnego zaangażowania w produkt i relacje między pracownikami") + "</li>"
        "</ul>"
    ),
    "process": [
        ("Spotkanie zapoznawcze", "Zrozumiem w jakim stanie jest Twój produkt. Poznam główne bolączki, potrzeby i oczekiwania wobec współpracy ze mną."),
        ("Plan ramowy pracy", "**Przed podpisaniem umowy** przedstawię Ci ramowy plan wspólnych działań. Wspólnie go omówimy, poprawimy i zatwierdzimy."),
        ("Warsztaty z zespołem", "UX zaczyna się od Twojego zespołu. Przeprowadzę warsztaty, które pozwolą angażować Twój zespół w odpowiednich momentach."),
        ("Realizacja planu", "Zgodnie z wyznaczonym planem będziemy poprawiać UX w Twoim produkcie – zgodnie z dostępnymi zasobami."),
        ("(Opcjonalnie) Wsparcie operacyjne", "Jeżeli w danym momencie będzie brakowało „rąk do pracy”, to mogę przejąć operacyjne rzeczy lub przekierować to do mojej agencji."),
    ],
    "casestudy": {"tag": "Case study", "title": "Zarządzanie UX — start-up fintech",
                  "desc": "Czyli o tym jak zarządzałem doświadczeniem klientów w start-upie, który z moją pomocą doszedł do 54 mln finansowania w rok.",
                  "link": ("Przeczytaj to case study", "https://krzysztofmiotk.pl/zarzadzanie-ux-case-study-start-upu-finansowego/")},
})

SERVICES.append({
    "slug": "segmentacja-klientow", "name": "Segmentacja klientów",
    "h1": "Segmentacja klientów",
    "lead": "Zrozum, którzy klienci przynoszą największy zysk i jak o nich zadbać.",
    "intro_h": "Czym jest segmentacja klientów i czym wyróżniają się efekty mojej pracy?",
    "intro_html": (
        "<p>" + md("Segmentacja klientów pozwala na **dobre zrozumienie grupy docelowej i wypracowaniu dla niej działań produktowych i marketingowych.**") + "</p>"
        "<p>" + md("Przy odpowiednim wdrożeniu pozwala **śledzić klientów i projektować ich przejścia na bardziej rentowne archetypy (persony).**") + "</p>"
        "<p>Przy pracy ze mną:</p>"
        "<ol class=\"prose-ol\">"
        "<li>" + md("Wypracujemy (wspólnie) **wskaźniki zachowań ludzi w Twoim produkcie.** Na bazie tego podzielimy ludzi tak, aby firma wiedziała **jak komunikować się do poszczególnych segmentów i jak budować produkt(y) dla nich.**") + "</li>"
        "<li>" + md("Stworzę od zera **szablon segmentu dostosowany do kontekstu Twojej firmy, który uzupełnimy o dane, które zbiorę**. Zero „gotowych wzorców”, które po prostu nie sprawdzają się w biznesie.") + "</li>"
        "<li>" + md("Odkryję bolączki i potrzeby klientów, aby firma wiedziała **jakie wartości przedstawiać klientom** (te wartości też możemy wspólnie wypracować).") + "</li>"
        "<li>" + md("Przeprowadzę **warsztaty**, które pozwolą Twojej firmie **śledzić za pomocą analityki swoich użytkowników tak, aby móc wpływać na ich zachowania** (ponowne zakupy, przejście na segment bardziej rentowny).") + "</li>"
        "</ol>"
    ),
    "process": [
        ("Badania interesariuszy", "Zrozumiem czego potrzebują Twoi pracownicy, aby rozwijać Twój produkt. Na bazie tego zaprojektuję badania klientów."),
        ("Badania jakościowe", "Podczas wywiadów zrozumiem potrzeby i bolączki Twoich klientów. Wypracuję główny podział segmentów."),
        ("Badania ilościowe", "Ten krok ma na celu poznać skalę bolączek, motywacji i wyróżnić znaczące segmenty Twoich klientów."),
        ("Warsztaty wdrożeniowe", "Wykorzystamy zasoby Twojej firmy i wypracujemy plan działań na wykorzystanie segmentów, aby zasilić biznes."),
        ("(Opcjonalnie) Wsparcie wdrożeniowe", "Jeżeli Twój zespół będzie potrzebował dalszego wsparcia merytorycznego lub zasobowego – pomogę."),
    ],
    "casestudy": {"tag": "Case study", "title": "Archetypy behawioralne OLX",
                  "desc": "Stworzenie segmentacji behawioralnej dla OLX. Czyli nowa segmentacja klientów w OLX Group, z której firma była tak zadowolona, że chciała, aby mówiono o niej na konferencjach."},
})

SERVICES.append({
    "slug": "audyt-ux", "name": "Audyt UX",
    "h1": "Audyt UX/UI + WCAG",
    "lead": "Zwiększ konwersję dzięki spojrzeniu na UX w Twoim produkcie **na bazie mojej wiedzy i analityki.** Dostosuj stronę do wymogów EAA i WCAG.",
    "intro_h": "Czym jest audyt UX w moim wykonaniu?",
    "intro_html": (
        "<p>" + md("Audyt UX/UI bierze pod uwagę **kontekst biznesu, rynku**, w którym uczestniczy badany produkt **oraz wzorce projektowe bazujące** na **Heurystykach Nielsena** oraz **naukach kognitywistycznych**.") + "</p>"
        "<p>" + md("**Do całości zostaje dodane moje doświadczenie**, czyli tysiące godzin z różnymi produktami i branżami.") + "</p>"
        "<p>" + md("Dzięki temu mój audyt pozwala **zwiększyć konwersję na wielu etapach, zwiększyć ROI z marketingu, oraz wpłynąć na retencję** (powracalność) obecnych klientów.") + "</p>"
        "<p>" + md("Każdy błąd jest podzielony według **3-stopniowej skali**, co pozwala zarządzić Ci priorytetami zmian (i budżetem). A do tego do każdego błędu otrzymujesz **rekomendację** jak naprawić ten błąd.") + "</p>"
        "<p>Mój proces Audytu UX/UI to:</p>"
        "<ul class=\"checklist\">"
        "<li><svg viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'><path d='M20 6L9 17l-5-5'/></svg> " + md("**Analiza danych historycznych**, np. Google Analytics i HotJar – pozwala wykryć błędy systemu z przeszłości.") + "</li>"
        "<li><svg viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'><path d='M20 6L9 17l-5-5'/></svg> " + md("**Analiza ekspercka** – przechodzimy przez ustalone ścieżki zakupowe i wykrywamy błędy niezgodne z przyjętymi wzorcami – pozwala to wykryć błędy, na które użytkownicy jeszcze nie trafiają.") + "</li>"
        "<li><svg viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'><path d='M20 6L9 17l-5-5'/></svg> " + md("**Analiza WCAG** – aby strona była nie tylko użyteczna, ale też dostępna (więcej osób z niej skorzysta + dostosujesz się do wymogów EAA).") + "</li>"
        "</ul>"
    ),
    "process": [
        ("Omówienie celów biznesowych", "Spotykamy się na videorozmowę i rozmawiamy o Twoim produkcie. Poznaję **kontekst Twojego produktu, ograniczenia technologiczne i możliwości.**"),
        ("Dostęp do danych analitycznych", "Przekazujesz mi dostępy do danych analitycznych Twojego produktu – np. Google Analytics, HotJar/Clarity. Jeżeli nie posiadasz tych narzędzi – powiem Ci jak to dodać przed audytem."),
        ("Sprawdzenie danych historycznych", "Początek audytu zaczynam od danych historycznych – **na bazie udzielonych dostępów wytyczam ścieżki i diagnozuję** w jaki sposób powinien być przeprowadzony audyt."),
        ("Wykorzystanie kognitywistyki i wzorców", "Korzystając z moich doświadczeń, ale też wiedzy o kognitywistyce, heurystykach i wzorcach projektowych wykonuję **audyt ekspercki.** W połączeniu z analityką uzyskujemy **listę błędów.**"),
        ("Priorytetyzacja błędów i rekomendacje", "Każdy błąd ma nadany **poziom, priorytet naprawy (3 stopnie)** i **rekomendacje** – aby Twój zespół mógł rozsądnie zaplanować naprawę."),
        ("Kontrola rezultatów po 3 miesiącach", "To optymalny czas, aby naprawić najważniejsze rzeczy i widzieć rezultaty. **Po 3 miesiącach możesz podziękować sobie** za to, że zaufałeś(-aś) mi przy audycie."),
    ],
    "reasons_h": "Dlaczego warto zrobić audyt UX ze mną?",
    "reasons": [
        ("Ponad 2500 sesji badawczych w kilkudziesięciu firmach", "Jestem doświadczonym moderatorem, który prowadził badania dla zróżnicowanych branż i grup docelowych – od usług bankowych, przez start-upy, aż po usługi offline dla sektora publicznego. **Tę wiedzę wykorzystuję również w audycie dla Ciebie.**"),
        ("Umiejętność przekuwania badań w rozwiązania", "Pracowałem jako Project Manager, a na co dzień jestem konsultantem biznesowym. Nie tylko pozyskuję dane, ale widzę **jak można je przekuć w rozwiązania – zarówno projektowe, jak i strategiczne.**"),
        ("Priorytetyzacja wyników i błędów użyteczności", "Każdy mój raport posiada wskazanie **5-10 najważniejszych** wniosków, które zasilą Twój biznes. Błędy użyteczności dzielę na **3-stopniową skalę, która wskazuje priorytet naprawy**."),
    ],
    "casestudy": {"tag": "Przykładowy projekt", "title": "Raport z Audytu UX/UI sklepu noo.ma",
                  "desc": "Zostaw mail i rzuć okiem na uproszczony raport dla sklepu noo.ma. Oprócz raportu otrzymasz też dostęp do mojego newslettera z unikalnymi treściami.",
                  "link": ("Chcę raport", "kontakt.html")},
})

SERVICES.append({
    "slug": "konsultacje-i-mentoring", "name": "Konsultacje i mentoring",
    "h1": "Konsultacje i mentoring",
    "lead": "Indywidualnie przedyskutuj rzeczy lub podnieś swoje kompetencje w UX.",
    "intro_h": "Jaka jest różnica między mentoringiem i konsultacjami?",
    "intro_html": (
        "<p>" + md("Konsultacje to **pojedyncze spotkania** (może być to seria pojedynczych spotkań), gdzie omawiasz swój problem – w **produkcie**, w **karierze** lub w życiu (syndrom oszusta dotyka nie tylko w karierze 🙂).") + "</p>"
        "<p>Czyli jeżeli potrzebujesz zbić myśli lub przedyskutować problem – to widzimy się na konsultacjach.</p>"
        "<h3>No to czym jest Mentoring?</h3>"
        "<p>" + md("Mentoring jest **procesem i relacją**. Na podstawie Twoich celów wyznaczamy proces pt.: „Jak to osiągnąć?” – a następnie realizujemy. Ważna jest tutaj **cykliczność spotkań i obustronne zaufanie** przy rozmowach.") + "</p>"
        "<p>Dlatego nie obraź się – ale nie z każdą osobą zgadzam się na mentoring.</p>"
    ),
    "process_h": "Jak wygląda proces mentoringu?",
    "process": [
        ("Wyznaczenie Twojego celu", "Prawdopodobnie przychodzisz z jakimś **problemem** lub **celem**. W obu przypadkach musimy skończyć nasze pierwsze spotkanie na celu. Bo to on będzie naszą „**Gwiazdą polarną**”."),
        ("Zaprojektowanie procesu rozwoju", "Na podstawie celu wyznaczamy proces dotarcia do niego – pozwoli nam to określić **liczbę potrzebnych spotkań i tematów**, które musimy omówić. Ten krok możemy zrobić na spotkaniu lub asynchronicznie."),
        ("Spotkania 1:1 i Twoja praca indywidualna", "Zgodnie z planem realizujemy spotkania 1:1, a Ty wykonujesz (czasem) zadania pomiędzy sesjami. Co 25% procesu robimy status, gdzie sprawdzamy czy idziemy zgodnie z celem."),
        ("Zostajemy w kontakcie", "Właściwie z każdą mentorowaną osobą mamy kontakt choć raz na jakiś czas. Utrzymujemy relacje po zakończonym mentoringu – już bez korzyści biznesowych 🙂"),
    ],
    "casestudy": {"tag": "Historia", "title": "Jak Magda zmieniła swoją karierę po kilkunastu latach w marketingu",
                  "desc": "Po pół roku mentoringu została badaczką UX w banku."},
})

SERVICES.append({
    "slug": "wystapienia-i-szkolenia", "name": "Wystąpienia i szkolenia",
    "h1": "Wystąpienia i szkolenia",
    "lead": "Zaproś mnie na konferencję lub podnieś kompetencje swojego zespołu.",
    "intro_h": "Wystąpienia, warsztaty i szkolenia z UX",
    "intro_html": (
        "<p>Występuję na konferencjach i prowadzę szkolenia z badań UX oraz wartości badań dla biznesu. "
        "Po wystąpieniach w 2023 roku przylgnął do mnie przydomek „UX Wiedźmin”. Współtworzę też „UX po Godzinach” – najstarszy aktywny podcast o UX w Polsce.</p>"
        "<p>Napisz, jaki temat i poziom zaawansowania Cię interesuje – przygotuję autorskie wystąpienie lub warsztat dopasowany do Twojego zespołu.</p>"
    ),
})


for s in SERVICES:
    service_page(s)


# ===========================================================================
#  USŁUGI — hub
# ===========================================================================
def hub_cards():
    cards = ""
    for slug, label in SERVICE_NAV:
        ico = ICONS[slug]
        cards += f'''      <a href="{slug}.html" class="card">
        <div class="ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{ico}</svg></div>
        <h3>{label}</h3>
        <p>{TAGLINES[slug]}</p>
        <span class="card-foot link-arrow">Zobacz usługę {ARROW}</span>
      </a>\n'''
    return cards


uslugi_body = f'''
<section class="page-hero">
  <div class="wrap">
    <p class="breadcrumbs"><a href="index.html">Start</a><span>/</span>Usługi</p>
    <p class="eyebrow">Usługi</p>
    <h1 style="max-width:18ch; margin-top:.6rem">Wsparcie UX dopasowane do <span class="uline">etapu Twojego produktu</span></h1>
    <p class="lead">Od pojedynczych badań, przez audyty i segmentację, po stałe przywództwo UX. Wybierz usługę, aby przeczytać szczegóły i przykładowe wdrożenie.</p>
  </div>
</section>

<section class="section--tight">
  <div class="wrap">
    <div class="grid grid-3 reveal">
{hub_cards()}    </div>
    <div class="center" style="margin-top:2.5rem">
      <a href="kontakt.html" class="btn btn--primary btn--lg">Umów videorozmowę {ARROW}</a>
    </div>
  </div>
</section>

<section class="section--tight center">
  <div class="wrap"><p class="motto">„{MOTTO}"</p></div>
</section>'''

write("uslugi.html", "Usługi — Krzysztof Miotk",
      "Usługi UX: Badania UX, Zewnętrzny Dyrektor UX, Segmentacja klientów, Audyt UX, Konsultacje i mentoring, Wystąpienia i szkolenia.",
      "uslugi", uslugi_body)


# ===========================================================================
#  KONTAKT (1:1)
# ===========================================================================
brief_options = ["Nie wiem. Potrzebuję pomocy z wyborem.", "Badanie UX", "Audyt UX",
                 "Zewnętrzny Dyrektor UX", "Wystąpienie", "Szkolenie", "Konsultacja",
                 "Mentoring", "Inna usługa UX", "Złożony projekt"]
brief_select = "".join(f"            <option>{o}</option>\n" for o in brief_options)

kontakt_body = f'''
<section class="page-hero">
  <div class="wrap">
    <p class="breadcrumbs"><a href="index.html">Start</a><span>/</span>Kontakt</p>
    <p class="eyebrow">Kontakt</p>
    <h1 style="max-width:14ch; margin-top:.6rem">Porozmawiajmy</h1>
    <p class="lead">Lubię kontakt twarzą w twarz, więc wrzuć w mój kalendarz spotkanie i zobaczmy co dobrego możemy wspólnie zrobić 🙂</p>
    <div class="hero-cta" style="margin-top:1.6rem">
      <a href="#kalendarz" class="btn btn--primary btn--lg">Umów videorozmowę {ARROW}</a>
      <a href="#kontakt" class="btn btn--ghost btn--lg">Napisz wiadomość</a>
      <a href="#brief" class="btn btn--ghost btn--lg">Wyceń projekt</a>
    </div>
  </div>
</section>

<section class="section--tight" id="kalendarz">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">Kalendarz</p>
      <h2>Wrzuć spotkanie w mój kalendarz</h2>
      <p class="lead">Wybierz dogodny termin na bezpłatną videorozmowę — porozmawiamy o Twoim produkcie i celu.</p>
    </div>
    <div id="calendar-embed" class="reveal"></div>
  </div>
</section>

<section class="section--tight" id="kontakt">
  <div class="wrap split">
    <div class="reveal">
      <h2 class="mb-2">Umów rozmowę lub napisz do mnie</h2>
      <form data-form data-subject="Kontakt ze strony — Krzysztof Miotk" class="card" style="padding:clamp(24px,3vw,36px)">
        <div class="field"><label for="k-name">Imię *</label><input id="k-name" name="imie" type="text" required placeholder="Twoje imię" /></div>
        <div class="field"><label for="k-email">Adres e-mail *</label><input id="k-email" name="email" type="email" required placeholder="jan@firma.pl" /></div>
        <div class="field"><label for="k-www">Twoja strona www / nazwa aplikacji</label><input id="k-www" name="www" type="text" placeholder="np. twojadomena.pl" /></div>
        <div class="field"><label for="k-msg">W czym mogę Ci pomóc? *</label><textarea id="k-msg" name="wiadomosc" required placeholder="Opisz krótko swój produkt i wyzwanie..."></textarea></div>
        <button type="submit" class="btn btn--primary btn--lg btn--block">Wyślij {ARROW}</button>
        <p class="small muted" data-note style="margin-top:.9rem; font-size:.85rem">Wysyłając formularz, akceptujesz <a href="polityka-prywatnosci.html">politykę prywatności</a>.</p>
      </form>
    </div>
    <aside class="reveal">
      <div class="sidecard">
        <h4>Bezpośredni kontakt</h4>
        <p class="muted" style="font-size:.95rem; margin:.5rem 0 1.2rem">Wolisz napisać od razu? Odpowiadam na każdą wiadomość.</p>
        <ul class="checklist">
          <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6L9 17l-5-5"/></svg> <a href="mailto:krzysiek@quale.agency" style="color:var(--brand);font-weight:600">krzysiek@quale.agency</a></li>
          <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6L9 17l-5-5"/></svg> Videorozmowa — wrzuć spotkanie w mój kalendarz</li>
          <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6L9 17l-5-5"/></svg> Wycena briefu w ciągu 24h</li>
        </ul>
      </div>
      <div class="sidecard" style="margin-top:1rem; background:var(--brand-light); border-color:transparent">
        <span class="pill" style="background:#fff">Quale UX</span>
        <p style="margin-top:.8rem; color:var(--brand-deep); font-weight:600">Działam w ramach Quale — agencji UX research &amp; strategy.</p>
        <a href="https://quale.agency" target="_blank" rel="noopener" class="link-arrow" style="margin-top:.6rem">quale.agency {ARROW}</a>
      </div>
    </aside>
  </div>
</section>

<section class="section section--soft" id="brief">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">Brief</p>
      <h2>Chcesz otrzymać wycenę bez spotkania?</h2>
      <p class="lead">Uzupełnij uproszczony brief, a otrzymasz orientacyjną wycenę <strong>w ciągu 24h!</strong></p>
    </div>
    <form data-form data-subject="Brief / wycena — Krzysztof Miotk" class="card reveal" style="padding:clamp(24px,3vw,36px); max-width:760px">
      <div class="grid grid-2" style="gap:0 1.2rem">
        <div class="field"><label for="b-name">Imię i nazwisko *</label><input id="b-name" name="imie_nazwisko" type="text" required /></div>
        <div class="field"><label for="b-email">Adres e-mail *</label><input id="b-email" name="email" type="email" required /></div>
        <div class="field"><label for="b-role">Twoje stanowisko</label><input id="b-role" name="stanowisko" type="text" /></div>
        <div class="field"><label for="b-service">Jaką usługę rozważasz?</label>
          <select id="b-service" name="usluga">
{brief_select}          </select>
        </div>
      </div>
      <div class="field"><label for="b-product">O jaki produkt / usługę / firmę chodzi?</label><input id="b-product" name="produkt" type="text" /></div>
      <div class="field"><label for="b-goal">Cel biznesowy</label><input id="b-goal" name="cel_biznesowy" type="text" /></div>
      <div class="field"><label for="b-target">Grupa docelowa</label><input id="b-target" name="grupa_docelowa" type="text" /></div>
      <div class="field"><label for="b-other">Inne przydatne informacje</label><textarea id="b-other" name="inne"></textarea></div>
      <button type="submit" class="btn btn--dark btn--lg btn--block">Prześlij {ARROW}</button>
      <p class="small muted" data-note style="margin-top:.9rem; font-size:.85rem">Możesz się wypisać kiedy chcesz. Więcej informacji w <a href="polityka-prywatnosci.html">polityce prywatności</a>.</p>
    </form>
  </div>
</section>

<section class="section--tight center">
  <div class="wrap"><p class="motto">„{MOTTO}"</p></div>
</section>'''

write("kontakt.html", "Kontakt — Krzysztof Miotk",
      "Porozmawiajmy — umów videorozmowę lub wypełnij brief i otrzymaj wycenę w ciągu 24h. krzysiek@quale.agency",
      "kontakt", kontakt_body)

# ===========================================================================
#  POLITYKA PRYWATNOŚCI (RODO)
# ===========================================================================
polityka_body = f'''
<section class="page-hero">
  <div class="wrap">
    <p class="breadcrumbs"><a href="index.html">Start</a><span>/</span>Polityka prywatności</p>
    <h1 style="margin-top:.4rem">Polityka prywatności</h1>
    <p class="lead">Zasady przetwarzania danych osobowych oraz wykorzystania plików cookies w serwisie krzysztofmiotk.pl.</p>
  </div>
</section>

<section class="section--tight">
  <div class="wrap legal reveal">
    <p class="note">Ten dokument jest wzorem przygotowanym pod ten serwis. Przed publikacją uzupełnij dane administratora (pełna nazwa działalności, NIP, adres) i — jeśli używasz analityki lub newslettera — dopisz konkretne narzędzia i ich dostawców.</p>

    <h2>1. Administrator danych</h2>
    <p>Administratorem Twoich danych osobowych jest Krzysztof Miotk, prowadzący działalność pod adresem e-mail <a href="mailto:krzysiek@quale.agency">krzysiek@quale.agency</a> (dalej „Administrator”). Dane rejestrowe: <strong>[pełna nazwa działalności]</strong>, NIP <strong>[NIP]</strong>, adres <strong>[adres]</strong>.</p>

    <h2>2. Jakie dane zbieram</h2>
    <p>Przetwarzam dane, które samodzielnie podajesz w formularzach na stronie:</p>
    <ul>
      <li><strong>Formularz kontaktowy:</strong> imię, adres e-mail, opcjonalnie adres strony/aplikacji oraz treść wiadomości.</li>
      <li><strong>Brief / wycena:</strong> imię i nazwisko, adres e-mail, stanowisko oraz informacje o produkcie i celu biznesowym.</li>
      <li><strong>Newsletter:</strong> adres e-mail (jeśli zapiszesz się do newslettera).</li>
      <li><strong>Dane techniczne:</strong> informacje zbierane automatycznie przez pliki cookies (patrz pkt 5).</li>
    </ul>

    <h2>3. Cele i podstawy prawne przetwarzania</h2>
    <ul>
      <li>Odpowiedź na zapytanie i obsługa kontaktu — art. 6 ust. 1 lit. b oraz f RODO (podjęcie działań na żądanie / uzasadniony interes Administratora).</li>
      <li>Przygotowanie wyceny i ewentualne zawarcie umowy — art. 6 ust. 1 lit. b RODO.</li>
      <li>Wysyłka newslettera — art. 6 ust. 1 lit. a RODO (Twoja zgoda), którą możesz w każdej chwili wycofać.</li>
      <li>Zapewnienie poprawnego działania serwisu — art. 6 ust. 1 lit. f RODO.</li>
    </ul>

    <h2>4. Dobrowolność podania danych</h2>
    <p>Podanie danych jest dobrowolne, ale niezbędne do wysłania zapytania, otrzymania wyceny lub newslettera. Bez nich nie będę w stanie odpowiedzieć na Twoją wiadomość.</p>

    <h2>5. Pliki cookies</h2>
    <p>Serwis korzysta z plików cookies niezbędnych do jego prawidłowego działania (m.in. zapamiętanie zgody na cookies). Jeżeli w przyszłości zostaną dodane narzędzia analityczne lub marketingowe (np. Google Analytics), zostaną one uruchomione dopiero po wyrażeniu zgody, a niniejsza polityka zostanie zaktualizowana o ich dostawców i okresy przechowywania. Ustawienia cookies możesz zmienić w swojej przeglądarce.</p>

    <h2>6. Odbiorcy danych</h2>
    <p>Twoje dane mogą być powierzone zaufanym podmiotom wspierającym działanie serwisu, w szczególności: dostawcy hostingu, dostawcy usługi obsługi formularzy (np. Formspree), dostawcy kalendarza rezerwacji (np. Calendly / Cal.com) oraz dostawcy narzędzia do newslettera — wyłącznie w zakresie niezbędnym do realizacji powyższych celów.</p>

    <h2>7. Okres przechowywania</h2>
    <p>Dane z korespondencji przechowuję przez czas niezbędny do obsługi sprawy oraz przez okres przedawnienia ewentualnych roszczeń. Dane przetwarzane na podstawie zgody (newsletter) — do czasu jej wycofania.</p>

    <h2>8. Twoje prawa</h2>
    <p>Masz prawo do: dostępu do danych, ich sprostowania, usunięcia, ograniczenia przetwarzania, przenoszenia danych, wniesienia sprzeciwu oraz cofnięcia zgody w dowolnym momencie. Przysługuje Ci również prawo wniesienia skargi do Prezesa Urzędu Ochrony Danych Osobowych (UODO).</p>

    <h2>9. Kontakt</h2>
    <p>We wszystkich sprawach dotyczących danych osobowych napisz na: <a href="mailto:krzysiek@quale.agency">krzysiek@quale.agency</a>.</p>

    <p class="muted" style="margin-top:2rem; font-size:.9rem">Ostatnia aktualizacja: 2026. Dokument może być aktualizowany wraz z rozwojem serwisu.</p>
  </div>
</section>'''

write("polityka-prywatnosci.html", "Polityka prywatności — Krzysztof Miotk",
      "Zasady przetwarzania danych osobowych i wykorzystania plików cookies w serwisie krzysztofmiotk.pl.",
      "", polityka_body)

print("\\nGotowe — podstrony 1:1 wygenerowane.")
