answer = [1,2,3,4,5]
num_list = list(map(int,input().split()))
while True:
    for i in range(4):
        if num_list[i] > num_list[i+1]:
            num_list[i], num_list[i+1] = num_list[i+1], num_list[i]
            for j in range(5):
                print(num_list[j],end=' ')
            print()
    if num_list == answer:
        break