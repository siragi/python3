"""Zahlen zusammenrechnen."""
ersteZahl = input("Welche Zahl ist die erste Zahl der Rechnung?")
grundrechenart = input("*, /, + oder -")
zweiteZahl = input("Welche Zahl ist die zweite Zahl der Rechnung?")
rechnung = (ersteZahl + grundrechenart + zweiteZahl)
print(eval(rechnung))
