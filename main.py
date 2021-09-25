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
        if other in Student:
            return self.average_grade > other.average_grade
        else:
            return 'Ошибка'

    def __lt__(self, other):
        if other in Student:
            return self.average_grade < other.average_grade
        else:
            return 'Ошибка'

    def __ge__(self, other):
        if other in Student:
            return self.average_grade >= other.average_grade
        else:
            return 'Ошибка'

    def __le__(self, other):
        if other in Student:
            return self.average_grade <= other.average_grade
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    # def rate_hw(self, student, course, grade):
    #     if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
    #         if course in student.grades:
    #             student.grades[course] += [grade]
    #         else:
    #             student.grades[course] = [grade]
    #     else:
    #         return 'Ошибка'


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def average_grade(self, grades):
        amount = 0
        for grade in self.grades.values():
            amount += sum(grade)
        return amount / len(self.grades)

    def __str__(self):
        return f' Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка: {self.average_grade():.1f}'


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


# Students
paul = Student('Paul', 'Atreides', 'male')
paul.courses_in_progress += ['Python']
paul.finished_courses += ['English']

liu = Student('Liu', 'Kang', 'male')
liu.courses_in_progress += ['English']
liu.finished_courses += ['Kung-Fu']

# Lecturer
obi_wan = Lecturer('Obi-Wan', 'Obi-Wan')
obi_wan.courses_attached += ['Python']

hannibal = Lecturer('Hannibal', 'Lecter')
obi_wan.courses_attached += ['English']

# Reviewer
minerva = Reviewer('Minerva', 'McGonagall')

altiera = Reviewer('Altiera', 'Cunningham')


# Test
minerva.rate_student(paul, 'Python', 9)
altiera.rate_student(paul, 'Python', 6)
minerva.rate_student(paul, 'Python', 10)

altiera.rate_student(liu, 'English', 7)
minerva.rate_student(liu, 'English', 10)
altiera.rate_student(liu, 'Python', 9)

paul.rate_lecturer()



# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['Python']
#
# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
#
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)

# print(best_student.grades)
