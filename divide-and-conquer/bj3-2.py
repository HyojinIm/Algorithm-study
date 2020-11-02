import sys

N = int(sys.stdin.readline().rstrip())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
num = [0, 0, 0]

def cut(startX, startY, n):
    global num
    first = paper[startX][startY]
    for i in range(startX, startX+n):
        for j in range(startY, startY+n):
            if paper[i][j] != first:
                for a in range(3):
                    for b in range(3):
                        cut(startX+b*(n//3), startY+a*(n//3), n//3)
                return
    if first == -1:
        num[0] += 1
    elif first == 0:
        num[1] += 1
    else:
        num[2] += 1
    return

cut(0, 0, N)
print(num[0])
print(num[1])
print(num[2])