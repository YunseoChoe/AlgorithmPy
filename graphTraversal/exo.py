import copy

exo = ["카이", "백현", "수호", "세훈", "디오", "찬열", "타오", "크리스", "첸", "레이", "루한", "시우민"]

arr = []
all_arr = []
UNIT_SIZE = 6
def func(next):
    if len(arr) == UNIT_SIZE:
        all_arr.append(copy.deepcopy(arr))
        return
    for i in range(next, len(exo)):
        if i not in arr:
            arr.append(i)
            func(i + 1)
            arr.pop()

func(0)
print(all_arr)


for i in range(len(all_arr)):
    for j in range(UNIT_SIZE):
        all_arr[i][j] = exo[all_arr[i][j]]

print(all_arr)