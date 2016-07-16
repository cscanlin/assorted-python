inventory = []
inventory3 = []

def chooseweapon ():
    inventory2 = []
    elsecounter = 2
    elsecounterdmg = 1

    weapon = input("Which weapon do you want to have? Sword, Dagger or Staff: ").lower()
    if weapon == "sword":
        inventory2 = ["Bastard Sword"]
    elif weapon == "dagger":
        inventory2 = ["Shiv"]
    elif weapon == "staff":
        inventory2 = ["Oak Staff"]
    else:
        while elsecounter > 1:
            elsecounter -= elsecounterdmg

            firstchoice = input("Which weapon do you want to keep? Sword, Dagger or Staff: ").lower()
            if firstchoice == "sword":
                inventory2 = ["Bastard Sword"]
            elif weapon == "dagger":
                inventory2 = ["Shiv"]
            elif weapon == "staff":
                inventory2 = ["Oak Staff"]

print("Your inventory is:", inventory)
chooseweapon()
inventory3 = inventory2 in chooseweapon()
inventory += inventory3

print("Your inventory is now:", inventory)
choice1 =input("Do you want to try to open the door or listen at the keyhole?: ")
input("\n\nPress the enter key to exit.")
