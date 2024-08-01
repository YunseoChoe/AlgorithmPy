# 부등호
import copy

def check(a, b, sign):
    if sign == '<':
        return a < b
    else:
        return a > b

k = int(input())
sign = input().split() # 부등호 입력

arr = []
min_arr = [9] * (k + 1)
max_arr = [-1] * (k + 1)

# 순열 구하기
def func():

    # 부등호를 만족하는 arr 완성
    if len(arr) == (k + 1):
        # 최댓값, 최솟값 구하기
        global max_arr, min_arr
        if min_arr > arr:
            min_arr = copy.deepcopy(arr)
        if max_arr < arr:
            max_arr = copy.deepcopy(arr)
    else:
        for i in range(0, 10):
            if i not in arr: 

                # 부등호 조건 비교
                j = len(arr) - 1 
                if len(arr) == 0 or check(arr[j], i, sign[j]): 
                    arr.append(i)
                    func()
                    arr.pop()
                   
func()

# 출력
for i in range(len(max_arr)):
    print(max_arr[i], end = "")
print()
for i in range(len(min_arr)):
    print(min_arr[i], end = "")
