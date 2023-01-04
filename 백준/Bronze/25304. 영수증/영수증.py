x = int(input())
n = int(input())
sum = 0
for i in range(n):
    a, b = map(int, input().split())
    c = a * b
    sum += c
if x == sum:
    print("Yes")
else:
    print("No")