x = bin(int(input()))

c = 0
for i in reversed(x):
    if i == '1':
        break
    c += 1

print(c)