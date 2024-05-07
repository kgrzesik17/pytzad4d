import csv

def count(price_key="cena", amount_key="ilosc", file="dane.csv"):
    """
    This function counts a total revenue from a CSV file.

    Input:
    price_key - price key in the CSV file
    amount_key - amount key in the CSV file
    file - name of a file a user wants to analyze

    Output:
    float - total revenue.
    boolean value - False if failed.
    """
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
            return False

        else:
            print(f"Indeks ceny: {price_index}")

        if amount_index == False:
            print("Nie znaleziono klucza ilosci.")
            return False

        else:
            print(f"Indeks ilosci: {amount_index}")

        for row in rows[1::]:
            final += float(row[price_index]) * float(row[amount_index])

    return float(final)

print(f"Calkowity przychod: {count()}")