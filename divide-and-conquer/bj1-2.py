import sys

N = int(sys.stdin.readline().rstrip())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
white = 0
blue = 0

def cut(startX, startY, n):
    global white
    global blue
    num = paper[startX][startY]
    for i in range(startX, startX+n):
        for j in range(startY, startY+n):
            if paper[i][j] != num:
                for a in range(2):
                    for b in range(2):
                        cut(startX+b*(n//2), startY+a*(n//2), n//2)
                return
    if num == 0:
        white += 1
    else:
        blue += 1
    return

cut(0, 0, N)
print(white)
print(blue)