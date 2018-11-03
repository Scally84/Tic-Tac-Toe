from Classes import GameSetting
from Classes import Player
from Classes import Computer
from Classes import Grid
from Classes import WaysToWin
from Classes import isMatch

import random
import time

'''Start the Game'''
def runGame():
    
    '''Set up the game and creating objects'''

    #Set print break
    def pb():
        print("")
        print("")

    #Creating level of difficulty array
    difficultyLevelArray = [1,2]

    #Setting the 8 ways to win
    across1 = [7,8,9]
    across2 = [4,5,6]
    across3 = [1,2,3]
    down1 = [7,4,1]
    down2 = [8,5,2]
    down3 = [9,6,3]
    highLow = [7,5,3]
    lowHigh = [1,5,9]

    #Creating GameSetting object
    setting = GameSetting()

    #Creating Player object
    player = Player()

    #Creating Computer object
    computer = Computer()

    #Creating Grid object
    gridDisplay = Grid()

    #Creating a waysToWin object
    w2w = WaysToWin()

    #Adding the 8 ways to win into w2w' wtwArray
    w2w.setWtwArray(across1)
    w2w.setWtwArray(across2)
    w2w.setWtwArray(across3)
    w2w.setWtwArray(down1)
    w2w.setWtwArray(down2)
    w2w.setWtwArray(down3)
    w2w.setWtwArray(highLow)
    w2w.setWtwArray(lowHigh)

    '''Run Game'''

    print("xxx-----------------------------------------------------------------------xxx")                                    
    print("")
    print("                                        Tic Tac Toe")
    print("")                      
    print("xxx-----------------------------------------------------------------------xxx")

    pb()
    #Adding player name
    pName = input("Enter your name...")
    player.setName(pName)

    #Choosing a level of difficulty
    level = int(input("Choose the level of difficulty: 1 for Easy. 2 for Hard..."))

    while level not in difficultyLevelArray:
                level = int(input("That is not a level, please choose another one..."))

    setting.setLevel(level)

    #Choosing who goes 1st and 2nd
    position = int(input("Would you like to go first or second?: Enter 1 for first or 2 for second..."))

    setting.setPosition(position, player, computer)

    #Setting the symbol for each player
    firstPlayer = setting.getFirstPlayer()
    firstPlayer.setSymbol("O")
    secondPlayer = setting.getSecondPlayer()
    secondPlayer.setSymbol("X")

    pb()
    print("************************START ************************")
    pb()
    #Display Grid at starting point
    gridDisplay.displayGrid()

    #Start game loop

    #Setting which player is playersTurn
    for item in range(0,9):
        if item%2 == 0:
            playersTurn = setting.getFirstPlayer()
        else:
            playersTurn = setting.getSecondPlayer()

        #Perform actions for computer
        if playersTurn.getName() == "Computer":
            level = setting.getLevel()
            symbol = computer.getSymbol()
            playerSymbol = player.getSymbol()
            grid = setting.getGridArray()
            selection = computer.compSelection(level, symbol, playerSymbol, grid)

            #Update computer's eyes with selection
            computer.updateEyes(selection, symbol)

            #Deleting selection from grid
            grid.remove(selection)

            #Adding selection to playersTurn's array
            computer.addToArray(selection)

            #Adding selection to Grid array
            gridDisplay.addSelectionToGridArray(selection, symbol)
            
            #display grid
            print("The Computer is thinking...")
            pb()
            pb()
            pb()
            pb()
            pb()
            pb()
            pb()
            time.sleep(4)
            print("-------------The Computer has placed","'",symbol,"'","on number",selection,"-------------")
            pb()
            gridDisplay.displayGrid()
            pb()
            pb()
            pb()
            pb()
            pb()
            pb()
            pb()

        #Perform actions for player
        else:

            grid = setting.getGridArray()

            print(playersTurn.getName(),",using the number pad, choose a number from the remaining spaces")
            selection = int(input("Enter your selection and press Enter..."))

            #Checking selection is in gridArray
            while selection not in grid:
                selection = int(input("That is not available, please choose another one..."))

            #Deleting selection from grid
            grid.remove(selection)

            #Adding selection to playersTurn's array
            playersTurn.addToArray(selection)

            #Update computer's eyes with player selection
            symbol = player.getSymbol()
            computer.updateEyes(selection, symbol)

            #Adding selection to Grid array
            gridDisplay.addSelectionToGridArray(selection, symbol)

            pb()
            print("------------------You placed","'",symbol,"'","on number",selection,"------------------")
            pb()
            #display grid
            gridDisplay.displayGrid()

        #Check isMatch() if game loop is between 3 and 8
        if (item  >= 4) and (item < 8) :
            if (isMatch(playersTurn, w2w)):
                print(playersTurn.getName(),"WINS!")
                pb()
                print("End of Game")
                break

        else:

            #draw or win on last move
            if item == 8:
                if (isMatch(playersTurn, w2w)):
                    print(playersTurn.getName(),"WINS!")
                    pb()
                    print("End of Game")
                    break
                if (isMatch(playersTurn, w2w)) == False:
                    print("It's a DRAW!")
                    pb()
                    print("End of Game")
                    pb()
                    break

    #Play Again?
    answer = int(input("Would you like to play again? 1 for Yes or 2 for No..."))
    if answer == 1:
        runGame()
    elif answer == 2:
        print("End of game. Thank you for playing")   
        
runGame()






