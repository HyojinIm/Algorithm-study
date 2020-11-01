import sys

def hanoiTower(n, start, arrival, remain):
    if n == 1:
        print(start, arrival)
    else:
        hanoiTower(n-1, start, remain, arrival)
        print(start, arrival)
        hanoiTower(n-1, remain, arrival, start)

N = int(sys.stdin.readline().rstrip())
print(2**N-1)
hanoiTower(N, 1, 3, 2)