m, n, h = map(int, input().split())

mat = []
for i in range(h):
    mat_list = []
    for j in range(n):
        mats = list(map(int, input().split()))
        mat_list.append(mats)
    mat.append(mat_list)

print(mat)




