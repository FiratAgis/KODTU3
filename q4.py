def cutAndUpdate(blocks, index, direction, amount):
    X = blocks[index][0]
    Y = blocks[index][1]
    Z = blocks[index][2]
    if(direction == 0):
        mult = Y * Z
        blocks[0] += mult * mult
        blocks.append((amount, Y, Z, amount * mult))
        blocks.append((X - amount, Y, Z, (X - amount) * mult))

    elif(direction == 1):
        mult = X * Z
        blocks[0] += mult * mult
        blocks.append((X, amount, Z, amount * mult))
        blocks.append((X, Y - amount, Z, (Y - amount) * mult))

    elif(direction == 2):
        mult = X * Y
        blocks[0] += mult * mult
        blocks.append((X, Y, amount, mult * amount))
        blocks.append((X, Y, Z - amount, mult * (Z - amount)))
    blocks.pop(index)
    return blocks

def newList(blocks):
    returnList = []
    for block in blocks:
        returnList.append(block)
    return returnList

def solExsits(blocks, val, K):
    if(val == 0):
        length = min(2, len(blocks))
    else:
        length = len(blocks)
    for x in range(0, length):
        newVal = val + blocks[x][3]
        if(newVal < K):
            if(solExsits(blocks[x + 1: ], newVal, K)):
                return True
        elif(newVal == K):
            return True
    return False
        
def allCuts(blocks, minSolution):
    length = len(blocks)
    configureList = []
    cost = blocks[0]
    for index in range(1, length):
        X = blocks[index][0]
        Y = blocks[index][1]
        Z = blocks[index][2]
        if(Y * Z + cost < minSolution and X != Y and X != Z):
            for amount in range(1, int(X/2) + 1):
                configureList.append(cutAndUpdate(newList(blocks), index, 0, amount))
        if(X * Z + cost < minSolution and Y != Z):
            for amount in range(1, int(Y/2) + 1):
                configureList.append(cutAndUpdate(newList(blocks), index, 1, amount))
        if(X * Y + cost < minSolution):
            for amount in range(1, int(Z/2) + 1):
                configureList.append(cutAndUpdate(newList(blocks), index, 2, amount))
    return configureList

def solver(X, Y, Z, K):
    minSolution = X * Y * X * Y + X * (Z - 1) * X * (Z - 1)  + (Y - 1) * (Z - 1) * (Y - 1)* (Z - 1)
    configurations = [[0, (X, Y, Z, X * Y * Z)]]
    dcount = 0
    dlimit = 5
    while(len(configurations) > 0 and dcount < dlimit):
        count = 0
        length = len(configurations)
        while(count < length):
            configuration = configurations[0]
            configurations.pop(0)
            if(solExsits(configuration[1: ], 0, K)):
                minSolution = min(minSolution, configuration[0])
            elif(configuration[0] < minSolution):
                configurations += allCuts(configuration, minSolution)
            count += 1
        dcount += 1
    return minSolution

count = int(input())
situations = []

for x in range(0, count):
    situations.append(input().split())

for x in range(0, count):
    print(solver(int(situations[x][0]), int(situations[x][1]), int(situations[x][2]), int(situations[x][3])))
