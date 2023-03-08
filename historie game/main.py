import os
from PIL import Image

# lister av ting du kan få i historien
weapons = []
skatt = []
hode = []

# lager choice 1
def choice_1():
    #åpner listene
    global weapons
    global skatt
    global hode
    #fjerner alt i listene
    if "laser pistol" in weapons:
        weapons.remove("laser pistol")
    if "øks og skjold" in weapons:
        weapons.remove("øks og skjold")
    if "Skatt" in skatt:
        skatt.remove("Skatt")
    if "Hode" in hode:
        hode.remove("Hode")
    # fjerner alt av det som har blitt skrivd før i terminalen
    os.system('cls')
    #printer farge til teksten
    print("\033[34m")
    #printer teksten i terminalen
    print("Labyrintens Farlige Skjulte Skatt: En Romfarers Kamp")
    # \n gjør at den går til en ny linje i terminalen
    print("\nRomfarer Maksim drar til en avsidesliggende planet med et enkelt mål: å utforske og fullføre det legendariske oppdraget som ingen har greid før.")
    print("Når han lander på planeten Necrosphere så støtter han på en fornuftig labyrint og han bestemmer seg for å …")
    # tar vekk tekst fargen     
    print("\033[0m")
    #åpner bildet
    img1 = Image.open("labyrint.png")
    #viser bildet
    img1.show()
    #går til choice 2
    choice_2()

#lager choice 2
def choice_2():
    #printer teksten under
    print("1: Gå inn i labyrinten")
    print("2: Ikke gå inn i labyrinten")
    # dette er en loop som kjører hele tiden jeg er i choice 2
    while True:
        choice = input("Hva vil du gjøre? 1 eller 2: ")
        # om du skriver inn 1 så skjer ...
        if choice == "1":
            # fjerner alt av the som har blitt skrivd før i terminalen
            os.system('cls')
            #printer farge til teksten
            print("\033[34m")
            print("Han bestemmer seg for gå inn i den. Mens han vandrer gjennom labyrinten, blir han plutselig vitne til noe overnaturlig, et svært monster som er større enn han.")
            print("Han tar opp kampen, forberedt på å drepe monsteret.")
            img2 = Image.open("shadow.png")
            img2.show()
            choice_3()
            #fjerner fargen til teksten
            print("\033[0m")
            # om du ikke skriver inn 1 eller 2 så breaker den koden son at loopen går igjen og viser alt på nytt
            break
        #eller om du skriver in 2 så skjer ...
        elif choice == "2":
            os.system('cls')
            print("\033[34m")
            print("Han bestemmer seg for å la være å gå inn i den. Han har hørt om overnaturlig mystikk monster som skjuler seg inne i labyrinten, og han vil ikke risikere sitt liv for å finne skatten.")
            print("I stedet for å utforske labyrinten, velger Maksim å undersøke området rundt den.")
            choice_4()
            break
        # eller om du ikke skriver inn 1 eller 2 så skriver den ut det under
        else:
            print('\nTrykk på 1 eller 2, DUMBASS\n')

 ### sånn som jeg har skrivd over funker hele koden bortsett fra noen adre ting som jeg skal kommentere på under
 ### på alle img så åpner den bildet og viser bildet
 ### på choice_1-10() så går den til den choicen
 ### \n gjør sånn at du går til neste linje i terminalen
 ### os.system("cls") fjerner alt det forrige i terminalen
 ### print("\033[34-31-33m")legger til forskjellige farger mens 0m fjerner alt av fargene
 ### def choice_1-10() lager choicene sånn at du kan gå til/tilbake til dem med choice_1-10()

def choice_3():
    print("\033[0m")
    print("1: slåss mot monsteret")
    print("2: stikk ut av labyrinten")
    while True:
        choice = input("Hva vil du gjøre? 1 eller 2: ")
        if choice == "1":
            # om du har laser pistolen fra våpen listen så skjer...
            if "laser pistol" in weapons:
                os.system('cls')
                print("\033[31m")
                print("\nDøde, laser pistolen funker ikke på monsteret.")
                print("\033[0m")
                print("Trykk enter for å starte på nytt")
                input()
                choice_1()
                break
            # eller om du har øks og sjoldet i våpen listen så skjer ...
            elif "øks og skjold" in weapons:
                os.system('cls')
                print("\033[34m")
                print("Maksim kutter av hode til monsteret med øksen mens han beskytter seg selv med skjoldet.")
                choice_9()
                break
            # om du ikke har noe i våpen listen så skjer dette ...
            else:
                os.system('cls')
                print("\033[31m")
                print("\nDØDE, hadde ikke våpen")
                print("\033[0m")
                print("Trykk enter for å starte på nytt")
                input()
                choice_1()
                break
        elif choice == "2":
            os.system('cls')
            print("\033[34m")
            print("Han stikker ut av labyrinten.")
            choice_4()
            print("\033[0m")
            break        
        else:
            print('\nTrykk på 1 eller 2, DUMBASS\n')

def choice_4():
    print("\033[34m")
    print("Maksim bestemmer seg for å gå videre og han finner et våpen lager")
    print("\033[0m")
    img4 = Image.open("lager.png")
    img4.show()
    print("1: gå inn i våpen lageret")
    print("2: ikke gå inn i våpen lageret")
    while True:
        choice = input("Hva vil du gjøre? 1 eller 2: ")
        if choice == "1":
            os.system('cls')
            #går til choice 5
            choice_5()
            break
        elif choice == "2":
            os.system('cls')
            #går til choice 6
            choice_6()
            break
        else:
            print('\nTrykk på 1 eller 2, DUMBASS\n')

def choice_5():
    print("\033[34m")
    print("Han finner et laser pistol, en øks og et skjold inni våpen lageret...")
    print("\033[0m")
    img4 = Image.open("våpen.png")
    img4.show()
    print("1: ta laser pistolen")
    print("2: ta øksen og skjoldet")
    while True:
        choice = input("Hva vil du gjøre? 1 eller 2: ")
        if choice == "1":
            os.system('cls')
            choice_7()
            break
        elif choice == "2":
            os.system('cls')
            choice_8()
            break
        else:
            print('\nTrykk på 1 eller 2, DUMBASS\n')

def choice_6():
    print("\033[34m")
    print("Maksim går videre og han finner en landsby.")
    print("Han går inn i landsbyen.")
    print("\033[0m")
    img5 = Image.open("by.png")
    img5.show()
    print("1: Kjøp en leiglighet og bod i byen resten av livet")
    print("2: Hils på alle innbyggerene")
    while True:
        choice = input("Hva vil du gjøre 1 eller 2: ")
        if choice == "1":
            #om du har skatt i listen skatt så skjer...
            if "Skatt" in skatt:
                os.system('cls')
                print("\033[31m")
                print("Han kjøpte en leiglighet og bodde der resten av livet")
                print("Helt til han tok livet av seg selv fordi han hatet dette stedet og rakketen hans ble ødelagt så han kunne ikke reise tilbake")
                print("\033[0m")
                print("Trykk enter for å starte på nytt")
                input()
                choice_1()
                break
            # eller om du har hode så skjer...
            elif "Hode" in hode:
                os.system('cls')
                print("\033[31m")
                print("\nInnbyggerene ble sure og drepte han fordi han drepte mesteren dems")
                print("\033[0m")
                print("Trykk enter for å starte på nytt")
                input()
                choice_1()
                break
            # eller så skjer dette...
            else:
                os.system('cls')
                print("\033[34m")
                print("Maksim ble kastet ut fordi han var fattig")
                print("\033[0m")
                choice_10()
        elif choice == "2":
            #om du har hode fra listen hode så skjer dette...
            if "Hode" in hode:
                os.system('cls')
                print("\033[31m")
                print("\nInnbyggerene ble sure og drepte han fordi han drepte mesteren dems")
                print("\033[0m")
                print("Trykk enter for å starte på nytt")
                input()
                choice_1()
                break
            # om du ikke har hode så skjer dette...
            else:
                os.system('cls')
                print("\033[31m")
                print("Maksim hilser på alle innbygerene og han blir tilbedt et sted og bo")
                print("Maksim la seg til å sove etter en lang dag på den nye planeten og han våkner aldri opp ogjen")
                print("\033[0m")
                print("Trykk enter for å starte på nytt")
                input()
                choice_1()
                break
        else:
            print("\nTrykk på 1 eller 2 DUMBASS\n")         

def choice_7():
    #her så åpner den weapons listen
    global weapons
    print("\033[34m")
    print("Maksim tok laser pistolen for beskyttelse, hvor skal han gå nå?")
    print("\033[0m")
    #her så gir den laser pistol våpene til våpen listen
    weapons.append("laser pistol")
    print("1: gå tilbake til labyrinten")
    print("2: gå videre")
    while True:
        choice = input("Hva vil du gjøre? 1 eller 2: ")
        if  choice == "1":
            os.system('cls')
            choice_3()
            break
        elif choice == "2":
            os.system('cls')
            choice_6()
            break
        else:
            print('\nTrykk på 1 eller 2, DUMBASS\n')

def choice_8():
    #her så åpner den weapons listen
    global weapons
    print("\033[34m")
    print("Maksim tok øksen og skjoldet for beskyttelse, hvor skal han gå nå?")
    print("\033[0m")
    # her så legger den til øks og skjold til i våpen listen
    weapons.append("øks og skjold")
    print("1: gå tilbake til labyrinten")
    print("2: gå videre")
    while True:
        choice = input("Hva vil du gjøre? 1 eller 2: ")
        if  choice == "1":
            os.system('cls')
            choice_3()
            break
        elif choice == "2":
            os.system('cls')
            choice_6()
            break
        else:
            print('\nTrykk på 1 eller 2, DUMBASS\n')

def choice_9():
    print("Maksim finner skatten bak mønstere han drepte")
    print("\033[0m")
    img6 = Image.open("skatt.png")
    img6.show()
    print("1: ta med skatten og hode til monsteret å dra tilbake til hjem planeten sin")
    print("2: ta med skatten til monsteret og gå ut av labyrinten og videre forbi våpen lageret")
    print("3: ta med hode til monsteret og gå ut av labyrinten og videre forbi våpen lageret")
    while True:
        choice = input("Hva vil du gjøre? 1, 2 eller 3: ")
        if choice == "1":
            os.system('cls')
            print("\033[32m")
            print("Han dro hjem til planeten sin og fortalte om historien sin. Maksim blir den rikeste mannen på jorda")
            print("Han henger monsteret sitt hode på veggen og lever lykkelig resten av livet")
            print("Maksim fikk den brae slutten")
            print("\033[0m")
            print("Trykk enter for å starte på nytt")
            input()
            choice_1()
            break
        elif choice =="2":
            os.system('cls')
            #her så åpner denn skatt listen og legger till skatt i den
            global skatt
            skatt.append("Skatt")
            #går til choice 6
            choice_6()
            break
        elif choice =="3":
            os.system('cls')
            #her så åpner den hode listen og legger til hode i listen
            global hode
            hode.append("Hode")
            #går til choice 6
            choice_6()
        else:
            print('\nTrykk på 1, 2 eller 3 DUMBASS\n')

def choice_10():
    print("1: Dra hjem")
    print("2: Dra tilbake til hulen")
    while True:
        choice = input("Hva vil du gjøre? 1 eller 2: ")
        if choice == "1":
            os.system('cls')
            print("\033[32m")
            print("\nMaksim dro hjem og hadde ingen historie og fortelle")
            print("Maksim fikk den dårlige slutten")
            print("\033[0m")
            print("Trykk enter for å starte på nytt")
            input()
            choice_1()
        elif choice =="2":
            os.system('cls')
            print("\033[34m")
            print("Maksim dro tilbake til hulen for å fullføre den legendariske oppgaven")
            print("\033[0m")
            choice_2()
            break
        else:
            print('\nTrykk på 1 eller 2, DUMBASS\n')

# her så definer den alle choicene i rekkefølge sånn at spille fungerer som den skall istedenfor at den starter på choice 5 f.eks.
choice_1()
choice_2()
choice_3()
choice_4()
choice_5()
choice_6()
choice_7()
choice_8() 
choice_9()
choice_10()