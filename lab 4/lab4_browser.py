#----------------------------------------------------
# Lab 4: Web browser simulator
# Purpose of code:
#
# Author:
# Collaborators/references:
#----------------------------------------------------

from stack import Stack

def getAction():
    """
    prompts user for input
    returns only correct input
    """
    allInp = ["=", "<", ">", "q"]
    correctInp = False
    while not correctInp:
        inp = input("Enter = to enter a URL, < to go back, > to go forward, q to quit: ")
        if inp in allInp:
            correctInp = True
        else:
            print("Invalid entry.")

    return inp

def goToNewSite(current, bck, fwd):
    """
    takes in current url, back stack and forward stack, asks for new url
    returns new url and updates to current, the back stack, cleans forward stack
    """
    inp = input("URL: ")
    bck.push(current)
    for _ in range(fwd.size()):
        fwd.pop()
    current = inp
    return inp

def goBack(current, bck, fwd):
    """
    adds current to forward stack, and
    pops top of back stack to current
    """
    if bck.size() < 1:
        print("Cannot go back.")
    else:
        fwd.push(current)
        current = bck.pop()
    return current


def goForward(current, bck, fwd):
    """
    adds current to back stack, and
    pops top of forward stack to current
    """
    if fwd.size() < 1:
        print("Cannot go forward.")
    else:
        bck.push(current)
        current = fwd.pop()
    return current

def main():
    HOME = 'www.cs.ualberta.ca'
    back = Stack()
    forward = Stack()

    current = HOME
    quit = False

    while not quit:
        print('\nCurrently viewing', current)
        action = getAction()

        if action == '=':
            current = goToNewSite(current, back, forward)
        elif action == '<':
            current = goBack(current, back, forward)
        elif action == '>':
            current = goForward(current, back, forward)
        elif action == 'q':
            quit = True

    print('Browser closing...goodbye.')


if __name__ == "__main__":
    main()
