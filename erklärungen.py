# ### Grundaufbau Programm
# ggf. Module importiert z.B. random, math, ...
# Funktionen definieren
# restliches Programm inklusive Aufruf von Funktionen


# ### Variablen
# string / str
text = "string"

# integer / int
ganzzahl = 20

# float
fliesskommazahl = 20.0   # WICHTIG: Muss mit "." geschrieben werden

# dictionary / dict
dictionary = {"Bezeichnung 1": "Wert 1", "Bezeichnung 2": "Wert 2"}     # Werte werden über die Bezeichnung aufgerufen

# list (wie Tuple, nur Werte überschreibbar)
liste = ["Wert 1", "Wert 2"]    # Werte werden mit Index 0, 1, ... aufgerufen

# tuple (wie Liste, nur nicht veränderlich)
tuple_bsp = ("Wert 1", "Wert 2")    # Werte werden mit Index 0, 1, ... aufgerufen

# ### Datentypen umwandeln (es können auch z.B. Tuples in Listen umgewandelt werden)
wert = "120"
wert_integer = int(wert)    # Wert in einen Integer umwandeln
wert_float = float(wert)    # Wert in einen Float umwandeln
wert_string = str(wert)     # Wert in einen String umwandeln

# ### String-Operationen
text.lower()    # ändert alles auf Kleinbuchstaben
text.upper()    # ändert alles auf Großbuchstaben
text.strip()    # entfernt am Anfang und Ende das Element, welches in der Klammer steht bzw. die Leerzeichen
text.lstrip()   # wie strip, aber nur auf der linken Seite des strings
text.rstrip()   # wie strip, aber nur auf der rechten Seite des strings
text.split()    # trennt den string anhand des Elements in Klammern in eine Liste auf

# ### Listen-Operationen
liste.append("Wert, welcher in die Liste soll")     # hängt einen Inhalt an eine Liste an
liste.sort()    # Sortiert die Liste nach Alphabet und Wert
liste = sorted(liste)   # wie sort
liste.reverse()     # kehrt die Reihenfolge der Elemente in der Liste um

# ### Print-Befehle
# Ausgabe eines Strings
print("Dies ist ein reiner Text")

# Ausgabe einer Variable
print(text)

# Ausgabe einer Kombination aus String und Text
print("Die Variable text enthält folgenden Text:", text)
# oder
print(f"Die Variable text enthält folgenden Text: {text}")

# Ausgabe der Werte von Liste, Tuple und Dictionary
# Liste
print(liste[0])     # Liste: wird mit Index hochzählend von 0 aufgerufen
print(tuple_bsp[0])     # Tuple: wird mit Index hochzählend von 0 aufgerufen
print(dictionary["Bezeichnung 1"])  # Dictionary: wird über die Bezeichnung des jeweiligen Werts aufgerufen

# ### for-Schleife
# Schleife, welche 10-mal ausgeführt wird
for variablenname in range(10):
    # Code der Schleife, welcher immer wieder ausgeführt wird, z.B.
    print(f"Durchlauf {variablenname}")
    if variablenname == 5:
        break   # Verlässt die Schleife
    else:
        continue    # Führt die Schleife fort

# Schleife, welche alle Elemente einer Liste durchgeht
for element in liste:
    # Code der Schleife, welcher immer wieder ausgeführt wird, z.B.
    print(element)

# ### while-Schleife
# wird ausgeführt, solange Bedingung wahr ist
while text == "Test":
    print("text ist Test")

# wird ausgeführt, solange keine fehlerfreie Eingabe vorhanden ist
fehler = True   # Variable für Schleifenbedingung Fehler definieren
while fehler:   # Schleife durchlaufen lassen, solange ein Fehler vorliegt
    eingabe = input("Eingabe: ")    # Eingabe abfragen
    if eingabe.isdigit():   # Prüfen, ob Eingabe eine Ziffer ist bzw. korrekt ist
        fehler = False      # Wenn die Eingabe korrekt ist, Fehler auf False setzen, um die Schleife zu beenden

# wird ausgeführt, bis die Schleife durch break beendet wird
while True:
    print("Test")
    break

# ### if-Abfrage
if text == "Test":  # prüft, ob die Variable text Test ist
    print("Text Test")      # wird ausgeführt, wenn die Bedingung wahr ist
elif text == "anderer_Test":    # Bedingung, die geprüft wird, wenn die andere nicht wahr ist
    print("Text anderer_Test")
else:                           # sonst, ohne Bedingung
    print("Text kein Test")     # wenn keine der vorherigen Bedingungen erfüllt ist


# ### Funktionen
# Funktion definieren
# so viele Parameter wie nötig angeben, ggf. Standardwerte mit = definieren
def funktionsname(parameter_1, parameter_2="Standardwert"):
    # Programmcode innerhalb der Funktion z.B.
    if parameter_1 == parameter_2:
        return "Stimmt überein"     # Sobald ein return ausgeführt wird, wird die Funktion beendet
    return None     # Wäre nicht nötig, da eine Funktion immer None zurückgibt, wenn nichts anderes definiert ist


# Funktion aufrufen, mit Übergabe eines Wertes für parameter_1, Verwendung Standardwert für parameter_2
funktionsname("Standardwert")

# Funktion aufrufen, mit Übergabe eines Wertes für parameter_1 und parameter_2 und Ausgabe der Rückgabe
print(funktionsname("Standardwert"))

# Funktion aufrufen, mit Übergabe eines Wertes für parameter_1 und parameter_2 und Speichern der Rückgabe
ergebnis_funktion = funktionsname("Test")

# ### Try Except
try:    # Code, der probiert wird auszuführen
    float(ergebnis_funktion)    # z.B. Umwandlung einer Variable in einen Float
except ValueError:      # Im Falle eines Fehlers im Try Block wird das ausgeführt
    fehler = True

# Try Except mit Schleife
while True:     # Unendliche Schleife, die durch break verlassen wird
    try:    # Probiert
        eingabe = int(input("Eingabe: "))
        if eingabe < 1 or eingabe > 10:     # Bedingung zum Fehler produzieren
            raise ValueError    # ValueError produzieren
        break   # Wenn alles vorher im Try funktioniert, wird das break ausgeführt und beendet die Schleife
    except ValueError:  # wird ausgeführt, wenn im Try-Block ein Fehler auftritt
        print("Fehler")

# ### Dateien verwenden
# mit Variable
# Datei öffnen mit Argumenten Dateiname und Lese-/Schreibmodus
# a = append (anhängen), w = write (überschreiben), r = read (lesen)
datei = open("dateiname.txt", "w")  # Datei öffnen und einer Variablen zuweisen
datei.write(ergebnis_funktion)  # Etwas in die Datei schreiben
datei.close()   # Datei schließen

# with open
# öffnet eine Datei für den darunter eingerückten Block und gibt dieser einen Variablennamen
with open("dateiname.txt", "a") as d:
    d.write(f"Text: {text}\n")  # Schreibt einen Text in die Datei (\n ist ein Zeilenumbruch)
