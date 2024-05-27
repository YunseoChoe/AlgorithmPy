# 체스판 다시 칠하기

# 입력받기
n, m = map(int, input().split()) # 8 <= n, m <= 50
all_list = []
for i in range(n): # 행 
    s = input()
    all_list.append(s)

cnt = []
for i in range(n - 7):
    for j in range(m - 7):
        # 8 * 8
        w_cnt = 0
        b_cnt = 0
        for a in range(i, i + 8):
            for b in range(j, j + 8):
                if (a + b) % 2 == 0: # 짝수
                    if all_list[a][b] == 'B': 
                        w_cnt += 1 # 첫 번째가 'W' 이길 기대
                    else: 
                        b_cnt += 1 # 첫 번째가 'B' 이길 기대
                else: # 홀수
                    if all_list[a][b] == 'W': 
                        w_cnt += 1 # 첫 번째가 'W' 이길 기대
                    else:
                        b_cnt += 1 # 첫 번째가 'B' 이길 기대
        cnt.append(min(w_cnt, b_cnt))
print(min(cnt))