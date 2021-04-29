### Assignment 1 ### CMPUT175
# - Author: Sukanta Saha
# - Student ID: 1624111

def main():
    """main program"""

    products = createProductsDB()
    zones = createZonesDB()
    orders = createOrdersDB()
    allAddr = createAddrDB(orders)

    close = False
    while not close:

        inp = mainMenu()

        innerLoop = True
        while innerLoop:

            # option 1 - total orders by zones
            if inp == '1':

                # create summary database for the week
                summary, uniqueAddr = createSummary(allAddr, zones)
                # calculate the figures for the week
                totalDrivers, totalDeliveryCost, percDelCost = calculateSummary(summary, uniqueAddr,
                                                                                orders, products)
                # printing formatted weekly summary
                displayOpt1(summary, totalDrivers, totalDeliveryCost, percDelCost)
                innerLoop = False

            # option 2 - orders by address
            elif inp == '2':
                addrInp = input("Address: ")

                if addrInp in allAddr:
                    # creating invoice items and the total
                    invoice, total = createInvoice(addrInp, orders, products)
                    # printing formatted invoice
                    displayOpt2(addrInp, invoice, total)
                    # saving invoice.txt
                    writeInvoice(addrInp, invoice, total)
                    innerLoop = False
                else:
                    print("Invalid address")
                    innerLoop = False

            # option 3 - quit
            elif inp == '3':
                print("Thank you for using the Small Business Delivery Program! Goodbye.")
                innerLoop = False
                close = True



def getInput():
    """ asks for and returns the correct input (1,2,3)"""

    promptAttempt = 1
    correctInp = False

    while not correctInp:

        if promptAttempt < 2:
            inp = input("> ")
        elif promptAttempt >= 2:
            inp = input("Sorry, invalid entry. Please enter a choice from 1 to 3.\n> ")

        # checking for correct input
        if inp in ['1','2','3']:
            correctInp = True
        else:
            promptAttempt += 1

    return inp

def mainMenu():
    """displays main menu options
    returns correct choice (1,2,3)"""

    print("""\n**********************************************
Welcome to the Small Business Delivery Program
**********************************************
What would you like to do?
1. Display DELIVERY SUMMARY TABLE for this week
2. Display and save DELIVERY ORDER for specific address
3. Quit""")
    inp = getInput()

    return inp

def createZonesDB():
    """reads zones.txt, creates
    returns a zones database as dict obj"""

    with open('zones.txt') as fHandle:
        fHandle = fHandle.readlines()

    # creating the database
    readZones = [i.rstrip() for i in fHandle]
    zonesDB = dict()  # {zoneName : [zoneCode1, zoneCode2, ...]}
    for i in readZones:
        i = i.split(sep='#')
        zoneName = i[0]
        zoneCodes = i[1]
        zonesDB[zoneName] = [zoneCodes]

    for key, val in zonesDB.items():
        val = val[0].split(sep=',')
        zonesDB[key] = val

    return zonesDB

def createProductsDB():
    """reads products.txt, creates
    returns a products database as dict obj"""

    with open('products.txt') as fHandle:
        fHandle = fHandle.readlines()

    # creating the database
    readProds = [i.rstrip() for i in fHandle]
    prodDB = dict()  # {prodID : [prodName, prodCost]}
    for i in readProds:
        i = i.split(sep=';')
        prodID = i[0]
        prodName = i[1]
        prodCost = i[2]
        prodDB[prodID] = [prodName, prodCost]

    return prodDB

def createOrdersDB():
    """reads orders.txt, creates
    returns an orders database as list obj"""

    with open('orders.txt') as fHandle:
        fHandle = fHandle.readlines()

    # creating the database
    readOrders = [i.rstrip() for i in fHandle]
    ordersDB = []  # [[orderDate, userName, orderAddress, orderItemCode, orderItemQuantity], [...], ...]
    for i in readOrders:
        i = i.split(sep='%')
        ordersDB.append(i)

    ordersDB = sorted(ordersDB)  # for sorting the dates

    return ordersDB

def createAddrDB(orders):
    """creates a list of all addresses from
    each order of the week, including ducplicates"""

    allAddr = []
    for order in orders:
        allAddr.append(order[2])

    return allAddr

## Option 1 func definitions

def createSummary(allAddr, zones):
    """takes in all the addresses from each order and the zones database
    returns the summary and uniqe addresses for the week"""

    uniqueAddr = []
    for i in allAddr:
        if i not in uniqueAddr:
            uniqueAddr.append(i)

    postalCodes = []
    for i in uniqueAddr:
        postalCode = i[-7:-4]
        postalCodes.append(postalCode)

    counts = {}
    for key in zones.keys():
        counts[key] = 0
        for code in postalCodes:
            if code in zones[key]:
                counts[key] += 1

    summary = []
    for key in counts.keys():
        if counts[key] > 0:
            summaryItem = []
            summaryItem.append(key)  # zoneName
            summaryItem.append(counts[key])  # deliveries per zone

            drivers = driversNeeded(counts[key])  # number of drivers per zone
            summaryItem.append(drivers)
            summary.append(summaryItem)

    summary = sorted(summary) # sorting into alphabetical order

    return summary, uniqueAddr

def calculateSummary(summary, uniqueAddr, orders, products):
    """takes in the weekly summary, unique addresses, orders and products databases
    returns the total number of drivers needed, total delivery cost and their percentage"""

    costPerDel = 1200
    totalDeliveries = len(uniqueAddr)
    totalWeeklyPurchases = getTotalWeeklyPurchasesCost(products, orders)
    totalDeliveryCost = costPerDel * totalDeliveries
    percDelCost = (totalDeliveryCost/totalWeeklyPurchases) * 100

    totalDrivers = 0
    for line in summary:
        totalDrivers += line[-1]

    return totalDrivers, totalDeliveryCost, percDelCost

def getTotalWeeklyPurchasesCost(prodDB, ordersDB):
    """gets product, quantity and cost per item from prodDB and ordersDB
    returns the total cost in pennies of all the products bought in the
    week by all customers"""

    productsBought = []  # [[itemCode, quantity], [...], ...]
    for order in ordersDB:
        itemCode, quantity = order[-2], order[-1]
        productsBought.append([itemCode, quantity])

    for order in productsBought:  # [[itemCode, quantity, itemCost, itemSubtotal], [...], ...]
        itemCost = prodDB[order[0]][1]
        itemSubtotal = int(itemCost) * int(order[1])
        order.append(itemCost)
        order.append(itemSubtotal)

    total = 0
    for order in productsBought:
        total += order[-1]  # total = total + itemSubtotal

    return total

def driversNeeded(num):
    """returns the number of drivers needed for
    each zone depending on the num of deliveries"""

    result = num//10
    if result != num/10:
        result += 1

    return result

def displayOpt1(summary, totalDrivers, totalDeliveryCost, percDelCost):
    """takes weekly summary and figures
    displays option 1 output"""

    print("+", "-"*15, "+", "-"*12, "+", "-"*11, "+", sep='')
    print("| Delivery Zone | Deliveries |  Drivers  |")
    print("+", "-"*15, "+", "-"*12, "+", "-"*11, "+", sep='')
    for line in summary:
        zone = "%-13s" % line[0]
        print("| {0} | {1:" "^10} | {2:" "^9} |".format(
            zone, line[1], line[2]))
    print("+", "-"*15, "+", "-"*12, "+", "-"*11, "+", sep='')
    print("| Total Drivers Needed {0:" ">17} |".format(totalDrivers))
    totalDeliveryCost = totalDeliveryCost/100
    print("| Total Delivery Cost          $ %7.2f |" % totalDeliveryCost)
    print("| Delivery Cost/purchases %13.1f%% |" % percDelCost)
    print("+", "-"*40, "+", sep="")

## Option 2 func definitions

def createInvoice(addrInp, orders, products):
    """takes in addrInp, orders and products database
    returns invoice, total"""

    invoice = []  # full invoice for the address in input
    for order in orders:

        invoiceItem = []  # each line of the requested invoice
        if addrInp == order[2]:
            invoiceItem.append(order[0])   # orderDate
            invoiceItem.append(order[-1])  # orderQuantity
            invoiceItem.append(products[order[-2]][0])  # orderItemName

            totalItemCost = (int(order[-1]) * int(products[order[-2]][1]))/100   # (orderQuantity * itemCostPerUnit)/100
            invoiceItem.append(totalItemCost)
            invoice.append(invoiceItem)

    total = 0
    for i in invoice:
        total += i[-1]

    return invoice, total

def displayOpt2(addrInp, invoice, total):
    """takes addrInp and invoice
    displays option 2 output"""

    months = {'01': 'JAN', '02': 'FEB', '03': 'MAR', '04': 'APR', '05': 'MAY', '06': 'JUN',
              '07': 'JUL', '08': 'AUG', '09': 'SEP', '10': 'OCT', '11': 'NOV', '12': 'DEC'}

    if len(addrInp) <= 30:
        print("\nDelivery for: {0:" ">30}".format(addrInp))
    else:
        print("\nDelivery for: {0:" ">29}*".format(addrInp[:29]))
    print("="*44)
    print("Date    Item                        Price   ")
    print("------  --------------------------  --------")
    for line in invoice:
        if len(line[2]) > 20:
            itemDescription = line[2][:19] + "*"
        else:
            itemDescription = line[2]
        subTotal = "%7.2f" % line[-1]
        print("{0} {1}  {2:0>3} x {3:" "<20}  ${4}".format(months[line[0][5:7]], line[0][8:],
                                                           line[1], itemDescription, subTotal))
    print(" "*35, "--------")
    print(" "*35, "$%7.2f" % total)

def writeInvoice(addrInp, invoice, total):
    """writes the displayed output to invoice.txt file
    file is created if does not exist"""

    months = {'01': 'JAN', '02': 'FEB', '03': 'MAR', '04': 'APR', '05': 'MAY', '06': 'JUN',
                '07': 'JUL', '08': 'AUG', '09': 'SEP', '10': 'OCT', '11': 'NOV', '12': 'DEC'}

    with open("invoice.txt", 'w') as handle:
        if len(addrInp) <= 30:
            handle.write("Delivery for: {0:" ">30}\n".format(addrInp))
        else:
            handle.write("Delivery for: {0:" ">29}*\n".format(addrInp[:29]))
        handle.write("="*44 + '\n')
        handle.write("Date    Item                        Price   \n")
        handle.write("------  --------------------------  --------\n")
        for line in invoice:
            if len(line[2]) > 20:
                itemDescription = line[2][:19] + "*"
            else:
                itemDescription = line[2]
            subTotal = "%7.2f" % line[-1]
            handle.write("{0} {1}  {2:0>3} x {3:" "<20}  ${4}\n".format(months[line[0][5:7]], line[0][8:],
                                                                        line[1], itemDescription, subTotal))
        handle.write(" "*35 + " --------\n")
        handle.write(" "*35 + " $%7.2f\n" %total)



main()


