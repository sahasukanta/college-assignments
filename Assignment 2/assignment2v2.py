import domino175 as d

class Table:
    """Empty Domino game table grid with 3 stacks"""

    def __init__(self):
        """
        initialises a gameDeck as DominoDeck obj, 3 DominoStack objects in the playing area, and a grid with domino objects as nested lists
        """
        self.__gameDeck = d.DominoDeck()
        self.__playingArea = [d.DominoStack(), d.DominoStack(), d.DominoStack()]
        self.__grid = []

        self.__rows = 4
        self.__cols = 7
        self.__screenWidth = 65
        self.__stackStatus = [None, None, None]

    def dealGrid(self, useFile):
        """
        populates the game deck with dominoes from a file if useFile is True, otherwise generates a shuffled double-six set of dominoes
        """
        self.__gameDeck.populate(useFile)
        for _ in range(self.__rows):
            row = []
            for _ in range(self.__cols):
                domino = self.__gameDeck.deal()
                row.append(domino)
            self.__grid.append(row)

    def select(self, row, col):
        """
        selects and returns the domino at [row][col], replaces the dom with " *** " in grid
        inputs: row int and col int
        returns: faced up string representation of domino at [row][col]
        """
        assert type(row) == int and type(col) == int, "Invalid arguments--"
        assert 0 <= row <= 3 and 0 <= col <= 6, "Invalid arguments=="

        if self.__grid[row][col] == " *** ":
            raise Exception(f"There is no domino at row {row}, column {col}")
        else:
            domino = self.__grid[row][col]
            self.__grid[row][col] = " *** "
            domino.turnOver()
            self.__stackStatus = [True, True, True]
            return domino

    def playDomino(self, domino, stackNum):
        """
        plays the domino obj onto the stackNum, checks for isWinner() condition and prints congratulations message if isWinner is True
        inputs: domino obj and the stack number
        returns: True if successfully played, False otherwise
        """
        assert type(domino) == d.Domino and stackNum in [0,1,2], "Invalid argument~~"
        try:
            print(f"Playing {str(domino)} on stack {stackNum}: ", end="")
            self.__playingArea[stackNum].push(domino)
        except Exception:
            print(f"Cannot play {str(domino)} on stack {stackNum}")
            self.__stackStatus[stackNum] = False
            return False
        else:
            print("Success!")
            return True

    def isWinner(self):
        """
        Checks if conditions are met for declaring the user as winner or loser
        returns: True if at least one of the 3 stacks has 6 dominoes,
        False if a new domino cannot be played onto any of the 3 stacks,
        None otherwise.
        """
        lengths = []
        for stack in self.__playingArea:
            lengths.append(stack.size())
            if 6 in lengths:
                return True
        if True not in self.__stackStatus:
            return False

    def revealGrid(self):
        """displays the grid with all remaining dominoes faced up, does not change the facedown state of the original grid"""
        # face up
        for i in range(self.__rows):
            for j in range(self.__cols):
                self.__grid[i][j].turnOver()
        grid = str(self)
        grid = grid[20:355]
        print("/"*self.__screenWidth)
        print("For testing purposes, the grid contains:")
        print(grid)
        print("/"*self.__screenWidth)
        # face down
        for i in range(self.__rows):
            for j in range(self.__cols):
                self.__grid[i][j].turnOver()

    def getNumStacks(self):
        """returns the integer number of stacks in the playing area"""
        return len(self.__playingArea)

    def getNumRows(self):
        """returns the integer number of rows in the grid of dominoes"""
        return self.__rows

    def getNumColumns(self):
        """returns the integer number of cols in the grid of dominoes"""
        return self.__cols

    def __str__(self):
        """string representation of the table"""
        # converting all domino object into its proper string representation
        grid = []
        for i in self.__grid:
            row = []
            for j in i:
                row.append(str(j))
            grid.append(row)

        # column line
        colHeader = "      "
        for i in range(7):
            colHeader += f"{i}        "
        # row lines
        rows = []
        for i in range(self.__rows):
            row = f"{i}   "
            for j in range(self.__cols):
                row += f"{grid[i][j]}    "
            rows.append(row)

        grid = f"\nSelection Grid:\n{colHeader}\n{rows[0]}\n{rows[1]}\n{rows[2]}\n{rows[3]}\n"

        stacks = "\nDomino Stacks:\n"
        for i in range(len(self.__playingArea)):
            stacks += f"{i}|| "
            stacks += str(self.__playingArea[i])
            stacks = stacks[:-1] + "\n"

        display = grid + stacks + "-"*self.__screenWidth
        return display



def main():

    msg = "Welcome to DOMINOES 175"
    print("="*len(msg))
    print(msg)
    print("="*len(msg))

    correctInp = False
    while not correctInp:
        print("Please select your play mode:")
        print("1. Test mode")
        print("2. Game mode")
        inp = input("> ")
        try:
            inp = int(inp)
            if int(inp) in [1, 2]:
                correctInp = True
            else:
                raise Exception
        except:
            print("Invalid selection. You must enter 1 or 2.")

    if inp == 1:
        try:
            # creating new game table
            table = Table()
            table.dealGrid(False)
        except Exception as e:
            print(e)
        else:
            ################## -- testing purposes
            table.revealGrid()
            ################## -- testing purposes
            print(table)
            # playing dominoes
            end = False
            while not end:
                try:
                    inpCoordinates = input(f"Please select grid row (0-{table.getNumRows()-1}) and column (0-{table.getNumColumns()-1}) numbers as 'row,col': ")
                    inpCoordinates = inpCoordinates.split(sep=",")
                    for i in range(2):
                        inpCoordinates[i] = int(inpCoordinates[i])
                    domino = table.select(inpCoordinates[0], inpCoordinates[1])
                    print(f"Domino selected: {str(domino)}")

                    dominoPlayed = False
                    while not dominoPlayed:
                        inpPlayStack = input(f"\nPlease select the stack number (0-{table.getNumStacks()-1}) to play domino on: ")
                        inpPlayStack = int(inpPlayStack)

                        dominoPlayed = table.playDomino(domino, inpPlayStack)

                        if table.isWinner() == True or table.isWinner() == False:
                            dominoPlayed = True
                            end = True
                except Exception as e:
                    end = True
                    print(e)
                else:
                    if dominoPlayed == True:
                        print(table)
                    if table.isWinner():
                        print("\nCongratulations - WINNER!")
                    elif table.isWinner() == False:
                        print("\nGAME OVER. Better luck next time.")

        finally:
            print("Thank you for playing. Goodbye...")

    elif inp == 2:
        table = Table()
        table.dealGrid(True)
        table.revealGrid()
        print(table)
        print("Under Construction...")


main()
