# Tablut-MALI 
University project for Fundamentals for Artificial Intelligence. It's a Tablut player that plays according to Ashton's rules.

## How does it work?
It's quite simple. Magic.

Just kidding, after all MALI stands for Much Artificial and little Intelligent.
We decided to use a state search approach by implementing Minimax, a recursive backtracking algorithm that is used in decision making and game theory to find the optimal move for a player, assuming that your opponent also plays optimally. The initial depth when starting the search for the next move is 3 but if it reaches a timeout state (the timeout parameter passed to the script minus 15-20 seconds) it changes to a lower depth, in order to find a faster but "not so smart" solution. 
The Minimax algorithm at its root (also literally, it generates a decision tree) is powered by some heuristics defined by us, which define a score (increase for "max" black, decrease for "min" white). Among the heuristics we have: 
- If black surrounds the king it wins, so that's good, like a thousand points to Griffindor good.
- If the king escapes then white wins, so we lower the score a lot
- If a piece can eat/block an oppenent piece from it's position
- The amount of black pieces near the king.
- The amount of potential good black/white moves.
- ecc. -> look at heuristics.py

By using this kind of approach we can play at our best both as white and black.


## How to run the player: 

- Install python3 and numpy library (they have already provided in the virtual machine)
- Open a new terminal and run the following command: "./AI_more_A_little_I.sh <colorname> <timeout> <IP address>



TODO: improve heuristics (Tablut is a complex game and this approach is heavy on us developers finding good stategies) and optimize the decision tree generation in order to increase the initial depth level while still being able to return a move in satisfying time.


## Special thanks to: 
Every collaborator. Good guys.
But also to this bidoof:


He helped us smile when we couldn't. 




