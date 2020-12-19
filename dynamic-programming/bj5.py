import sys

N = int(sys.stdin.readline().rstrip())
costs = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

totalCosts = costs[0]
for i in range(1, len(costs)):  #집
    temp = totalCosts[:]    #i-1번째 집까지 더해진 비용
    for j in range(3):  #3가지 색
        minCost = min([temp[k] for k in range(3) if k != j]) + costs[i][j]
        totalCosts[j] = minCost

print(min(totalCosts))