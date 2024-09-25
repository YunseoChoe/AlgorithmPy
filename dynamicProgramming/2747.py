# 피보나치 수
n = int(input())

fibo = []
fibo.append(0)
fibo.append(1)

sum = 1
now = 2

while now != (n + 1):
    now_1 = fibo[now - 1]
    now_2 = fibo[now - 2]

    sum = now_1 + now_2
    
    fibo.append(sum)
    now += 1

print(fibo[n])
