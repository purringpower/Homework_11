students = {
    'Vasya': {
        'math': [4, 4, 4],
        'biology': [3, 5, 4],
        'music': [5, 5, 5]
    },
    'Masha': {
        'math': [3, 4, 4],
        'biology': [3, 5, 4],
        'music': [5, 3, 4]
    }
}

student_name, subject, mark = input("Enter student's name, subject and type of mark:").split(' ')
subject = subject.lower()


class NoSuchStudent(Exception):
    pass


class NoSuchSubject(Exception):
    pass


class NoSuchMark(Exception):
    pass


if student_name not in students:
    raise NoSuchStudent("There is no such a student in the class!")
if subject not in students[student_name]:
    raise NoSuchSubject("There is no such a subject for this student!")
if mark.isalpha() is True or int(mark) > 3 or int(mark) <= 0:
    raise NoSuchMark("There is no such a mark for this subject!")
else:
    mark = int(mark) - 1


try:
    print(students[student_name][subject][mark])
except ValueError:
    print('Your data is incorrect. Check your input!')
