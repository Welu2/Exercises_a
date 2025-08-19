# Problem: Nested Lists - https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

if __name__ == '__main__':
    n = int(input())
    students = []
    for _ in range(n):
        name = input()
        score = float(input())
        students.append([name, score])
    
    students.sort(key=lambda x: x[1]) 
    second_lowest_score = None
    lowest_score = students[0][1]
    for i in range(1, n):
        if students[i][1] > lowest_score:
            second_lowest_score = students[i][1]
            break
    
    second_lowest_students = []
    for student in students:
        if student[1] == second_lowest_score:
            second_lowest_students.append(student[0])
    
    second_lowest_students.sort()
    for name in second_lowest_students:
        print(name)
