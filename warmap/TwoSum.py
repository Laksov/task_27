'https://leetcode.com/problems/two-sum/'
nums = list(map(int, input().split()))
tar = int(input())
lis = []
flag = False

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == tar:
            lis.append(i)
            lis.append(j)
            print(lis)
            flag = True
            break
    if flag:
        break
