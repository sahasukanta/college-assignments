#----------------------------------------------------
# Lab 3: Magic Square class
#
# Author: Sukanta Saha - ID# 1624111
# Collaborators/References: n/a
#----------------------------------------------------

class MagicSquare:
    def __init__(self, n):
        '''
        Initializes an empty square with n*n cells.
        Inputs:
           n (int) - number of rows in square, or equivalently, the number of columns
        Returns: None
        '''
        self.square = []  # list of lists, where each internal list represents a row
        self.size = n  # number of columns and rows of square

        for _ in range(self.size):
            row = []
            for _ in range(self.size):
                row.append(0)
            self.square.append(row)


    def cellIsEmpty(self, row, col):
        '''
        Checks if a given cell is empty, or if it already contains a number
        greater than 0.
        Inputs:
           row (int) - row index of cell to check
           col (int) - column index of cell to check
        Returns: True if cell is empty; False otherwise
        '''
        return self.square[row][col] == 0


    def drawSquare(self):
        '''
        Displays the current state of the square, formatted with column and row
        indices shown along the top and left side, respectively.
        Inputs: N/A
        Returns: None
        '''
        # printing col num
        print("  ", end="")
        for i in range(self.size):
            print(" {0: ^4}".format(i), end="")
        # printing line below col num
        print("\n  +" + "-"*((4*self.size)+self.size-1) + "+")

        # printing square
        colNum = 0
        for row in self.square:
            print(colNum, end="")
            colNum += 1
            print(" |", end="")

            for col in row:
                if col == 0: col = "."
                print("{0: ^4}".format(col), end="")
                print("|", end="")

            # printing line below each row
            print("\n  +" + "-"*((4*self.size)+self.size-1) + "+")


    def update(self, row, col, num):
        '''
        Assigns the integer, num, to the cell at the provided row and column,
        but only if that cell is empty and only if the number isn't already
        in another cell in the square (i.e. it is unique)
        Inputs:
           row (int) - row index of cell to update
           col (int) - column index of cell to update
           num (int) - entry to place in cell
        Returns: True if attempted update was successful; False otherwise
        '''
        # check uniqueness
        unique = True
        for valuesInRow in self.square:
            if num in valuesInRow:
                unique = False

        # try to update cell
        if unique:
            if row < self.size and row >= 0:
                if col < self.size and col >= 0:
                    if self.cellIsEmpty(row, col):
                        self.square[row][col] = num
                        return True
        return False


    def isFull(self):
        '''
        Checks if the square has any remaining empty cells.
        Inputs: N/A
        Returns: True if the square has no empty cells (full); False otherwise
        '''
        for row in self.square:
            if 0 in row:
                return False
        return True


    def isMagic(self):
        '''
        Checks whether the square is a complete, magic square:
          1. All cells contain a unique, positive number (i.e. greater than 0)
          2. All lines sum up to the same value (horizontals, verticals, diagonals)

        Inputs: N/A
        Returns: True if square is magic; False otherwise
        '''
        # checking if square is full
        complete = True
        for row in self.square:
            for col in row:
                if type(col) != int:
                    complete = False
        full = complete and self.isFull()

        if full:
            unique = True
            positiveInt = True
            rowTotals, colTotals, diagTotals = [], [], []
            diag1, diag2 = [], []

            for row in range(self.size):
                # checking row totals
                rowTotal = sum(self.square[row])
                rowTotals.append(rowTotal)

                # diagonal totals
                diag1.append(self.square[row][row])
                diag2.append(self.square[row][self.size-1-row])

                # checking uniqueness and positive integer
                column = []
                for col in range(self.size):
                    originalNum = self.square[row][col]
                    if originalNum <= 0: positiveInt = False
                    if positiveInt:
                        self.square[row][col] = 0
                        updated = self.update(row, col, originalNum)
                        if not updated:
                            unique = False
                    self.square[row][col] = originalNum

                    # column totals
                    column.append(self.square[col][row])
                    if len(column) == self.size:
                        colTotal = sum(column)
                        colTotals.append(colTotal)

            diagTotals += [sum(diag1), sum(diag2)]

            sameTotal = True
            allTotals = rowTotals + colTotals + diagTotals
            for i in allTotals:
                if allTotals[0] != i:
                    sameTotal = False

        return full and unique and positiveInt and sameTotal




if __name__ == "__main__":
    # TEST EACH METHOD THOROUGHLY HERE
    # complete the suggested tests; more tests may be required

    # start by creating an empty 3x3 square and checking the contents of the square attribute
    mySquare = MagicSquare(3)
    print(mySquare.square)

    # check if a specific cell (any cell) is empty, as expected.
    print(mySquare.cellIsEmpty(-1,-1))

    # does the entire square display properly when you draw it?
    mySquare.drawSquare()

    # assign a number to an empty cell and display the entire square
    mySquare.update(0,0,10)
    mySquare.drawSquare()

    # try to assign a number to a non-empty cell. What happens?
    # print(mySquare.update(0,0,10))

    # check if the square is full. Should it be full after only 1 entry?
    print(mySquare.isFull())

    # check if the square is a magic square. Should it be after only 1 entry?
    print(mySquare.isMagic())

    # add values to the square so that every line adds up to 21. Display the square.
    #(Check out the example at the beginning of the lab description for values to put into each cell.)
    mySquare.update(0,1,3)
    mySquare.update(0,2,8)

    mySquare.update(1,0,5)
    mySquare.update(1,1,7)
    mySquare.update(1,2,9)

    mySquare.update(2,0,6)
    mySquare.update(2,1,11)
    mySquare.update(2,2,4)

    # check if the square is full
    print(mySquare.isFull())

    # check if the square is magic
    print(mySquare.isMagic())

    # write additional tests, as needed
    print(mySquare.square)
    mySquare.square[0][0] = 0
    mySquare.drawSquare()
    print(mySquare.isMagic())

    mySquare.square[0][0] = 10
    mySquare.square[0][2] = 'j'
    mySquare.drawSquare()
    print(mySquare.isMagic())

