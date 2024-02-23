# 소트인사이드
n = input() # 문자열 입력

num = []
for i in range(len(n)):
    num.append(n[i])

# 문자 -> 정수
for i in range(len(num)):
    num[i] = int(num[i])

# 오름차순 정렬
num.sort()
# reverse
num.reverse()

# 출력
for i in range(len(num)):
    print(num[i], end = "")