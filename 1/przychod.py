import csv

def count(price_key="cena", amount_key="ilosc", file="dane.csv"):
    with open(file, newline='') as csvfile:
        price_index = False
        amount_index = False

        final = 0

        reader = csv.reader(csvfile, delimiter=';')

        rows = [row for row in reader]

        keys = rows[0]

        for i in range(len(keys)):
            if keys[i] == price_key:
                price_index = i
            
            if keys[i] == amount_key:
                amount_index = i

        if price_index == False:
            print("Nie znaleziono klucza ceny.")

        else:
            print(f"Indeks ceny: {price_index}")

        if amount_index == False:
            print("Nie znaleziono klucza ilosci.")

        else:
            print(f"Indeks ilosci: {amount_index}")

        for row in rows[1::]:
            final += int(row[price_index]) * int(row[amount_index])

    return final

print(f"Calkowity przychod: {count()}")