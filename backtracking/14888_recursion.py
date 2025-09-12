# 14888 (재귀 방법)

max_value = -10000000000
min_value = 10000000000

n = int(input())
num = list(map(int, input().split()))
add, sub, mul, div = list(map(int, input().split()))

# idx: 내가 지금 계산하려고 하는 숫자를 가리키는 인덱스
def func(idx, result):
    global max_value, min_value, add, sub, mul, div, n
    
    if idx == n - 1:
        max_value = max(max_value, result)
        min_value = min(min_value, result)
        return
    
    if add > 0:
        add -= 1
        func(idx + 1, result + num[idx + 1])
        add += 1
    if sub > 0:
        sub -= 1
        func(idx + 1, result - num[idx + 1])
        sub += 1
    if mul > 0:
        mul -= 1
        func(idx + 1, result * num[idx + 1])
        mul += 1
    if div > 0:
        div -= 1
        func(idx + 1, int(result / num[idx + 1]))
        div += 1

func(0, num[0])
print(max_value)
print(min_value)
