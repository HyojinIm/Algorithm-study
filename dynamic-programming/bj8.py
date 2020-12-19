import sys

N = int(sys.stdin.readline().rstrip())

all = [0, 0, 1, 1]
for i in range(4, N+1):
    temp = []
    if i%2 == 0:
        temp.append(all[i//2]+1)
    if i%3 == 0:
        temp.append(all[i//3]+1)
    temp.append(all[i-1]+1)
    all.append(min(temp))

print(all[N])