# Author: Sukanta Saha
# Student ID# 1624111

class StudentNode:

    def __init__(self, iD, faculty, first, last):
        """all parameters must be inserted as str format"""
        self.iD = iD
        self.faculty = faculty
        self.first = first
        self.last = last
        self.next = None
        self.previous = None

    """setters"""
    def setID(self, iD):
        """sets iD as the student iD"""
        self.iD = iD

    def setFac(self, fac):
        """sets fac as the student faculty"""
        self.faculty = fac

    def setFirstName(self, first):
        """sets first as the first name of student"""
        self.first = first

    def setLastName(self, last):
        """sets last as the last name of student"""
        self.last = last

    def setNext(self, next):
        """sets next as the next node of student"""
        self.next = next

    def setPrev(self, previous):
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
        return self.__size

    def isEmpty(self):
        return self.__size == 0

    def cmputIndex(self, studentID):
        """
        computes and returns the index of a given student ID based the specified algorithm. ex. studentID "123456" would return (12 + 34 + (56)^2)%self.__capacity
        """
        try:
            num = [studentID[i:i+2] for i in range(0, len(studentID), 2)]
            return (int(num[0]) + int(num[1]) + (int(num[2]))**2) % self.__maxCapacity
        except Exception as e:
            print(e)

    def insert(self, item):
        """
        item is a student node. inserts the new student node in the right location on the enrollment table.
        """
        assert type(item) == StudentNode, "typeError: incorrect item type"
        assert item.getFac() in self.__faculties, "item faculty currently not supported, currently supported faculties include SCI, ENG, BUS, ART, or EDU"

        itemID = item.getID()
        index = self.cmputIndex(itemID)
        # case 1: if slot at index is empty (None)
        if self.__table[index] == None:
            self.__table[index] = item
        # case 2: if slot at index is not empty
        else:
            currentNode = self.__table[index]
            currentNodeID = currentNode.getID()
            # case 2.1: if itemID is smaller than the first node ID, insert new item at the beginning of the linked list
            if itemID < currentNodeID:
                self.__table[index] = item
                item.setNext(currentNode)
            # case 2.2: if itemID is larger than the first node ID:
            else:
                # traverse through the list until the end is reached or a node with a bigger ID is reached
                while currentNode.getNext() != None and itemID > currentNode.getNext().getID():
                    currentNode = currentNode.getNext()
                    # currentNodeID = currentNode.getID()
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
        try:
            index = self.cmputIndex(studentID)
            if 0 > index > self.__capacity-1: raise Exception
            if self.__table[index] == None: raise Exception
        except:
            print("incorrect studentID argument")
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
                    # currentNodeID = currentNode.getID()
                    # if there is no match after traversing through the linked list
                    if currentNode.getNext() == None:
                        return False
                # case 2.1: if node to be removed is in the middle
                if currentNode.getNext().getNext() != None:
                    currentNode.setNext(currentNode.getNext().getNext())
                    # del currentNode
                # if node to be removed is a terminal node
                else:
                    currentNode.setNext(None)
                    # del currentNode

            self.__size -= 1
            return True

    def isEnrolled(self, studentID):
        """returns True if studentID is in table, False otherwise"""
        assert type(studentID) == str and len(studentID) == 6, "incorrect studentID argument, must be str of length 6"
        index = self.cmputIndex(studentID)
        # case 1: if slot at index is empty (None):
        if self.__table[index] == None:
            return False
        # case 2: if slot is not empty:
        else:
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
        string = "["
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
                string = string[:-2] + "]\n"

        return string


class PriorityQueue:

    def __init__(self):
        self.__priorDict = {"SCI": 4, "ENG": 3, "BUS": 2, "ART": 1, "EDU": 0}

        # internal queue heads and tails based on faculty
        self.innerRef = [self.__SCIhead, self.__SCItail, self.__ENGhead, self.__ENGtail, self.__BUShead, self.__BUStail, self.__ARThead, self.__ARTtail, self.__EDUhead, self.__EDUtail]
        # setting references to internal queues
        for index in range(len(self.innerRef)):
            self.innerRef[index] = StudentNode(None, None, None, None)
        for index in range(len(self.innerRef)-1):
            self.innerRef[index].setNext(self.innerRef[index+1])
        for index in range(1, len(self.innerRef)):
            self.innerRef[index].setPrev(self.innerRef[index-1])
        # main queue head and tail
        self.__head = None
        self.__tail = None

        self.__size = 0

    def size(self):
        return self.__size

    def isEmpty(self):
        """returns True if queue is empty, False otherwise"""
        return self.__size == 0

    def enqueue2(self, item):

        # CASE 0: SCI Queue
        if item.getFac() == "SCI":
            # case 0.1: adding the first item of this faculty (head):
            if self.__SCIhead.getID() == None:
                self.__SCIhead = item
                self.__head = self.__SCIhead
                self.__size += 1
                # if this item is the first item in the main queue
                if self.__size == 1:
                    self.__head.setNext(self.__tail)
            # case 0.2: adding the second item of this faculty (tail):
            elif self.__SCIhead.getID() != None and self.__SCItail.getID() == None:
                self.__SCItail = item
                self.__size += 1
                # if this item is the second item in the main queue:
                if self.__size == 2:
                    self.__tail = self.__SCItail
            # case 0.3: adding items beyond the second item of this faculty:
            elif self.__SCIhead.getID() != None and self.__SCItail.getID() != None:
                item.setPrev(self.__SCItail)
                self.__SCItail.setNext(item)
                self.__SCItail = item
                self.__size += 1

        # CASE 1: ENG Queue
        elif item.getFac() == "ENG":
            # case 1.1: adding the first item of this faculty (head):
            if self.__ENGhead.getID() == None:
                self.__ENGhead = item
                self.__size += 1
                if self.__size == 1:
                    self.__head = self.__ENGhead
                    self.__head.setNext(self.__tail)
                elif self.__size == 2:
                    # case 1.1.1: if the previous item is of higher priority:
                    if self.__priorDict[self.__head.getFac()] > self.__priorDict[item.getFac()]:
                        self.__tail = item
                        self.__tail.setPrev(self.__head)
                        self.__head.setNext(item)
                    # case 1.1.2: if the previous item is of lower priority:
                    elif self.__priorDict[self.__head.getFac()] < self.__priorDict[item.getFac()]:
                        temp = self.__head
                        self.__head = item
                        self.__tail = temp
                        self.__head.setNext(self.__tail)
                        self.__tail.setPrev(self.__head)
                elif:
            # case 1.2: adding the second item of this faculty (tail):
            elif self.__ENGhead.getID() != None and self.__ENGtail.getID() == None:
                self.__ENGtail = item
                item.setPrev(self.__ENGhead)
                self.__ENGhead.setNext(item)
                self.__size += 1
        # CASE 2: BUS Queue
        # CASE 3: ART Queue
        # CASE 4: EDU Queue

    def enqueue(self, item):
        """
        adds new item according to its priority into the queue.
        item must be a studentNode.
        """
        assert type(item) == StudentNode, "typeError: incorrect item type"
        studentFac = item.getFac()
        # case 1: when queue is completely empyty, make head=item, tail=None:
        if self.__head == None:
            self.__head = item
        # case 2: when only tail=None:
        elif self.__tail == None:
            if self.__priorDict[studentFac] < self.__priorDict[self.__head.getFac()]:
                self.__tail = item
                self.__head.setNext(self.__tail)
                self.__tail.setPrev(self.__head)
            elif self.__priorDict[studentFac] > self.__priorDict[self.__head.getFac()]:
                self.__tail = self.__head
                self.__head = item
                self.__tail.setPrev(self.__head)
                self.__head.setNext(self.__tail)
            else:
                self.__tail = item
                item.setPrev(self.__head)
                self.__head.setNext(item)
        # case 3: when queue has at least 2 items:
        else:
            currentNode = self.__head
            currentNodeFac = currentNode.getFac()
            # 3.1 traversing to the right faculty:
            while self.__priorDict[currentNodeFac] > self.__priorDict[studentFac] and currentNode.getNext() != None:
                currentNode = currentNode.getNext()
                currentNodeFac = currentNode.getFac()
            # 3.2.1 if at the beginning of the main queue:
            if currentNode.getPrev() == None:
                if self.__priorDict[currentNode.getFac()] < self.__priorDict[studentFac]:
                    item.setNext(self.__head)
                    self.__head.setPrev(item)
                    self.__head = item
                elif self.__priorDict[currentNode.getFac()] == self.__priorDict[studentFac]:
                    item.setPrev(self.__head)
                    self.__head.getNext().setPrev(item)
                    item.setNext(self.__head.getNext())
                    self.__head.setNext(item)
            # 3.2.2 if already at the end of the main queue:
            elif currentNode.getNext() == None:
                self.__tail.setNext(item)
                item.setPrev(self.__tail)
                self.__tail = item
            # 3.2.3 if currentNode is at the first item after last item of the previous faculty and there are no other items of the new item's faculty but there are other items of other faculties down the priority queue:
            elif currentNode.getPrev() != None:
                if self.__priorDict[currentNode.getPrev().getFac()] > self.__priorDict[studentFac] > self.__priorDict[currentNode.getFac()]:
                    item.setPrev(currentNode.getPrev())
                    item.setNext(currentNode)
                    item.getNext().setPrev(item)
                    currentNode.getPrev().setNext(item)
            # 3.2.4 if currentNode is at the first item of the new item's faculty:
            elif self.__priorDict[currentNode.getFac()] == self.__priorDict[studentFac]:
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
            self.__size -= 1
            return temp
        elif self.__size == 2:
            temp = self.__head
            self.__head = self.__head.getNext()
            self.__tail = None
            self.__head.setNext(self.__tail)
            self.__head.setPrev(None)
            temp.setNext(None)
            self.__size -= 1
            return temp
        elif self.__size == 1:
            temp = self.__head
            self.__head = None
            self.__size -= 1
            return temp

    def __str__(self):
        if not self.isEmpty():
            string = "["
            currentNode = self.__head
            while currentNode != None:
                string += f"{currentNode.getID()} {currentNode.getFac()} {currentNode.getFirstName()} {currentNode.getLastName()}, "
                currentNode = currentNode.getNext()
            string = string[:-1] + "]\n"
            return string
        else:
            return "[]"


if __name__ == "__main__":

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
    # num = [studentID[i:i+2] for i in range(0, len(studentID), 2)]
    #             return (int(num[0]) + int(num[1]) + (int(num[2]))**2)%self.capacity
    a = None
    b = a
    print(b)




