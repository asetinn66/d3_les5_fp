from prettytable import PrettyTable

namen = ["Frank","Jolien","Hendrik","Pedro","Paola"]
tabel = PrettyTable(["Naam"])
for naam in namen:
    tabel.add_row([naam])

print(tabel)