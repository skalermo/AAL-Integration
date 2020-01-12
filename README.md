# AAL-Integration

Roman Moskalenko, 295136

## Treść polecenia

#### Integracja

Pracownicy wielkiego zakładu produkcyjnego wyjeżdżają na wyjazd integracyjny 
w kiku turnusach. Dział HR chce, aby jego trakcie pracownicy lepiej się poznali, 
dlatego w jednym turnusie będą uczestniczyły osoby, które się wcześniej nie znały. 
Mając dane informacje, mówiące o tym które osoby się znają, zaproponować algorytm, 
który wyznaczy minimalną liczbę potrzebnych turnusów, oraz dokona przydziału 
pracowników.

## Tryby wykonania

Program uruchamiany jest za pomocą polecenia `python Main.py` z odpowiednimi
parametrami. Dodatkowo za pomocą argumentu `-g` można graficznie przedstawić rozwiązanie.

1. `m1` - Dane dostarczane ze strumienia wejściowego (standardowego lub pliku)

    **Przykład**: wczytanie grafu z pliku *input.txt* i wypisanie wyników na standardowe
    wyjście:
    
        python Main.py m1 < input.txt
        
    Argument `-b` wymusi użycie algorytmu Brute force do znalezienia kolorowania.

2. `m2` - Dane generowane automatycznie (losowo) z możliwością
parametryzacji generacji określaną przez użytkownika

    Opis argumentów dla generowania grafu:
    
    - `-n` *Liczba wierzchołków* w grafie
    
    - `-d` *Gęstość grafu* - stosunek liczby krawędzi w grafie do wygenerowania do
           liczby krawędzi w grafie N-pełnym
           
    - `-k` *Dzielność grafu*. Wygenerowany graf będzie k-dzielny
    
    - `-p` *Ręczny podział grafu* w przypadku podania argumentu `-k`. Argumentem jest
    lista list z wierzchołkami grafu
    
    - `-s` `--seed` Inicjowanie objektu `Random` podaną wartością. Zapewnia
    wygenerowanie tych samych danych dla powtarzających wartości
    
    - `-b` Wymuszenie użycia algorytmu Brute force do znalezienia kolorowania.
    
    **Przykład**: wygenerowanie 3-dzielnego grafu o liczbie wierzchołków rownej 150, 
    gęstości 0.75. Ręczny podział grafu jak i podanie wartości seed jest opcjonalne.
    Wynik dziłania jest przekierowany do pliku output.txt
    
        python Main m2 -n 150 -d 0.75 -k 3 > output.txt
        
3. `m3` - Wykonanie z generacją danych, pomiarem czasu i prezentacją 
wyników pomiarów.

    Opis argumentów:
    
    - `-w` Użycie algorytmu WelshPowell
    
    - `-b` Użycie algorytmu Brute force
    
    - `-n`, `-d`, `-k` podobnie jak dla `m2`
    
    - `-c` *Liczba problemów* do rozwiązania
    
    - `-s` `-step` *Krok* - opisuje jak zmienia się wielkość danych w problemie
    w stosunku do poprzedniego
    
    - `-r` *Liczba wygenerowanych instancji* problemu
    
    - `-f` Zapisywanie tymczasowych wyników pomiarów do pliku .results
    
    Nie jest przewidziane użycie argumentów `-w` i `-b` naraz.
    
    **Przykład**: pomiar czasu dla 30 problemów o wielkościach 
    1000, 1500, 2000 itd. Gęstość generowanych grafów - 0.5. Dla każdej wielkości
    losowanych 10 instancji problemu. Wyniki podać w postaci tabeli.
    
        python Main m3 -w -n 1000 -d 0.5 -c 30 -s 500 -r 10 > table.md
    
    **Uwaga**: wynik jest sformatowany dla wyświetlania w postaci `.md` (markdown)
    
## Dane wejściowe i prezentacja wyników

Program przyjmuje dane wejściowe sformatowane w postaci `.json`. Najwygodniej jest
używać generatoru grafów `GraphGen.py` gdyż wygenerowane przez niego grafy są w
tej postaci.

Wyniki działania programu (kolorowanie i liczba zużytych kolorów) są podawane na
standardowym wyjściu. 

Wyniki pomiarów czasu wykonania są podawane na standardowym wyjściu w postaci `.md`

## Krótki opis rozwiązania

- Struktura danych

    Dla rozwiązania problemu stworzono klasę grafu `Graph`. Zawiera ona słownik
    (dictionary), gdzie jako klucze występują wierzchołki grafu, wartościom
    odpowiadają listy sąsiadów odpowiednio dla każdego wierzchołku. Klasa ta posiada
    metody dla dodawania/usuwania wierchołków/krawędzi etc
    
- Zastosowane algorytmy
    
    *Brute force* - poszukiwanie wśród wszystkich możliwych kolorowań właściwe.
    
    *Algorytm Bron-Kerbosch* - znajdowanie w grafie największej kliki, przydaje się
    do oszacowanie granicy dolnej algorytmu *Brute force*
    
    *Altorytm Welsh-Powell* - heurtyczny algorytm do zachłannego pokolorowania
    grafu
    
## "Przewodnik" po plikach źródłowych

- `Main.py` odpowiada za parsowanie argumentów i przyjmowanie danych wejściowych
oraz wypisywanie wyników

- `IOHandling.py` zawiera funkcje do odczytywania i zapisywania plików .json
oraz wypisuje wyniki pomiarów czasowych

- `Graph.py` zawiera implementacje klasy grafu

- `GraphGen.py` generuje grafy o zadanych parametrach. Jest możliwość uruchomienia
bezpośrednio tego pliku dla wygenerowania i zapisania grafu do pliku

- `Algorithms.py` zawiera implementacje wspomnianych wyżej algorytmów, oraz funkcji
pomocniczych

- `Benchmark.py` odpowiada za przeprowadzenie pomiarów czasu wykonania algorytmów
i przekazanie wyników do `IOHandling.py` dla dalszego wyświetlenia. Przy bezpośrednim
uruchomieniu tego skryptu ładuje dane z pliku .results o ile istnieje, przetwarza i przekazuje je
dalej jak opisano wyżej.

- `DrawUtils.py` umożliwia rysowanie grafu i rozwiązania. Wymaga spełnienia zależności opisanych
w pliku `requirements.txt`.
