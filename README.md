# GraphScout

## Opis projektu
GraphScout to inteligentny asystent wykorzystujący modele AI do analizy i nawigacji po szlakach górskich przedstawionych w formie grafu. Projekt umożliwia interaktywne planowanie tras oraz eksplorację połączeń terenowych poprzez naturalną rozmowę z modelem językowym.

Projekt skupia się w obecnej chwili nad nawigacją po Tatrach Polskich, *oraz jest w fazie rozwojowej co oznacza że może popełniać błędy.* **Zawsze należy dodatkowo sprawdzić poprawność danych aby wykluczyć możliwe halucynajce**.

### Planowany rozwój aplikacji
* Dodanie możliwości wyboru przez użytkownika modelu z jakiego chce korzystać np. (Olama, Gpt, Gemini)
* Przechowywanie informacji w bazie danych (SQLite)
* Rozbudowa informacji o ścieżce o informacje o podłoży, aby rozważyć czy szlak nadaje się dla osób z dziećmi, osób niepełnosprawnych itd.
* Opracowanie mechanizmu kategoryzacji wysiłku na szlaku za pomocą punktów GOT
* Dodanie rang użytkowników które pomogą w wyznaczaniu odpowiednich szlaków, rangi poniżej:
  *   Spacerowicz Dolny
  *   Turysta tatrzański
  *   Turysta wysokogórski
  *   Taternik
* Dodanie połączenia z OSM w celu zwracania użytkowniką informacji i parkingach
* Dodanie autentykacji użytkowników

## Główne funkcjonalności
* **Reprezentacja grafowa:** Szlaki górskie i szczyty zapisane jako węzły i krawędzie.
* **Interfejs konwersacyjny:** Intuicyjny chat ułatwiający wyszukiwanie optymalnych dróg.
* **Analiza topologii:** Wykorzystanie algorytmu A* do wyszukania najlepszej ścieżki.
* **Pogoda:** Połączenie z OpenMeteoAPI do informowania o możliwych zmianach pogodowych.
* **Interface:** Zaprojektowany za pomocą biblioteki streamlit.

### Reprezentacja szlaków
---
Szkalki górskie są implementowane za pomocą dokumentów w formacie JSON, poniżej została opisana implementacja danych.

Punkty na mapie:
```json
{
  "nodes": [
        {
            "id": "Kuznice", #nazwa punktu
            "elevation": 1010, #wysokość nad poziomem moża
            "lat": 49.2694, #szerokość geograficzna
            "lon": 19.9806, #długość geograficzna
            "type": "parking" #typ punktu
        }
    ]
}
```
Typy szlaków ich znaczenie:
```json
{
   "summit" : "Szczyt",
   "shelter" : "Schronisko",
   "parking" : "Punkt od którego rozpoczyna się szlak",
   "pass" : "Szlak połączeniowy pomiędzy punktem A i B"
   "junction" : "Szlak któy łączy się z wieloa innymi szlakami"
}
```
Węzły pomiędzy punktami:
```json
{
    "links": [
        {
            "source":"Odejscie_na_Nosalowa_Przelecz", #punkt1
            "target": "Przelecz_miedzy_Kopami", #punkt2
            "time_forward": 90, #czas w minutach z punktu1 -> punktu2
            "time_backward": 65, #czas w minutach z punktu2 -> punktu1
            "distance_km": 2.8, #dystans pomiędzy punktami w km
            "difficulty": 2, #stopień zaawansowania szlaku
            "color": "blue", #kolor szlaku
            "winter_closure" : false #czy szlak zamnięty na zime
        }
    ]
}
```

### Obsługa danych pogodowych
---
* **Prognoza z wyprzedzeniem:** API dostarcza dane pogodowe z wyprzedzeniem 8 godzin.
* **Formatowanie danych:** Surowe informacje o pogodzie są przetwarzane i modyfikowane tak, aby były w pełni czytelne i zrozumiałe dla użytkownika końcowego.
* **Mapowanie kodów pogodowych:** Tekstowe opisy stanów pogodowych są mapowane na podstawie kodów zapisanych w pliku konfiguracyjnym `config/weather_code.json`.

## Użyte technologie
* Python 3.13.5 - język bazowy
* streamlit 1.56.0 - forntend aplikacji
* google-genai 1.69 - integracja z Gemini API
* pandas 3.0.2 - analiza oraz strukturyzacja danych
* pydantic 2.12.5 - wlidacja danych
* networkx 3.6.1 - budownaie grafu prezentującego mape szlaków
* Requests - obsługa zapytań z openMeteoAPI
* JSON - przetwarzanie struktur danych z API, odczyt konfiguracji

## Struktura projektu
* `.vscode/` - Konfiguracja dla debugu
* `config/` - Konfiguracja z APIs.
* `src/` – Logika aplikacji.
    * `pathfinder/` - Algorytmy wyszukiwania najlepszej ścieżki w grafie.
    * `views/` - Strony oraz podstrony aplikacji.
    * `helpers/` - Metody pomocniczne.
* `data/` – Dane o szlakach i połączeniach.
    * `trails/` - Szlaki zapisane w formacie JSON.
    * `visualizations/` - Wizualizacje całego grafu szlaków w formie grafu.
* `tests/` - Testy jednostkowe.
* `main.py` – Główny punkt wejścia do aplikacji.

## Uruchomienie
Zainstalowanie wszystkich potrzebnych bibliotek:
```bash
pip install -r requirements.txt
```

Dodanie do pliku `/config/geminie_api.json` swojego klucza do autoryzacji w pole `api_key`, na potrzeby działania aplikacji w formie demo zostawiam swój klucz. Można wykonywać 5 zapytań na minute, po przekroczeniu limitu token zostanie zablokowany.


Uruchomienie projektu z terminala:
```bash
streamlit run main.py
```
