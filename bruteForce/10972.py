# 다음 순열
n = int(input())
nums = map(int, input().split())
nums = list(nums)

is_changed = False
# target 찾기
for i in range(len(nums) - 1, 0, -1):
    if nums[i] > nums[i - 1]:
        max_index = i
        is_changed = True
        break
else:
    pass

if is_changed:
    prev_nums = nums[0:max_index]
    after_nums = nums[max_index:]
    target = nums[max_index - 1]

    # swap할 수 찾기
    min_gap = 10000
    index = 0
    for i in range(len(after_nums)):
        if after_nums[i] - target >= 0:
            if min_gap > after_nums[i] - target:
                min_gap = after_nums[i] - target
                index = i
    index = index + len(prev_nums)
    # swap    
    nums[index], nums[max_index - 1] = nums[max_index - 1], nums[index]

    # 오름차순 정렬
    prev_nums = nums[0: max_index]
    after_nums = nums[max_index:]
    after_nums.sort()

    # 출력
    nums = prev_nums + after_nums
    for i in range(len(nums)):
        print(nums[i], end = " ")

    
else:
    print(-1)