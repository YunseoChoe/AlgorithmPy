# 부분수열의 합
n, s = list(map(int, input().split(' ')))
nums = list(map(int, input().split(' ')))

arr = []
cnt = 0
def func(start):
    global arr, cnt
    if len(arr) > 0 and sum(arr) == s:
        cnt += 1 
    for i in range(start, n):
        arr.append(nums[i])
        func(i + 1)
        arr.pop()

func(0)
print(cnt)
