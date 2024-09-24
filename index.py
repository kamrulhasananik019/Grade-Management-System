from random import choice

student_grades = {}


def add_student(name, grade):
    student_grades[name] = grade
    print(f'added {name} with a {grade}')


def update_student(name, grade):
    if name in student_grades:
        student_grades[name]=grade
        print(f'{name} with marks are update {grade}')
    else:
        print(f'{name} is not found!')


def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f'{name} has been deleted successfully')
    else:
        print(f'{name} is not found!')


def display_all_student():
    if student_grades:
        for name, grade in student_grades.items():
            print(f'{name} : {grade}')

    else:
        print('no student found!')


def main():
    while True:
        print('1. Add student')
        print('2. Update student')
        print('3. Delete student')
        print('4. view student')
        print('5. Exit')

        choice = int(input('enter your choice:'))
        if choice == 1:
            name = input("enter student name:")
            grade = int(input('Enter student Grade:'))
            add_student(name, grade)

        elif choice == 2:
            name = input("enter student name:")
            grade = int(input('Enter student Grade:'))
            update_student(name, grade)

        elif choice == 3:
            name = input("enter student name:")
            delete_student(name)

        elif choice == 4:
            display_all_student()

        elif choice == 5:
            print('closing the  program')
            break

        else:
            print('invalid choice')


main()


