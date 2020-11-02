import sys

def cut(N, paper):
    WB = [0, 0]
    if N == 1:
        if paper[0][0] == 0:
            WB[0] += 1
        else:
            WB[1] += 1
        return WB
    count = 0
    for i in paper:
        count += i.count(0)
    if count!=0 and count!=N*N:
        temp = cut(N//2, [i[:N//2] for i in paper[:N//2]])
        WB[0] += temp[0]
        WB[1] += temp[1]
        temp = cut(N//2, [i[N//2:] for i in paper[:N//2]])
        WB[0] += temp[0]
        WB[1] += temp[1]
        temp = cut(N//2, [i[:N//2] for i in paper[N//2:]])
        WB[0] += temp[0]
        WB[1] += temp[1]
        temp = cut(N//2, [i[N//2:] for i in paper[N//2:]])
        WB[0] += temp[0]
        WB[1] += temp[1]
        return WB
    else:
        if count == 0:
            WB[1] += 1
        else:
            WB[0] += 1
        return WB

N = int(sys.stdin.readline().rstrip())
paper = []
for i in range(N):
    paper.append(list(map(int, sys.stdin.readline().split())))
temp = cut(N, paper)
print(temp[0])
print(temp[1])