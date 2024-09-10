"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Michaela Žák Štarková
email: michaela.zakstarkova@gmail.com
discord: michaelazak_07263
"""                      

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
which are about 300 feet thick. ''',
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

# VÝBĚR UŽIVATELE
USERS_PASSWORDS = {
        "bob": "123",
        "ann": "pass123",
        "mike": "password123",
        "liz": "pass123"
        }
oddelovac = "-" *50

user_name = input("Enter your user name: ")
password = input("Enter your password: ")



if USERS_PASSWORDS.get(user_name) == password: 
    print(f"username: {user_name}\npassword: {password}")
    print(f"{oddelovac}\nWelcome to the app, {user_name.capitalize()}.\nWe have 3 texts to be analyzed.\n{oddelovac}")
    

    selection = input("Enter a number btw. 1 and 3 to select: ")
    titles = 0
    capitals = 0  
    lower_case = 0
    digits = 0
    digits_sum = []
    lomitko = "|"

    if selection.isnumeric() is True:
    
        if int(selection) in range(1, 4):

            text_split = TEXTS[int(selection)-1].split()
            wordcount = len(text_split)

            count_list = []


            for word in text_split: # Opraveno dle poznámek lektora č.2

                if word[0].istitle(): # VYMAZÁNO "and word.isalpha()"
                    titles += 1
                        
                if word.isupper() and word.isalpha():
                    capitals += 1

                if word.islower(): 
                    lower_case += 1

                if word.isdigit():
                    digits += 1
                    digits_sum.append(int(word)) 

                new_word = word.replace(".", "").replace(",", "").replace("-", "") 
                count = len(new_word)   
                count_list.append(count)    
                count_words = {i: count_list.count(i) for i in range(1, 12)} # Opraveno dle poznámek lektora č. 4

               
                # max_occurence = max(count_list.count(x) for x in range(1, 12))
                # space = max_occurence + 2            

            print(f"{oddelovac}\n"
                "There are " + str(wordcount) + " words in the selected text.",
                "There are " + str(titles) + " titlecase words.",
                "There are " + str(capitals) + " uppercase words.",
                "There are " + str(lower_case) + " lowercase words.",
                "There are " + str(digits) + " numeric strings.",
                "The sum of all the numbers is " + str(sum(digits_sum)) + ".",
                sep="\n"
                )
          
           
            print(f"{oddelovac}\nLEN|  OCCURENCES      |NR.\n{oddelovac}")
           
            
            for length, count in count_words.items():
                print(f"{length:<3}| {"*"*count:<17}| {count:<10}")

        else:
            print(f"Enter {selection} cannot be selected.") # Oprava dle poznámek lektora č.1
    
    else:
        print("Enter is not numerical.")
else:
    print("Wrong user name or password. Terminating the program..")

# Opraveno dle pozámek lektora: 
# 1. Uživatelský vstup pro výběr textu není ošetřen: při zadání většího čísla než 3 a menšího než 0, program spadně na KeyError. Určitě je potřeba program řízeně ukončit.
# 2. Neefektivní statistiky: používáš pro každou statistiky jeden for cyklus, lze to napsat v jednom for cyklu. - Neberu jako chybu, spíše doporučení
# 3. Statisika pro slova začínající velkým písmenem: není úplně správně napsaná, nech si vypsat co se vše teď počítáš do titlecase
# 4. Nesedí ti hodnoty v grafu, potřeba upravit.
# 5. Kód je potřeba odevzdat .py souboru bob
