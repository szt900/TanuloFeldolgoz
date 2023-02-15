print("Tanulók feldolgozása!")

tanulok = []
while True:
    print("\nKérem a tanuló adatait: ")
    nev = input("Add meg a tanuló nevét: ")
    szId = input("Add meg a születési dátumot: ")
    magassag = int(input("Magasság: "))

    tanulo = (nev, szId, magassag)
    tanulok.append(tanulo)

    valasz = input("További tanulo? y/n ")
    if valasz.lower() != 'y':
        break

#2 Fasz se tudja


#3 Hozzáférés listaelem segítségével
for item in tanulok:
    print(f"Név: {item[0]}"), születési ideje: {item[1]}, magasság: {item[2]}"
