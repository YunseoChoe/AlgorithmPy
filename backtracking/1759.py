# 암호 만들기
import copy

l, c = list(map(int, input().split()))
chrs = list(input().split(' '))
# 정렬 되어있는지 and 최소 한 개의 모음 & 최소 두 개의 자음인지
def check(arr):
    vowel = ['a', 'e', 'i', 'o', 'u'] # 모음
    consonant = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z'] # 자음
    is_in_vowel = False 
    is_in_consonant = False
    is_consonant = 0
    
    for i in range(len(arr)):
        if arr[i] in vowel:
            is_in_vowel = True
        if arr[i] in consonant:
            is_consonant += 1
        if is_consonant >= 2:
            is_in_consonant = True
    
    if is_in_consonant and is_in_vowel:
        return True
    else:
        return False

arr = []
all_arr = []
def func(start):
    global all_arr
    if len(arr) == l:
        # 조건 비교
        if check(arr):
            # 배열 저장
            all_arr.append(copy.deepcopy(arr))
            return
        
    for i in range(start, len(chrs)):
        arr.append(chrs[i])
        func(i + 1)
        arr.pop()

chrs.sort() # 미리 정렬
func(0)

# 출력
all_arr.sort() # 사전순 정렬
for i in range(len(all_arr)):
    for j in range(len(all_arr[i])):
        print(all_arr[i][j], end = "")
    print()
