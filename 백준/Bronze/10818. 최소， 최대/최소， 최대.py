n = int(input())
num_list = list(map(int,input().split()))
num_max = num_list[0]
num_min = num_list[0]
for i in range(n):
    if num_max < num_list[i]:
        num_max = num_list[i]
    if num_min > num_list[i]:
        num_min = num_list[i]

print(num_min, num_max)