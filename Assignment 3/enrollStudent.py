# Author: Sukanta Saha
# Student ID# 1624111

class StudentNode:

    def __init__(self, iD, faculty, first, last):
        """all parameters must be inserted as str format"""
        assert type(iD) == str and len(iD) == 6, "iD must be string of length 6"
        assert type(faculty) == str and len(faculty) == 3, "faculty must be string of length 3"
        assert type(first) == str, "first must be of type string"
        assert type(last) == str, "last must be of type string"

        self.iD = iD
        self.faculty = faculty
        self.first = first
        self.last = last
        self.next = None
        self.previous = None

    """setters"""
    def setID(self, iD):
        assert type(iD) == str and len(iD) == 6, "iD must be string of length 6"
        """sets iD as the student iD"""
        self.iD = iD

    def setFac(self, fac):
        assert type(faculty) == str and len(faculty) == 3, "faculty must be string of length 3"
        """sets fac as the student faculty"""
        self.faculty = fac

    def setFirstName(self, first):
        assert type(first) == str, "first must be of type string"
        """sets first as the first name of student"""
        self.first = first

    def setLastName(self, last):
        assert type(last) == str, "last must be of type string"
        """sets last as the last name of student"""
        self.last = last

    def setNext(self, next):
        assert type(next) == StudentNode or next == None, "next item must be a StudentNode or None"
        """sets next as the next node of student"""
        self.next = next

    def setPrev(self, previous):
        assert type(previous) == StudentNode or previous == None, "previous item must be a StudentNode or None"
        """sets previous as the previous node of student"""
        self.previous = previous

    """getters"""
    def getID(self):
        """returns the student ID"""
        return self.iD

    def getFac(self):
        """returns the student faculty"""
        return self.faculty

    def getFirstName(self):
        """returns the first name of student"""
        return self.first

    def getLastName(self):
        """returns the last name of student"""
        return self.last

    def getNext(self):
        """returns the next student node"""
        return self.next

    def getPrev(self):
        """returns the previous student node"""
        return self.previous

    def __str__(self):
        """string representation of the student node"""
        string = f"[{self.getID()} {self.getFac()} {self.getFirstName()} {self.getLastName()}]"
        return string

class EnrollTable:

    def __init__(self, capacity):
        self.__capacity = capacity
        self.__maxCapacity = 51
        assert 0 < self.__capacity <= self.__maxCapacity, "Improper capacity: must be at least 1 and at most 51"

        self.__table = []
        for i in range(self.__maxCapacity):
            self.__table.append(None)

        self.__size = 0
        self.__faculties = ["SCI", "ENG", "BUS", "ART", "EDU"]

    def size(self):
        """returns the number of students currently enrolled"""
        return self.__size

    def isEmpty(self):
        """returns True is table is empty"""
        return self.__size == 0

    def cmputIndex(self, studentID):
        """
        computes and returns the index of a given student ID based the specified algorithm. ex. studentID "123456" would return (12 + 34 + (56)^2)%51
        """
        assert type(studentID) == str and len(studentID) == 6, "incorrect studentID argument, must be str of length 6"

        try:
            num = [studentID[i:i+2] for i in range(0, len(studentID), 2)]
            return (int(num[0]) + int(num[1]) + (int(num[2]))**2) % self.__maxCapacity
        except Exception as e:
            print(e)

    def insert(self, item):
        """
        item is a student node. inserts the new student node in the
        right location on the enrollment table.
        """
        assert type(item) == StudentNode, "typeError: incorrect item type"
        assert item.getFac() in self.__faculties, "item faculty currently not supported, currently supported faculties include SCI, ENG, BUS, ART, or EDU"
        assert self.isEnrolled(item.getID()) == False, "cannot enroll studentID that is already enrolled"

        # getting studentID to calculate index
        itemID = item.getID()
        index = self.cmputIndex(itemID)

        # case 1: if slot at index is empty (None)
        if self.__table[index] == None:
            self.__table[index] = item

        else:  # case 2: if slot at index is not empty
            currentNode = self.__table[index]
            currentNodeID = currentNode.getID()
            # case 2.1: if itemID is smaller than the first node ID, insert new item at the beginning of the linked list
            if itemID < currentNodeID:
                self.__table[index] = item
                item.setNext(currentNode)
            else:  # case 2.2: if itemID is larger than the first node ID:
                # traverse through the list until the end is reached or a node with a bigger ID is reached
                while currentNode.getNext() != None and itemID > currentNode.getNext().getID():
                    currentNode = currentNode.getNext()
                # inserting at the terminal
                if currentNode.getNext() == None:
                    currentNode.setNext(item)
                # inserting in the middle
                else:
                    item.setNext(currentNode.getNext())
                    currentNode.setNext(item)

        self.__size += 1

    def remove(self, studentID):
        """
        removes the student node using studentID
        input: studentID as string
        returns: True if removed successfully, False otherwise
        """
        assert type(studentID) == str and len(studentID) == 6, "incorrect studentID argument, must be str of length 6"
        assert self.isEnrolled(studentID) == True, "studentID not enrolled, must be enrolled first before being removed"

        try:
            index = self.cmputIndex(studentID)
            if 0 > index > self.__capacity-1: raise Exception("StudentID index out of range")
            if self.__table[index] == None: raise Exception("StudentID does not exist")
        except Exception as e:
            print(e)
            return False
        else:
            currentNode = self.__table[index]
            currentNodeID = currentNode.getID()
            # case 1: if the first node is to be removed:
            if currentNodeID == studentID:
                self.__table[index] = currentNode.getNext()
                del currentNode
            else:
                # case 2: if the first node is not the one to be removed:
                while currentNode.getNext().getID() != studentID:
                    currentNode = currentNode.getNext()
                    # if there is no match after traversing through the linked list
                    if currentNode.getNext() == None:
                        return False
                # case 2.1: if node to be removed is in the middle
                if currentNode.getNext().getNext() != None:
                    currentNode.setNext(currentNode.getNext().getNext())
                # if node to be removed is a terminal node
                else:
                    currentNode.setNext(None)

            self.__size -= 1
            return True

    def isEnrolled(self, studentID):
        """returns True if studentID is in table, False otherwise"""
        assert type(studentID) == str and len(studentID) == 6, "incorrect studentID argument, must be str of length 6"

        index = self.cmputIndex(studentID)
        # case 1: if slot at index is empty (None):
        if self.__table[index] == None:
            return False
        else:  # case 2: if slot is not empty:
            currentNode = self.__table[index]
            currentNodeID = currentNode.getID()
            # case 2.1: if the first node is matched to studentID:
            if currentNodeID == studentID:
                return True
            # case 2.2: if first node is not matched to studentID
            else:
                found = False
                while currentNodeID < studentID and not found and currentNode.getNext() != None:
                    currentNode = currentNode.getNext()
                    currentNodeID = currentNode.getID()
                    if currentNodeID == studentID:
                        found = True
                return found

    def __str__(self):
        """returns the str representation of a table object"""
        string = "\n["
        for index in range(self.__capacity):
            currentNode = self.__table[index]
            if self.__table[index] != None:
                string += f"{index}:"
                while currentNode != None:
                    if 0 < index < 10: string += " "
                    node = f" {currentNode.getID()} {currentNode.getFac()} {currentNode.getFirstName()} {currentNode.getLastName()}"
                    string += node
                    currentNode = currentNode.getNext()
                    if currentNode != None:
                        string += ","
                string += "\n"
            if index == self.__capacity-1:
                string = string[:-1] + "]\n"

        return string


class PriorityQueue:

    def __init__(self):
        self.__priorDict = {"SCI": 4, "ENG": 3, "BUS": 2, "ART": 1, "EDU": 0}
        self.__head = None
        self.__tail = None
        self.__size = 0

    def size(self):
        """returns the number of items currently in priority queue"""
        return self.__size

    def isEmpty(self):
        """returns True if queue is empty, False otherwise"""
        return self.__size == 0

    def enqueue(self, item):
        """
        adds new item according to its priority into the queue.
        item must be a studentNode.
        """
        assert type(item) == StudentNode, "typeError: incorrect item type, must be a StudentNode"
        itemFac = item.getFac()

        # case 1: when queue is completely empty, make head=item, tail=None:
        if self.__head == None:
            self.__head = item
        # case 2: when only tail=None:
        elif self.__tail == None:
            if self.__priorDict[self.__head.getFac()] >= self.__priorDict[itemFac]:
                self.__tail = item
                item.setPrev(self.__head)
                self.__head.setNext(item)
            elif self.__priorDict[self.__head.getFac()] < self.__priorDict[itemFac]:
                temp = self.__head
                self.__head = item
                self.__tail = temp
                self.__head.setNext(self.__tail)
                self.__tail.setPrev(self.__head)
        else:  # case 3: when queue has at least 2 items:
            currentNode = self.__head
            currentNodeFac = currentNode.getFac()
            # 3.1 traversing to the right faculty:
            while currentNode.getNext() != None and self.__priorDict[currentNode.getNext().getFac()] >= self.__priorDict[itemFac]:
                currentNode = currentNode.getNext()
                currentNodeFac = currentNode.getFac()
            # 3.2.1 if at the beginning of the main queue:
            if currentNode.getPrev() == None:
                if self.__priorDict[currentNode.getFac()] < self.__priorDict[itemFac]:
                    item.setNext(self.__head)
                    self.__head.setPrev(item)
                    self.__head = item
                elif self.__priorDict[currentNode.getFac()] == self.__priorDict[itemFac]:
                    item.setPrev(self.__head)
                    self.__head.getNext().setPrev(item)
                    item.setNext(self.__head.getNext())
                    self.__head.setNext(item)
                elif self.__priorDict[currentNode.getFac()] > self.__priorDict[itemFac] > self.__priorDict[currentNode.getNext().getFac()]:
                    item.setPrev(self.__head)
                    item.setNext(self.__head.getNext())
                    self.__head.getNext().setPrev(item)
                    self.__head.setNext(item)
            # 3.2.2 if already at the end of the main queue:
            elif currentNode.getNext() == None:
                if self.__priorDict[currentNode.getFac()] >= self.__priorDict[itemFac]:
                    item.setPrev(self.__tail)
                    self.__tail.setNext(item)
                    self.__tail = item
            # 3.2.3 if currentNode is at the first item after last item of the previous faculty and there are no other items of the new item's faculty but there are other items of other faculties down the priority queue:
            elif currentNode.getPrev() != None and currentNode.getNext() != None:
                if self.__priorDict[currentNode.getFac()] >= self.__priorDict[itemFac] > self.__priorDict[currentNode.getNext().getFac()]:
                    item.setPrev(currentNode)
                    item.setNext(currentNode.getNext())
                    item.getNext().setPrev(item)
                    currentNode.setNext(item)
            # 3.2.4 if currentNode is at the first item of the new item's faculty:
            elif self.__priorDict[currentNode.getFac()] == self.__priorDict[itemFac]:
                while self.__priorDict[currentNode.getNext().getFac()] == self.__priorDict[currentNode.getFac()]:
                    currentNode = currentNode.getNext()
                item.setPrev(currentNode)
                item.setNext(currentNode.getNext())
                item.getNext().setPrev(item)
                currentNode.setNext(item)

        self.__size += 1

    def dequeue(self):
        """returns the student node with the highest priority from the front of the queue"""
        assert self.__head != None, "cannot dequeue from empty queue"

        if self.__size > 2:
            temp = self.__head
            self.__head = self.__head.getNext()
            self.__head.setPrev(None)
            temp.setNext(None)

        elif self.__size == 2:
            temp = self.__head
            self.__head = self.__head.getNext()
            self.__tail = None
            self.__head.setNext(self.__tail)
            self.__head.setPrev(None)
            temp.setNext(None)

        elif self.__size == 1:
            temp = self.__head
            self.__head = None

        self.__size -= 1
        return temp

    def __str__(self):
        """string representation of the priority queue"""
        if not self.isEmpty():
            string = "["
            currentNode = self.__head
            while currentNode != None:
                string += f"{currentNode.getID()} {currentNode.getFac()} {currentNode.getFirstName()} {currentNode.getLastName()}, "
                currentNode = currentNode.getNext()
            string = string[:-2] + "]\n"
            return string
        else:
            return "[]\n"


if __name__ == "__main__":
    pass
    # table = EnrollTable(50)
    # student1 = StudentNode("162411", "SCI", "Sukanta", "Saha")
    # student2 = StudentNode("162410", "BUS", "Jesus", "Christ")
    # student3 = StudentNode("134234", "ART", "Helsey", "Halls")
    # student4 = StudentNode("163321", "ENG", "Judy", "Jones")
    # student5 = StudentNode("129422", "SCI", "Kevin", "Malone")
    # table.insert(student1)
    # table.insert(student2)
    # table.insert(student3)
    # table.insert(student4)
    # table.insert(student5)
    # print(table)
    # table.remove(student5.getID())
    # table.remove(student1.getID())
    # print(table)

    # pq = PriorityQueue()
    # student1 = StudentNode("122344", "BUS", "Janet", "Kim")
    # student2 = StudentNode("111222", "ENG", "Jung", "Kim")
    # student3 = StudentNode("123456", "ENG", "Kimchee", "Kimch")
    # student4 = StudentNode("198356", "SCI", "El", "Chapo")
    # student5 = StudentNode("534121", "ART", "Kimmy", "Granger")
    # student6 = StudentNode("324587", "SCI", "Eleanor", "Park")
    # pq.enqueue(student1)
    # pq.enqueue(student3)
    # pq.enqueue(student2)
    # pq.enqueue(student4)
    # pq.enqueue(student5)
    # pq.enqueue(student6)
    # print(pq)
    # a = pq.dequeue()
    # print(pq)
    # print(a)
    # print(pq.dequeue())
    # print(pq.dequeue())
    # print(pq.dequeue())
    # print(pq.dequeue())
    # print(pq.dequeue())



