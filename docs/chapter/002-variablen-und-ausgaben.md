# Python - Grundlagen zu Variablen und Ausgaben
Python ist eine Skriptsprache in der die Ausführung immer von oben nach unten erfolgt. Das heißt der Befehl in Zeile 1 wird normalerweise vor dem in Zeile 2 gemacht. 

## Ausgaben
Die zwei Möglichkeiten von Ausgaben sind: Die Ausgabe auf der Konsole oder im Terminal und die andere Möglichkeit wäre die Ausgabe innerhalb einer GUI (Grafische Oberfläche engl. Graphical User Interface) zu machen. Da wir allerdings aktuell nichts in einer GUI
machen wollen arbeiten wir mit einer Konsole und den Ausgaben innerhalb dieser. 

Eine Ausgabe kann in Python mit der Funktion `print()` erfolgen. Innerhalb der Klammern von print kommt der Text, die Zahlen oder aber die Variable die wir auf der Konsole ausgeben wollen. Hier ein paar Beispiele:

```python
print("Hallo")
print("Welt")
print("Hallo TKR")
print("Dies ist mal ein etwas längerer Satz")
print("Auch Zahlen können in einem Text stehen")
print(10)
print(meineVariable)
```

## Datentypen
Mittels eines Datentyps einer Variablen kann bestimmt werden, welche Werte diese Variable annehmen kann oder welche Operationen wir auf Sie anwenden können. 
So kann man auf Text die + Operation anwenden um Texte miteinander zu kombinieren und auf Zahlen 
 +,-,/ und *. Außerdem kann noch unterschieden Werden zwischen einem Float (Fließkommazahl) und einem Int (Ganzzahl)

## Kommentare
Kommentare sind in einem Programm Zeilen, die vom Computer nicht beachtet werden. Das heißt Sie werden bei der Ausführung einfach ignoriert. In Python kann man einen Kommentar schreiben, indem man eine Raute (#) vor einer Zeile packt.

```python
# Ich bin ein Kommentar
```

## Aufgaben
Hier sind ein paar Aufgaben, die du machen kannst um noch etwas weiter zu üben:

### Name Ausgeben
Erstelle ein Programm, das deinen Vorname, Nachname und dein Geburtsdatum auf der Konsole ausgibt.

> Zusatzaufgabe: Erweitere das Programm, so dass es zusätzlich noch deine Adresse und deine Telefonnummer auf der Konsole ausgibt. 

### Temperatur umrechnen
Schreibe ein Programm, das Temperaturen in verschiedene Skalensystemen ineinander umwandelt. Das Programm soll zu Beginn eine Auswahl mit den verschiedenen Möglichkeiten anbieten:

- Umrechnung von Celsius nach Kelvin
- Umrechnung von Celsius nach Fahrenheit
- Umrechnung von Kelvin nach Celsius
- Umrechnung von Kelvin nach Fahrenheit
- Umrechnung von Fahrenheit nach Celsius
- Umrechnung von Fahrenheit nach Kelvin

>Dies kann dir sicher helfen.
>- Celsius = 5/9 * (Fahrenheit - 32).
>- Celsius = Kelvin - 273.15.
>- Die tiefste mögliche Temperatur ist den absoluten Nullpunkt 0K.