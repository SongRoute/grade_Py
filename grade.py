def get_student_info():
    name = input(f"학생 이름을 입력하세요: ")
    num = input(f"{name}학생의 학번을 입력하세요: ")
    eng = float(input(f"{name}학생의 영어 성적을 입력하세요: "))
    Clang = float(input(f"{name}학생의 C언어 성적을 입력하세요: "))
    Pyth = float(input(f"{name}학생의 파이썬 성적을 입력하세요: "))
    return {'이름': name, '학번': num, '영어': eng, 'C언어': Clang, '파이썬': Pyth}

def calculate_grades(student):
    total_score = student['영어'] + student['C언어'] + student['파이썬']
    average_score = total_score / 3
    if average_score >= 90:
        grade = 'A'
    elif average_score >= 80:
        grade = 'B'
    elif average_score >= 70:
        grade = 'C'
    elif average_score >= 60:
        grade = 'D'
    else:
        grade = 'F'
    student.update({'총점': total_score, '평균': average_score, '학점': grade})
    return student

def print_results(student):
    print(f"이름: {student['이름']}, 학번: {student['학번']}, 총점: {student['총점']}, 평균: {student['평균']}, 학점: {student['학점']}")

def main():
    students = []
    
    for i in range(5):
        students.append(get_student_info())
    
    for student in students:
        calculate_grades(student)
        
    students.sort(key=lambda x: x['평균'], reverse=True)

    print("\n[결과]")
    for student in students:
        print_results(student)

if __name__ == "__main__":
    main()
