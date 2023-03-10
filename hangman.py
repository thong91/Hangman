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
    else:
        return None
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
    count_w = 0  #count_w wrong
    winner = False
    ori_len = len(letter) # Original leng of letter
    results=[]
    count_r =0 #count_w right
    for a in range(ori_len):
        results.append('_ ')
    while count_w < 5:
        print("Word: ", results)
        guess_letter = input("Player 2 guess alphabet letter of random word: ") #alphabet letter (a,b,c...)
        if guess_letter.lower() in letter:
            #process for array of results
            posit = letter.index(guess_letter.lower())
            results.insert(posit,letter[posit])
            results.pop(posit+1) #remove the next position of inserted position
            count_r  += 1 #count_w right
            #print("Word: ", results)
            print("That's righ letter. Keep going:")
            print("-------------------------------")
            #process for array of letter
            letter.insert(posit,'_ ')
            letter.pop(posit+1) #remove correct letter from array
            if count_r ==ori_len:
                winner=True
                return winner
            else:
                continue
        else:
            count_w += 1 #count_w wrong number
            #print("Word: ",results)
            print("That's wrong letter. Try again:")
            print(draw_hangman(count_w))
            print("-------------------------------")   
    return winner

print ("------GAME HANGEMAN-------")
while play == True:
    letter.clear() #reset letter 
    #---input topic
    #try:
    print ("--------------------------------------------")
    start = int(input("1. Play\n2. Exit\nChoose: ")) #only number 
    if start == 1:
        choose_category = int(input("\nPlayer 1 enter topic number 1.countries; 2.car brands; 3.animals; 4.fruits: \nChoose: "))
        if def_category(choose_category)==None:
            print("Your input is invalid! Play again!")
            continue
        print("Your category is: ",def_category(choose_category))
        rand_word = random.choice(topic[choose_category - 1]) #Random choose one of the word in this topic , -1 because first position in array is 0
        print ("Hint!: The 3 random word's letter:", rand_word[0],rand_word[1],rand_word[2])
        print ("--------------------------------------------")
        for i in rand_word.lower():
            letter.append(i)
        if game_start(letter) == False:
            print("The random word is: ",rand_word)
            print("Player 2 LOSE! Do you want to play again?")
            print ("--------------------------------------------")
        else:
            print("The random word is: ",rand_word)
            print("Player 2 WIN!  Do you want to play again?")
            print ("--------------------------------------------")
            win_number += 1
        play_number += 1
    elif start == 2:
        play = False
        print("---------Results--------")
        print("How many time did you play: ",play_number)
        print("How many time did you win: ",win_number)
    else:
        print("Your input is invalid! Play again!")
        continue
    #except:
    #    print("Your input is invalid! Play again!")   
