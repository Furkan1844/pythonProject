def getInput(): # Displays options and gets an input
    print("====================\n Inventory Options\n====================\n")
    options = ("1) Add an Item\n2) Delete an Item\n3) Update Item Quantity\n4) Change Item Name\n5) Exit\n")
    print(options)
    choice = int(input("Chose an option:"))
    driveOptions(choice)

def driveOptions(choice): # Forwards input to function that user want
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

def deleteItem():
    pass

def updateQuantity():
    pass

def changeName():
    pass
