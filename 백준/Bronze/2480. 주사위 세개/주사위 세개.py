d1, d2, d3= map(int, input().split())
answer = 0
if d1 == d2 == d3:
    answer = 10000 + d1*1000
elif d1 == d2 or d1 == d3:
    answer = d1 * 100 + 1000
elif d2 == d3:
    answer = d2 * 100 + 1000
else:
    answer = max(d1, d2, d3) * 100
print(answer)