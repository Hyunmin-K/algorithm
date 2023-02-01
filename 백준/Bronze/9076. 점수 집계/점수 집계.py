# 점수 집계

T = int(input())
for i in range(T):
    n = list(map(int,input().split()))
    n.remove(max(n))
    n.remove(min(n))
    if max(n) - min(n) >=4:
        print('KIN')
    else:
        print(sum(n))
    