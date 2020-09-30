import sys

def checkCorrect(lst):
    change1 = 0
    change2 = 0
    temp = 'W'
    for i in range(8):
        for j in range(8):
            if lst[i][j] != temp:
                change1 += 1
            temp = ("B" if temp == 'W' else 'W')
        temp = ("B" if temp == 'W' else 'W')

    temp = 'B'
    for i in range(8):
        for j in range(8):
            if lst[i][j] != temp:
                change2 += 1
            temp = ("B" if temp == 'W' else 'W')
        temp = ("B" if temp == 'W' else 'W')
    return min(change1, change2)

a = sys.stdin.readline().rstrip()
a = list(map(int, a.split()))
chess = []
for i in range(a[0]):
    chess.append(sys.stdin.readline().rstrip())

changes = []
for i in range(a[0]-7):
    for j in range(a[1]-7):
        temp = [k[j:j+8] for k in chess[i:i+8]]
        changes.append(checkCorrect(temp))
print(min(changes))