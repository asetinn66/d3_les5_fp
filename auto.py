from prettytable import PrettyTable

def voeg_auto_toe():
    id = len(auto_data) + 1
    merk = input("geef merk in")
    model = input("geef model in")
    auto_data[id] = {"Merk":merk,"Model":model}
    myTable.add_row([id,merk,model])

auto_data = {
    1: {"Merk": "Ford", "Model": "Fiesta"},
    2: {"Merk": "Ford", "Model": "Ford"},
    3: {"Merk": "Audi", "Model": "A4"},
    4: {"Merk": "Opel", "Model": "Astra"},
}

myTable = PrettyTable(["id", "Merk", "Model"])
rij = []
for id, data in auto_data.items():
    rij.append(id)
    for auto in data.values():
        rij.append(auto)
    myTable.add_row(rij)
    rij.clear()

print(myTable)
voeg_auto_toe()
print(myTable)
print(auto_data)