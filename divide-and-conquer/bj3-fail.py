import sys

def cut(N, x, y):
    global paper
    paper2 = [k[y:y+N] for k in paper[x:x+N]]
    result = [0, 0, 0]
    if N == 1:
        if paper2[0][0] == -1:
            result[0] += 1
        elif paper2[0][0] == 0:
            result[1] += 1
        else:
            result[2] += 1
        return result
    num = [0, 0, 0]
    flag = True
    pre = paper2[0][0]
    for i in paper2:
        for j in i:
            now = j
            if pre != now:
                flag = False
                break
            if j == -1:
                num[0] += 1
            elif j == 0:
                num[1] += 1
            else:
                num[2] += 1
            pre = now
        if pre != now:
            flag = False
            break
    if not flag:
        for i in range(3):
            for j in range(3):
                #temp = cut(N//3, [k[j*(N//3):(j+1)*(N//3)] for k in paper[i*(N//3):(i+1)*(N//3)]])
                #paper = [k[j*(N//3):(j+1)*(N//3)] for k in paper[i*(N//3):(i+1)*(N//3)]]
                temp = cut(N//3, x+i*(N//3), y+j*(N//3))
                result = [a+b for a,b in zip(result, temp)]
        return result
    else:
        if num[0] != 0:
            result[0] += 1
        elif num[1] != 0:
            result[1] += 1
        else:
            result[2] += 1
        return result

N = int(sys.stdin.readline().rstrip())
paper = []
for i in range(N):
    paper.append(list(map(int, sys.stdin.readline().split())))
temp = cut(N, 0, 0)
print(temp[0])
print(temp[1])
print(temp[2])