T = int(input())
for i in range(T):
    s = list(map(str,input().split()))
    for j in range(len(s)):
        for k in range(len(s[j])-1,-1,-1):
            print(s[j][k],end='')
        print(end=' ')
    print()