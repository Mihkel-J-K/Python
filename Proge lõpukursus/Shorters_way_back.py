import time
def shortest_way_back(path: str) -> str:
    cordinate = [0,0]
    solution = ""
    for i in path.upper():
        if i == "N":
            cordinate[0] += 1
        if i == "S":
            cordinate[0] -= 1
        if i == "E":
            cordinate[1] += 1
        if i == "W":
            cordinate[1] -= 1
    while cordinate[0] > 0:
        cordinate[0] -= 1
        solution += "S"
        print(cordinate)
    while cordinate[0] < 0:
        cordinate[0] += 1
        solution += "N"
        print(cordinate[0])
    while cordinate[1] > 0:
        cordinate[1] -= 1
        solution += "W"
        print(cordinate)
    while cordinate[1] < 0:
        cordinate[1] += 1
        solution += "E"
        print(cordinate[1])
    return solution
start = time.time()
print(shortest_way_back("WWWW"))
print(time.time()-start)
