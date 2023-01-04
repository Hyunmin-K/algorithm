import sys
input = sys.stdin.readline
n = int(input())
n1, n2, cnt = 0, 0, 0
ans1, ans2 = 0,0
n1 = n // 10
n2 = n % 10
n3 = (n1 + n2) % 10
while True:
    cnt+=1    
    if n2*10 + n3 != n:
        n1, n2 = n2, n3
        n3 = (n1 + n2) % 10
    else:
        break
print(cnt)