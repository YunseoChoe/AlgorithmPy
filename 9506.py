# 약수들의 합
while True:
    n = int(input()) # n = -1이면 멈춤      
    if n == -1:
        exit()
    else:
        # n의 약수 구하기
        divisor = []
        for i in range(1, n + 1):
            if n % i == 0:
                divisor.append(i)
        # 완전수인지 체크
        sum = 0
        for i in range(len(divisor) - 1):
            sum += divisor[i]
        # print(f'sum:{sum}')
        if sum == n: 
            print(f'{n} = ', end = "")
            for i in range(len(divisor) - 1):
                if i == len(divisor) - 2:
                    print(f'{divisor[i]}')
                else:
                    print(f'{divisor[i]} +', end = " ")
        else:
            print(f'{n} is NOT perfect.')
# n = 6
# list = [1, 2, 3]
# result = str(n) + " = " + " + ".join(map(str, list))
# print(result)
