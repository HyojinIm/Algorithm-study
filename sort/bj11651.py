import sys

N = int(sys.stdin.readline().rstrip())
nums = []
for i in range(N):
    nums.append(list(map(int,sys.stdin.readline().rstrip().split())))
nums.sort(key=lambda x: (x[1], x[0]))
for i in nums:
    print(str(i[0])+' '+str(i[1]))