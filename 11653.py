# 소인수분해
# n의 소인수분해 결과를 오름차순으로 출력
n = int(input())

# n이 1일 때
if n == 1:
    exit()

# 약수 구하기
divisor = []
for i in range(2, n + 1): # 1제외
    if n % i == 0:
        divisor.append(i)

print(divisor)
# 나누기
i = 0
while n != 1:
    if n % divisor[i] == 0:
        print(f'n:{n}')
        print(f'divisor[i]:{divisor[i]}')
        n = n // divisor[i]  
        if n % divisor[i] != 0:
            i += 1

