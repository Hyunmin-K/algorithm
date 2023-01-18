compare = 'CAMBRIDGE'
line = input()
for i in line:
    if i in compare:
        continue
    else:
        print(i,end='')