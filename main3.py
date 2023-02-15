print("Tanulók feldolgozása!")

tanulok = []
while True:
    print("\nKérem a tanuló adatait: ")
    tanulo={}
    tanulo["nev"] = input("Add meg a tanuló nevét: ")
    tanulo["szId"] = input("Add meg a születési dátumot: ")
    tanulo["magassag"] = int(input("Magasság: "))

    tanulok.append(tanulo)

    valasz = input("További tanulo? y/n ")
    if valasz.lower() != 'y':
        break

#2 Fasz se tudja


#3 Hozzáférés listaelem segítségével
for item in tanulok:
    #!!!!! Figyelni kell arra hogy az f string és a kulcsoknak a határolói különbözőek legyenek.  
    print(f'Név: {item["nev"]}, születési ideje: {item["szId"]}, magasság: {item["magassag"]}')
