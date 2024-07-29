# 부등호
k = int(input())
sign = input().split() # 부등호 입력

arr = []
all_arr = [] # 부등호를 만족하는 순열을 저장하는 배열
def func():
    if len(arr) == (k + 1):
        # print(arr)
        # arr가 완성되면
        for i in range(len(sign)):
            if sign[i] == '<' and arr[i] < arr[i + 1]:
                pass
            elif sign[i] == '>' and arr[i] > arr[i + 1]:
                pass
            else:
                return
        all_arr.append(arr)
            
    else:
        for i in range(0, 10):
            if i not in arr:
                arr.append(i)
                func()
                arr.pop()

func()
print(all_arr)
