#0
print("Tanulok feldolgozása.")

#1
tanulok = []
while True:
    print("Kérem a tanuló adatait:")
    nev = input("Tanulo neve: ")
    szId = input("Tanuló születési ideje: ")
    magassag = int(input("Magasság: "))

    tanulo =(nev, szId, magassag)
    tanulok.append(tanulo)

    valasz = input("További tanuló? (igen/nem): ")
    if valasz.lower() != 'igen':
        break

#2


#3 Hozzáférés lista index segítségével.
print("\nTanulók listája\n")
i=0
while i<len(tanulok):
    print(f'Sorszám: {i+1}, Név: {tanulok[i]["nev"]}, születési ideje: {tanulok[i]["szId"]}, magasság: {tanulok[i]["magassag"]}')

    i+=1
