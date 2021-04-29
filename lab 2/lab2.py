# lab 2 - Cipher
def getInputFile():
    """ asks for and returns the .txt filename """

    promptAttempt = 1
    correctExtension = False

    while not correctExtension:

        if promptAttempt < 2:
            inp = input("Enter the input filename: ")
        elif promptAttempt >= 2:
            inp = input("Please re-enter the input filename: ")

        # checking for .txt extension
        if inp[-4:] == ".txt":
            correctExtension = True
        else:
            print("Invalid filename extension. ", end="")
            promptAttempt += 1

    return inp

def decrypt(fileName):
    """
    Returns the decrypted message from the given filename.
    Filename must be a .txt file with [0] = the cipher key and [1] = the encrypted message
    """
    with open(fileName) as fileHandle:
        file = fileHandle.readlines()

    # fixing excessively large keys to fit into the 26 letters framework
    maxAlphabets = 26
    key = int(file[0].strip())%maxAlphabets

    # getting the encrypted msg
    encMsg = file[1].strip().lower()  # enc = encrypted
    decMsg = ""                       # dec = decrypted

    for i in encMsg:

        unicodeOrd = ord(i)
        unicodeA = 97
        unicodeZ = 122

        # scoping into the a-z range in unicode orders
        if unicodeA+key <= unicodeOrd <= unicodeZ:
            decUnicodeOrd = unicodeOrd - key
            decLetter = chr(decUnicodeOrd)
        # adjusting lower boundary for key length and wrap around functionality
        elif unicodeA <= unicodeOrd <= unicodeA+key:
            decUnicodeOrd = unicodeOrd + maxAlphabets - key
            decLetter = chr(decUnicodeOrd)
        # converting everything outside of a-z to \s
        else:
            decLetter = " "
        # adding each decrypted letter to the deccryped message (decMsg)
        decMsg = decMsg + decLetter

    # converting to a list for getting rid of all the extra spaces
    decMsg = decMsg.split()
    # adding one space back between each word
    decMsg = " ".join(decMsg)

    print("The decrypted message is:", decMsg, sep='\n')


def main():
    """ main script """

    fileName = getInputFile()
    decrypt(fileName)


main()











