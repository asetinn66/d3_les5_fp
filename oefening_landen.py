from prettytable import PrettyTable

landen_data = {
    1: {"naam": "Nederland", "hoofdstad": "Amsterdam", "aantal_inwoners": 17000000, "continent": "Europa"},
    2: {"naam": "Verenigde Staten", "hoofdstad": "Washington, D.C.", "aantal_inwoners": 331000000,
        "continent": "Noord-Amerika"},
    3: {"naam": "Brazilië", "hoofdstad": "Brasília", "aantal_inwoners": 213993437, "continent": "Zuid-Amerika"},
    4: {"naam": "China", "hoofdstad": "Peking", "aantal_inwoners": 1444216107, "continent": "Azië"},
    5: {"naam": "Zuid-Afrika", "hoofdstad": "Pretoria", "aantal_inwoners": 60000000, "continent": "Afrika"},
}
gesorteerde_data = dict(sorted(landen_data.items(), key=lambda item: item[1]["hoofdstad"]))

# Aanmaken van PrettyTable
tabel = PrettyTable(["ID", "Land", "Hoofdstad", "Aantal Inwoners", "Continent"])

# Toevoegen van bestaande gegevens aan PrettyTable
for identificatie, gegevens in gesorteerde_data.items():
    tabel.add_row(
        [identificatie, gegevens["naam"], gegevens["hoofdstad"], gegevens["aantal_inwoners"], gegevens["continent"]])

print(gesorteerde_data)

# Vragen om extra gegevens toe te voegen
while True:
    toevoegen = input("Wil je een nieuw land toevoegen? (ja/nee): ").lower()

    if toevoegen != "ja":
        break

    naam = input("Naam van het land: ")
    hoofdstad = input("Hoofdstad van het land: ")
    inwoners = int(input("Aantal inwoners van het land: "))
    continent = input("Continent van het land: ")

    nieuwe_id = max(gesorteerde_data.keys()) + 1  # Genereer een nieuw ID
    gesorteerde_data[nieuwe_id] = {"naam": naam, "hoofdstad": hoofdstad, "aantal_inwoners": inwoners,
                                   "continent": continent}
    tabel.add_row([nieuwe_id, naam, hoofdstad, inwoners, continent])

# Afdrukken van de tabel
tabel.sortby = "Land"
print(tabel)