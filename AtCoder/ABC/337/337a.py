t = a = 0

for _ in range(int(input())):
    x, y = map(int, input().split())
    t += x
    a += y

if t == a:
    print('Draw')
elif t > a:
    print('Takahashi')
else:
    print('Aoki')