# 사분면 고르기
# 입력받기
x = int(input())
y = int(input())
# 출력하기
if x > 0 and y > 0:
    print("1")
elif x > 0 and y < 0:
    print("4")
elif x < 0 and y > 0:
    print("2")
elif x < 0 and y < 0:
    print("3")