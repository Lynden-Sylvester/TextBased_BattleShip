'''
Be sure to include docstrings
which are specific to your project
'''

import random


def Is_Hit(aBoard, aPos):
    '''Checks for a hit
    '''
    #Gets the column the user typed in
    col = ord(aPos[0].capitalize()) - ord("A")
    #Gets the row the user typed in
    row = int(aPos[1:])-1
    #checks if the guessed location is a hit, if so replace with an "x", else, an "O"
    if aBoard[row][col].isdigit():
        aBoard[row][col] = "X"
        return True
    aBoard[row][col] = "O"
    return False

def Display_Grid(aBoard, hideShip=True):
    '''Generates and updates the board
    '''
    #Generate The Letters for the Game field
    print("   A B C D E F G H I J")
    #Generates the current field
    for (row_index, row) in enumerate(aBoard):
        print("{:2d}".format(row_index+1), end=" ")
        for item in row:
            if hideShip and item.isdigit():
                item = "~"
            print(item, end=" ")
        print()    

def Valid_Input(aString, aBoard):
    '''Checks for valid input
    '''
    #checks for an empty string
    if aString == "":
        return False
    #checks if the string is "Q" and exits the program
    if aString.capitalize() == "Q":
        return True
    #checks the string starts with a letter A-J, else prints the user error & reprompts
    col = ord(aString[0].capitalize()) - ord("A")
    if col < 0 or col > 9:
        print("Must start with a character A-J")
        return False
    #checks the string ends with a number 1-10, else prints the user error & reprompts
    if aString[1:].isdigit():
        row = int(aString[1:])-1
    else:
        row = -1
    if row < 0 or row > 9:
        print("Must end with a number 1-10")
        return False
    #checks if the string was already guessed, if so, lets the user know & reprompts
    if (aBoard[row][col] == "X") or (aBoard[row][col] == "O"):
        print("Position already guessed")
        return False
        
    return True

def Statistics_Menu(aHit, aMiss, aShip):
    '''Calculates the statistics of the game at the end
    '''
    
    aTurn = aHit + aMiss
    #Calculates the user's accuracy
    aPercentage = (aHit/aTurn)*100
    #Prints the user's game statistics
    print("\n                Statistics")
    print("\nRank: ")
    if aTurn <= aShip:
        print("Master Chief Petty Officer of the Navy")
    
    elif aTurn <= aShip+7:
        print("Fleet/Force Master Chief Petty Officer")
    
    elif aTurn <= aShip+(7*2):
        print("Command Master Chief Petty Officer")

    elif aTurn <= aShip+(7*3):
        print("Master Chief Petty Officer")
        
    elif aTurn <= aShip+(7*4):
        print("Chief Petty Officer")
        
    elif aTurn <= aShip+(7*5):
        print("Petty Officer First Class")
    
    elif aTurn <= aShip+(7*6):
        print("Petty Officer Second Class")
    
    elif aTurn <= aShip+(7*7):
        print("Petty Officer Third Class")
    
    elif aTurn <= aShip+(7*8):
        print("Seaman")
    
    elif aTurn <= aShip+(7*9):
        print("Seaman Apprentice")
        
    elif aTurn <= aShip+(7*10):
        print("Seaman Recruit")
        
    else:
        print("Fish in Water")
        print("You were thrown overboard during a muntiny and were left behind!")
        
    print("\nTurns: " + str(aTurn))
    print("Accuracy: {:.2f}%".format(aPercentage))
    print("You Hit:", aHit, "times!")
    print("You Missed:", aMiss, "times!")

def Ship_Place(aBoard, shipLength):
    '''Places the ships
    '''
    validPosition = False
    #checks for valid ship positions
    while not validPosition:
    
        isHorizontal = random.randint(0, 1)
    
        if isHorizontal:
            chosenRow = random.randint(0, 9)
            chosenCol = random.randint(0, 10 - shipLength)
        else:
            chosenCol = random.randint(0, 9)
            chosenRow = random.randint(0, 10 - shipLength)
        
        validPosition = True
        #places a ship only if there is a valid spot
        for i in range(shipLength):
            if isHorizontal:
                if (aBoard[chosenRow][chosenCol + i]) != '~':
                    validPosition = False
                    break
            else:
                if (aBoard[chosenRow + i][chosenCol]) != '~':
                    validPosition = False
                    break
                
    for i in range(shipLength):
        if isHorizontal:
            aBoard[chosenRow][chosenCol+i] = str(shipLength)
        else:
            aBoard[chosenRow+i][chosenCol] = str(shipLength)
                   
def main():
    '''
    The main portion of your program should be in this
    function.  Other functions should be called from this
    function.
    '''
    #Defining global variables including CurrentBoard
    ShipTotal = 17
    HitCounter = 0
    MissCounter = 0
    #generates a static board
    CurrentBoard = [
        ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
        ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
        ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
        ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
        ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
        ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
        ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
        ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
        ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
        ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"]]
    
    print("This is my project!\n")
    print("BattleShip Grid\n")
    #places the ships
    Ship_Place(CurrentBoard, 5)
    Ship_Place(CurrentBoard, 4)
    Ship_Place(CurrentBoard, 3)
    Ship_Place(CurrentBoard, 3)
    Ship_Place(CurrentBoard, 2)
    #Runs the game until completion or exiting
    #Display_Grid(CurrentBoard, False)
    while HitCounter < ShipTotal:
        print()
        Display_Grid(CurrentBoard)
        userInput = ""
        #checks for valid user input
        while not Valid_Input(userInput, CurrentBoard):
            userInput = input("\nEnter a position: ")
        #checks if the user wants to quit the game
        if userInput.capitalize() == "Q":
            print("\nBye!")
            return
        #Checks if the user landed a hit
        if Is_Hit(CurrentBoard, userInput):
            print("You landed a hit!")
            HitCounter += 1
        
        else:
            print("You missed!")
            MissCounter += 1
    Display_Grid(CurrentBoard)
    Statistics_Menu(HitCounter, MissCounter, ShipTotal)
    
if __name__ == '__main__':
    main()