# 차이를 최대로
n = int(input())
nums = list(map(int, input().split()))

i_index = [] # 인덱스 배열
arr = []
max = n * (-100) - 1

def func():
    global max
    sum = 0
    if len(arr) == n:

        # 최댓값 계산
        for i in range(n - 1):
            sum += abs(arr[i] - arr[i + 1])

        if max < sum:
            max = sum
    
        return

    for i in range(n):
        if i not in i_index:
            i_index.append(i)
            arr.append(nums[i])
            func()
            arr.pop()
            i_index.pop()

func()
print(max)
