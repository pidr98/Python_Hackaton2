# Python_Hackaton2

Based on hangman game made on last hackaton, I added new features:
1. Player can see letters that he/she used and if the letter is used, user have to insert other letter again
2. Add titled hangman in terminal
3. If user lost, display red-coloured hangman

1.In first part, to show player what letters he used, I added if...else statement. If the guessed is not in list of guessed letters then it adds guess to guessed letter and prints list out.
Depending on place where it was used, it varies a little (else deleted and print moved to if).
As for already used letters, I created if statement that if letter was used, it goes back to asking for input.
<br/>2.For adding 'graphic' version of hangman I created module, that store various versions of hangman using list.