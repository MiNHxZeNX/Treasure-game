print("\n")
print("Welcome to the treasure island.\nYour goal is to find the treasure.")
sidedir = input("There are two ways for you to go.\nLeft or Right : ")
dir = sidedir.lower()
if (dir=="left"):
    print("\n")
    pond = input("Good Choice\nNow here is a pond, your can swim or walk by sideway.\nSwim or Walk : ")
    ond = pond.lower()
    if(ond=="walk"):
        print("\n")
        door = input("You are on final stage.\nNow you have three doors to find about the Treasure.\nThey are Red, Blue and Yellow : ")
        oor = door.lower()
        if (oor=="red"):
            print("\n")
            print("Behind the Red door there was fire.\nGame Over.")
        elif (oor=="blue"):
            print("\n")
            print("Behind the Blue door there were Nuclear waste products.\nGame Over.")
        else:
            print("\n")
            print("Congratulations!!! You have found the treasures.\nGG.")
    else:
        print("\n")
        print("The pond was full of alligators.\nGame Over.")
else:
    print("\n")
    print("You've drown to steam of water.\nGame Over.")
