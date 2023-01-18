s = input()
line1 = []
line2 = []
for i in range(len(s)):
    line1.append(s[i])
    line2.append(s[-i-1])
if line1 == line2:
    print(1)
else:
    print(0)