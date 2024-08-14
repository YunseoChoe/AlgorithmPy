# 암호 만들기
# 순열 말고 조합, 왜냐하면 어차피 정렬하면 같은 값이기 때문, 재귀 조정 맘대로 해도 됨?
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
def func():
    if len(arr) == l:
        # 조건 비교
        if check(arr):
            # 출력
            for i in range(len(arr)):
                print(arr[i], end = "")
            print()
            return
        
    for i in range(len(chrs)):
        # arr가 비어있을 경우
        if len(arr) == 0:
            arr.append(chrs[i])
            func()
            arr.pop()

        # arr가 안 비어있을 경우
        else:
            if arr[-1] < chrs[i]: # 정렬
                arr.append(chrs[i])
                func()
                arr.pop()

func()
