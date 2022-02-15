# Python - Grundlagen zu Variablen und Ausgaben
Computer können nichts besser als rechnen, daher kann man auch in allen Programmiersprachen mit den Zahlen berechnungen anstellen.
Python stellt uns dafür verschiedene Operatoren zur Verfügung:

- &#43; (Pluszeichen) dient zur Addition
- &#45; (Minuszeichen) dient zur Subtraktion
- &#42; (Asteriks) dient zur Multiplikation
- / (Slash oder Schrägstrich) dient zur Division

Dabei muss man aber aufpassen mit welchen Datentyp man zu tun hat, denn je nachdem welcher Datentyp es ist 
stehen nur wenige oder alle Operatoren zur Verfügung. Es ist allerdings auch verstädnlich, dass man bei einem Text keine Division durchführen kann und das nur bei Zahlen geht.


## Aufgaben
Hier sind ein paar Aufgaben, die du machen kannst um noch etwas weiter zu üben. Nächste Woche bekommt ihr dann die Lösung dafür:

### Weitere Operatoren
Probiere die unten stehenden Operatoren mit verschiedenen Zahlen aus und notiere dir, was sie tun. Setze für x und y verschiedene Zahlen ein, bis du herausgefunden hast, was die Operatoren tun.

```python
x + y
x - y
x * y
x / y
x ** y
x // y
x % y
```

> In der nächsten PDF werden diese Operatoren natürlich oben ergänzt, so dass ihr auch eine Erklärung habt.



### Was gibt das Programm aus?
Was ist der Rückgabewert des unten stehenden Programms? Gehe es zuerst im Kopf durch und probiere es anschliessend aus, in dem du das Programm mit PyCharm in einer neuen Datei abspeicherst.

```python
x = 2
y = 3
z = x + y
x = z
y = x
print(x)
print(y)
print(z)
```

### Zeit umrechnen
Schreibe ein Programm, welches eine Zeitangabe in Stunden, Minuten und Sekunden in die Anzahl Sekunden insgesamt umrechnet

### Werkstatt kosten
Eine Werkstatt verlangt für die Benützung einer Maschine eine Grundgebühr von 60 Franken sowie 35 Fanken pro Stunde. Man überlege sich, welche Daten einzugeben und wel che Daten zu berechnen sind und erstelle ein passendes Programm.

### Leihwagen kosten
Ein Kleinunternehmen stellt seinen Kunden für Tran sporte einen Lieferwagen und einen Lastwagen zur Verfügung. Für Transporte mit dem Lieferwagen werden Fr. 1.60 pro Kilometer verrechnet, für den Lastwagen beträgt der Tarif Fr. 2.80 pro Kilometer. Welche Gebühr hat ein Kunde zu bezahlen, wenn der Lieferwagen 85 km und der Lastwagen 120 km zurückgelegt hat?

### Der Weinhändler
Ein Weinhändler verkauft Rotwein zu 18 Franken pro Flasche, Roséwein zu 13 und Weisswein zu 12 Franken pro Flasche. Ein Kunde bestellt (beispielsweise) 12 Flaschen Rotwein, 6 Flaschen Rosé und 24 Flaschen Weisswein. Schreibe ein Programm, welches den Gesamtpreis berechnet.
