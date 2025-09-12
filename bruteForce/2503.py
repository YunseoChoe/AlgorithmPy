# 숫자 야구
from itertools import permutations

data = list(range(1, 10)) 
nums = list(permutations(data, 3))

n = int(input())
for _ in range(n):
    answer, strike, ball = list(map(int, input().split())) # 123 1 1
    for i in range(len(nums)): # [[1, 2, 3], [1, 2, 4], [1, 2, 5], ≥..]
        s_count = 0
        b_count = 0
        # nums[i] = [1, 2, 3]
        # answer = 123
        for j in range(3):
            answer = str(answer)
            if str(nums[j]) == answer[j]: # answer = "123", answer[0], answer[1], answer[2]
                s_count += 1
            elif str(nums[j]) in answer:
                b_count += 1

    
                
        