# 그대로 출력하기
while True:
    try:
        s = input()
        if s[0] == " " or s[-1] == " ":
            break
        else:
            print(s)
    # 예외 (더 이상 읽을 내용이 없을 때)
    except EOFError:
        break