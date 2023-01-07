import os


def checkFolderExist(): # Checks if the file exist in the current path through os module
    fileControl = os.listdir()
    filename = "items.txt"
    for file in fileControl:
        if file == "items.txt":
            return getInput()
    else:
        yesno = input("File can not found!\nDo you want to create one?(y/n) : ")
        if yesno == "y":
            file = open(filename, "x")
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
    print("====================\n Adding Item\n====================\n")
    item = {
        "id" : "",
        "name" : None,
        "quantity" : None,
        "date" : ""
    }
    item["name"] = input("Enter item's name : ")
    item["quantity"] = input("Enter item's quantity : ")
    w = open("items.txt", "a")
    w.write("\n{\n")
    for key,value in item.items():
        w = open("items.txt", "a")
        w.write(key + " : " + value + "\n")
    w.write("}")
    w.close

def writeItemToFile():
    pass

def deleteItem(): # Delete item by id
    pass

def updateQuantity(): # Changes the quantity by id of the item
    pass

def changeName(): # Changes the name by id of the item
    pass

checkFolderExist()
