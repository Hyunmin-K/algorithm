n = int(input())
num_list = []
for i in range(n):
    m = int(input())
    num_list.append(m)
sort_list = sorted(num_list)
for i in range(len(sort_list)):
    print(sort_list[i])