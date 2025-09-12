# 네 번째 점
# x, y 각각 2개씩

a_list = []
b_list = []
for i in range(3):    
    a, b = map(int, input().split())
    a_list.append(a)
    b_list.append(b)

# 각 리스트에서 요소가 1개인 것 찾기
# ex. a_list = [5, 5, 7]이면 7을 찾으면 됨

# a
# 0번째
if a_list[1] == a_list[2] and a_list[0] != a_list[1]:
    x = a_list[0]
# 1번째
elif a_list[0] == a_list[2] and a_list[1] != a_list[0]:
    x = a_list[1]
# 2번째
elif a_list[0] == a_list[1] and a_list[2] != a_list[0]:
    x = a_list[2]

# b
# 0번째
if b_list[1] == b_list[2] and b_list[0] != b_list[1]:
    y = b_list[0]
# 1번째
elif b_list[0] == b_list[2] and b_list[1] != b_list[0]:
    y = b_list[1]
# 2번째
elif b_list[0] == b_list[1] and b_list[2] != b_list[0]:
    y = b_list[2]

print(x, y)