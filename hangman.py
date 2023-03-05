import os
import sys
import random
play = True
choose_category=0
rand_word=""
play_number = 0
win_number = 0
letter = []  # Slit ramdom word to separately letter
topic = [["Russia","Germany","United Kingdom","France","Italy","Spain","Ukraine","Poland","Netherlands","Finland","Vietnam","Thailan","Lao","Campodia","China"],#topic 1
         ["Audi","BMW","Bentley","Chevrolet","Dodge","Ford","Honda","Hyundai","Infiniti","Jaguar","Jeep","Kia","Land Rover","Lexus","Lincoln"],#topic 2
         ["Dog","Bear","Elephant","Polar bear","Turtle","Tortoise","Crocodile","Rabbit","Porcupine","Har","Hen","Pigeon","Albatross","Crow","Fish"],#topic 3
         ["apples","pears","oranges","grapefruits","mandarins","limes","apricots","peaches","plums","tropical","exotic","bananas","mangoes","berries","strawberries"]]#topic 4

#Define for each topic    
def def_category(choose_category):
    if choose_category == 1:
        return ("Countries")
    if choose_category == 2:
        return ("Car brands")
    if choose_category == 3:
        return ("Animals")
    if choose_category == 4:
        return ("Fruits")

#Draw function
def draw_hangman(player_lives):
	if player_lives == 1:
		return"""
		_______
		|     |
		|     
		|
		|
		|
		|
		|________
		|        |
		"""
	elif player_lives == 2:
		return"""
		_______
		|     |
		|     O
		|     |
		|
		|
		|
		|________
		|        |
		"""
	elif player_lives == 3:
		return"""
		_______
		|     |
		|     O
		|    /|\ 
		|
		|
		|
		|________
		|        |
		"""
	elif player_lives == 4:
		return"""
		_______
		|     |
		|     O
		|    /|\ 
		|    / \ 
		|    
		|
		|________
		|        |
		"""
	elif player_lives == 5:
		return"""
		_______
		|     |
		|     l0
		|    |||
		|     |
		|    | |
		|
		|________
		"""
	elif player_lives == 6:
		return"""
⠛⠛⣿⣿⣿⣿⣿⡷⢶⣦⣶⣶⣤⣤⣤⣀⠀⠀⠀
⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀
⠀⠀⠀⠉⠉⠉⠙⠻⣿⣿⠿⠿⠛⠛⠛⠻⣿⣿⣇⠀
⠀⠀⢤⣀⣀⣀⠀⠀⢸⣷⡄⠀⣁⣀⣤⣴⣿⣿⣿⣆
⠀⠀⠀⠀⠹.⠀⠀⠀⣿⣧⠀⠹⣿⣿⣿⣿⣿⡿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠿⠇⢀⣼⣿⣿⠛⢯⡿⡟
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠦⠴⢿⢿⣿⡿⠷⠀⣿⠀
⠀⠀⠀⠀⠀⠀⠀⠙⣷⣶⣶⣤⣤⣤⣤⣤⣶⣦⠃⠀
⠀⠀⠀⠀⠀⠀⠀⢐⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⠟
		"""	

#Main function
def game_start(letter):
    count = 0
    winner = False
    ori_len = len(letter) # Original leng of letter
    results=[]
    while count < 5:
        guess_letter = input("Player 2 guess alphabet letter of random word: ") #alphabet letter (a,b,c...)
        #print("DEbug",letter)
        for c in range(len(letter)): #go through position of array
            if guess_letter.lower()==letter[c]:
                results.append(letter[c])
                print("That's righ letter. Keep going:")
                print("Word: ",results)
                letter.pop(c)
                #print("DEbug",len(results),ori_len)
                if len(results)==ori_len:
                    winner=True
                    #print("DEbug",len(results),ori_len)
                    return winner
                break
            else:
                count += 1
                print("That's wrong letter. Try again:")
                print(draw_hangman(count))
                print("Word: ",results)
                break    
    return winner

while play == True:
    start = int(input("1. Play\n2. Exit")) #only number 
    letter.clear() #reset letter 
    #print("DEbug",letter)
    if start == 1:
        choose_category = int(input("\nPlayer 1 enter topic number 1.countries; 2.car brands; 3.animals; 4.fruits: "))
        print("Your category is: ",def_category(choose_category))
        rand_word = random.choice(topic[choose_category - 1]) #Random choose one of the word in this topic , -1 because first position in array is 0
        print ("Hint!: Your random word is ", rand_word)
        print ("--------------------------------------------")
        for i in rand_word.lower():
            letter.append(i)
        if game_start(letter) == False:
            print("Player 2 LOSE! Do you want to play again?")
        else:
            print("Player 2 WIN!  Do you want to play again?")
            win_number += 1
        play_number += 1
    else:
        play = False
        print("How many time did you play: ",play_number)
        print("How many time did you win: ",win_number)
        