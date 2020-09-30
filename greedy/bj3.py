import sys

N = int(sys.stdin.readline().rstrip())
times = list(map(int, sys.stdin.readline().rstrip().split()))
time = 0

times.sort()

for i in range(len(times)):
    time += sum(times[:i+1])
print(time)