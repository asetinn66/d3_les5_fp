import csv

data = {
    1: {"Naam": "Jan", "Functie": "CEO", "Loon": 7500},
    2: {"Naam": "Sofie", "Functie": "CFO", "Loon": 5000},
    3: {"Naam": "Patrick", "Functie": "CTO", "Loon": 5000},
    4: {"Naam": "Mario", "Functie": "Project Manager", "Loon": 4000},
    5: {"Naam": "Javid", "Functie": "Project Manager", "Loon": 4000},
    6: {"Naam": "Elien", "Functie": "Senior Dev", "Loon": 3200},
    7: {"Naam": "Luca", "Functie": "Senior Dev", "Loon": 3200},
    8: {"Naam": "Nina", "Functie": "Junior Dev", "Loon": 2600},
    9: {"Naam": "Leonardo", "Functie": "Junior Dev", "Loon": 2600},
    10: {"Naam": "Pieter", "Functie": "Junior Dev", "Loon": 2600},
    11: {"Naam": "Daisy", "Functie": "Junior Dev", "Loon": 2600},
    12: {"Naam": "Inge", "Functie": "Stagiair Dev", "Loon": 0},
}

# Specify the CSV file name
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