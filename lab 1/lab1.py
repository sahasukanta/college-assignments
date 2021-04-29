# lab 1
# Exercise 1
print("Exercise 1-----------------------------------------")
numbers = [11, 25, 32, 4, 67, 18, 50, 11, 4, 11]

oddNumbers = []
print("The contents of object {ID} are {content}".format(ID=id(oddNumbers), content=oddNumbers))

for i in numbers:
    if i%2 == 1:
        oddNumbers.append(i)
print("The contents of object {ID} have been updated to {content}".format(ID=id(oddNumbers), content=oddNumbers))

oddNumbers.sort()
oddNumbers.reverse()
smallest = oddNumbers.pop(-1)
largest = oddNumbers.pop(0)
print("The smallest odd number, {num}, has been removed from the list of odd numbers.".format(num=smallest))
print("The largest odd number, {num}, has been removed from the list of odd numbers.".format(num=largest))
print("The contents of object {ID} have been updated to {content}".format(ID=id(oddNumbers), content=oddNumbers))

OGlen = len(numbers)
print("There are {OGlen} numbers in the original list.".format(OGlen=OGlen))
smallestOdd = min(oddNumbers)
for i in numbers:
    if i == smallestOdd:
        numbers.remove(i)
print("After removing the smallest odd number, there are {newlen} numbers in the list: \n{newlist}".format(newlen=len(numbers), newlist=numbers))

# Exercise 2
print("\nExercise 2-----------------------------------------")
months = ('JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL',
          'AUG', 'SEP', 'OCT')
print("The contents of object {ID} are {content}".format(ID=id(months), content=months))

months = months + ("NOV", "DEC")
print("The contents of object {ID} are {content}".format(ID=id(months), content=months))

precipitation2020 = [15.5, 12.1, 18.5, 15.6, 10.7, 62.2,
                     41.4, 58.3, 15.7, 15.3, 24.8]
precipitation2020.insert(6, 67.8)
print(precipitation2020)

month = months.index("MAY")
ppt = precipitation2020[month]
print("{ppt}mm fell in {month} 2020.".format(month=month, ppt=ppt))

inp = input("Please enter a month: ")
if inp in months:
    month = months.index(inp)
    ppt = precipitation2020[month]
    print("{ppt}mm fell in {month} 2020.".format(month=inp, ppt=ppt))
else:
    print("No match found")

# Exercise 3
print("\nExercise 3-----------------------------------------")
animals = {'dog', 'cat', 'fish', 'snake'}
print("The contents of object {ID} are {content}".format(ID=id(animals), content=animals))

animals.remove("snake")
animals.add("bird")
print("The contents of object {ID} are {content}".format(ID=id(animals), content=animals))

alice = {"dog", "cat", "hamster", "rabbit"}

print("Alice could buy {common} from Pets R Us.".format(common=alice & animals))

# Exercise 4
print("\nExercise 4-----------------------------------------")
bulbsForSale = {'daffodil': 0.35, 'tulip': 0.33, 'crocus': 0.25,
                'hyacinth': 0.75, 'bluebell': 0.50}

orders = {"Mary":[(50, "daffodil"),(100, "tulip")]}

bulbsForSale["tulip"] = round(bulbsForSale["tulip"]*1.25, 2)

orders["Mary"].insert(1, (30, "hyacinth"))

codes = {"daffodil":"DAF", "tulip":"TUL", "crocus":"CRO", "hyacinth":"HYA", "bluebell":"BLU"}
print("You have purchased the following bulbs:")
totalQuantity = 0
totalAmount = 0
for i in orders["Mary"]:
    code = codes[i[1]]
    quantity = i[0]
    itemCost = bulbsForSale[i[1]]
    subtotal = quantity * itemCost
    print("{0:5} *{1:4} = ${2:6.2f}".format(code, quantity, subtotal))
    totalQuantity += quantity
    totalAmount += subtotal
print("Thank you for purchasing %d bulbs from Bluebell Greenhouses. Your total comes to $%6.2f" %(totalQuantity, totalAmount))



