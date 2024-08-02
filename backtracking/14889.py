# 스타트와 링크
import copy
from itertools import permutations

n = int(input())

s = [] # 2차원 행렬
for i in range(n):
    s.append(list(map(int, input().split())))

# 팀이 될 수 있는 경우의 수 계산하기 (조합)
arr = []
team = []
def func(start):
    if len(arr) == n//2:
        team.append(copy.deepcopy(arr))
        return
    else:
        for i in range(start, n + 1):
            if i not in arr:
                arr.append(i)
                func(i + 1)
                arr.pop()
func(1)

# 능력치 구하기 (a,b 팀)
teams_gaps = [] # 각 순열마다 팀의 능력치의 차이를 담은 배열
for i in range(len(team) // 2):
    # 각 팀이 될 수 있는 순열 선언
    team_a = team[i]
    team_b = team[len(team) - i - 1]

    # 2명씩 팀 배정
    team_a_persons = list(permutations(team_a, 2)) # 2명씩 순열
    team_b_persons = list(permutations(team_b, 2)) # 2명씩 순열

    # 각 팀들의 능력치 합 구하기
    team_a_sum = 0 # team_a의 합
    team_b_sum = 0 # team_b의 합

    for j in range(len(team_a_persons)):
        team_a_sum += s[team_a_persons[j][0] - 1][team_a_persons[j][1] - 1]
        team_b_sum += s[team_b_persons[j][0] - 1][team_b_persons[j][1] - 1]
        
    gap = abs(team_a_sum - team_b_sum) # 두 팀의 능력치 차이
    teams_gaps.append(gap)

print(min(teams_gaps))
