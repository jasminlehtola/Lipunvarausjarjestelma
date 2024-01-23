def nayta_UI():
    """Näyttää käyttöliittymän asiakkaalle"""
    while True:
        print("Tervetuloa elokuviin!")
        print("Valitse toiminto:")
        print("1. Tarkastele päivän elokuvia.")
        print("2. Varaa istumapaikka näytökseen. Tarkista päivän elokuvatarjonta ensin!")
        print("0. Poistu.")
        print("100. Olen ylläpitäjä.")

        valinta = int(input("Valintasi: "))
        print()

        if valinta == 1:
            selaile_elokuvia()

        elif valinta == 2:
            nimi = input("Anna elokuvan nimi: ")
            varaa_paikka(nimi)

        elif valinta == 100:
            menu()
            
        elif valinta == 0:
            print("Kiitos ja hei!")
            print()
            break


def menu():
    """Näyttää käyttöliittymän ylläpitäjälle"""
    while True:
        print("Hei ylläpitäjä!")
        print("Valitse toiminto:")
        print("1. Lataa tiedot tiedostosta.")
        print("2. Tallenna tiedostoon.")
        print("3. Lisää elokuva.")
        print("4. Tarkastele varauksia.")
        print("5. Tyhjennä varaukset tiedostosta.")
        print("6. Tyhjennä elokuvatiedot tiedostosta.")
        print("0. Poistu.")
        print("100. Siirry asiakkaan käyttöliittymään.")

        valinta = int(input("Valintasi: "))
        print()

        if valinta == 1:
            lataa_tiedot()

        elif valinta == 2:
            tallenna_tiedostoon()

        elif valinta == 3:
            nimi = input("Anna elokuvan nimi: ")
            aika_ja_sali = input("Anna esitysaika ja sali (1-3) muodossa 00.00/0 (esim. 18.00/1): ")
            lisaa_elokuva(nimi, aika_ja_sali)
            print("Lisäsit elokuvan:", nimi, "Aika:", aika_ja_sali[0:5], "Sali:", aika_ja_sali[-1])
            print("Elokuva lisätty onnistuneesti!")
            print()

        elif valinta == 4:
            selaile_varauksia()

        elif valinta == 5:
            varmistus = input("Haluatko varmasti tyhjentää varaustiedot? k/e: ")
            print()
            if varmistus == "k":
                tyhjenna_varaukset()
                print("Tyhjennetty.")
            else:
                menu()

        elif valinta == 6:
            varmistus = input("Haluatko varmasti tyhjentää elokuvalistan? k/e: ")
            print()
            if varmistus == "k":
                tyhjenna_elokuvat()
                print("Tyhjennetty.")
            else:
                menu()

        elif valinta == 100:
            nayta_UI()   

        elif valinta == 0:
            print("Kiitos ja hei!")
            print()
            break


def selaile_elokuvia():
    """Näyttää käyttäjälle päivän elokuvat, kellonajat sekä salinumerot"""
    print("Päivän elokuvat:")
    for avain in naytokset:
        print(avain, naytokset[avain])
    print()

def varaa_paikka(nimi: str):
    """Asiakas voi varata istumapaikan haluamaansa elokuvaan"""
    # Salien maksimikapasiteetit
    sali1_max = 15
    sali2_max = 10
    sali3_max = 8

    # Ilmoitetaan, mikäli haettua elokuvaa ei ole näytöksissä ja
    # palataan takaisin päävalikkoon   
    if nimi not in naytokset:
        print("Hakemaasi elokuvaa ei löytynyt! Tarkistathan oikeinkirjoituksen.")
        print()
        nayta_UI()

    # Haetaan salin numero halutun elokuvan tiedoista ja
    # varataan sen mukaan paikka oikeasta salista
    sali = naytokset[nimi][-1]

    if sali == "1":
        if len(paikat1_varatut) < sali1_max:
            print("Vapaana olevat paikat:", set(paikat1).difference(set(paikat1_varatut)))
            istuinnumero = int(input("Minkä paikan haluat varata?: "))
            paikat1_varatut.append(istuinnumero)
            print("Varaus onnistui!")
            print("Sinulle on varattu paikka numero:", istuinnumero)
            print()
        else:
            print("Vapaita paikkoja ei ole tähän näytökseeen.")
       
    elif sali == "2":
        if len(paikat2_varatut) < sali2_max:
            print("Vapaana olevat paikat:", set(paikat2).difference(set(paikat2_varatut)))
            istuinnumero = int(input("Minkä paikan haluat varata?: "))
            paikat2_varatut.append(istuinnumero)
            print("Varaus onnistui!")
            print("Sinulle on varattu paikka numero:", istuinnumero)
            print()
        else:
            print("Vapaita paikkoja ei ole tähän näytökseeen.")

    elif sali == "3":
        if len(paikat3_varatut) < sali3_max:
            print("Vapaana olevat paikat:", set(paikat3).difference(set(paikat3_varatut)))
            istuinnumero = int(input("Minkä paikan haluat varata?: "))
            paikat3_varatut.append(istuinnumero)
            print("Varaus onnistui!")
            print("Sinulle on varattu paikka numero:", istuinnumero)
            print()      
        else:
            print("Vapaita paikkoja ei ole tähän näytökseeen.")



def lisaa_elokuva(nimi: str, aika_ja_sali: str)-> dict:
    """Ylläpitäjä voi lisätä uuden elokuvan"""
    naytokset[nimi] = aika_ja_sali

    
def selaile_varauksia():
    """Ylläpitäjä voi selailla salien varauksia"""
    print("Salien varaustilanne:")
    print(f"Salista 1 on varattu {len(paikat1_varatut)} paikkaa.")
    print(f"Varattuna ovat paikat {paikat1_varatut}")
    print(f"Salista 2 on varattu {len(paikat2_varatut)} paikkaa.")
    print(f"Varattuna ovat paikat {paikat2_varatut}")
    print(f"Salista 3 on varattu {len(paikat3_varatut)} paikkaa.")
    print(f"Varattuna ovat paikat {paikat3_varatut}")
    print()



def tallenna_tiedostoon():
    """Tallentaa tiedot tiedostoon"""
    
    # Tallennetaan elokuvat omaan tiedostoon
    with open("elokuvateatteri.txt", "a") as tiedosto:
        for nimi, aika_ja_sali in naytokset.items():
            rivi = f"{nimi},{aika_ja_sali}\n"
            tiedosto.write(rivi)

    # Tallennetaan istumapaikkavaraukset omaan tiedostoon
    # Kaikille kolmelle salille oma tiedosto
    # Sali 1:
    with open("varaukset1.txt", "w") as varaukset1:
        for luku in paikat1_varatut:
            varaukset1.write(str(luku) + "\n")
    # Sali 2:
    with open("varaukset2.txt", "w") as varaukset2:
        for luku in paikat2_varatut:
            varaukset2.write(str(luku) + "\n")
    # Sali 3:
    with open("varaukset3.txt", "w") as varaukset3:
        for luku in paikat3_varatut:
            varaukset3.write(str(luku) + "\n")

    print("Tiedot tallennettu.")
    print()
            

def lataa_tiedot()-> list:
    """Lataa tiedot tiedostosta"""
    # Lataa lisätyt lokuvat
    with open("elokuvateatteri.txt") as tiedosto:
        for rivi in tiedosto:
            tiedot = rivi.strip().split(",")
            naytokset[tiedot[0]] = tiedot[1]

    # Lataa paikkavaraukset kaikille kolmelle salille
    with open("varaukset1.txt") as varaukset1:
        for numero in varaukset1:
            tiedot1 = numero.strip().split(",")
            paikat1_varatut.append(tiedot1)
           
    with open("varaukset2.txt") as varaukset2:
        for numero in varaukset2:
            tiedot2 = numero.strip().split(",")
            paikat2_varatut.append(tiedot2)

    with open("varaukset3.txt") as varaukset3:
        for numero in varaukset3:
            tiedot3 = numero.strip().split(",")
            paikat3_varatut.append(tiedot3)

    print("Tiedot ladattu.")
    print()


def tyhjenna_varaukset():
    open("varaukset1.txt", 'w').close()
    open("varaukset2.txt", 'w').close()
    open("varaukset3.txt", 'w').close()

def tyhjenna_elokuvat():
    open("elokuvateatteri.txt", 'w').close()


# ------------------    
# PÄÄOHJELMA
# ------------------

naytokset = {}
paikat1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
paikat2 = [1,2,3,4,5,6,7,8,9,10]
paikat3 = [1,2,3,4,5,6,7,8]
paikat1_varatut = []
paikat2_varatut = []
paikat3_varatut = []


menu()








