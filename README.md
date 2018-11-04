# Tic-Tac-Toe
A take on the classic noughts and crosses game. Player vs Computer

Additional info on how the game works rather than using comments in the files.

Main.py file:

      The game can be run from here.
      The file can be broken down into 4 parts:
      
            Setting up the game - seen from Start the Game comment
            Computer's move - seen from Perfom actions for computer comment
            Player's move - seen from Perform actions for player comment
            Checking the game state - seen from Check isMatch() if game loop is between 3 and 8 comment
            
Classes.py file:

      Most of the classes are self-explanatory
      For the Computer class its function is dependant on the difficulty level
      The computer is designed to perform 3 particuar functions in order:
      
            Check if possible to win game - seen from compSelection method
            Check if possible to prevent player winning - seen from defend method
            
            if level 1 - random selection is made
            if level 2 - check if possible to make an intelligent move - seen from think method
       
