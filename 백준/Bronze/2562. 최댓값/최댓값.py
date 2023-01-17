num_list = []
max = 0
max_index = 0
for i in range(9):
    n = int(input())
    num_list.append(n)
    if max < num_list[i]:
        max = num_list[i]
        max_index = i+1
print(max)
print(max_index)