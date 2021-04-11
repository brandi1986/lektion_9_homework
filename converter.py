# Umrechnungsprogramm von Meilen in Kilometer und umgekehrt

milestokm = 1.60934
kmtomiles = 0.621371
choose = 0

print("Willkommen beim Kilometer Meilen Umrechner")

while choose != 3:

    print("--------------------------")
    print("(1) Kilometter ==> Meilen")
    print("(2) Meilen ==> Kilometer")
    print("(3) Beenden")
    print("--------------------------")

    choose = input("Bitte wählen sie: ")
    choose = int(choose)

    if choose == 1:
        kilometer = input("Geben Sie bitte die Anzahl der Kilometer an die sie Umrechnen möchten? ")
        kilometer = float(kilometer)
        meilen = kilometer * kmtomiles
        print(str(kilometer) + " Kilometer = " + str(meilen) + " Meilen")
    elif choose == 2:
        meilen = input("Geben Sie bitte die Anzahl der Meilen an die sie Umrechnen möchten? ")
        meilen = float(meilen)
        kilometer = meilen * milestokm
        print(str(meilen) + "meilen = " + str(meilen) + "Kilometer")
    elif choose == 3:
        print("Danke das sie dieses Programm benutzt haben")
    else:
        print("Falsche Eingabe!")
1