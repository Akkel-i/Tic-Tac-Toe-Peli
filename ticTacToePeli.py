import random

lauta = [["-", "-", "-"],
        ["-", "-", "-"],
        ["-", "-", "-"]
    ]


x = 0
y = 0
i = 0
k = 0
mones_vuoro = 1


def piirra_lauta():
    x = 0
    k = 0
    y = 0
    while x < 3:
        i = 0
        while i < 1:
            print(lauta[x][y], "|", lauta[x][y+1], "|", lauta[x][y+2])
            if k < 2:
                print("---------")
            k += 1    
            i += 1
        x +=1 

def voitto_tarkistus_O():
    
    if lauta[0][0] == "O" and lauta[0][1] == "O" and lauta[0][2] == "O":
        voitto_o = True
        return voitto_o 
    if lauta[1][0] == "O" and lauta[1][1] == "O" and lauta[1][2] == "O":
        voitto_o = True
        return voitto_o 
    if lauta[2][0] == "O" and lauta[2][1] == "O" and lauta[2][2] == "O":
        print("1,1. 1,2. 3,3 palauttaa tämän")
        voitto_o = True
        return voitto_o 
    if lauta[0][0] == "O" and lauta[1][1] == "O" and lauta[2][2] == "O":
        voitto_o = True
        return voitto_o 
    if lauta[0][2] == "O" and lauta[1][1] == "O" and lauta[2][0] == "O":
        voitto_o = True
        return voitto_o 
    if lauta[0][0] == "O" and lauta[1][0] == "O" and lauta[2][0] == "O":
        voitto_o = True
        return voitto_o 
    if lauta[0][1] == "O" and lauta[1][1] == "O" and lauta[2][1] == "O":
        voitto_o = True
        return voitto_o 
    if lauta[0][2] == "O" and lauta[1][2] == "O" and lauta[2][2] == "O":
        voitto_o = True
        return voitto_o 

def voitto_tarkistus_X():
    if lauta[0][0] == "X" and lauta[0][1] == "X" and lauta[0][2] == "X":
        voitto_x = True
        return voitto_x
    if lauta[1][0] == "X"and lauta[1][1] == "X" and lauta[1][2] == "X":
        voitto_x = True
        return voitto_x
    if lauta[2][0] == "X" and lauta[2][1] == "X" and lauta[2][2] == "X":
        voitto_x = True
        return voitto_x
    if lauta[0][0] == "X" and lauta[1][1] == "X" and lauta[2][2] == "X":
        voitto_x = True
        return voitto_x
    if lauta[0][2] == "X" and lauta[1][1] == "X" and lauta[2][0] == "X":
        voitto_x = True
        return voitto_x
    if lauta[0][0] == "X" and lauta[1][0] == "X" and lauta[2][0] == "X":
        voitto_x = True
        return voitto_x
    if lauta[0][1] == "X" and lauta[1][1] == "X" and lauta[2][1] == "X":
        voitto_x = True
        return voitto_x
    if lauta[0][2] == "X" and lauta[1][2] == "X" and lauta[2][2] == "X":
        voitto_x = True
        return voitto_x

def tasapeli():
    if lauta[0][0] != "-" and lauta[0][1] != "-" and lauta[0][2] != "-" and lauta[1][0] != "-" and lauta[1][1] != "-" and lauta[1][2] != "-" and lauta[2][0] != "-" and lauta[2][1] != "-" and lauta[2][2] != "-":
        tasapeli = True
        return tasapeli
        

def kaksi_pelaajaa():
    mones_vuoro = 1
    while True:
        if mones_vuoro == 1:
            piirra_lauta()
        if mones_vuoro % 2 == 1:
            print("O vuoro, valitse nappulan paikka")
        else: 
            print("X vuoro, valitse nappulan paikka")
        vaakarivi = int(input("Anna vaakarivi väliltä 1-3: "))
        pystyrivi = int(input("Anna pystyrivi väliltä 1-3: "))

        if lauta[int(vaakarivi)-1][int(pystyrivi)-1] != "-" or vaakarivi < 1 or vaakarivi > 3 or pystyrivi < 1 or pystyrivi > 3:
            print("Tuo siirto ei ole sallittu, yritä uudelleen!")
            vaakarivi = int(input("Anna vaakarivi väliltä 1-3: "))
            pystyrivi = int(input("Anna pystyrivi väliltä 1-3: "))

        if mones_vuoro % 2 == 1:
            lauta[vaakarivi-1][pystyrivi-1] = "O"
            piirra_lauta()
        if mones_vuoro % 2 == 0:
            lauta[vaakarivi-1][pystyrivi-1] = "X"
            piirra_lauta()
        mones_vuoro += 1
        if voitto_tarkistus_O() == True or voitto_tarkistus_X() == True:
            if voitto_tarkistus_O() == True:
                print("O voitti pelin!")
            if voitto_tarkistus_X == True:
                print("X voitti pelin!")
            break
        if tasapeli() == True:
            print("Tasapeli! Hyvä yritys!")
            break

def peli_konetta_vastaan():
    mones_vuoro = 1
    while True:
        if mones_vuoro == 1:
            piirra_lauta()
        if mones_vuoro % 2 == 1:
            print("O vuoro, valitse nappulan paikka")
        else: 
            print("X vuoro, kone pelaa vuoron")
        if mones_vuoro % 2 == 1:
            vaakarivi = int(input("Anna vaakarivi väliltä 1-3: "))
            pystyrivi = int(input("Anna pystyrivi väliltä 1-3: "))
            if lauta[int(vaakarivi)-1][int(pystyrivi)-1] != "-" or vaakarivi < 1 or vaakarivi > 3 or pystyrivi < 1 or pystyrivi > 3:
                print("Tuo siirto ei ole sallittu, yritä uudelleen!")
                vaakarivi = int(input("Anna vaakarivi väliltä 1-3: "))
                pystyrivi = int(input("Anna pystyrivi väliltä 1-3: "))
        if mones_vuoro % 2 == 0:
            vaakarivi = random.randint(1, 3)
            pystyrivi = random.randint(1, 3)
            if lauta[int(vaakarivi)-1][int(pystyrivi)-1] != "-" or vaakarivi < 1 or vaakarivi > 3 or pystyrivi < 1 or pystyrivi > 3:
                while lauta[int(vaakarivi)-1][int(pystyrivi)-1] != "-" and vaakarivi >= 1 and vaakarivi <= 3 and pystyrivi >= 1 and pystyrivi <= 3:
                    vaakarivi = random.randint(1, 3)
                    pystyrivi = random.randint(1, 3)
        if mones_vuoro % 2 == 1:
            lauta[vaakarivi-1][pystyrivi-1] = "O"
            piirra_lauta()
        if mones_vuoro % 2 == 0:
            lauta[vaakarivi-1][pystyrivi-1] = "X"
            piirra_lauta()
        mones_vuoro += 1
        if voitto_tarkistus_O() == True or voitto_tarkistus_X() == True:
            if voitto_tarkistus_O() == True:
                print("O voitti pelin!")
            if voitto_tarkistus_X == True:
                print("X voitti pelin!")
            break
        if tasapeli() == True:
            print("Tasapeli! Hyvä yritys!")
            break


if __name__ == "__main__":
    print("\nTervetuloa peliin!\n")
    print("Valitse haluatko pelata kaverin kanssa vai tietokonetta vastaan!\n")
    print("1. Peli kaverin kanssa \n2. Peli tietokonetta vastaan\n")
    valinta = int(input("Valitse 1. tai 2.\n"))
    if valinta < 1 or valinta > 2:
        valinta = int(input("Valitse sopiva luku!\n"))
    if valinta == 1:
        kaksi_pelaajaa()
    if valinta == 2:
        peli_konetta_vastaan()
