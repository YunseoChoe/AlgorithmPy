# 별 찍기 - 7
n = int(input())
for i in range(n):
    for j in range(n - 1, i, -1):
        print(" ", end = "")
    for k in range((i * 2) + 1):
        print("*", end = "")
    print()

for i in range(n - 2, -1, -1):
    for j in range((n - 1) - i):
        print(" ", end = "")
    for k in range((2 * i) + 1):
        print("*", end = "")
    print()


# for i in range(3):
#     # " "
#     for j in range(3 - 1, i, -1):
#         print(" ", end = "")
#     # "*"
#     for k in range(i * 2 + 1):
#         print("*", end = "")
#     print()   

# for i in range(3 - 2, -1, -1):
#     # " "
#     for k in range((3 - 1) - i):
#         print(" ", end = "")
#     # "*"
#     for j in range(2 * i + 1):
#         print("*", end = "")
#     print()