"""
readme.txt
~Brief Summary of the Project~
Rie Kurita
16 November, 2018
"""

Background:
I used to play the board game called "Othello" when I was young with my sister.
Othello is an universal game and played by various people from children to
adults. It would be a great recreation if you could play it on your computer
by yourself.

Summary of game:
Right after you start running the file "final.py", the game screen of game board
with the initial four stone at the middle. Your color is "black" so you can
select any square that can sandwitch white stones to make them reversed to your
color. Computer will automatically place its stone for the next tern and you can
choose your square again. You keep choosing squares until there's no square that
either you or computer can choose or all squared are filled with stones. If you
have more stones than computer(= if there are more black stones than white stones),
you win! The screen will show whether you won or lost and options of whether you want
To, start a new game or not. You can click either "Yes"(which shows a new game screen)
or "No"(which closes the screen and exit the system).When you want to quit during the 
game, you can just click "Quit" at the right bottom corner.

What is needed to run the game:
- main program file(final.py)
- class files(board.py, game_state.py, graphics.py)
This program has two classes, GameState and Board. GameState class is to keep track
on the state of game(color of each square, the number of each color's stones,
clickable squares etc.) and Board class is to reflect those on the screen.
- installation of pygame, copy, time
The program is depending upon pygame to get a mouse input and flip the image when
its color is changed. In addition, to make a computer player anticipate the next
board, it uses deepcopy from copy and to show a certain screen for a certain time,
it uses time.
- images file(black.jpg, white.jpg, empty.jpg, board.jpg)
The program requires those four images and these are going to be used as images
for stones and a board.

Future prospects:
This game can be played by one player against computer, however, the computer moves
are the move that can get the most stones of computer player in the next state of
the game. For future improvement, it can be considered to make the computer smarter
by differentiating corners and edges and to make several levels.

Acknowledgement:
Appreciate to Jeff Ondich and Eva Grench who have helped me with making this
program a lot.
