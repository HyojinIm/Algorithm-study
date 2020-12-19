import sys

N = int(sys.stdin.readline().rstrip())
nums = []

for i in range(N):
    nums.append(int(sys.stdin.readline().rstrip()))

score = [[0], [nums[0]]]
for i in range(1, N):
    temp = []
    temp.append(max(score[-2])+nums[i])
    temp.append(score[-1][0]+nums[i])
    score.append(temp)
    print(score)
print(max(score[-1]))