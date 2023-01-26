n = int(input())
num_list = list(range(1,n+1))
for i in range(n-1):
    print(num_list[0],end=' ')
    num_list.remove(num_list[0])
    num_list.append(num_list[0])
    num_list.remove(num_list[0])
print(num_list[0])