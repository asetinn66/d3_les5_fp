import csv

def read_csv_to_dict(file_path):
    data = {}  # Rename the dictionary to 'data'
    with open(file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            employee_id = row['ID']
            employee_data = {
                'Naam': row['Naam'],
                'Functie': row['Functie'],
                'Loon': row['Loon']
            }
            data[employee_id] = employee_data
    return data

file_path = 'employee_data.csv'
data = read_csv_to_dict(file_path)

if __name__ == "__main__":

    for id,personeeel in data.items():
        print(id)
        for k,v in personeeel.items():
            print(k,v)