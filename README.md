# Krzysztof Miotk — strona (propozycja w brandingu QUALE)

Statyczna, wielostronicowa witryna UX Researchera Krzysztofa Miotka, zaprojektowana spójnie z [quale.agency](https://quale.agency) i brandingiem QUALE (fonty Hanken Grotesk / Inter / Geist Mono, fiolet marki, ostre narożniki, logotyp „Krzysztof Miotk").

## Strony (struktura 1:1 z krzysztofmiotk.pl)
`index.html` · `uslugi.html` (hub) + 6 podstron usług (Badania UX, Zewnętrzny Dyrektor UX, Segmentacja klientów, Audyt UX, Konsultacje i mentoring, Wystąpienia i szkolenia) · `kontakt.html`

Nawigacja: **Usługi** (rozwijane menu) + **Kontakt**.

## Podgląd lokalny
Bez serwera — otwórz `index.html` w przeglądarce. Albo:

```bash
python3 serve.py 8080   # http://localhost:8080
```

## Struktura
- `css/styles.css` — system designu (tokeny brandingu QUALE)
- `js/main.js` — menu mobilne, filtr Insights, animacje
- `assets/` — logo (SVG) i zdjęcia
- `build.py` — generator podstron (wspólny header/stopka)

Formularze są w wersji demonstracyjnej (bez backendu).
