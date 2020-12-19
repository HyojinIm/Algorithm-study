import sys

N = int(sys.stdin.readline().rstrip())
nums = []

for i in range(N):
    nums.append(int(sys.stdin.readline().rstrip()))

total = [0, nums[0]]
for i in range(1, N):
    temp = []
    temp.append(max(total[-2])+nums[i])
    temp.append(total[-1][0]+nums[i])
    total.append(temp)
print(max(map(max, total)))