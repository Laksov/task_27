'https://leetcode.com/problems/min-max-game/'
li = list(map(int, input().split()))
flag = True  # чётная пара
index = 0
res = 0
d = len(li)

if d == 1:
    print(li[0])
    exit()

while d != 2:
    for i in range(1, d, 2):
        if flag:
            res = min(li[i - 1], li[i])
            flag = False
        else:
            res = max(li[i - 1], li[i])
            flag = True
        li[index] = res
        index += 1
    index = 0
    d = d // 2
    print(li[:d])
print(min(li[0], li[1]))

