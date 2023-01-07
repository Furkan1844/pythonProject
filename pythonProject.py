import os

def itemDict(): # Makes a dict of items
    pass
def checkFolderExist(): # Checks if the file exist in the current path through os module
    getCWD = os.getcwd()
    fileControl = os.listdir()
    filename = "items.json"
    for file in fileControl:
        if file == "items.json":
            return getInput()
    else:
        yesno = input("File can not found!\nDo you want to create one?(y/n) : ")
        if yesno == "y":
            file = open(filename, "w")
            return getInput()

def getInput(): # Displays options
    print("====================\n Inventory Options\n====================\n")
    options = ("1) Add an Item\n2) Delete an Item\n3) Update Item Quantity\n4) Change Item Name\n5) Exit\n")
    print(options)
    choice = int(input("Choose an option : "))
    driveOptions(choice)

def driveOptions(choice): # Forwards input to function that user chose
    if choice == 1:
        addItem()
    if choice == 2:
        deleteItem()
    if choice == 3:
        updateQuantity()
    if choice == 4:
        changeName()
    if choice == 5:
        pass

def addItem(): 
    pass

def addQuantity(): # When user add an item, this func will ask the quantity
    pass

def deleteItem(): # Delete item by id
    pass

def updateQuantity(): # Changes the quantity by id of the item
    pass

def changeName(): # Changes the name by id of the item
    pass
