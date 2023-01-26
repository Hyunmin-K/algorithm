k = int(input())
num_list = [0]
for i in range(k):
    n = int(input())
    if n != 0 :
        num_list.append(n)
    else:
        num_list.pop()
print(sum(num_list))