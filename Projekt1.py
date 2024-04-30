"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Jakub Dostál
email: gozo.jakub@gmail.com
discord: gozo197, Gozo#2494
"""
import texts
import uzivatele

def add_line():
    print("-" * 20)

def check_user(username, password):
    if username in uzivatele.users and uzivatele.users[username] == password:
        return True
    else:
        return False

def select_analyze_text():
    try:
        select = int(input("Zadej hodnotu 1-3 pro vyber textu: "))
        add_line()
        if select < 1 or select >3:
            print("Neplatna volba, program skonci")
            return
        text = (texts.TEXTS[select-1])
        print(text)
    except ValueError:
        print("Nebylo vybrano cislo, program skonci")
        return
    
    words = text.split()
    word_count = len(words)
    title_count = sum(1 for word in words if word.istitle())
    upper_count = sum(1 for word in words if word.isupper())
    lower_count = sum(1 for word in words if word.islower())
    numbers = [int(word) for word in words if word.isdigit()]
    number_count = len(numbers)
    sum_numbers = sum(numbers)
    add_line()
    print(f"Pocet slov: {word_count}")
    print(f"Pocet slov zacinajicich velkym pismenem: {title_count}")
    print(f"Pocet slov psanych velkymi pismeny: {upper_count}")
    print(f"Pocet slov psanych malymi pismeny: {lower_count}")
    print(f"Pocet cisel: {number_count}")
    print(f"Suma vsech cisel: {sum_numbers}")
    add_line()
    print(f"{'*' * word_count} {word_count}")
    print(f"{'*' * title_count} {title_count}")
    print(f"{'*' * upper_count} {upper_count}")
    print(f"{'*' * lower_count} {lower_count}")
    print(f"{'*' * number_count} {number_count}")
    
username = input("Zadejte uzivatelske jmeno: ")
password = input("Zadejte heslo: ")
if check_user(username, password):
    add_line()
    print(f"Prihlaseni uspesne. Vitej uzivateli, {username}")
    print("V nabidce jsou 3 texty pro analyzu")
    add_line()
    select_analyze_text()
    add_line()
else:
    print("Prihlaseni selhalo. Neplatne uzivatelske jmeno nebo heslo.")
    exit()

