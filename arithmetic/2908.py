# # 상수
# # 입력
num = input().split()

# 수 뒤집기 (문자열은 reverse()라는 함수가 존재하지 않음. 따라서 리스트 형태로 바꾸고 사용해야 함)
a = list(num[0])
b = list(num[-1])

# 문자열 list -> 정수형 list
# for i in range(len(a)):
#     a[i] = int(a[i])
# for i in range(len(b)):
#     b[i] = int(b[i])

# 수 뒤집기
a.reverse()
b.reverse()

# list -> 문자열
str_a = ''.join(a)
str_b = ''.join(b)

# 문자열 -> 정수
str_a = int(str_a)
str_b = int(str_b)

# 비교 후 출력
if str_a > str_b:
    print(str_a)
elif str_a < str_b:
    print(str_b)
else:
    pass