GAME HANGMAN

Description:

I) How to play?
1) Player 1 choose one of two option: 1.Play, 2.Exit to start the game.
1) Player 1 choose one of four option that player 1 would like to (1.fruits, 2.animals, 3.car brands, 4.countries).
2) The game will randomly choose one of 15 words in that category have been chosen.
3) A hint appear with 3 letter of the word which give an opportunity to player 2 .
3) Player 2 guess each letter of the random word.
After giving a guess, program print out the result.
4) Every time is a wrongly guessed letter, the hanged man picture will appear.
5) Player 2 wins if the hanged man picture is not finalized.
6) When the game has stopped the program should display number of plays and number of wins.
7) The program allow user to play over and over again until user chooses to exit using it.
9) In case, user input an incorrect option, the program allow user to play again and notify an message "Your input is invalid! Play again!" 
10) The program allow user to input Upper or Lower character.

II) Example:

------GAME HANGEMAN-------
--------------------------------------------
1. Play
2. Exit
Choose: klajskldjf
Your input is invalid! Play again!
--------------------------------------------
1. Play
2. Exit
Choose: 9
Your input is invalid! Play again!
--------------------------------------------
1. Play
2. Exit
Choose: 1

Player 1 enter topic number 1.countries; 2.car brands; 3.animals; 4.fruits: 
Choose: 2
Your category is:  Car brands
Hint!: The 3 random word's letter: I n f
--------------------------------------------
Player 2 guess alphabet letter of random word: i
Word:  ['i']
That's righ letter. Keep going:
-------------------------------
Player 2 guess alphabet letter of random word: nf
Word:  ['i']
That's wrong letter. Try again:

		_______
		|     |
		|     
		|
		|
		|
		|
		|________
		|        |
		
-------------------------------
Player 2 guess alphabet letter of random word: n
Word:  ['i', 'n']
That's righ letter. Keep going:
-------------------------------
Player 2 guess alphabet letter of random word: f
Word:  ['i', 'n', 'f']
That's righ letter. Keep going:
-------------------------------
Player 2 guess alphabet letter of random word: sadf
Word:  ['i', 'n', 'f']
That's wrong letter. Try again:

		_______
		|     |
		|     O
		|     |
		|
		|
		|
		|________
		|        |
		
-------------------------------
Player 2 guess alphabet letter of random word: asdf
Word:  ['i', 'n', 'f']
That's wrong letter. Try again:

		_______
		|     |
		|     O
		|    /|\ 
		|
		|
		|
		|________
		|        |
		
-------------------------------
Player 2 guess alphabet letter of random word: 
Word:  ['i', 'n', 'f']
That's wrong letter. Try again:

		_______
		|     |
		|     O
		|    /|\ 
		|    / \ 
		|    
		|
		|________
		|        |
		
-------------------------------
Player 2 guess alphabet letter of random word: 
Word:  ['i', 'n', 'f']
That's wrong letter. Try again:

		_______
		|     |
		|     l0
		|    |||
		|     |
		|    | |
		|
		|________
		
-------------------------------
The random word is:  Infiniti
Player 2 LOSE! Do you want to play again?
--------------------------------------------
--------------------------------------------
1. Play
2. Exit
Choose: 2
---------Results--------
How many time did you play:  1
How many time did you win:  0
