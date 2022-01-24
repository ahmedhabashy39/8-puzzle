from board import Board


root = [1, 2, 5, 3, 4, 0, 6, 7, 8]
goal = [0, 1, 2, 3, 4, 5, 6, 7, 8]


def state(tree):
    newstate = Board(tree[0])
    return newstate


def children(parent):

    pos = parent.poszero

    if pos == 0:
        modelright = parent.right()
        modeldown = parent.down()
        mlist = [modeldown, modelright]
    elif pos == 1:
        modelright = parent.right()
        modeldown = parent.down()
        modelleft = parent.left()
        mlist = [modeldown, modelleft, modelright]
    elif pos == 2:
        modeldown = parent.down()
        modelleft = parent.left()
        mlist = [modeldown, modelleft]
    elif pos == 3:
        modelup = parent.up()
        modelright = parent.right()
        modeldown = parent.down()
        mlist = [modelup, modeldown, modelright]
    elif pos == 4:
        modelup = parent.up()
        modelright = parent.right()
        modeldown = parent.down()
        modelleft = parent.left()
        mlist = [modelup, modeldown, modelleft, modelright]
    elif pos == 5:
        modelup = parent.up()
        modeldown = parent.down()
        modelleft = parent.left()
        mlist = [modelup, modeldown, modelleft]
    elif pos == 6:
        modelup = parent.up()
        modelright = parent.right()
        mlist = [modelup, modelright]
    elif pos == 7:
        modelup = parent.up()
        modelleft = parent.left()
        modelright = parent.right()
        mlist = [modelup, modelleft, modelright]
    else:
        modelup = parent.up()
        modelleft = parent.left()
        mlist = [modelup, modelleft]
    return mlist


tree = [root]


def addgen(tree):
    newmlist = children(state(tree))
    for x in newmlist:
        tree.append(x)
    return tree


def BFS(queue, goal):
    visited = []
    while queue:
        addgen(queue)
        vertex = queue.pop(0)
        visited.append(vertex)
        if vertex == goal:
            return visited, "found"


def printmode(root):
    print(root[0], root[1], root[2])
    print(root[3], root[4], root[5])
    print(root[6], root[7], root[8])


mode = int(input("choose mode : 1-Ai , 2-Human : "))
if mode == 1:
    print(BFS(tree, goal))
elif mode == 2:
    while root != goal:
        printmode(root)
        move = int(input("Choose 1-up , 2-down , 3- left , 4- right : "))
        pos = root.index(0)
        if move == 1:
            if pos in (0, 1, 2):
                print("Error Can't go up")
                continue
            else:
                root[pos], root[pos-3] = root[pos-3], root[pos]
                continue
        elif move == 2:
            if pos in (6, 7, 8):
                print("Error Can't go down")
                continue
            else:
                root[pos], root[pos+3] = root[pos+3], root[pos]
                continue
        elif move == 3:
            if pos in (0, 3, 6):
                print("Error Can't go left")
                continue
            else:
                root[pos], root[pos-1] = root[pos-1], root[pos]
                continue
        elif move == 4:
            if pos in (2, 5, 8):
                print("Error Can't go right")
                continue
            else:
                root[pos], root[pos+1] = root[pos+1], root[pos]
                continue
        else:
            print("Error unidentified number!")
            continue
    print("Goal reached")
    printmode(root)
else:
    print("Error unidentified number")
