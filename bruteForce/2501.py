# 약수 구하기
n, k = map(int, input().split())

divisor = [] # 약수 리스트
# n의 약수 구하기
for i in range(1, n + 1):
    if n % i == 0:
        divisor.append(i)

# k번 째로 작은 수 구하기
# k가 약수의 개수보다 작으면 
if k <= len(divisor):
    print(divisor[k - 1])
else:
    print(0)