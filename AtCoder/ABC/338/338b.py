s = input()
freq = {}

for c in s:
    freq[c] = freq.get(c, 0)+1
max = max(freq.values())

ans = 'z'
for c in freq:
    if freq[c] == max:
        ans = min(ans, c)

print(ans)