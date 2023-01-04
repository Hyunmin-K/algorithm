import sys
input = sys.stdin.readline
n = int(input())
for i in range(n):
    j = i+1
    print(" " * (n-j) + "*"*(j))