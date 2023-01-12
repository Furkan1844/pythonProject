import os
import json
from datetime import datetime

item = {
    "id" : "",
    "name" : "",
    "quantity" : "",
    "date" : ""
    }

def checkFileExist(): # Checks if the file exist in the current path through os module
    fileControl = os.listdir()
    fn = "elements.json"
    try:
        for file in fileControl:
            if file == "elements.json":
                return getInput()
        else:
            yesno = input("File can not found!\nDo you want to create one?(y/n) : ")
            cptlz = yesno.capitalize()
            if cptlz == "Y":
                with open(fn, "x") as file: # "x", creates a file, returns an error if the file exist
                    file.write('{\n\t"elements" : [\n\t]\n}')
                    file.close
                with open(fn) as jsonFile:
                    returnFile = json.load(jsonFile)
                    elmntsOfJson = returnFile["elements"]
                    loadItemDict = item
                    loadItemDict["id"] = 0
                    elmntsOfJson.append(loadItemDict)
                    jsonDump(returnFile)
                return getInput()
            else:
                print("File couldn't created.")
    except:
        pass
    
def getInput(): # Displays options
    print("\n====================\n Inventory Options\n====================\n")
    options = ("1) Add an Item\n2) Delete an Item\n3) Update Item Quantity\n4) Change Item Name\n5) Exit\n")
    print(options)
    try:
        choice = int(input("Choose an option : "))
        if choice > 5 or choice < 1:
            print("Please enter valid number!\n")
            return getInput()
        else:
            driveOptions(choice)
    except:
        pass

def driveOptions(choice): # Forwards input to function that user chose
    try:
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
    finally:
        pass

def addItem():
    print("====================\n    Adding Item\n====================\n")
    fn = "elements.json"
    with open(fn) as f:
        idAssign = json.load(f)
        idIndex = idAssign["elements"][-1]
        idNum = idIndex["id"]
        idNum += 1
    item["id"] = idNum
    item["name"] = input("Enter the name of item : ")
    item["quantity"] = int(input("Enter the quantity of item : "))
    # day = datetime.today()
    # item["date"] = day
    
    with open(fn) as jsonFile:
        returnFile = json.load(jsonFile)
        elmntsOfJson = returnFile["elements"]
        loadItemDict = item
        elmntsOfJson.append(loadItemDict)
        jsonDump(returnFile)

def jsonDump(data):
    fn = "elements.json"
    with open(fn, "w") as f:
        json.dump(data, f, indent= 4)
    f.close

def deleteItem():
    print("====================\n   Deleting Item\n====================\n")
    dlt = int(input(f"Enter item's id number that you want to delete : "))
    nullData = []
    fn = "elements.json"
    with open(fn) as f:
        returnFile = json.load(f)
        returnList = returnFile["elements"]
        returnList[dlt] = nullData
        a = returnList.append(returnList)
        jsonDump(returnFile)

def updateQuantity(): # Changes the quantity by id of the item
    pass

def changeName(): # Changes the name by id of the item
    pass
