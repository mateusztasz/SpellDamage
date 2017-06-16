# Spell Damage

## Opis
Celem aplikacji jest obliczenie poziomu uszkodzenia tekstu.

## Typ danych wejściowych
Napis (string). Napis powinien zaczynać się od `'fe'` i kończyć `'ai'`.
 W środku sylaby które powiększają uszkodzenie to
`'dai'`
`'jee'`
`'ain'`
`'je'`
`'ne'`
`'ai'`.
Inne literały obniżają wartość uszkodzenia. Wartość uszkodzenia dla każdego literału można znaleźć w kodzie. Ta informacja jest przechowywany w słowniku: `globalSubspells`.

## Sposób użycia modułu
```python
from task2 import  damage

print(damage('feaineain'))
```

## Uruchomienie aplikacji
```
python task2.py
```
## Uruchomienie testów
```
python -m unittest
```
