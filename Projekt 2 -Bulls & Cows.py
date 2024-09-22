"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Alena Rusínová
email: Rusinova.a@email.cz
discord: Alena Rusínová #0364

"""

print("Hi, there!")
print("-" * 47)
print("I've generated a random 4 digit number for you.\nLet's play a bulls and cows game.")
print("-" * 47)

 
import random  
import datetime

# Začátek počítání času
start = datetime.datetime.now()
  
# Číslo převedené na seznam stringů:
def cislo_str(pocitac):
    cislo = []
    for i in str(pocitac):
        cislo.append(i)
    return cislo
 
# Číslo nesmí obsahovat duplicitu         
def bez_opakovani(pocitac): 
    soucet_cislic = cislo_str(str(pocitac))  
    if len(soucet_cislic) == len(set(soucet_cislic)): 
        return True
    else: 
        return False
    
# Číslo musí být čtyřmístné
def nahodne_cislo(): 
    while True: 
        pocitac = random.randint(1000,9999) 
        if bez_opakovani(pocitac): 
            return pocitac
    
# Výsledek bull and cow
def vysledek(pocitac,hrac): 
    bull_cow = [0,0] 
    computer = cislo_str(pocitac) 
    guess = cislo_str(hrac) 
      
    for i,j in zip(computer,guess): 
 
        if j in computer: 
            
            bull_cow[1] += 1
           
            if j == i: 
                bull_cow[0] += 1
                     
    return bull_cow 
      
pocitac = nahodne_cislo()
#print(pocitac)
pocet_pokusu = 0

# Vyhodnocení čísla zadaného hráčem
while True:       
    
    hrac = (input("Zadej číslo: "))
    print("-" * 47)
    print(">>>",hrac)

    if not bez_opakovani(str(hrac)): 
        print("Číslo se nesmí opakovat")
        pocet_pokusu += 1 
        continue

    if not hrac.isdigit():
        print("Nebyly zadány číselné znaky")
        pocet_pokusu += 1
        continue

    if int(hrac) < 1000 or int(hrac) > 9999: 
        print("Číslo není čyřmístné")
        pocet_pokusu += 1
        continue

    bull_cow = vysledek(pocitac,hrac) 
    print(f"{bull_cow[0]} bulls, {bull_cow[1]} cows") 
    pocet_pokusu += 1

    if bull_cow[0] == 4: 
        print("Correct, you've guessed the right number in 4 guesses!") 
        break

    if bull_cow[1] == 0: 
        print("That's {amazing, average, not so good, ...}")
        
# Konec měření času uhádnutím čísla
stop = datetime.datetime.now()
diff = stop - start

# Vypsání měřených parametrů
print(f"Uplynulý čas: {diff}") 
print("Počet pokusů:", pocet_pokusu)


