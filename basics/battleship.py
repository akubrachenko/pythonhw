import random
def getShips():
    ships = []
    l = 4 #count of ships
    status = 0
    while status != l:
        x = random.randrange(0,9)
        y = random.randrange(0,9)
        if [x,y] not in ships: 
            ships.append([x,y])
            status += 1
    return ships    
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
    battle_ships = getShips()
    status = 0
    did = []
    oldxy = []
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
            if ships[i] == [x,y]: 
                shipxy = 1
                break
            else: shipxy = 0
        for i in range(l):
            arr=[]
            arrdid=[]
            old = ""
            for j in range(l):
                if i == x and j == y and shipxy == 1 and [i,j] not in did:
                    arr.append("1")
                    status += 1
                    done = 1
                    did.append([i,j])
                elif [i,j] in did: arr.append("o")
                elif [i,j] in oldxy: arr.append("x")
                else:
                    arr.append("*")
            saved_arena.append(arr)
        viewArena(saved_arena)
        #Use this code if you are CHITER or Uchitel
        for i in range(len(ships)):
            print(ships[i])
        if done == 1: print("Good Shoot!")
        else:
            oldxy.append([x,y]) 
            print("MiMo, try again")
            answer = input("Do you want to continue? Please enter 'y' or 'n': ")
            if answer == "n": status = len(battle_ships)
    print("The end. Good game")
startGame()
