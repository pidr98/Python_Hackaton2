# Python_Hackaton2 - 03.Hangman

New features:
1. Player can see letters that he/she used and if the letter is used, user have to insert other letter again
2. Add 'graphic' version of hangman
3. If user lost, display red-coloured hangman

1.In first part, to show player what letters he used, I added if...else statement. If the guessed is not in list of guessed letters then it adds guess to guessed letter and prints list out.
Depending on place where it was used, it varies a little (else deleted and print moved to if).
As for already used letters, I created if statement that if letter was used, it goes back to asking for input.
<br/>2.For adding 'graphic' version of hangman I created module, that store various versions of hangman using list.
Then, after every bad move, depending on how many tries we still have, we print same index in list as number of tries left.
<br/>3.For color, I installed 'termcolor' in windows cmd using pip install, then imported it to the file that contained graphic of hangman.
Then, in first index, I used colored(-graphic of hangman-, -color-).