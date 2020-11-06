import sys

N = int(sys.stdin.readline().rstrip())
paper = [sys.stdin.readline().rstrip() for _ in range(N)]
result = ''

def cut(startX, startY, n):
    global result
    s = paper[startY][startX]
    for i in range(startY, startY+n):
        for j in range(startX, startX+n):
            if paper[i][j] != s:
                result += '('
                for a in range(2):
                    for b in range(2):
                        cut(startX+b*(n//2), startY+a*(n//2), n//2)
                result += ')'
                return
    if s == '0':
        result += '0'
    else:
        result += '1'
    return

cut(0, 0, N)
print(result)