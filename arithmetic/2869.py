# 달팽이는 올라가고 싶다

# solution 1. -> 시간 초과
# 입력받기
# a, b, v = input().split()
# a = int(a) # 낮
# b = int(b) # 밤
# v = int(v) # 도달 목표 높이

# height = 0
# day = 0

# while height < v:
#     if height + a >= v:
#         height += a
#         day += 1
#         break
#     else:
#         height += (a + (-b))
#         day += 1

# print(day)

# solution2
a, b, v = map(int, input().split())
days = (v - a) // (a + (-b)) + 1

# 나머지가 없는 경우
if (v - a) % (a + (-b)) == 0:
    print(days)
# 나머지가 있는 경우
else:
    print(days + 1)