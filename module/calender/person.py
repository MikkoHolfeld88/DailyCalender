import datetime

unknown = "unbekannt"

class Person():
    def __init__(self, vorname = unknown, nachname = unknown, geburtstag = unknown, nationalitaet = unknown, wohnort = unknown, geburtsort = unknown):
        # Basisdaten
        self.vorname = vorname
        self.nachname = nachname
        self.geburtstag = geburtstag
        self.geburtsort = geburtsort
        self.nationalitaet = nationalitaet
        self.wohnort = wohnort
        self.alter = self.geburtstagZuAlter()

        self.basis_daten = {
            "Vorname": self.vorname,
            "Nachname": self.nachname,
            "Alter": self.alter,
            "Geburtstag": self.geburtstag,
            "Geburtsort": self.geburtsort,
            "Nationalitaet": self.nationalitaet,
            "Wohnort": self.wohnort
        }

    def get_basis_daten(self, key):
        return self.basis_daten[key]

    def print_basis_daten(self):
        for key in self.basis_daten:
            print(key + ": " + str(self.basis_daten[key]))

    def print_basis_datum(self, key):
        print(self.basis_daten[key])

    # Hilfsfuntion für Alterermittlung aus Geburtstag !!! SCHALTJAHR NOCH NICHG MIT IN BERECHNUNGEN
    def geburtstagZuAlter(self):
        tag = self.geburtstag[0:2]
        monat = self.geburtstag[3:5]
        jahr = self.geburtstag [6:10]
        alter = datetime.datetime(int(jahr), int(monat), int(tag)) - datetime.datetime.now()
        alter = alter / (-365.0)
        alter = alter.days
        return alter

if __name__ == "__main__":
    Mikko = Person("Mikko Maximilian Hans", "Holfeld", "15.10.1988" , "deutsch", "Leipzig", "Leverkusen" )
    Mikko.print_basis_datum("Alter")
