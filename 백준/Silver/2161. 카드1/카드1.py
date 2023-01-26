n = int(input())
num_list = list(range(1,n+1))
ans_list = []
while len(num_list) > 1:
    ans_list.append(num_list.pop(0))
    # num_list.pop(0)
    num_list.append(num_list.pop(0))
print(*ans_list, num_list[0])