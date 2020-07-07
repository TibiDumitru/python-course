# Implementarea unui joc Spânzurătoarea (Hangman) în linie de comandă.
# Acesta va avea loc între un jucător și calculator, cel din urmă 
# alegând cuvântul ce trebuie ghicit. La pornirea jocului se va cere
# numele sau un nickname al jucătorului ce va fi folosit pe parcursul
# jocului.
# 
# Jocul Hangman va fi alcătuit din 4 componente principale:
# 1. Desenarea planșei de joc în toate stările ei posibile:
#    a. inițială (ca mai jos)
#    b. cap:  
#         O
#    c. cap și brațe:
#         O
#        / \
#    d. cap, brațe și trunchi:
#         O
#        /|\
#         |
#    e. complet (jucătorul a pierdut):
#         O
#        /|\
#         |
#        / \
# 2. Alegerea unui cuvânt la întâmplare dintr-un dicționar creat de tine
#    sau construit cu ajutorul unor biblioteci și oferirea unui mesaj
#    către utilizator de forma: K _ _ _ _ _ _ K pentru KNAPSACK
# 3. Logica prin care se verifică apartenența unei litere (inputul de la
#    utilizator) la cuvântul ales la începutul jocului și reafișarea noii
#    forme a cuvântului.
# 4. Actualizarea planșei în funcție de literele introduse greșit de către
#    utilizator și afișarea unui mesaj la final de tipul "Game Over user!" :D.
# 
# Mai jos se află un exemplu de cum arată planșa de joc la început și cum
# arată după ce ai pierdut. Dacă ai altă idee go for it :D
# 
#     --------
#    |       |
#    |       
#    |     
#    |      
#    |      
#    |
# -------
# 
#     --------
#    |       |
#    |       O
#    |      /|\
#    |       |
#    |      / \
#    |
# -------
import random
import urllib.request
import json


stage_a = """
        You are safe now!
            --------
           |       |
           |       
           |     
           |      
           |      
           |
        -------
        """

stage_b = """
        Not great, not terrible!
            --------
           |       |
           |       O
           |      
           | 
           | 
           |
        -------
        """

stage_c = """
        You can still do this!
            --------
           |       |
           |       O
           |      / \\
           | 
           | 
           |
        -------
        """

stage_d = """
        You are in danger!
            --------
           |       |
           |       O
           |      /|\\
           |       |
           | 
           |
        -------
        """

stage_e = """
        You are dead!
            --------
           |       |
           |       O
           |      /|\\
           |       |
           |      / \\
           |
        -------
        """

state = {0: stage_a, 1: stage_b, 2: stage_c, 3: stage_d, 4: stage_e}


def get_word():
    with urllib.request.urlopen("https://www.randomlists.com/data/words.json") as url:
        data = json.loads(url.read().decode())
        while True:
            chosen_word = random.choice(data['data']).upper()
            if len(chosen_word) > 4:
                return chosen_word


def play(username, chosen_word):
    mistakes = 0
    finished = False
    no_letters = len(chosen_word)
    first = chosen_word[0]
    last = chosen_word[no_letters - 1]
    current_word = no_letters * ['_']
    missing_letters = set()

    for i in range(no_letters):
        if chosen_word[i] == first:
            current_word[i] = first
        elif chosen_word[i] == last:
            current_word[i] = last
        else:
            missing_letters.add(chosen_word[i])

    while not finished:
        print(state[mistakes])
        if mistakes == 4:
            print('Sorry, ' + username + '! GAME OVER!')
            finished = True
            continue
        print("".join(current_word))
        print()
        print('Choose a letter:')
        chosen_letter = input()
        if not chosen_letter.isalpha() or len(chosen_letter) > 1:
            print('Wrong input, try again!')
            continue
        if chosen_letter.islower():
            chosen_letter = chosen_letter.upper()
        if chosen_letter in missing_letters:
            print('Good job, ' + username + '!')
            for i in range(no_letters):
                if chosen_word[i] == chosen_letter:
                    current_word[i] = chosen_letter
            missing_letters.remove(chosen_letter)
            if len(missing_letters) == 0:
                print('\nCongratulations, ' + username + '! You WIN!')
                print('The word was: ' + "".join(current_word))
                finished = True
        else:
            print('Nope, try something else!')
            mistakes += 1


def main():
    print('============== Welcome to Hangman! ================')
    print('Please choose a nickname: ')
    username = input()
    print("Let's play, " + username + "!")
    while True:
        chosen_word = get_word()
        play(username, chosen_word)
        print()
        print('===============================================')
        print('Wanna play again, ' + username + '? (Y / N)')
        ans = input().upper()
        if ans == 'N':
            break


if __name__ == "__main__":
    main()
