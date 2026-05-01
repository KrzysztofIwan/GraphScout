# GraphScout

## Opis projektu
GraphScout to inteligentny asystent wykorzystujący modele AI do analizy i nawigacji po szlakach górskich przedstawionych w formie grafu. Projekt umożliwia interaktywne planowanie tras oraz eksplorację połączeń terenowych poprzez naturalną rozmowę z modelem językowym.

Projekt skupia się w obecnej chwili nad nawigacją po Tatrach Polskich.

## Główne funkcjonalności
* **Reprezentacja grafowa:** Szlaki górskie i szczyty zapisane jako węzły i krawędzie.
* **Interfejs konwersacyjny:** Intuicyjny chat ułatwiający wyszukiwanie optymalnych dróg.
* **Analiza topologii:** Wykorzystanie algorytmu A* do wyszukania najlepszej ścieżki.
* **Interface:** Zaprojektowany za pomocą biblioteki strealit.

## Użyte technologie
TODO

## Struktura projektu
* `.vscode/` - Konfiguracja dla debugu
* `config/` - Konfiguracja z APIs.
* `src/` – Logika grafu oraz integracja z modelem AI.
    * `pathfinder/` - Algorytmy wyszukiwania najlepszej ścieżki w grafie.
* `data/` – Dane o szlakach i połączeniach.
    * `trails/` - Szlaki zapisane w formacie JSON.
    * `visualizations/` - Wizualizacje całego grafu który tworzymy.
* `tests/` - Testy jednostkowe.
* `main.py` – Główny punkt wejścia do aplikacji.

## Uruchomienie
Zainstalowanie wszystkich potrzebnych bibliotek 
```bash
pip install -r requirements.txt
```

Uruchomienie projektu z terminala 
```bash
streamlit run main.py'
```