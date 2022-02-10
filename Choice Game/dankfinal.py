import random as rand
from datetime import datetime
import time


# TODO finish the help sort of text thing
# TODO add a message when saving/loading

# TODO add more items in general
# TODO selling - print list of items in inventory with their words, getting user input from them(use hasItemBasedOn and check they have it) pass obj into removeFromInv and force save and then add worth, assign i then do assignment.worth should work


num = int()

names = (
    "Kim K", "Elon Musk", "Matt", "Peter Griffin", "Joe ", "Alfie Berwick", "Joe Sandy", "Ethan Mountain")
troll = ("Clapped", "rolled and trolled", "ezpz")


class Item:
    def __init__(self, worth, desc, name):
        self.worth = worth
        self.desc = desc
        self.name = name

    def getItemsAsList(self):
        return [self.worth, self.desc, self.name]

    def __str__(self):
        return "{} {} {} {} {}".format("This item is valued at", self.worth, self.desc, "This item is called a",
                                       self.name)


class Inventory:
    def __init__(self):
        self.inv = []

    def addToInv(self, item):
        self.inv.append(item)

    def getInventoryInFileWritableFormat(self):
        invList = []
        for item in self.inv:
            invList.append(item.getItemsAsList())
        return invList

    def has_Item(self, item):
        if item in self.inv:
            print("yes")
        else:
            print("no")

    def hasItemBasedOnStringInput(self, itemName):
        for i in self.inv:
            if i.name == itemName:
                return True, i
        return False, None

    def hasItemBasedOnStringInputVersion2(self, itemName):  # -> (bool, Item)
        print("Passed Item Name: " + itemName)
        for i in self.inv:
            print("Testing Against: " + i.name)
            if i.name.strip() == itemName.strip():
                return True, i
        return False, None

    def viewInv(self):
        print(self.inv)

    def removeFromInv(self, item):
        if item in self.inv:
            return None
        else:
            self.inv.remove(item)
            return item

    def moveToAnotherInventory(self, item, otherInv):
        theItem = self.removeFromInv(item)
        if theItem is not None:
            otherInv.addToinv(theItem)
            return otherInv
        else:
            return None

    def convertStringToItem(self):
        i = self[1:-1].split(",")
        itemAsList = [itemAttribute.replace("", "") for itemAttribute in i]
        return Item(itemAsList[2], itemAsList[1], itemAsList[0])


class InventoryFileManager:
    def __init__(self, filename):
        self.filename = filename if ".txt" in filename else filename + ".txt"

    def readInventory(self) -> Inventory:
        with open(self.filename, 'r') as f:
            iv = Inventory()
            for itemString in f.readlines():
                theItem = self.getItemFromString(itemString.strip())
                iv.addToInv(theItem)

        return iv

    def writeInventory(self, inv):  # -> None:
        with open(self.filename, "w") as f:
            for item in inv.getInventoryInFileWritableFormat():
                f.write(str(item))
                f.write("\n")

    def appendItemToInventoryFile(self, item):  # -> None:
        with open(self.filename, "a") as f:
            f.write(str(item.getItemAsList()))
            f.write("\n")

    def getItemFromString(self, s):  # -> Item:
        if s == "" or s == "[]":
            return None
        i = s[1:-1].split(",")
        itemAsList = [itemAttribute.replace('"', "").replace("'", "") for itemAttribute in
                      i]  # Order of list is [name, desc, worth]
        return Item(itemAsList[2].strip(), itemAsList[1].strip(),
                    itemAsList[0].strip())  # Because constructor is (worth, desc, name)


actualInv = Inventory()

Duck = Item(200, "common duck found after hunting.", "duck")  # defines the items here
Fish = Item(150, "placeholder", "fish")
Deer = Item(300, "placeholder", "deer")
Dragon = Item(10000, "placeholder", "dragon")
HuntingRifle = Item(10000, "Its useful for killing animals", "Hunting Rifle")
FishingPole = Item(50000, "Find fish get rich", "Fishing Pole")
Laptop = Item(10000, "post memes about cats or something idk", "Laptop")
Cookie = Item(15000, "Eat this for insane gains", "Cookie")
MiningComputer = Item(1000000, "It mines money over a period of time usually spans around ten minutes",
                      "Mining Computer")
GoldenFish = Item(800, "rare fish placeholder", "Golden Fish")
GoldenDeer = Item(1000, "rare deer placeholder", "Golden Deer")
CellPhone = Item(10000, "make tiktoks why not", "Cell Phone")


def addingItemsTest():  # using this when im testing inventory because it cant read the inventory back into the file yet  # opens inventory
    actualInv.addToInv(Duck)  # adds all of the items
    actualInv.addToInv(Fish)
    actualInv.addToInv(Dragon)
    actualInv.addToInv(Deer)
    actualInv.addToInv(Laptop)
    actualInv.addToInv(HuntingRifle)
    actualInv.addToInv(FishingPole)
    actualInv.addToInv(MiningComputer)
    actualInv.addToInv(CellPhone)
    actualInv.addToInv(Cookie)


def ChoosingMemes():  # uses method to check for item in inventory
    amountEarned = rand.randint(0, 842)
    if amountEarned > 200:
        print("Well at least it did okay, you've earned", amountEarned, "dogecoin")
        f = open("Balance.txt", "r")
        cash = int(f.read())
        f.close()
        newBalanceAfterPosting = amountEarned + cash
        f = open("Balance.txt", "w")
        f.write(str(newBalanceAfterPosting))
        f.close()

    elif amountEarned < 200:
        print("Nice it did pretty decently, you've earned", amountEarned, "dogecoin")
        f = open("Balance.txt", "r")
        cash = int(f.read())
        f.close()
        newBalanceAfterPosting = amountEarned + cash
        f = open("Balance.txt", "w")
        f.write(str(newBalanceAfterPosting))
        f.close()


    elif amountEarned < 400:
        print("Wow you got some very nice earnings there!, you've earned", amountEarned, "dogecoin")
        f = open("Balance.txt", "r")
        cash = int(f.read())
        f.close()
        newBalanceAfterPosting = amountEarned + cash
        f = open("Balance.txt", "w")
        f.write(str(newBalanceAfterPosting))
        f.close()

    elif amountEarned < 600:
        print("You'll be rich if you keep this up, you've earned", amountEarned, "dogecoin")
        f = open("Balance.txt", "r")
        cash = int(f.read())
        f.close()
        newBalanceAfterPosting = amountEarned + cash
        f = open("Balance.txt", "w")
        f.write(str(newBalanceAfterPosting))
        f.close()


def addinghighlow():
    f = open("Balance.txt", "r")  # opens file for reading
    cash = int(f.read())  # reads file as int
    cash2 = cash + num  # adds cash and num variable lower down in code
    f.close()  # closes file
    file = open("Balance.txt", "w")  # opens file in order to overwrite balance
    file.write(str(cash2))  # writes file as "string"
    file.close()  # closes file


def balance():
    f = open("Balance.txt", "r")  # opens file to read
    bal = int(f.read())  # reads file as int
    print("Your balance is", bal)  # prints balance


def newBalance():
    f = open("Balance.txt", "r")  # opens file to read
    bal = int(f.read())  # reads file as int
    print("Your new balance is", bal)  # prints balance


def searchingMoneyItems():
    whatIsFound = ["Gold Nugget", "IPhone", "Broken Laptop", "Fossil", "Tiny Diamond"]
    whatCanBeFound = rand.choice(whatIsFound)
    print("You have found a", whatCanBeFound)
    if whatCanBeFound == whatIsFound[0]:
        numberOfCoin = rand.randint(0, 541)
        f = open("Balance.txt", "r")
        cash = int(f.read())
        f.close()
        newAmountOfCash = numberOfCoin + cash
        f = open("Balance.txt", "w")
        f.write(str(newAmountOfCash))
        f.close()
        newBalance()
    elif whatCanBeFound == whatIsFound[1]:
        numberOfCoin = rand.randint(0, 762)
        f = open("Balance.txt", "r")
        cash = int(f.read())
        f.close()
        newAmountOfCash = numberOfCoin + cash
        f = open("Balance.txt", "w")
        f.write(str(newAmountOfCash))
        f.close()
        newBalance()
    elif whatCanBeFound == whatIsFound[2]:
        numberOfCoin = rand.randint(0, 121)
        f = open("Balance.txt", "r")
        cash = int(f.read())
        f.close()
        newAmountOfCash = numberOfCoin + cash
        f = open("Balance.txt", "w")
        f.write(str(newAmountOfCash))
        f.close()
        newBalance()
    elif whatCanBeFound == whatIsFound[3]:
        numberOfCoin = rand.randint(2502, 5410)
        f = open("Balance.txt", "r")
        cash = int(f.read())
        f.close()
        newAmountOfCash = numberOfCoin + cash
        f = open("Balance.txt", "w")
        f.write(str(newAmountOfCash))
        f.close()
        newBalance()
    elif whatCanBeFound == whatIsFound[4]:
        numberOfCoin = rand.randint(0, 362)
        f = open("Balance.txt", "r")
        cash = int(f.read())
        f.close()
        newAmountOfCash = numberOfCoin + cash
        f = open("Balance.txt", "w")
        f.write(str(newAmountOfCash))
        f.close()
        newBalance()


def searchingForItems():
    whereCanBeSearched = ["Sofa", "Chair", "Cupboard", "Table", "Car", "Backpack", "Bed", "Shop", "Boat", "Bus",
                          "Train", "Garden", "The Sea", "Museum", "Police Station"]
    searchOne = rand.choice(whereCanBeSearched)
    searchTwo = rand.choice(whereCanBeSearched)
    searchThree = rand.choice(whereCanBeSearched)
    print("=======================================")
    print("1.", searchOne)
    print("2.", searchTwo)
    print("3.", searchThree)
    choiceOfSearch = input("Pick somewhere to search here: 1 or 2 or 3\n=======================================")
    choiceOfSearch = choiceOfSearch.strip().lower()
    if choiceOfSearch == "1":
        searchingMoneyItems()
    elif choiceOfSearch == "2":
        searchingMoneyItems()
    elif choiceOfSearch == "3":
        searchingMoneyItems()


def shopSetup():  # im convinced this is insanely complex, not as complex as I think refactoring complete also
    shopPage = input(
        "What page would you like to view?\n1.Tools\n2.Consumables\n3.idk wtf this is yet\n4.Mining Machines\nChoose or press E to exit shop:")  # asking user what page they wanna go to
    if shopPage == "4":
        shopPage1 = input(
            "View more information about:\n1.Mining Computer\nChoose or press E to exit shop: ")
        if shopPage1 == "1":
            print(str(MiningComputer))
            finalize = input("Press R if you are ready to finalize your purchase or press E to exit")
            if finalize == "r":
                f = open("Balance.txt", "r")
                cash = int(f.read())
                f.close()
                priceSubFromBal = cash - MiningComputer.worth
                f = open("Balance.txt", "w")
                f.write(str(priceSubFromBal))
                f.close()
                actualInv.addToInv(MiningComputer)
                print("Purchase finalized and item added to inventory")
                printingTheInventory = actualInv.getInventoryInFileWritableFormat()
                print(printingTheInventory)
                newBalance()

    if shopPage == "1":  # picking page
        shopPage1 = input(
            "View more information about:\n1.Hunting Rifle\n2.Fishing Pole\n3.Laptop\nChoose or press E to exit shop:")  # option of pages
        if shopPage1 == "1":
            print(str(HuntingRifle))  # description of item that is printed
            finalize = input(
                "Press R if you are ready to finalize your purchase or press E to exit")  # confirmation of pages
            if finalize == "r":
                f = open("Balance.txt", "r")  # reads bal
                cash = int(f.read())
                f.close()
                priceSubFromBal = cash - HuntingRifle.worth  # pulls worth and subtracts from balance
                f = open("Balance.txt", "w")
                f.write(str(priceSubFromBal))  # saves final calculations
                f.close()  # closes file
                actualInv.addToInv(HuntingRifle)  # and then adds the inventory
                print("Purchase finalized and item added to inventory!")  # completion message
                printingTheInventory = actualInv.getInventoryInFileWritableFormat()  # an attempt to print out the inventory haven't figured this one out yet
                print(printingTheInventory)
                newBalance()  # finally it shows the new balance

        if shopPage1 == "2":
            print(str(FishingPole))
            finalize = input("Press R if you are ready to finalize your purchase or press E to exit")
            if finalize == "r":
                f = open("Balance.txt", "r")
                cash = int(f.read())
                f.close()
                priceSubFromBal2 = cash - FishingPole.worth
                f = open("Balance.txt", "w")
                f.write(str(priceSubFromBal2))
                f.close()
                actualInv.addToInv(FishingPole)
                print("Purchased finalized and added to inventory")
                printingTheInventory = actualInv.getInventoryInFileWritableFormat()
                print(printingTheInventory)
                newBalance()

        if shopPage1 == "3":
            print(str(Laptop))
            finalize = input("Press R if you are ready to finalize your purchase or press E to exit")
            if finalize == "r":
                f = open("Balance.txt", "r")
                cash = int(f.read())
                f.close()
                priceSubFromBal3 = cash - Laptop.worth
                f = open("Balance.txt", "w")
                f.write(str(priceSubFromBal3))
                f.close()
                actualInv.addToInv(Laptop)
                print("Purchased finalized and added to inventory")
                printingTheInventory = actualInv.getInventoryInFileWritableFormat()
                print(printingTheInventory)
                newBalance()
            else:
                print("Something")


def beggingcash():
    f = open("Balance.txt", "r")
    cash = int(f.read())
    value = rand.randint(0, 763)  # generates number between zero and 763
    cash2 = cash + value  # cash is added to the rand number
    randomchoiceofnames = rand.choice(names)  # random choice of name
    print(randomchoiceofnames, "gave you", value, "dogecoin")
    f.close()  # closes file
    file = open("Balance.txt", "w")  # overwrites file
    file.write(str(cash2))  # writes as string
    file.close()


def robbingcash():
    f = open("Balance.txt", "r")
    cash = int(f.read())
    value = rand.randint(0, 763)  # random number between 0 - 763
    cash2 = cash + value
    lol = rand.choice(names)  # random choice of names
    lol2 = rand.choice(troll)  # random choice of "insult"
    print("You stole", value, "dogecoin from", lol, lol2)  # printing the final result
    newBalance()  # calling balance to show updated user balance
    f.close()
    file = open("Balance.txt", "w")
    file.write(str(cash2))  # writes file as string
    file.close()


def highlow():
    number = rand.randint(0, 100)  # generates number from 0 - 100
    num2 = input("Guess if the number is higher or lower!")
    if num2 == "higher" and number > 50:  # asking for the guess and checking for the number
        print("Well done! You guessed correctly")
        addinghighlow()  # calls on earlier sub
        newBalance()  # shows balance because user got it write
    if num2 == "higher" and number < 50:
        print("Unlucky, the answer was", number)
    if num2 == "lower" and number < 50:
        print("Well done! You guessed correctly")
        addinghighlow()
        newBalance()
    if num2 == "lower" and number > 50:
        print("Unlucky, the answer was", number)
    else:
        print(
            "You've done something wrong")  # FIXME this doesnt work returns this error message even when entering correct input


def huntingTime():
    doesUserHave = actualInv.hasItemBasedOnStringInputVersion2("Hunting Rifle")
    if doesUserHave[0]:
        number = rand.randint(0, 10)
        if number < 5:
            print("You got one duck! Sell it for profit")
            actualInv.addToInv(Duck)
        if number > 5:
            print("You got three ducks nice! Sell them for profit")
            for i in range(0, 3):
                actualInv.addToInv(Duck)
                # figure out how to write inventory ask lucas later write the list to a file


def savingItemsAsWrite():
    fileManager = InventoryFileManager("Inventory.txt")
    fileManager.writeInventory(actualInv)
    print("Saving.................Complete!")
    f = open("Inventory.txt", "r")
    readingInventory = f.read()
    f.close()
    print(readingInventory)


def sellingItems():  # TODO ill come back to this
    print("======================================================================\nThis is everything in your "
          "inventory\n======================================================================")
    actualInventory = Inventory()
    ReadingInventory()
    whatIsSold = input("What from this list do you want to sell?")
    doTheyHaveSaidItem = actualInventory.hasItemBasedOnStringInputVersion2(whatIsSold)
    if doTheyHaveSaidItem:
        actualInventory.removeFromInv(whatIsSold)
        savingItemsAsWrite()


def fishingTime():
    doesUserHave = actualInv.hasItemBasedOnStringInputVersion2("Fishing Pole")
    print(doesUserHave[0])
    chanceOfDragon = rand.randint(0, 150)
    if doesUserHave[0]:
        number = rand.randint(0, 10)
        if number < 5:
            print("You found a fish whilst fishing!")
            actualInv.addToInv(Fish)
        elif number == 7:
            print("You got a golden fish!")
            actualInv.addToInv(GoldenFish)
        elif number > 5:
            print("You found three fish, nice!")
            for i in range(0, 3):
                actualInv.addToInv(Fish)
        elif chanceOfDragon == 1:
            print("Damn, you fished up a dragon!")
            actualInv.addToInv(Dragon)


def postMemes():
    doesUserHave = actualInv.hasItemBasedOnStringInputVersion2("Laptop")
    print(doesUserHave[0])
    if doesUserHave[0]:
        choiceOfMeme = input(
            "What would you like to post?\nA.Fresh Meme\nB.Repost\nC.Trending Meme\nD.Something completely random\nE.End")
        choiceOfMeme = choiceOfMeme.lower()
        if choiceOfMeme == "a":
            ChoosingMemes()

        elif choiceOfMeme == "b":
            ChoosingMemes()

        elif choiceOfMeme == "c":
            ChoosingMemes()

        elif choiceOfMeme == "d":
            ChoosingMemes()


def MiningMachines():
    doesUserHave = actualInv.hasItemBasedOnStringInputVersion2("Mining Computer")
    print(doesUserHave[0])
    f = open("Balance.txt", "r")
    cash = int(f.read())
    f.close()
    if doesUserHave[0]:
        for i in range(0, 10):
            miningMachineValue = rand.randint(800, 2000)
            print("========================================")
            print("Your machine found", miningMachineValue, "dogecoin, Nice!")
            newBalance()
            print("========================================")
            totalMiningValue = miningMachineValue + cash
            f = open("Balance.txt", "w")
            f.write(str(totalMiningValue))
            f.close()
            time.sleep(10)
            print("========================================")
            print("Your machine found", miningMachineValue, "dogecoin, Nice!")
            newBalance()
            print("========================================")
            totalMiningValue = miningMachineValue + cash
            f = open("Balance.txt", "w")
            f.write(str(totalMiningValue))
            f.close()


def ReadingInventory():
    inventoryManagement = InventoryFileManager("Inventory.txt")
    somethingElse = inventoryManagement.readInventory()
    for i in somethingElse.inv:
        print(i)
    return somethingElse


x = 0  # fix all of this mess
while x != 1:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("===================================")
    print("Welcome to Choice!\nThe time is", current_time, "\n===================================")
    Choice = input("What would you like to do?")
    Choice = Choice.strip().lower()

    if Choice == "beg":
        beggingcash()
        newBalance()

    elif Choice == "bal":
        balance()

    elif Choice == "highlow":
        highlow()

    elif Choice == "rob":
        robbingcash()

    elif Choice == "add":
        addingItemsTest()

    elif Choice == "shop":
        shopSetup()

    elif Choice == "e":
        x = 1
        print("You've exited, Goodbye!")

    elif Choice == "hunt":
        huntingTime()

    elif Choice == "save":
        savingItemsAsWrite()

    elif Choice == "pm":
        postMemes()

    elif Choice == "load":
        actualInv = ReadingInventory()

    elif Choice == "mine":
        MiningMachines()

    elif Choice == "fish":
        fishingTime()

    elif Choice == "search":
        searchingForItems()

    elif Choice == "view":
        print("======================================================================\nThis is everything in your "
              "inventory\n======================================================================")
        ReadingInventory()

    elif Choice == "sell":
        sellingItems()

    elif Choice == "help":
        print(
            "As of right now things that you should now and or things that are in the game are here:\n1.At the start "
            "of the game you can beg for money to earn income\n2.As you get richer you can use shop and buy items "
            "such as laptops and rifles however once you obtain items remember to use 'load' when opening the game "
            "and 'save' when exiting\n3. You can press 'e' to exit pretty much anything in the game\n4. You can use "
            "'rob' to rob people\n5.You can use 'highlow' to gamble and try your luck\n6.Im adding items "
            "overtime\n7.Use 'search' to find items and get payed for it.\n8.As of right now you may have to "
            "load/save cycle a couple time in order to get your items to work its weird")
# a sort of wall of text that displays all the commands
