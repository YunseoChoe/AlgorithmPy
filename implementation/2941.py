# 크로아티아 알파벳
# 위 목록에 없는 알파벳은 한 글자씩 센다.
'''
č	c=
ć	c-
dž	dz=
đ	d-
lj	lj
nj	nj
š	s=
ž	z=
'''

s = input() 
cnt = 0
i = 0
while i < len(s): 
    if s[i] == 'c' and i < len(s) - 1 and s[i + 1] == '=':
        # print("c=")
        cnt += 1
        i += 2
    elif s[i] == 'c' and i < len(s) - 1 and s[i + 1] == '-':
        # print("c-")
        cnt += 1
        i += 2
    elif s[i] == 'd' and i < len(s) - 2 and s[i + 1] == 'z' and s[i + 2] == '=':
        # print("dz=")
        cnt += 1
        i += 3
    elif s[i] == 'd' and i < len(s) - 1 and s[i + 1] == '-':
        # print("d-")
        cnt += 1
        i += 2
    elif s[i] == 'l' and i < len(s) - 1 and s[i + 1] == 'j':
        # print("lj")
        cnt += 1
        i += 2
    elif s[i] == 'n' and i < len(s) - 1 and s[i + 1] == 'j':
        # print("nj")
        cnt += 1
        i += 2
    elif s[i] == 's' and i < len(s) - 1 and s[i + 1] == '=':
        # print("s=")
        cnt += 1
        i += 2
    elif s[i] == 'z' and i < len(s) - 1 and s[i + 1] == '=':
        # print("z=")
        cnt += 1
        i += 2
    # 다른 알파벳 (a ~ z)
    elif ord(s[i]) <= ord('z') and ord(s[i]) >= ord('a'):
        cnt += 1
        i += 1
    else:
        cnt += 0
        i += 1

print(cnt)