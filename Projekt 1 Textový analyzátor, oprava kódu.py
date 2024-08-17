# Projekt-1
"Textový analyzátor"

"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Alena Rusínová
email: rusinova.a@email.cz
discord: Alena Rusínová#4931
"""

# Přihlašovací jméno a heslo:
user = input("Username:")
password = input("Password:")
print("-" * 40)

# Registrovaní uživatelé:
users = {"Bob": "123", "Ann": "pass123", "Mike": "password123", "Liz": "pass123"}

# Ověření vstupních údajů:
if users.get(user) == password:
    print("Welcome to the app,", user)
    print("We have 3 texts to be analyzed.")
    print("-" * 40)
    
else: 
    print("unregistered user, terminating the program")  
    exit()

# Zadané texty:
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]    
    
# Výběr textu uživatelem:
text_cislo = input("Enter a number btw. 1 and 3 to select:")
# Špatně zadané číslo textu
if text_cislo.isalpha():
    print("Wrong text number.")

elif int(text_cislo) not in range(1,4):
    print("Wrong text number.")

else:
    text = int(text_cislo) - 1
    print("-" * 40)

    # Počet slov v textu:    
    pocet_slov = []
    for slovo in TEXTS[text].split(): 
        pocet_slov.append(slovo)

    print("There are", len(pocet_slov)," words in the selected text.")

    # Počet slov s velkým písmenem na začátku slova:          
    slova_velke_pismeno = []

    for slovo in TEXTS[text].split(): 
         if slovo[0].isupper():
             slova_velke_pismeno.append(slovo)
        
    print("There are", len(slova_velke_pismeno) ," titlecase words")
    
    # Počet slov se všemi velkými písmeny:
    slova_velka_pismena = []

    for slovo in TEXTS[text].split(): 
        if slovo.isupper() and slovo.isalpha():
            slova_velka_pismena.append(slovo)
            
    print("There are", len(slova_velka_pismena)," uppercase words.")

    #Počet slov s malými písmeny:    
    slova_male_pismeno = []

    for slovo in TEXTS[text].split(): 
        if slovo[0].islower():
            slova_male_pismeno.append(slovo)
        
    print("There are", len(slova_male_pismeno)," lowercase words.")

    # Počet čísel v textu:    
    cisla = []

    for cislo in TEXTS[text].split(): 
        if cislo.isdigit():
            cisla.append(cislo)
        
    print("There are", len(cisla)," numeric strings.")

    # Součet čísel v textu:    
    vysledek = []

    for num in TEXTS[text].split():
         if num.isdigit():
             vysledek.append(num)

    celkova_suma = sum(int(cislo) for cislo in vysledek)

    print("The sum of all the numbers", celkova_suma)

    # Délka slov textu + grafické zobrazení
    char_to_remove = "."
    uprava_text = TEXTS[text].replace(char_to_remove, "")

    char_to_remove = ","
    cleaned_text = uprava_text.replace(char_to_remove, "")

    pocet_slov = []
    for slovo in cleaned_text.split():
        pocet_slov.append(slovo)

    print("-" * 40)
    print(" LEN|","    OCCURENTES","    |NR")
    print("-" * 40)
    
    Delka_slov = []
    for slovo in pocet_slov:
        hodnota = len(slovo)
        Delka_slov.append(hodnota)

    counts = {}
    for cislo in Delka_slov:
        if cislo not in counts:
            counts[cislo] = 1
        
        else:
            counts[cislo] = counts[cislo] + 1
        
    for klic, hodnota in sorted(counts.items()):
        print(" "*(2 - len(str(klic))),klic,"|","*"*klic," "*(17 - klic),"|", hodnota)        

    

   
