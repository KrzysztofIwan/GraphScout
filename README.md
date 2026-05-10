# GraphScout

## Opis projektu
GraphScout to inteligentny asystent wykorzystujący modele AI do analizy i nawigacji po szlakach górskich przedstawionych w formie grafu. Projekt umożliwia interaktywne planowanie tras oraz eksplorację połączeń terenowych poprzez naturalną rozmowę z modelem językowym.

Projekt skupia się w obecnej chwili nad nawigacją po Tatrach Polskich, *oraz jest w fazie rozwojowej co oznacza że może popełniać błędy.* **Zawsze należy dodatkowo sprawdzić poprawność danych aby wykluczyć możliwe halucynajce**.

## Główne funkcjonalności
* **Reprezentacja grafowa:** Szlaki górskie i szczyty zapisane jako węzły i krawędzie.
* **Interfejs konwersacyjny:** Intuicyjny chat ułatwiający wyszukiwanie optymalnych dróg.
* **Analiza topologii:** Wykorzystanie algorytmu A* do wyszukania najlepszej ścieżki.
* **Pogoda:** Połączenie z OpenMeteoAPI do informowania o możliwych zmianach pogodowych.
* **Interface:** Zaprojektowany za pomocą biblioteki streamlit.

## Użyte technologie
* Python 3.13.5 - język bazowy
* streamlit 1.56.0 - forntend aplikacji
* networkx 3.6.1 - budownaie grafu prezentującego mape szlaków
* Requests - obsługa zapytań z openMeteoAPI
* JSON - przetwarzanie struktur danych z API, odczyt konfiguracji

## Struktura projektu
* `.vscode/` - Konfiguracja dla debugu
* `config/` - Konfiguracja z APIs.
* `src/` – Logika grafu oraz integracja z modelem AI.
    * `pathfinder/` - Algorytmy wyszukiwania najlepszej ścieżki w grafie.
* `data/` – Dane o szlakach i połączeniach.
    * `trails/` - Szlaki zapisane w formacie JSON.
    * `visualizations/` - Wizualizacje całego grafu szlaków w formie grafu.
* `tests/` - Testy jednostkowe.
* `main.py` – Główny punkt wejścia do aplikacji.

## Uruchomienie
Zainstalowanie wszystkich potrzebnych bibliotek 
```bash
pip install -r requirements.txt
```

Dodanie do pliku `/config/geminie_api.json` swojego klucza do autoryzacji w pole `api_key`


Uruchomienie projektu z terminala 
```bash
streamlit run main.py'
```
