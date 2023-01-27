T = int(input())
n_list = list(map(int,input().split()))
n_dict={}
cnt = 0
for i in n_list:
    if i not in n_dict:
        n_dict[i] = 1
    else:
        n_dict[i]+=1
        cnt+=1
print(cnt)