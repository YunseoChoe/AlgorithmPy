# 이전 순열
n = int(input())
nums = map(int, input().split())
nums = list(nums)

# target
target = 0
index = 0
is_changed = False
for i in range(len(nums) - 2, -1, -1):
    if nums[i] > nums[i + 1]:
        target = nums[i]
        index = i
        is_changed = True
        break
    else:
        pass

if is_changed:
    # after_nums에서 target보다 바로 작은 수 찾기
    prev_nums = nums[0:i + 1]
    after_nums = nums[i + 1:]

    min_gap = 50000
    min_index = 0
    for i in range(len(after_nums)):
        if target - after_nums[i] >= 0:
            if min_gap > target - after_nums[i]:
                min_gap = target - after_nums[i]
                min_index = i
    min_index += len(prev_nums)

    # swap
    nums[index], nums[min_index] = nums[min_index], nums[index]

    # 내림차순 정렬
    prev_nums = nums[0:index + 1]
    after_nums = nums[index + 1:]
    after_nums.sort(reverse=True)
    nums = prev_nums + after_nums

    # 출력
    for i in range(len(nums)):
        print(nums[i], end = " ")

else:
    print(-1)