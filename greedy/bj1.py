import sys

temp = sys.stdin.readline().rstrip().split()
N = int(temp[0])
K = int(temp[1])

coins = []
answer = 0
for i in range(N):
    coins.append(int(sys.stdin.readline().rstrip()))

for i in reversed(coins):
    if i <= K:
        answer += K//i
        K -= K//i * i
    if K == 0:
        break

print(answer)