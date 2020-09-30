import sys

n = int(sys.stdin.readline().rstrip())
a = []

for i in range(n):
    temp = int(sys.stdin.readline().rstrip())
    if temp == 0:
        a.pop()
    else:
        a.append(temp)

print(sum(a))