import sys

N = int(sys.stdin.readline().rstrip())
sonsil = list(map(int, sys.stdin.readline().rstrip().split()))

sonsil.sort()
temp = []
if N%2 == 0:    #짝수
    for i in range(N//2):
        temp.append(sonsil[i]+sonsil[-i-1])
else:   #홀수
    for i in range((N-1)//2):
        temp.append(sonsil[i]+sonsil[-i-2])
    temp.append(sonsil[-1])
print(max(temp))
