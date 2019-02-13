"""Zahlen zusammenrechnen."""
# from ast import literal_eval (kann leider nur + und -)
# Author: Enea Giger

def isdigit(x):
    try:
        float(x)
        return True
    except ValueError:
        return False


def startRechner():
    """Starte Rechner."""
    try:
        ersteZahl = input(
            "Welche Zahl ist die erste Zahl der Rechnung? ")
        while not isdigit(ersteZahl):
            ersteZahl = input("Eine Zahl bitte ")

        grundrechenart = input(
            "Bitte Grundrechenart eingeben (* / + - ) ")
        while grundrechenart not in "*/+-":
            grundrechenart = input("Wähle * / + - ")

        zweiteZahl = input(
            "Welche Zahl ist die zweite Zahl der Rechnung? ")
        while not isdigit(zweiteZahl):
            zweiteZahl = input("Eine Zahl bitte ")

        try:
            rechnung = ersteZahl + grundrechenart + zweiteZahl  # Stringconcat!
            resultat = eval(rechnung)
        except ZeroDivisionError:
            zweiteZahl = input("Anderer Divisor bitte, nicht 0 ")
            while not isdigit(zweiteZahl):
                zweiteZahl = input("Eine Zahl bitte ")
            rechnung = ersteZahl + grundrechenart + zweiteZahl  # Strings only!
            resultat = eval(rechnung)
        print(rechnung, '=')
        print("Resultat:", resultat)

        again = input("==================== nochmal? (J/n) ")
        if again not in ['n', 'N']:
            startRechner()
    except (TypeError, ValueError) as e:
        print(e)


startRechner()
