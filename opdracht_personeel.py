from prettytable import PrettyTable
from werken_met_csv_read import read_csv_to_dict

def lees_data_in():
    file_path = 'employee_data.csv'
    data = read_csv_to_dict(file_path)
    return data

def toon_data():
    myTable = PrettyTable(["ID", "Naam", "Functie", "Loon"])
    rij = []
    for sleutel, gegevens in data.items():
        rij.append(sleutel)
        for personeel in gegevens.values():
            rij.append(personeel)
        myTable.add_row(rij)
        rij.clear()
    print(myTable)
    print("")

def voeg_toe():
    myTable = PrettyTable(["ID", "Naam", "Functie", "Loon"])
    id = len(data) + 1
    naam = input("Wat is zijn/haar naam? : ")
    functie = input("Wat is zijn/haar functie? : ")
    loon = input("Wat is zijn/haar loon? : ")
    data[id] = {"Naam":naam,"Functie":functie,"Loon":loon}
    myTable.add_row([id,naam,functie,loon])
    print("Personeel is toegevoegd!")
    print("")

def verwijder():
    toon_data()
    id = input("Geef het id van de personeel die je wenst te verwijderen : ")
    if id in data.keys():
        data.pop(id)
        print("Personeel is verwijderd!")
    else:
        print("Personeel is niet verwijderd!")
    print("")

def verhoging():
    procent = int(input("Met hoeveel procent wil je verhogen? : "))
    verhogingsfactor = 1 + procent / 100
    for personeel in data.values():
        loon_str = personeel.get("Loon")
        try:
            loon = float(loon_str)
            personeel["Loon"] = loon * verhogingsfactor
        except ValueError:
            print(f"Error: Invalid 'Loon' value for personeel {personeel}. Skipping.")
    print(f"Lonen zijn verhoogd met {procent}%.")
    print("")

def verander():
    id = input("Geef het ID van de persoon voor verandering : ")
    if id in data.keys():
        functie = input("Geef nieuwe functie : ")
        data[id]["Functie"] = functie
        data[id]["Loon"] = float(input("Geef het nieuwe loon : "))
    else:
        print("ID niet gevonden!!!")
    print("")

def sorteer():
    gesorteerde_data = dict(sorted(data.items(), key=lambda item: item[1]["Naam"]))
    tabel = PrettyTable(["ID", "Naam", "Functie", "Loon"])
    for identificatie, gegevens in gesorteerde_data.items():
        tabel.add_row([identificatie, gegevens["Naam"], gegevens["Functie"], gegevens["Loon"]])
    print(tabel)
    print("")

def personeel_loongrens():
    loongrens = float(input("Toon iedereen met een minimum loongrens van? : "))
    tabel = PrettyTable(["ID", "Naam", "Functie", "Loon"])
    for identificatie, gegevens in data.items():
        if float(gegevens["Loon"]) > loongrens:
            tabel.add_row([identificatie, gegevens["Naam"], gegevens["Functie"], gegevens["Loon"]])
    print(tabel)
    print("")

def bewaar():
    import csv
    csv_file = "employee_data.csv"
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Naam", "Functie", "Loon"])
        for id, employee_data in data.items():
            writer.writerow([id, employee_data["Naam"], employee_data["Functie"], employee_data["Loon"]])
    print(f"Data is weggeschreven naar {csv_file}")

# HOOFDPROGRAMMA
data = lees_data_in()
keuze_menu = {1: toon_data, 2: voeg_toe, 3: verwijder, 4: verhoging, 5: verander, 6: sorteer,
              7: personeel_loongrens, 8: bewaar, 0:quit}
keuze = ""
while keuze != 0:
    print("1 : Toon data")
    print("2 : Voeg personeel")
    print("3 : Verwijder personeel")
    print("4 : Verhoog lonen")
    print("5 : Verander functie, geef nieuwe loon")
    print("6 : Toon namen a-z")
    print("7 : Toon personeel met specifieke loongrens")
    print("8 : Bewaar data naar csv")
    print("0 : Stop programma")
    keuze = int(input("Maak uw keuze : "))
    if keuze in keuze_menu.keys():
        print(keuze_menu[keuze]())
    else:
        print("Foutief keuze")