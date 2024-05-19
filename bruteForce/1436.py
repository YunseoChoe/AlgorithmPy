# 영화감독 숌
# 666부터 시작해서 +1씩 증가해주고, 만약 조건에 맞으면 (6이 3개 있으면) 그 값을 반환
n = int(input())

count = 1
number = 666

while 1:
    if n == count:
        print(number)
        break
    else:
        number += 1
        s = str(number)
        if '666' in s:
            count += 1