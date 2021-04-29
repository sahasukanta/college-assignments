#******************
# Lab 9: Exercise 2
# Author: Sukanta Saha
# Collaborators/References: n/a
#******************

class Student():
    def __init__(self, idNum, name, mark):
        '''Initialize the object properties'''
        self.__id = idNum
        self.__name = name
        self.__mark = mark

    def getMark(self):
        '''Returns the value of the Student's mark'''
        return self.__mark

    def __str__(self):
        '''Informal string representation of Student'''
        return ' - {}, {}, {}'.format(self.__id, self.__name, self.__mark)

    def __lt__(self, anotherStudent):
        '''
        Checks if the mark of the student is less than the mark of another
        Student object
        Input: anotherStudent (Student)
        Returns: boolean
	    '''
        selfMarks = self.getMark()
        otherMarks = anotherStudent.getMark()
        if selfMarks < otherMarks:
            return True
        else:
            return False

def merge(left, right):
    """
    merging for merge sort, ascending order
    inputs : two lists containing integers
    returns: combined and sorted version of the two lists
    """
    leftIndex, rightIndex = 0, 0
    newList = []

    while leftIndex < len(left) and rightIndex < len(right):
        if left[leftIndex] < right[rightIndex]:
            newList.append(left[leftIndex])
            leftIndex += 1
        elif right[rightIndex] < left[leftIndex]:
            newList.append(right[rightIndex])
            rightIndex += 1
        elif left[leftIndex] == right[rightIndex]:
            newList.append(left[leftIndex])
            newList.append(right[rightIndex])
            leftIndex += 1
            rightIndex += 1

    newList += left[leftIndex:]
    newList += right[rightIndex:]

    return newList

def recursive_merge_sort(data):
    '''
    Uses MergeSort to sort the list of data in INCREASING order
    Returns: the sorted list of Students
    '''
    # Set the base case
    if len(data) <= 1:
        return data
    #Find the middle of the data list
    middleIndex = len(data)//2
    #Recursively calling merge sort function for both halves of the data list
    left = recursive_merge_sort(data[:middleIndex])
    right = recursive_merge_sort(data[middleIndex:])
    # merge the two halves of the data list and return the data list
    return merge(left, right)


if  __name__== "__main__":
    # Read the data
    students_file = open('student_list.txt', 'r')
    students_data = students_file.readlines()
    student_list = []

    # Create a Student object corresponding to each line in input file
    for student in students_data:
        fields = student.split(', ')
        ID = fields[0]
        name = fields[1]
        mark = fields[2]
        student_list.append(Student(ID, name, int(mark)))

    # Print the original data
    print('Original data:')
    for student in student_list:
        print(student)

    # Sort the students
    sorted_students = recursive_merge_sort(student_list)

    # Print the sorted data
    print('Sorted data:')
    for student in sorted_students:
        print(student)
