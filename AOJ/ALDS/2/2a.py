def bubbleSort(a, n, cnt):
    flag = True
    while flag:
        flag = False
        for i in range(n-1, 0, -1):
            if a[i] < a[i-1]:
                a[i], a[i-1] = a[i-1], a[i]
                flag = True
                cnt += 1
    return cnt

n = int(input())
a = list(map(int, input().split()))

cnt = bubbleSort(a, n, 0)

print(' '.join(map(str, a)))
print(cnt)
