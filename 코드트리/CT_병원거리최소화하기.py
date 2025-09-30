def get_distance(selected_hospitals, people):
    """
    people의 사람들과 selected_hospitals의 병원들 사이의 최소 거리 합을 반환
    """
    total_distance = 0
    for px, py in people:
        person_min = float('inf')
        for hx, hy in selected_hospitals:
            dist = abs(hx - px) + abs(hy - py) # 맨해튼 거리
            person_min = min(person_min, dist)
        total_distance += person_min
    return total_distance

def backtrack(hospitals, selected_hospitals, people, idx, m, board):
    global ans # ans 값을 수정하기 때문에, main이 아닌 함수에서도 global을 붙어야 함.
    if len(selected_hospitals) == m:
        # 최소 거리 갱신
        ans = min(ans, get_distance(selected_hospitals, people))
        return
    
    for i in range(idx, len(hospitals)):
        selected_hospitals.append(hospitals[i])
        backtrack(hospitals, selected_hospitals, people, i + 1, m, board)
        selected_hospitals.pop()

def choose_hospital(n, m, board):
    hospitals = []
    people = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 2:
                hospitals.append((i, j))
            if board[i][j] == 1:
                people.append((i, j)) # 사람 정보
    backtrack(hospitals, [], people, 0, m, board)
    
def main():
    global ans # 전역 변수
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    ans = 9900 # 사람 최대 수(100) * 최대 맨허튼 거리(99)

    choose_hospital(n, m, board)
    print(ans)

if __name__ == "__main__":
    main()
