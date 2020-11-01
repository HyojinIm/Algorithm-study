import sys

def factorial(n):
    return 1 if n==1 or n==0 else n*factorial(n-1)

N = int(sys.stdin.readline().rstrip())
print(factorial(N))