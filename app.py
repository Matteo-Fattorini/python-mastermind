# @author Matteo Fattorini

import random


randomNumber = random.sample(range(1, 9), 5)
print(randomNumber)

guessedNumber = []
answer = ""
game = True
attempts = 0

print("Benvenuto in Mastermind! Cerca di indovinare la sequenza numerica di 5 cifre generata dal pc! Ogni volta che inserisci un numero avrai in risposta una 'X' per ogni numero corretto e nella posizione giusta e un 'O' per ogni numero corretto ma in posizione errata. Buona Fortuna! ")


while game:
    userInput = str(input("Inserisci una sequenza di 5 numeri unici\t"))
    while (len(userInput) != len(set(userInput)) or not(userInput.isdigit()) or len(userInput) != 5):
        userInput = str(input("Inserisci una sequenza di 5 numeri unici\t"))
    for num in userInput:
        guessedNumber.append(num)
        

        
    for i in range(len(guessedNumber)):
        if int(guessedNumber[i]) == int(randomNumber[i]):
            answer+= "X "
        elif int(guessedNumber[i]) in randomNumber:
            answer += "O "
        else: 
            answer += "_ "
            
    print(answer)
    
    if answer.replace(" ", "") == "XXXXX":
        print("Hai vinto!! Ci hai messo {} tentativi!\n".format(attempts))
        game = False
        again = input("Vuoi giocare ancora? y/n\n").lower()
        while again != "y" and again != "n":
            again = input("Vuoi giocare ancora? y/n\n").lower()
        if again == "y":
            game = True
            randomNumber = random.sample(range(1, 9), 5)
            attempts = 0
            guessedNumber = []
            answer = ""
            
    else: 
        answer= ""
        guessedNumber = []
        attempts += 1
        

    