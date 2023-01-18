line = input()
for i in range(len(line)):
    print(line[i],end='')
    if i%10 == 9:
        print()