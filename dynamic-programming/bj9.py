import sys

N = int(sys.stdin.readline().rstrip())

num = [[] for _ in range(N+2)]

num[1] = [0,1,1,1,1,1,1,1,1,1]

for i in range(2, N+1):
    num[i].append(num[i-1][1] % 1000000000)
    for j in range(1, 9):
        num[i].append(num[i-1][j-1] + num[i-1][j+1] % 1000000000)
    num[i].append(num[i-1][8] % 1000000000)

print(sum(num[N]) % 1000000000)