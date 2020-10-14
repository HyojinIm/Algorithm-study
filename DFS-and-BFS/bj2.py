import sys

V = int(sys.stdin.readline().rstrip())
E = int(sys.stdin.readline().rstrip())
adjacent = [[] for i in range(V)]
for i in range(E):
    edge = list(map(int, sys.stdin.readline().rstrip().split()))
    adjacent[edge[0]-1].append(edge[1])
    adjacent[edge[1]-1].append(edge[0])

stack = []
result = []
stack.append(1)
while stack:
    temp = stack.pop()
    if temp not in result:
        result.append(temp)
    for i in adjacent[temp-1]:
        if i not in result:
            stack.append(i)

print(len(result)-1)