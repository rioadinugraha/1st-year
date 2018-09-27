top = {}
mid ={}
bot = {}
space = 10
while True:
    status =  str(input("Do you want to use fridge Y/N? "))
    status = status.lower()
    if status == "y":
        container = str(input("what container do you want to put "))
        item = str(input("what item do you want to take or put in "))
        addOrTake = str(input("do you want to remove or add "))
        number = int(input("how many of the item"))
        addOrTake = addOrTake.strip()

        if addOrTake == "remove":
            number = 0 - number

        if container == "top":
            itemValue = top.get(item,0) + number
            chkCont = sum(top.values()) + number
        if chkCont > space:
            print("not enough space")
        elif itemValue < 0:
            print("you take too many")
        else:
            top.update({item:itemValue})

        print(top)

    if status == "n":
        break

