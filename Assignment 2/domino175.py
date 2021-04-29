# CMPUT 175 Assignment 2
# Author: Sukanta Saha
# Student ID# 1624111

from queues import CircularQueue as cq
import random

class Domino:
    """Domino object with max of 6 dots"""

    def __init__(self, dotsA, dotsB):
        """
        Creates a domino with dots A and B
        inputs: two integers b/w 0 and 6
        returns: domino object with sides dotsA and dotsB
        """
        self.__minDots = 0
        self.__maxDots = 6  # max set to 6 dots
        assert type(dotsA) == int and self.__minDots <= dotsA <= self.__maxDots, "Invalid parameter: dotsA"
        assert type(dotsB) == int and self.__minDots <= dotsB <= self.__maxDots, "Invalid parameter: dotsB"

        self.dotsA = dotsA
        self.dotsB = dotsB
        self.__top = max(self.dotsA, self.dotsB)
        self.__bottom = min(self.dotsA, self.dotsB)
        self.__faceDown = False

    def setTop(self, dots):
        """Updates the dots parameter end of the domino as the top and the other end as the bottom"""
        assert dots == self.dotsA or dots == self.dotsB, f"Domino does not have {dots} dots face -> Value error"
        if dots == self.dotsA:
            self.__top = self.dotsA
            self.__bottom = self.dotsB
        else:
            self.__top = self.dotsB
            self.__bottom = self.dotsA

    def turnOver(self):
        """switches the self.__faceDown attribute"""
        if self.__faceDown: self.__faceDown = False
        else: self.__faceDown = True

    def getTop(self):
        """returns the integer number of dots on the top of the domino"""
        return self.__top

    def getBottom(self):
        """returns the integer number of dots at the bottom of the domino"""
        return self.__bottom

    def isFaceDown(self):
        """returns True if domino is faced down, False otherwise"""
        return self.__faceDown == True

    def __str__(self):
        """returns the string format of a Domino object [bottom|top]"""
        if self.__faceDown:
            top = "?"
            bottom = "?"
        else:
            top = self.__top
            bottom = self.__bottom

        return f"[{bottom}|{top}]"


class DominoDeck:
    """Deck of dominoes with the standard double-six set or with input dominoes of size 28"""
    def __init__(self):
        self.__maxCapacity = 28
        self.__deck = cq(self.__maxCapacity)


    def populate(self, useFile):
        """
        populates deck with dominoes
        useFile=True: prompts user for domino dot integer file
        useFile=False: automatically creates deck with double-six dominoes
        """
        assert useFile == True or useFile == False, "Cannot populate deck: invalid argument provided."
        if useFile:
            inp, fHandle = self.__getUseFileName()
            self.__popUseFile(inp, fHandle)
        else:
            self.__popDontUseFile()

    def __getUseFileName(self):
        """gets correct user input for populating self.__deck file name containing domino dot integers"""
        correctFileName = False
        while not correctFileName:
            try:
                inp = input("Name of file that should be used to populate the grid of dominoes: ")
                fHandle = open(inp)
            except FileNotFoundError:
                print(f"Cannot read from {inp}.")
            else:
                correctFileName = True

        return inp, fHandle

    def __popUseFile(self, inp, fHandle):
        """populates self.__deck with user input dominoes from the specified .txt file"""
        deckNotFull = False
        invalidData = False
        fHandleLines = fHandle.readlines()
        for line in fHandleLines:
            try:
                line = line.strip()
                line = line.split("/")
                dotsA = int(line[0])
                dotsB = int(line[1])
            except Exception:
                invalidData = True
            else:
                domino = Domino(dotsA, dotsB)
                self.__deck.enqueue(domino)

        # checking if deck is full
        if self.size() != self.__maxCapacity:
            deckNotFull = True
        # reverting changes due to bad data
        if invalidData or deckNotFull:
            self.__deck.clear()
            fHandle.close()
            raise Exception(f"Cannot populate deck: invalid data in {inp}")

    def __popDontUseFile(self):
        """automatically populates self.__deck with double-six dominoes"""
        ADots = []
        BDots = []
        dominoes = []
        newDominoes = []  # contains lists of 28 dominoes
        for i in range(7):
            ADots.append(i)
            BDots.append(i)
        # creating sets of dominoes [{1}, {1,2}, {1,3}, ...]
        for i in ADots:
            for j in BDots:
                domino = {i, j}
                if domino not in dominoes:
                    dominoes.append(domino)
        # converting sets to lists [[1], [1, 2], ...]
        for domino in dominoes:
            newDomino = []
            for dot in domino:
                newDomino.append(dot)
            newDominoes.append(newDomino)
        # creating repeated integer dominoes [[1,1], [1,2], [0,0], ...]
        for newDomino in newDominoes:
            if len(newDomino) == 1:
                newDomino.append(newDomino[0])
        # shuffling
        newDominoes = random.sample(newDominoes, len(newDominoes))

        del ADots, BDots, dominoes
        # creating domino objects and enqueueing them into self.__deck
        for i in newDominoes:
            domino = Domino(i[0], i[1])
            self.__deck.enqueue(domino)

    def deal(self):
        """returns the front domino faced down"""
        if self.__deck.isEmpty(): raise Exception("Cannot deal domino from empty deck.")
        else:
            returnDomino = self.__deck.dequeue()
            returnDomino.turnOver()
            return returnDomino

    def isEmpty(self):
        """returns True if Deck empty, False otherwise"""
        return self.__deck.size() == 0

    def size(self):
        """returns the current length of the deck"""
        return self.__deck.size()

    def __str__(self):
        """return str representation of deck as <<<-- front back <--|"""
        string = "<<<--" + str(self.__deck) + "<--|"
        return string

class DominoStack():
    """Stack to play a domino onto"""
    def __init__(self):
        self.__stack = []

    def peek(self):
        """returns the number of dots on the top of the Domino that is at the top of the stack"""
        assert len(self.__stack) > 0, "Error: cannot peek into an empty stack"
        return self.__stack[-1].getTop()

    def isEmpty(self):
        """returns True if stack is empty, False otherwise"""
        return len(self.__stack) == 0

    def size(self):
        """returns the current length of the stack"""
        return len(self.__stack)

    def push(self, domino):
        """
        Adds a domino onto the top of the stack, such that the one already on top has the same number of dots on its top as the bottom side of the newly added domino. If stack was empty, simply adds the new domino.
        input: domino instance
        """
        assert type(domino) == Domino, "Can only push Dominoes onto the DominoStack"
        domTop = domino.getTop()
        domBot = domino.getBottom()

        if self.isEmpty():
            self.__stack.append(domino)
        else:
            lastDomTop = self.peek()
            if lastDomTop in [domTop, domBot]:
                self.__stack.append(domino)
                if lastDomTop == domTop:
                    domino.setTop(domBot)
                elif lastDomTop == domBot:
                    domino.setTop(domTop)
            else:
                raise Exception(f"Cannot play {domino} on stack.")

    def __str__(self):
        """returns the string representation of the stack, with the last item on the right as bottom top->"""
        string = ""
        for dom in self.__stack:
            string = string + str(dom) + "-"
        string = string + ">"
        return string



if __name__ == "__main__":
    pass
    # ---Task 1 tests
    # d1 = Domino(0, 0)
    # print(d1)
    # # d2 = Domino(-1, 2)  >> AssertionError
    # d3 = Domino(3, 5)
    # print(d3)
    # d3.turnOver()
    # print(d3)
    # print(d3.getBottom())
    # d3.turnOver()
    # d3.setTop(3)
    # print(d3)
    # print(d3.getTop())
    # print(d3.isFaceDown())
    # d3.turnOver()
    # print(d3.isFaceDown())

    # ---Task 2 tests
    # dDeck1 = DominoDeck()
    # dDeck1.populate(useFile=False)
    # print(dDeck1)
    # dom1 = dDeck1.deal()
    # print(dDeck1)
    # print(dom1)
    # dDeck2 = DominoDeck()
    # dDeck2.populate(useFile=True)
    # print(dDeck2)
    # print(dDeck2.size())
    # dom2 = dDeck2.deal()
    # print(dom2)
    # dom2.turnOver()
    # print(dom2)
    # print(dDeck2.size())
    # for i in range(dDeck2.size()):
    #     dDeck2.deal()
    # print(dDeck2.size())
    # print(dDeck2)

    # ---Task 3 tests
    # domStack = DominoStack()
    # print(domStack)
    # print(domStack.isEmpty())
    # d1 = Domino(0, 6)
    # domStack.push(d1)
    # print(domStack.isEmpty())
    # print(domStack)
    # d2 = Domino(3, 6)
    # domStack.push(d2)
    # print(domStack)
    # d3 = Domino(4, 1)
    # # domStack.push(d3)  # >> Exception
    # print(domStack.peek())
    # d4 = Domino(3, 6)
    # domStack.push(d4)
    # print(domStack)
    # d5 = Domino(1, 6)
    # d6 = Domino(1, 5)
    # d7 = Domino(0, 5)
    # for d in [d5, d6, d7]:
    #     domStack.push(d)
    # print(domStack)
    # print(domStack.size())
    # print(domStack.isEmpty())
    # d8 = [0, 2]
    # # domStack.push(d8)  # >> Exception



