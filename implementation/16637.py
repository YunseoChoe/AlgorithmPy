# 괄호 추가하기
# 연산하는 함수
def cal(a, operator, b):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    else:
        return a * b
    
def dfs(idx, value):
    global max_value
    # idx 범위 확인
    if idx >= len(formula):
        return
    
    # 괄호가 없다면
    result = cal(value, formula[idx], formula[idx + 1])
    # 마지막 연산자가 아니라면
    if idx < len(formula) - 2:
        dfs(idx + 2, result)
    # 마지막 연산자라면
    else:
        # 최댓값 갱신
        max_value = max(max_value, result)
        return max_value

    # 괄호가 있다면
    bracket_reulst = cal(formula[idx + 1], formula[idx + 2], formula[idx + 3]) # 첫번째 연산의 괄호는 의미 없음. 
    result = cal(value, formula[idx], bracket_reulst) # value는 이전 수까지의 연산 결과
    # 마지막 연산자가 아니라면
    if idx + 4 < len(formula):
        dfs(idx + 4, result)
    # 마지막 연산자라면
    else:
        # 최댓값 갱신
        max_value = max(max_value, result)
        return max_value

if __name__ == '__main__':
    # 입력
    n = int(input())
    input_str = input()
    formula = []
    max_value = 0 # 최댓값 초기화

    # 정수화
    for i in range(len(input_str)):
        if input_str[i] != '+' and input_str[i] != '-' and input_str[i] != '*':
            formula.append(int(input_str[i]))
        else:
            formula.append(input_str[i])
    
    dfs(1, formula[0]) # 인덱스는 1부터
    print(max_value)
