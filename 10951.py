# A+B-4
sums = []
# 두 정수 입력 받기
for i in range(5):
    a, b = input().split()
    a = int(a)
    b = int(b)
    # 계산하기
    sum = a + b
    sums.append(sum)
    
# 출력하기
for i in range(len(sums)):
    print(sums[i])