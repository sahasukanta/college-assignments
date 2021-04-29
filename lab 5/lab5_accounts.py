import os
# lab 5 exception handling
def main():
    print(os.getcwd())
    close = False
    while not close:

        # getting the filename input
        inp = input("Enter filename > ")
        try:
            infile = open(inp)
        except OSError:
            print(f"File error: {inp} does not exist")
        else:
            accounts = readAccounts(infile)
            processAccounts(accounts)
        finally:
            print("Exiting program...goodbye.\n")
            close = True


def readAccounts(infile):
    """
    reads the accounts.txt file handler, warns about illegal illegal entries into values
    and does not add illegal accounts into returned dict
    input: accounts.txt file handler
    returns: dict with account name as key and balance as value
    """
    accounts = {}
    data = infile.readlines()
    for i in data:
        i = i.split('>')
        try:
            i[1] = float(i[1])
        except ValueError:
            print(f"Warning! Account for {i[0]} not added: illegal value for balance")
        else:
            accounts[i[0]] = i[1]

    infile.close()
    return accounts

def processAccounts(accounts):
    """
    prompts user for account name
    if name matches with existing accounts, prompts for transaction ammount
    input: accounts dict
    returns: None
    """
    quit = False
    while not quit:

        inp = input("Enter account name, or 'Stop' to exit: ")
        if inp == "Stop":
            quit = True
        else:
            try:
                balance = accounts[inp]
            except KeyError:
                print(f"Warning! Account for {inp} does not exist. Transaction cancelled.")
            else:
                amount = input(f"Enter transaction amount for {inp}: ")
                try:
                    accounts[inp] = balance + float(amount)
                    print(f"New balance for account {inp}: {accounts[inp]:.2f}")
                except ValueError:
                    print("Warning! Incorrect amount. Transaction cancelled")


main()
