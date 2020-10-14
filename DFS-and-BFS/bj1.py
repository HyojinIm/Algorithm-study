import sys

lst = list(map(int, sys.stdin.readline().rstrip().split()))
adList = [[] for i in range(lst[0])]
edges = []
for i in range(lst[1]):
    edges.append(list(map(int, sys.stdin.readline().rstrip().split())))
for i in edges:
    adList[i[0]-1].append(i[1])
    adList[i[1]-1].append(i[0])

stack = []
DFS = []
stack.append(lst[2])
while stack:
    temp = stack.pop()
    for i in sorted(adList[temp-1], key=lambda x:-x):
        if i not in DFS:
            stack.append(i)
    if temp not in DFS:
        DFS.append(temp)

queue = []
BFS = []
queue.append(lst[2])
while queue:
    temp = queue.pop(0)
    for i in sorted(adList[temp-1]):
        if i not in BFS:
            queue.append(i)
    if temp not in BFS:
        BFS.append(temp)

for i in DFS:
    print(i, end=' ')
print('')
for i in BFS:
    print(i, end=' ')