import random

spielstand_links = 0
spielstand_rechts = 0

anzahl_runden = int(input("Wie viele Runden möchtest du spielen "))

def gebeSpielstandAus():
    print("Spielstand " + str(spielstand_links) + ":" + str(spielstand_rechts))
    print("1 =  Schere")
    print("2 =  Stein")
    print("3 =  Papier")
    print("4 =  Echse")
    print("5 =  Spock")

auswahl = ["Schere", "Stein", "Papier", "Echse", "Spock"]


def bestimmeSieger(auswahl1, auswahl2):
    auswahl1_wort = auswahl[auswahl1]
    auswahl2_wort = auswahl[auswahl2]

    spock_gewinnt = ["Stein", "Schere"]

    if auswahl1_wort == "Spock" and auswahl2_wort in spock_gewinnt:
        return "Gewonnen"

    if auswahl1_wort == auswahl2_wort:
        return "Unentschieden"

    if (auswahl1_wort == "Schere" and auswahl2_wort == "Papier") or (auswahl1_wort == "Papier" and auswahl2_wort == "Stein") or (auswahl1_wort == "Stein" and auswahl2_wort == "Schere") or (auswahl1_wort == "Stein" and auswahl2_wort == "Echse"):
        return "Gewonnen"

    if auswahl1_wort == "Echse" and auswahl2_wort == "Spock":
        return "Gewonnen"
    if auswahl1_wort == "Spock" and auswahl2_wort == "Schere":
        return "Gewonnen"
    if auswahl1_wort == "Schere" and auswahl2_wort == "Echse":
        return "Gewonnen"
    if auswahl1_wort == "Echse" and auswahl2_wort == "Papier":
        return "Gewonnen"
    if auswahl1_wort == "Papier" and auswahl2_wort == "Spock":
        return "Gewonnen"
    if auswahl1_wort == "Spock" and auswahl2_wort == "Stein":
        return "Gewonnen"

    if auswahl1_wort == "Schere" and auswahl2_wort == "Stein":
        return "Verloren"

    if auswahl1_wort == "Stein" and auswahl2_wort == "Papier":
        return "Verloren"

    if auswahl1_wort == "Papier" and auswahl2_wort == "Schere":
        return "Verloren"





durchlauf = 1
while(durchlauf <= anzahl_runden):
    gebeSpielstandAus()
    meine_auswahl = int(input("Spieler 1: "))
    gegnerische_auswahl = random.randint(0, len(auswahl) - 1)
    sieger = bestimmeSieger(meine_auswahl, gegnerische_auswahl)
    print(sieger)

    if sieger == "Gewonnen":
        spielstand_links = spielstand_links + 1
    elif sieger == "Verloren":
        spielstand_rechts = spielstand_rechts + 1

    durchlauf = durchlauf + 1
