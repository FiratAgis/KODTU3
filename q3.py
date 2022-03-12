def match_analyser(pile1, pile2):
    if(pile1 == 0 and pile2 == 0):
        return False
    elif(pile1 == pile2):
        return True
    elif(pile1 == 0 or pile2 == 0):
        return True
    elif(abs(pile1 - pile2) == 1):
        return False
    else:
        return True

match_count = int(input())
matches = []
for x in range(0, match_count):
    matches.append(input().split())
    

for x in range(0, match_count):
    if(match_analyser(int(matches[x][0]), int(matches[x][1]))):
        print("T")
    else:
        print("F")
