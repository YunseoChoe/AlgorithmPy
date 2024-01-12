# 곱셈
# 입력받기 (a, b는 세자리 자연수)
a = int(input())
b = input()
num_b = []
for i in range(len(b)):
    num_b.append(b[i])
# 정수화
for i in range(len(num_b)):
    num_b[i] = int(num_b[i])
# 출력하기
print(a * num_b[2])
print(a * num_b[1])
print(a * num_b[0])
print(a * (int(b)))