T = int(input())
for i in range(T):
    sum = 0
    n = int(input())
    num_list = list(map(int,input().split()))
    for j in range(n):
        sum +=num_list[j]
    print(sum)