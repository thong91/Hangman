import os
import sys
import random
play = True
choose_category=0
rand_word=""
guess_times = 5 #5 time to guess
play_number = 0
win_number = 0
topic = [["car", "caro", "carole"],#topic 1
         ["dog", "doga", "dogalo"],#topic 2
         ["apple", "appleni", "applenol"],#topic 3
         ["hot", "cold", "coldest"]]#topic 4

#Define for each topic    
def def_category(choose_category):
    if choose_category == 1:
        return ("Cars")
    if choose_category == 2:
        return ("Dogs")
    if choose_category == 3:
        return ("Apples")
    if choose_category == 4:
        return ("Weather")

#Draw function
def visuals(player_lives):
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
def game_start(rand_word):
    count = 0
    winner = False
    while count < 5:
        guess_word = input("Player 2 guess: ")
        if guess_word==rand_word:
            winner = True
            break
        else:
            count += 1
            print(visuals(count))
    return winner

#Main program
while play == True:
    start = int(input("1. Play\n2. Exit")) #only number 
    if start == 1:
        choose_category = int(input("\nPlayer 1 enter topic number (1.Cars; 2.Dogs; 3.Apples;4.Weather) : "))
        print("Your category is: ",def_category(choose_category))
        rand_word = random.choice(topic[choose_category - 1]) #Random choose one of the word in this topic , -1 because first position in array is 0
        print ("Your random word is: ", rand_word)
        if game_start(rand_word) == False:
            print("Player 2 LOSE! Do you want to play again?")
        else:
            print("Player 2 WIN!  Do you want to play again?")
            win_number += 1
        play_number += 1
    else:
        play = False
        print("How many time did you play: ",play_number)
        print("How many time did you win: ",win_number)
