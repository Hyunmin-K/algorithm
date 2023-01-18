T = int(input())
for i in range(T):
    r, s = map(str, input().split())
    for j in range(len(s)):
        print(s[j]*int(r),end='')
    print()