import sys

N = int(sys.stdin.readline().rstrip())
house = []
for i in range(N):
    temp = list(map(int, sys.stdin.readline().rstrip()))
    house.append(temp)
adjacent = {}
for i in range(len(house)):
    for j in range(len(house[i])):
        if house[i][j] == 1:
            adjacent[N*i+j]=[]
            if j != 0:
                if house[i][j-1] == 1:
                    adjacent[N*i+j].append(N*i+j-1)
            if j != N-1:
                if house[i][j+1] == 1:
                    adjacent[N*i+j].append(N*i+j+1)
            if i != 0:
                if house[i-1][j] == 1:
                    adjacent[N*i+j].append(N*(i-1)+j)
            if i != N-1:
                if house[i+1][j] == 1:
                    adjacent[N*i+j].append(N*(i+1)+j)

result = []
while adjacent:
    stack = [list(adjacent.keys())[0]]
    danji = []
    while stack:
        temp = stack.pop()
        for i in adjacent.get(temp):
            if i not in danji:
                stack.append(i)
        if temp not in danji:
            danji.append(temp)
    result.append(danji)
    for i in danji:
        del adjacent[i]

result.sort(key=lambda x:len(x))
print(len(result))
for i in result:
    print(len(i))