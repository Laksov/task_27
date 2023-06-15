'''
    Реализация классического бинарного поиска
'''

li = sorted(list(map(int, input().split())))
x = int(input())
l = 0
r = len(li) - 1

while l < r:
    m = (l + r) // 2
    if li[m] == x:
        print(m)
        break

    elif li[m] < x:
        l = m + 1
    else:
        r = m - 1

if li[r] == x:
    print(r)
else:
    print(-1)
