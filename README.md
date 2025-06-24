# Zber údajov o knižniciach
Tento projekt automaticky sťahuje údaje o mestských knižniciach v Českej republike pomocou Golemio API a ukladá ich do CSV súboru.
## 📌Ako skripty fungujú?
1. **Prvý skript**: Získa údaje o knižniciach cez Golemio API, spracuje ich a uloží do súboru `kniznice.csv`.
2. **Druhý skript**: Vytvorí úlohu v Plánovači úloh Windows, ktorá spustí prvý skript každý deň o 7:00 ráno.
## 🛠 Nastavenie
1. **Treba inštalácia Pythonu**(verziu 3.8 alebo novšiu)
2. **Treba knižnice**:
   ```bash
   pip install requests pandas
