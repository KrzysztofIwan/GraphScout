# GraphScout

## Opis projektu
GraphScout to inteligentny asystent wykorzystujący modele AI do analizy i nawigacji po szlakach górskich przedstawionych w formie grafu. Projekt umożliwia interaktywne planowanie tras oraz eksplorację połączeń terenowych poprzez naturalną rozmowę z modelem językowym.

Projekt skupia się w obecnej chwili nad nawigacją po Tatrach Polskich.

## Główne funkcjonalności
* **Reprezentacja grafowa:** Szlaki górskie i szczyty zapisane jako węzły i krawędzie.
* **Interfejs konwersacyjny:** Intuicyjny chat ułatwiający wyszukiwanie optymalnych dróg.
* **Analiza topologii:** Wykorzystanie algorytmów grafowych do nawigacji w trudnym terenie.

## Struktura projektu
* `config/` - Konfiguracja z API.
* `src/` – Logika grafu oraz integracja z modelem AI.
* `data/` – Dane o szlakach i połączeniach.
    * `trails/` - Szlaki zapisane w formacie JSON.
    * `visualizations/` - Wizualizacje całego grafu który tworzymy.
* `main.py` – Główny punkt wejścia do aplikacji.