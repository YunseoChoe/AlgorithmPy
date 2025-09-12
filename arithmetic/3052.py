# 나머지
# set함수 사용

# 입력받기
namuji = []
for i in range(10):
    num = int(input())
    namuji.append(num % 42)

# set으로 변경
namuji = set(namuji)
# 출력하기
print(len(namuji))