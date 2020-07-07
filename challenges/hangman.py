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
