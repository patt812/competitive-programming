s = input()

if not 65 <= ord(s[0]) <= 90:
    print('No')
    exit()

for c in s[1:]:
    if not 97 <= ord(c) <= 122:
        print('No')
        exit()

print('Yes')