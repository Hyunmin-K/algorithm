h, m = map(int, input().split())
a_h, a_m = h, m-45
if a_m < 0:
    a_h = a_h - 1
    a_m = a_m + 60
if a_h < 0:
    a_h = a_h + 24
print(a_h, a_m)