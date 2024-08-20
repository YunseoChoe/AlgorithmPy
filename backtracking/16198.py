# 에너지 모으기
n = int(input())
w = list(map(int, input().split(' ')))
max_e = 0

def func(e):
    global max_e 
    if len(w) == 2:
        max_e = max(max_e, e)
        return
    
    for i in range(1, n - 1):
        if i < len(w) - 1:    
            x = w.pop(i)
            func(e + w[i - 1] * w[i])
            w.insert(i, x)

func(0)
print(max_e)
