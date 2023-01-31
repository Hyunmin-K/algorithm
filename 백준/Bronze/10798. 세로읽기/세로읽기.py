# 세로 읽기
max_len = 0
word = []
for i in range(5):
    word.append(input())
    if len(word[i]) > max_len:
        max_len = len(word[i])

for i in range(max_len):    
    for j in range(5):
        if i >= len(word[j]):
            continue
        else:
            print(word[j][i], end='')