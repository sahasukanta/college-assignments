#----------------------------------------------------
# Lab 7, Exercise 2: Doubly Linked Lists
# TO DO: complete mandatory methods in DLinkedList class
# TO DO (optional): complete optional methods in DLinkedList class
# to get better understanding of manipulating linked lists
#
# Author: Sukanta Saha
# Collaborators/references:
#   - CMPUT 175 provided complete DLinkedListNode
#   - CMPUT 175 provided init, search, index methods for DLinkedList
#   - CMPUT 175 provided tests for DLinkedList
#----------------------------------------------------


class DLinkedListNode:
    # An instance of this class represents a node in Doubly-Linked List
    def __init__(self,initData,initNext,initPrevious):
        self.data = initData
        self.next = initNext
        self.previous = initPrevious

        if initNext != None:
            self.next.previous = self
        if initPrevious != None:
            self.previous.next = self

    def getData(self):
        return self.data

    def setData(self,newData):
        self.data = newData

    def getNext(self):
        return self.next

    def getPrevious(self):
        return self.previous

    def setNext(self,newNext):
        self.next = newNext

    def setPrevious(self,newPrevious):
        self.previous = newPrevious

class DLinkedList:
    # An instance of this class represents the Doubly-Linked List
    def __init__(self):
        self.__head=None
        self.__tail=None
        self.__size=0

    def getHead(self):
        return self.__head

    def search(self, item):
        """returns True if the item is an element in the list; False otherwise. The item can
        be any object"""
        current = self.__head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found= True
            else:
                current = current.getNext()
        return found

    def index(self, item):
        """returns the index of the item in the list (assuming that the head node is at index
        0), or -1 if the item is not in the list"""
        current = self.__head
        found = False
        index = 0
        while current != None and not found:
            if current.getData() == item:
                found= True
            else:
                current = current.getNext()
                index = index + 1
        if not found:
                index = -1
        return index

    def insert(self, pos, item):
        """inserts item at pos"""
        assert type(pos) == int and pos >= 0, "Position argument incorrect"

        if pos == 0:
            self.add(item)
        elif pos >= self.__size:
            self.append(item)
        else:
            current = self.__head
            if pos == 1:
                new_node = DLinkedListNode(item, current.getNext(), current)
            else:
                for i in range(pos):
                    current = current.getNext()  # traversing the list
                    if i == pos-2:
                        new_node = DLinkedListNode(item, current.getNext(), current)
            self.__size += 1

    def searchLarger(self, item):
        """returns the index of the first node that is larger than item"""
        current = self.__head
        while current != None:
            for node in range(self.__size):
                # if type(current.getData()) in [int, float]:
                if current.getData() > item:
                    return self.index(current.getData())
                current = current.getNext()
                if current == None:
                    return -1

    def getSize(self):
        return self.__size

    def getItem(self, pos):
        """returns item at position pos"""
        assert pos <= self.__size, "Index out of range."

        if pos < 0: pos = pos + self.__size
        current = self.__head
        for node in range(self.__size):
            if self.index(current.getData()) == pos:
                return current.getData()
            else:
                current = current.getNext()

    def __str__(self):
        string = ""
        current = self.__head
        while current != None:
            string += str(current.getData()) + " "
            current = current.getNext()
            if current == None: string = string[:-1]
        return string


    def add(self, item):
        """adds item at the beginning of the queue"""
        new_node = DLinkedListNode(item, self.__head, None)
        self.__head = new_node
        self.__size += 1
        if self.__size == 1:
            self.__tail = new_node

    def remove(self, item):
        # optional exercise
        pass

    def append(self, item):
        """appends item at the end of the queue"""
        if self.__size == 0:
            self.add(item)
        else:
            new_node = DLinkedListNode(item, None, self.__tail)
            self.__tail = new_node
            self.__size += 1

    def pop1(self):
        # optional exercise
        pass

    def pop(self, pos=None):
        # optional exercise
        # Hint - incorporate pop1 when no pos argument is given
        pass



def test():

    linked_list = DLinkedList()

    is_pass = (linked_list.getSize() == 0)
    assert is_pass == True, "fail the test"

    linked_list.insert(0, "Hello")
    linked_list.insert(1, "World")

    is_pass = (str(linked_list) == "Hello World")
    assert is_pass == True, "fail the test"

    is_pass = (linked_list.getSize() == 2)
    assert is_pass == True, "fail the test"

    is_pass = (linked_list.getItem(0) == "Hello")
    assert is_pass == True, "fail the test"


    is_pass = (linked_list.getItem(1) == "World")
    assert is_pass == True, "fail the test"

    is_pass = (linked_list.getItem(0) == "Hello" and linked_list.getSize() == 2)
    assert is_pass == True, "fail the test"

    '''
    OPTIONAL TESTS FOR OPTIONAL EXERCISE - do not need to demo
    '''
    '''
    is_pass = (linked_list.pop(1) == "World")
    assert is_pass == True, "fail the test"

    is_pass = (linked_list.pop() == "Hello")
    assert is_pass == True, "fail the test"

    is_pass = (linked_list.getSize() == 0)
    assert is_pass == True, "fail the test"

    int_list2 = DLinkedList()

    for i in range(0, 10):
        int_list2.add(i)
    int_list2.remove(1)
    int_list2.remove(3)
    int_list2.remove(2)
    int_list2.remove(0)
    is_pass = (str(int_list2) == "9 8 7 6 5 4")
    assert is_pass == True, "fail the test"

    for i in range(11, 13):
        int_list2.append(i)
    is_pass = (str(int_list2) == "9 8 7 6 5 4 11 12")
    assert is_pass == True, "fail the test"

    for i in range(21, 23):
        int_list2.insert(0,i)
    is_pass = (str(int_list2) == "22 21 9 8 7 6 5 4 11 12")
    assert is_pass == True, "fail the test"

    is_pass = (int_list2.getSize() == 10)
    assert is_pass == True, "fail the test"
    '''

    int_list = DLinkedList()

    is_pass = (int_list.getSize() == 0)
    assert is_pass == True, "fail the test"

    for i in range(9, -1, -1):
        int_list.insert(0,i)

    is_pass = (int_list.getSize() == 10)
    assert is_pass == True, "fail the test"

    is_pass = (int_list.searchLarger(8) == 9)
    assert is_pass == True, "fail the test"

    int_list.insert(7,801)

    is_pass = (int_list.searchLarger(800) == 7)
    assert is_pass == True, "fail the test"

    is_pass = (int_list.getItem(-1) == 9)
    assert is_pass == True, "fail the test"

    is_pass = (int_list.getItem(-4) == 801)
    assert is_pass == True, "fail the test"

    if is_pass == True:
        print ("=========== Congratulations! Your have finished exercise 2! ============")

if __name__ == '__main__':
    test()

