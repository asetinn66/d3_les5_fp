from werken_met_csv_read import read_csv_to_dict
def lees_data_in():
    file_path = 'employee_data.csv'
    data = read_csv_to_dict(file_path)
    return data
def toon_alle_data():
    for id, personeeel in data.items():
        print(id)
        for k, v in personeeel.items():
            print(k, v)
def voeg_personeel_lid_toe():
    id = int(input("geef id in"))
    if id in data.keys():
        print("id bestaat al")
    else:
        naam = input("geef de naam")
        functie = input("geef de functie")
        loon = int(input("geef het loon van de wn"))
        data[id] = {"Naam":naam,"Functie":functie,"Loon":loon}
def verwijder_personeelslid():
    toon_alle_data()
    id = input("geef het id van de persoon die je wenst te verwijderen")
    if id in data.keys():
        data.pop(id)
    else:
        print("persoon kan niet verwijderd worden")


def verhoog_lonen_met_x_procent():
    procent = int(input("Met hoeveel procent wil je verhogen? "))
    verhogingsfactor = 1 + procent / 100

    for personeel in data.values():
        loon_str = personeel.get("Loon")

        try:
            loon = float(loon_str)
            personeel["Loon"] = loon * verhogingsfactor
        except ValueError:
            print(f"Error: Invalid 'Loon' value for personeel {personeel}. Skipping.")

    print(f"Lonen zijn verhoogd met {procent}%.")
def verander_functie():
    id = input("geef het id van de persoon")
    if id in data.keys():
        functie = input("geef nieuwe functie")
        data[id]["Functie"] = functie
        data[id]["Loon"] = float(input("geef het nieuwe loon"))
    else:
        print("id niet gevonden")

def sorteer_op_naam():
    sorted_data = dict(sorted(data.items(), key=lambda x: x[1]["Naam"]))
    for id, personeel in sorted_data.items():
        print(f"{id}: {personeel['Naam']}, {personeel['Functie']}, {personeel['Loon']}")

def update_data_naar_csv():
    import csv
    csv_file = "employee_data.csv"

    # Open the CSV file in write mode
    with open(csv_file, 'w', newline='') as file:
        # Create a CSV writer object
        writer = csv.writer(file)

        # Write the header row
        writer.writerow(["ID", "Naam", "Functie", "Loon"])

        # Write data rows
        for id, employee_data in data.items():
            writer.writerow([id, employee_data["Naam"], employee_data["Functie"], employee_data["Loon"]])

    print(f"Data has been written to {csv_file}")


###hfd##
data = lees_data_in()
#verhoog_lonen_met_x_procent()
#toon_alle_data()
#verander_functie()
#toon_alle_data()
verwijder_personeelslid()
sorteer_op_naam()