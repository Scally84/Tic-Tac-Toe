from collections import Counter
import random

'''GameSetting Class'''
class GameSetting():
    def __init__(self):
        self.level = None
        self.first = None
        self.second = None
        self.gridArray = [1,2,3,4,5,6,7,8,9]

    def getLevel(self):
        return self.level

    def getFirstPlayer(self):
        return self.first

    def getSecondPlayer(self):
        return self.second

    def getPositions(self):
        pos = (self.first.getName(), self.second.getName())
        return pos

    def getGridArray(self):
        return self.gridArray

    def setLevel(self, aLevel):
        self.level = aLevel

    def setPosition(self, aPosition, aPlayer, theComputer):
        if aPosition == 1:
            self.first = aPlayer
            self.second = theComputer
        elif aPosition ==2:
            self.first = theComputer
            self.second = aPlayer

    def remove(self, aSelection):
        self.gridArray.remove(aSelection)
        

'''Player Class'''
class Player():
    def __init__(self):
        self.name = None
        self.chosenSQArray = [ ]
        self.symbol = None

    def getName(self):
        return self.name

    def getArray(self):
        return self.chosenSQArray

    def getSymbol(self):
        return self.symbol

    def setName(self, aName):
        self.name = aName

    def addToArray(self, aSquare):
        self.chosenSQArray.append(aSquare)

    def setSymbol(self, aSymbol):
        self.symbol = aSymbol


'''Computer Class'''
class Computer():
    def __init__(self):
        self.name = "Computer"
        self.chosenSQArray = [ ]
        self.symbol = None
        self.eyesArray = [{7:None,8:None,9:None},{4:None,5:None,6:None},
                          {1:None,2:None,3:None},{7:None,4:None,1:None},
                          {8:None,5:None,2:None},{9:None,6:None,3:None},
                          {7:None,5:None,3:None},{1:None,5:None,9:None}]
 
    def getName(self):
        return self.name

    def getArray(self):
        return self.chosenSQArray

    def getSymbol(self):
        return self.symbol

    def addToArray(self, aSquare):
        self.chosenSQArray.append(aSquare)

    def setSymbol(self, aSymbol):
        self.symbol = aSymbol

    def getEyesArray(self):
        return self.eyesArray

    def updateEyes(self, aSelection, aSymbol):
        for eachArray in self.eyesArray:
            if aSelection in eachArray:
                eachArray[aSelection] = aSymbol
        return self.eyesArray

    def compSelection(self, aLevel, aSymbol, aPlayerSymbol, aGrid):
        #check if selection can win game
        for eachArray in self.eyesArray:
            numOfSameSymbol = sum(value == aSymbol for value in eachArray.values())
            if numOfSameSymbol >= 2:
                theArray = eachArray
                for key, value in theArray.items():
                    if value == None:
                        return key
                        break
                    
        defendOrThinkKey = self.defend(aLevel, aSymbol, aPlayerSymbol, aGrid)
        return defendOrThinkKey

    def defend(self, aLevel, aSymbol, aPlayerSymbol, aGrid):
        #check if selection can prevent player winning
        for eachArray in self.eyesArray:
            numOfSameSymbol = sum(value == aPlayerSymbol for value in eachArray.values())
            if numOfSameSymbol >= 2:
                theArray = eachArray
                for key, value in theArray.items():
                    if value == None:
                        return key
                        break

        #Use think method if difficulty level is 2
        if aLevel == 2:  
            thinkKey = self.think(aSymbol, aGrid)
            return thinkKey

        else:
            randomSelection = random.choice(aGrid)
            return randomSelection

    def think(self, aSymbol, aGrid):
        if len(aGrid) == 9:
            array = [1,3,7,9]
            evenArray = [2,4,6,8]
            array.append(random.choice(evenArray))
            randomSelection = random.choice(array)
            return randomSelection

        else:
            array = [ ]
            for eachArray in self.eyesArray:
                numOfNone = sum(value == None for value in eachArray.values())
                symbol = sum(value == aSymbol for value in eachArray.values())
                if numOfNone == 2 and symbol == 1:
                    for key, value in eachArray.items():
                        if value == None:
                            array.append(key)
                            
            if len(array) == 0:
                randomSelection = random.choice(aGrid)
                return randomSelection

            else:
                count = 0
                index = 1
                mode = [ ]

                for eachItem in array:
                    for item in range(index, len(array)):
                        if eachItem == array[item]:
                            count += 1
                    index += 1

                    if count > 0:
                        mode.append(eachItem)
                        count = 0

                if len(mode) > 0:
                    randomSelection = random.choice(mode)
                    return randomSelection

                else:
                    oddArray = [ ]
                    for eachItem in array:
                        if eachItem % 2 != 0:
                            oddArray.append(eachItem)

                    if len(oddArray) > 0:
                        randomSelection = random.choice(oddArray)
                        return randomSelection

                    else:
                        randomSelection = random.choice(array)
                        return randomSelection


'''Grid class'''
class Grid():
    def __init__(self):
        self.gridArray = ["--","--","--","--","--","--","--","--","--"]

    def addSelectionToGridArray(self, aSelection, aSymbol):
        self.gridArray.insert(aSelection-1, aSymbol)
        del self.gridArray[aSelection]

    def displayGrid(self):
        c1 = self.gridArray[0]
        c2 = self.gridArray[1]
        c3 = self.gridArray[2]
        b1 = self.gridArray[3]
        b2 = self.gridArray[4]
        b3 = self.gridArray[5]
        a1 = self.gridArray[6]
        a2 = self.gridArray[7]
        a3 = self.gridArray[8]
        print("                                             THE GRID")
        print("")
        print("                           ",a1,"        ||        ",a2,"        ||         ",a3)
        print("                ================================")
        print("                           ",b1,"        ||        ",b2,"        ||         ",b3)
        print("                ================================")
        print("                           ",c1,"        ||        ",c2,"        ||         ",c3)
        print("")
        print("")
        print("")
        
        
'''WaysToWin Class'''       
class WaysToWin():
    def __init__(self):
        self.wtwArray = [ ]

    def getWtwArray(self):
        return self.wtwArray

    def setWtwArray(self, anArray):
        self.wtwArray.append(anArray)


'''isMatch Method'''
def isMatch(aPlayer, aWaysToWin):
    value = False
    count = 0
    array = aWaysToWin.getWtwArray()
    playersArray = aPlayer.getArray()
    
    for eachArray in array:
        for eachItem in eachArray:
            if eachItem in playersArray:
                count += 1
                if count >= 3:
                    value = True
                    break
        count = 0

    return value







