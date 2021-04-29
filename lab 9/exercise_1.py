#******************************************************
# Lab 9: Exercise 1
# Author: Sukanta Saha
# Collaborators/References: n/a
#******************************************************
# Which sorting algorithm takes the least amount of time to sort:
# a) list of randomly generated integers? -- merge sort
# b) list of ascending integers? -- merge sort
# c) list of descending integers? -- merge sort
#
# Why?
# Because the merge sort algorithm breaks each element down before comparing which one is bigger, it takes into account the property of transitivity. i.e. if A is bigger than B and B is bigger than C, then A must also be bigger than C. And therefore does not compare A and C directly. But the selection sort ends up comparing previously compared (indirectly) elements which takes longer per element on average and is therefore slower than merge sort.
#******************************************************

import random
import time


def recursive_selection_sort(data, data_len, index=0):
    '''
    Use Selection Sort to arrange the integers in a list (data) in descending order
    Inputs:
       data (list) - list of integers to be sorted
       data_len (int) - number of elements in the data
       index (int) - index of starting element
    Returns: None
    '''
    # Set the base case
    if index+1 >= data_len: return None
    # Find the maximum index
    maximumIndex = index
    for i in range(index, data_len):
        if data[i] > data[maximumIndex]:
            maximumIndex = i
    # Swap the data
    temp = data[index]
    data[index] = data[maximumIndex]
    data[maximumIndex] = temp
    # Recursively calling selection sort function
    return recursive_selection_sort(data, data_len, index+1)

def merge(left, right):
    """
    merging for merge sort, descending order
    inputs : two lists containing integers
    returns: combined and sorted version of the two lists
    """
    leftIndex, rightIndex = 0, 0
    newList = []

    while leftIndex < len(left) and rightIndex < len(right):
        if left[leftIndex] > right[rightIndex]:
            newList.append(left[leftIndex])
            leftIndex += 1
        elif right[rightIndex] > left[leftIndex]:
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
    Use MergeSort to arrange the integers in a list (data) in descending order
    Inputs:  data (list) - list of integers to be sorted
    Returns: sorted data list
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
    # # Define the list of random numbers
    # random_list = [random.randint(1,1000) for i in range(500)]
    # list_len = len(random_list)
    # ascending_list = sorted(random_list)
    # descending_list = sorted(random_list, reverse=True)

    # # Calculate the execution time to sort a list of random numbers #
    # start_sel = time.time()
    # recursive_selection_sort(random_list, list_len)
    # end_sel = time.time()

    # start_merge = time.time()
    # recursive_merge_sort(random_list)
    # end_merge = time.time()

    # # Print the rsults execution time to sort a list of random numbers
    # print('The execution time: to sort a random list of integers in descending order.')
    # print(' - Recursive selection sort: {}'.format(end_sel - start_sel))
    # print(' - Recursive merge sort: {}'.format(end_merge - start_merge))


    # # Calculate the execution time to sort a list of intergers already sorted in ascending order #
    # start_sel = time.time()
    # recursive_selection_sort(ascending_list, list_len)
    # end_sel = time.time()

    # start_merge = time.time()
    # recursive_merge_sort(ascending_list)
    # end_merge = time.time()

    # # Print the rsults execution time to sort a list of intergers already sorted in ascending order
    # print('The execution time: to sort a ascending list of integers in descending order.')
    # print(' - Recursive selection sort: {}'.format(end_sel - start_sel))
    # print(' - Recursive merge sort: {}'.format(end_merge - start_merge))


    # # Calculate the execution time to sort a list of intergers already sorted in descending order #
    # start_sel = time.time()
    # recursive_selection_sort(descending_list, list_len)
    # end_sel = time.time()

    # start_merge = time.time()
    # recursive_merge_sort(descending_list)
    # end_merge = time.time()

    # # Print the results execution time to sort a list of intergers already sorted in descending order
    # print('The execution time: to sort a descending list of integers in descending order.')
    # print(' - Recursive selection sort: {}'.format(end_sel - start_sel))
    # print(' - Recursive merge sort: {}'.format(end_merge - start_merge))

    a = [10, 200, 42, 4134, -1, -5245, 23]
    recursive_selection_sort(a, len(a))
    print(a)

