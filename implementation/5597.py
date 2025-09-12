# 과제 안 내신 분..?
# 학생 명단
students = []
for i in range(1, 31):
    students.append(i)

# 입력받기
for i in range(28):
    student = int(input())
    if student in students:
        students[student - 1] = -1
    
# 출력하기
for i in range(len(students)):
    if students[i] != -1:
        print(students[i])