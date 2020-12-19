import sys

N = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().split()))

lst = [nums[0], nums[1]]
for i in range(2, len(nums)):
    if nums[i]>lst[-2] and nums[i]<lst[-1]:
        lst[-1] = nums[i]
    elif nums[i]>lst[-1]:
        lst.append(nums[i])

print(lst)