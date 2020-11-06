import sys

a, b, c = map(int, sys.stdin.readline().split())

def remainder(a, b, c):
    if b == 1:
        return a%c
    elif b%2 == 0:  #짝수
        return remainder(a, b//2, c)**2%c
    else:   #홀수
        return remainder(a, b-1, c)*a%c

print(remainder(a, b, c))