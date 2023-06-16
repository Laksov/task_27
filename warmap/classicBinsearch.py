'''
    Реализация классического бинарного поиска
'''


def classic_binsearch(li, x):
    l = 0
    r = len(li) - 1

    while l <= r:
        m = (l + r) // 2
        if li[m] == x:
            return m

        elif li[m] < x:
            l = m + 1
        else:
            r = m - 1
    else:
        return -1


li = [1, 2, 4, 5]
ans = classic_binsearch(li, 3)
print(ans)

'''
LowerBound поиск нижней ля заданного числа в отсортированном массиве. 
Если такой нет, то выводим 2**100
'''


def lower_bound(li, el):
    l = 0
    r = len(li)

    if el < li[0]:
        return 2 ** 100

    while l + 1 < r:
        m = (l + r) // 2
        if li[m] < el:
            l = m
        else:
            r = m

    return li[l]


li = [1, 2, 4, 5, 6]
print("Lower bound")
print(lower_bound(li, 0))
print(lower_bound(li, 2))
print(lower_bound(li, 3))

'''
UpperBound поиск верхней для заданного числа в отсортированном массиве. 
Если такой нет, то выводим -2**100
'''


def upper_bound(li, el):
    l = -1
    r = len(li) - 1
    if li[-1] < el:
        return -2 ** 100

    while l + 1 < r:
        m = (l + r) // 2
        if li[m] < el:
            l = m
        else:
            r = m

    return li[r]


li = [1, 2, 3, 4, 5, 6, 10, 12]
print("Upper bound")
print(upper_bound(li, 5))
print(upper_bound(li, 7))
print(upper_bound(li, 13))
print(upper_bound(li, 0))