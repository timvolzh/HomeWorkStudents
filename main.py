class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def average_grade(self):
        amount = 0
        amount_len = 0
        for grades in self.grades.values():
            amount += sum(grades)
            amount_len += len(grades)
        return amount / amount_len

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and (
                course in self.courses_in_progress or course in self.finished_courses):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f' Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка: {self.average_grade():.1f}'

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.average_grade() > other.average_grade()
        else:
            return 'Ошибка'

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average_grade < other.average_grade
        else:
            return 'Ошибка'

    def __ge__(self, other):
        if isinstance(other, Student):
            return self.average_grade >= other.average_grade
        else:
            return 'Ошибка'

    def __le__(self, other):
        if isinstance(other, Student):
            return self.average_grade <= other.average_grade
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def average_grade(self):
        amount = 0
        amount_len = 0
        for grades in self.grades.values():
            amount += sum(grades)
            amount_len += len(grades)
        return amount / amount_len

    def __str__(self):
        return f' Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка: {self.average_grade():.1f}'

    def __gt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() > other.average_grade()
        else:
            return 'Ошибка'

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade < other.average_grade
        else:
            return 'Ошибка'

    def __ge__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade >= other.average_grade
        else:
            return 'Ошибка'

    def __le__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade <= other.average_grade
        else:
            return 'Ошибка'


class Reviewer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_student(self, student, course, grade):
        if isinstance(student, Student) and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f' Имя: {self.name}\n Фамилия: {self.surname}'


def av_gr_st(students, course):
    av_gr = 0
    gr_sum = 0
    for student in students:
        for course_in_progress, grade in student.grades.items():
            if course_in_progress == course:
                av_gr += sum(student.grades[course])
                gr_sum += len(student.grades[course])
    return f'Средний бал студентов по курсу {course}: {av_gr/gr_sum:.1f}'


def av_gr_lec(lecturers, course):
    av_gr = 0
    gr_sum = 0
    for lecturer in lecturers:
        for course_in_progress, grade in lecturer.grades.items():
            if course_in_progress == course:
                av_gr += sum(lecturer.grades[course])
                gr_sum += len(lecturer.grades[course])
    return f'Средний бал лекторов по курсу {course}: {av_gr/gr_sum:.1f}'


# Students
paul = Student('Paul', 'Atreides', 'male')
paul.courses_in_progress += ['Python', 'Make-Up']
paul.finished_courses += ['English']

liu = Student('Liu', 'Kang', 'male')
liu.courses_in_progress += ['English', 'Make-Up']
liu.finished_courses += ['Kung-Fu']

# Lecturer
obi_wan = Lecturer('Obi', 'Wan')
obi_wan.courses_attached += ['Python', 'Make-Up']

hannibal = Lecturer('Hannibal', 'Lecter')
hannibal.courses_attached += ['English', 'Make-Up']

# Reviewer
minerva = Reviewer('Minerva', 'McGonagall')

altiera = Reviewer('Altiera', 'Cunningham')


# Methods test
minerva.rate_student(paul, 'Python', 9)
altiera.rate_student(paul, 'Python', 6)
minerva.rate_student(paul, 'Python', 10)

minerva.rate_student(paul, 'Make-Up', 9)
altiera.rate_student(paul, 'Make-Up', 6)
minerva.rate_student(paul, 'Make-Up', 10)

minerva.rate_student(liu, 'Make-Up', 9)
altiera.rate_student(liu, 'Make-Up', 6)
minerva.rate_student(liu, 'Make-Up', 10)

altiera.rate_student(liu, 'English', 7)
minerva.rate_student(liu, 'English', 10)
altiera.rate_student(liu, 'Python', 9)

paul.rate_lecturer(obi_wan, 'Python', 9)
paul.rate_lecturer(obi_wan, 'Python', 7)
liu.rate_lecturer(obi_wan, 'Python', 7)

liu.rate_lecturer(hannibal, 'English', 2)
paul.rate_lecturer(hannibal, 'English', 6)
liu.rate_lecturer(hannibal, 'English', 7)

liu.rate_lecturer(hannibal, 'Make-Up', 8)
paul.rate_lecturer(hannibal, 'Make-Up', 6)
liu.rate_lecturer(hannibal, 'Make-Up', 7)

paul.rate_lecturer(obi_wan, 'Make-Up', 9)
paul.rate_lecturer(obi_wan, 'Make-Up', 3)
liu.rate_lecturer(obi_wan, 'Make-Up', 7)

paul.rate_lecturer(obi_wan, 'Make-Up', 9)
paul.rate_lecturer(obi_wan, 'Make-Up', 7)
liu.rate_lecturer(obi_wan, 'Make-Up', 7)

liu.rate_lecturer(hannibal, 'Make-Up', 2)
paul.rate_lecturer(hannibal, 'Make-Up', 6)
liu.rate_lecturer(hannibal, 'Make-Up', 7)


# Testing
student_list = [paul, liu]
lecturer_list = [obi_wan, hannibal]

print(av_gr_st(student_list, 'Make-Up'))
print(av_gr_lec(lecturer_list, 'Make-Up'))
