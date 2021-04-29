# lab 8
# Author: Sukanta Saha
# Student ID: 1624111


def mylen(someList):
    """
    recursive algo to determine the length of someList
    input: list item
    returns: length of list
    """
    if someList == []: return 0
    else: return 1 + mylen(someList[1:])


def intDivision(dividend, divisor):
    """
    recursive algo that returns dividend//divisor
    inputs: dividend and divisor must be positive int, dividend may be 0 as well"
    returns: dividend//divisor
    """
    assert dividend >= 0, "Dvidend must be positive integer or zero"
    assert divisor > 0, "Divisor must be positive integer"

    if dividend//divisor == 0:
        return 0
    else:
        dividend = dividend - divisor
        return 1 + intDivision(dividend, divisor)


def sumdigits(number):
    """
    recursive algo that sums the digits of number
    inputs: positive int
    returns: sum of digits as int
    """
    if len(str(number)) > 0:
        assert int(number) > 0, "Number must be a positive integer"
    number = str(number)
    if len(str(number)) == 0:
        return 0
    else:
        return int(number[0]) + sumdigits(number[1:])


def reverseDisplay(number):
    """
    recursive algo that reverses the digits of number
    input: positive int number
    returns: reversed number as string
    """
    if len(str(number)) > 0:
        assert int(number) > 0, "Number must be a positive integer"
    number = str(number)
    if number == "":
        return ""
    else:
        return reverseDisplay(number[1:]) + number[0]


def binary_search2(key, alist, lowerBound, upperBound):
    """
    recursive algo for binary search
    Finds and returns the position of key in alist,
    or returns -1 if key is not in the list
    inputs:
      - key is the target integer that we are looking for
      - alist is a list of integers, sorted in DECREASING order
      - lowerBound is the lowest index of alist
      - upperBound is the highest index of alist
    returns: index of key as int, or -1
    """
    guessIndex = (lowerBound+upperBound)//2
    guess = alist[guessIndex]
    if guess == key:
        return guessIndex
    elif upperBound-lowerBound < 1:
        return -1
    else:
        if guess > key:
            lowerBound = guessIndex + 1
        elif guess < key:
            upperBound = guessIndex - 1

        return binary_search2(key, alist, lowerBound, upperBound)


def main():

    # Exercise 1
    alist = [43, 76, 97, 86]
    print(mylen(alist))

    # Exercise 2
    n = int(input('Enter an integer dividend: '))
    m = int(input('Enter an integer divisor: '))
    print('Integer division', n, '//', m, '=', intDivision(n,m))

    # Exercise 3
    number = int(input('Enter a number:'))
    print(sumdigits(number))

    # Exercise 4
    number = int(input('Enter a number:'))
    print(reverseDisplay(number))

    # Exercise 5
    some_list = [9, 7, 5, 3, 1, -2, -8]
    print(binary_search2(9,some_list,0,len(some_list)-1))
    print(binary_search2(-8,some_list,0,len(some_list)-1))
    print(binary_search2(4,some_list,0,len(some_list)-1))


main()


