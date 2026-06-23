#!/bin/bash
# Dwuklik uruchamia lokalny serwer strony Krzysztof Miotk.
# Zostaw to okno Terminala otwarte. Zamknięcie okna zatrzyma serwer.
cd "$(dirname "$0")"
PORT=8080
echo "============================================================"
echo "  Strona Krzysztof Miotk — serwer lokalny"
echo "  Otwórz w przeglądarce:  http://localhost:$PORT"
echo "  Zatrzymanie: zamknij to okno lub naciśnij Ctrl+C"
echo "============================================================"
# zwolnij port, jeśli zajęty
lsof -ti tcp:$PORT | xargs kill -9 2>/dev/null
sleep 1
# otwórz przeglądarkę po chwili
( sleep 2; open "http://localhost:$PORT" ) &
python3 serve.py $PORT
