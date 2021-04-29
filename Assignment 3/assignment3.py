# Author: Sukanta Saha
# Assignment 3

from enrollStudent import *

def main():

    # creating enrollment table:
    capacity = 50
    table = EnrollTable(capacity)
    pq = PriorityQueue()

    end = False
    while not end:

        # asking for first input (R, D, Q):
        validPrompt = False
        while not validPrompt:
            inp = input("\nWould you like to register or drop students [R/D]: ")
            if inp in ["R", "D", "Q"]:
                validPrompt = True

        if inp != "Q":

            # asking for second input (fileName):
            validFileName = False
            while not validFileName:
                fileName = input("\nPlease enter a filename for student records: ")
                try:
                    with open(fileName) as fHandle:
                        fHandle = [data.rstrip() for data in fHandle.readlines()]
                except:
                    validFileName = False
                else:
                    validFileName = True

            # formatting data in fileName
            fHandle = [data.split() for data in fHandle]

            # Registering Option
            if inp == "R":
                try:
                    # populating table and queue with nodes
                    for i in range(len(fHandle)):
                        node = StudentNode(fHandle[i][0], fHandle[i][1], fHandle[i][2], fHandle[i][3])
                        if fHandle.index(fHandle[i]) <= capacity-1:
                            table.insert(node)
                        else:
                            pq.enqueue(node)
                except Exception as e:
                    print(e)
                    print(f"{fHandle[i][2]} {fHandle[i][3]} (ID# {fHandle[i][0]}) is invalid data. Could not register. Exiting...")
                    end = True
                else:
                    # printing and writing to output files
                    print(table)
                    print(pq)
                    enrolledTXT = open("enrolled.txt", "w")
                    enrolledTXT.write(str(table))
                    waitlistTXT = open("waitlist.txt", "a")
                    waitlistTXT.write(str(pq))
                    enrolledTXT.close()
                    waitlistTXT.close()

            # Dropping Option
            elif inp == "D":
                try:  # updating table and queue
                    for i in range(len(fHandle)):
                        if table.isEnrolled(fHandle[i][0]):
                            table.remove(fHandle[i][0])
                            dqNode = pq.dequeue()
                            table.insert(dqNode)
                        else:
                            print(f"\nWARNING: {fHandle[i][2]} {fHandle[i][3]} (ID: {fHandle[i][0]}) is not currently enrolled and cannot be dropped.")
                except Exception as e:
                    print(e)
                    end = True
                else:  # updating waitlist.txt with queue
                    waitlistTXT = open("waitlist.txt", "a")
                    waitlistTXT.write(str(pq))
                    waitlistTXT.close()
                    ### Note: Assignment guidelines say nothing about updating enrolled.txt after Dropping, but if we are supposed to update it, uncomment the next three lines.
                    # enrolledTXT = open("enrolled.txt", "w")
                    # enrolledTXT.write(str(table))
                    # enrolledTXT.close()
        else:
            print("Thank you for using the program. Exiting...")
            end = True


main()

