"""
checkFileExist() =
driveOptions()   = seceneklerin tanimlandigi yer-->addItem, deleteItem, updateQuantity, changeName, exit
getInput()   = kullanicidan yapmak istedigi islemleri alma-->1 den 5 e kadar secenekler
addItem() = listeye yeni bir item ekleme
deleteItem() = listeden item silme
updateQuantity() = item miktarini guncelleme
changeName() = item ismini degistirme
        giveWarnings() = stock tukenmis ise kullaniciya uyari verme
        checkValidIndex() = girilen index numarasinin listedeki varligini kontrol eder
"""

import os
import json

item = {
        "id" : "",
        "name" : "",
        "quantity" : "",
        "date" : ""
    }

def checkFileExist(): # Checks if the file exist in the current path through os module
    fileControl = os.listdir()
    filename = "items.json"
    for file in fileControl:
        if file == "items.json":
            return getInput()
    else:
        yesno = input("File can not found!\nDo you want to create one?(y/n) : ")
        if yesno == "y":
            with open(filename, "x") as file: # "x", creates a file, returns an error if the file exist
                file.write("[\n{\n}")
            return getInput()
        else:
            pass
    
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

# idNumber = 0
# while idNumber == idNumber:        ID NUMBER
#     idNumber += 0
#     break

def addItem():
    print("====================\n    Adding Item\n====================\n")

    # item["id"] = ("{}").format(idNumber)            ID NUMBER
    item["name"] = input("Enter item's name : ")
    item["quantity"] = input("Enter item's quantity : ")
    with open("items.json", "a") as openjson:
        openjson.write(",\n")
        json.dump(item, openjson, indent=4)
        openjson.close
        
    # for key,value in item.items():
    #     opentxt.write(key + " : " + value + "\n")
    # opentxt.close

def deleteItem():
    print("====================\n    Deleting Item\n====================\n")
    # dlt = int(input("Enter item's id number that you want to delete : "))
    # x = open("items.json")
    # a = json.loads(open("items.json"))
    # for i, key in enumerate(a):
    #     print(i, key)
    # print(a[1])
    # a.remove(a[1])
    # print(a[1])
    # json.loads(open("items.json"))
    # x.close


def updateQuantity(): # Changes the quantity by id of the item
    pass

def changeName(): # Changes the name by id of the item
    pass

checkFileExist()
