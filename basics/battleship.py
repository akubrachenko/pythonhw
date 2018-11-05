import random
def createShips():
    ships = []
    i = 0
    j = 0
    l = 4 #count of ships
    for i in range(l):
        arr = []
        for j in range(l):
            arr.append(str(random.randrange(0,7))+str(random.randrange(0,7)))
        ships.append(arr)
    #checking the same x,y coordinates
    newships = []
    test = "#"
    for i in range(len(ships)):
        arr = []
        for j in range(l):
            if test == ships[i][0]: arr.append("#")
            else: arr.append(ships[i][0])
            test = ships[i][0]
        newships.append(arr)
    return newships          
def viewArena(arena):
    i=0
    j=0
    l=len(arena)
    arenas = "" 
    for i in range(l):
        for j in range(l):
                arenas += " " + arena[i][j] + " "
        print(arenas)
        arenas = ""
def startGame():
    battle_ships = createShips()
    status = 0
    did = ["99"]
    oldxy = ["99"]
    while status != len(battle_ships):
        xy = input("Please enter ship position (x,y): ")
        x = int(xy[0])
        y = int(xy[1])
        i=0
        j=0
        l=8 # size of map
        arenas = ""
        saved_arena = []
        ships = battle_ships
        shipxy = 0
        done = 0
        for i in range(len(ships)):
            if ships[i][0] == xy: 
                shipxy = 1
                break
            else: shipxy = 0
        for i in range(l):
            arr=[]
            arrdid=[]
            old = ""
            for j in range(l):
                if i == x and j == y and shipxy == 1:
                    arr.append("1")
                    status += 1
                    done = 1
                    did.append(str(i)+str(j))
                elif str(i)+str(j) in did: arr.append("o")
                elif str(i)+str(j) in oldxy: arr.append("x")
                else:
                    arr.append("*")
            saved_arena.append(arr)
        viewArena(saved_arena)
        #Use this code if you are CHITER or Uchitel
        for i in range(len(ships)):
            print(ships[i][0])
        if done == 1: print("Good Shoot!")
        else:
            oldxy.append(xy) 
            print("MiMo, try again")
            answer = input("Do you want to continue? Please enter 'y' or 'n': ")
            if answer == "n": status = len(battle_ships)
    print("The end. Good game")

startGame()
