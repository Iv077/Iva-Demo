THE FINAL GAME 



It's the typical rock, paper, scissors game but made more interesting 
by adding the lizard and spoke options. 
The game was originally created by Sam Kass with Karen Bryla and it 
became popular with the sitcom Big Bang Theory.

----------------------------------------------------------------------------

Rules:
The game is an expansion on the game Rock, Paper, Scissors. 
Each player picks a variable and reveals it at the same time. 
The winner is the one who defeats the others. In a tie, the process is 
repeated until a winner is found.

Scissors cuts Paper
Paper covers Rock
Rock crushes Lizard
Lizard poisons Spock
Spock smashes Scissors
Scissors decapitates Lizard
Lizard eats Paper
Paper disproves Spock
Spock vaporizes Rock
Rock crushes Scissors



Requirements:

What is needed to be able to play this game is the simple installation 
of the LED panel to be able to observe the development of the animations 
and the Python program to be able to execute the game code. In case you 
don't have it, you can check the following links to download what you need:

Simulator: https://github.com/Iv077/Iva-Demo/tree/main/simulator

Code of the game: https://github.com/Iv077/Iva-Demo/tree/main/Codes

Python instalation: https://www.python.org/downloads/



No special configuration or trubleshooting process needed.




CODE DESCRIPTION:

The game starts with blue and orange lights coming from the top and bottom 
of the panel, they intersect and the text 'WELCOME' appears scrolling from 
left to right and in predetermined colors simulating the rainbow. After that,
'PLAYER' appears in the same way as 'WELCOME' with the only difference that
this time the colors of the word are random and constantly changing which 
is finalized by the 'turning off' of all the leds from the middle of the 
panel in the right and left direction at the same time.

Once the sequence is finished, a definition will be opened in which we 
encompass the entire game so that when it is called, the production of the 
game is simple. At the beginning of the definition, the first text appears, 
which will not be reproduced in LEDs, but separately, since it is the one 
that gives us the first possibility of choosing, in this case, the weapon: 
rock, paper, scissors, lizard, spock .

When choosing our weapon, the panel has a random choice of theirs. When the 
choice is over, LEDs simulating 'loading' or 'travel to the future' are 
played to make it appear that the panel is thinking about its choice, 
followed by the two weapons on the panel that approach from the ends to the 
center and are divided by a 'vs' that symbolizes the confrontation of said. 
This last action is repeated in a cycle 2 times.

After that we can see how the text appears in LEDS 'WINNER' or 'LOSER' that 
does not imply our position. In the event of a tie, 'SORRY I DON'T KNOW WHO 
IS THE WINNER, PLEASE TRY AGAIN' appears on the interactive panel.

After which the game ends and we are asked if we want to play again. With 
two possible options 'YES' or 'NO'. If we choose 'NO' or write something 
random, the text "SAD, IT WAS A PLEASURE TO PLAY WITH YOU" will appear, but 
if we choose 'YES' the game will start again from the first choice.


