# 일곱 난쟁이
height = []
for i in range(9):
    num = int(input())
    height.append(num)

sum = 0
for i in range(len(height)):
    sum += height[i]

for i in range(8):
    for j in range(i + 1, 9):
        if sum - (height[i] + height[j]) == 100:
            remove_1 = height[i]
            remove_2 = height[j]
height.remove(remove_1)
height.remove(remove_2)

height.sort()

for i in range(len(height)):
    print(height[i])