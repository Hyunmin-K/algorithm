taebo = input()
left, right = 0,0
left_cnt, right_cnt = 0,0
for i in range(len(taebo)):
    if taebo[i:i+5] == '(^0^)':
        left = i
        right = i+5

for i in range(left):
    if taebo[i] == '@':
        left_cnt +=1
for i in range(right,len(taebo)):
    if taebo[i] == '@':
        right_cnt +=1
print(left_cnt, right_cnt)