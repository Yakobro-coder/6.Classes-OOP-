student_list = []

class Student:
    def __init__(self, name, surname,gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progerss = []
        self.grades = {}

    def add_finished_courses(self, courses):
        self.finished_courses.append(courses)

    # Если лектор ведёт два и более предмета, сделал что бы каждый предмет был отдельно оценён учениками.
    # p.s. сделав это в самом начале работы над первой задачей, в дальнейшем я понял на сколько же я себе усложнил
    # решение дальнейших задач:)))) Но сдаваться я уже не хотел:) Это было весело :D
    def rate_lector(self, lector, courses, grage):
        if isinstance(lector, Lecturer) \
                and courses in lector.courses_attached \
                and courses in self.courses_in_progerss:
            for dict_courses_grade in lector.grades:
                if courses in dict_courses_grade:
                    for key,val in dict_courses_grade.items():
                        if key == courses:
                            val.append(grage)
                elif courses not in dict_courses_grade:
                    dict_courses_grade[courses] = [grage]
        else:
            print('Error in entering the grade for the lecturer.')

    def __str__(self):
        if isinstance(self, Student):
            result = f'Имя: {self.name}\n' \
                     f'Фамилия: {self.surname}\n'
            # Т.к. у студента несколько предметов на изучении, выводит среднюю оценку за ДЗ по всем что есть.
            for key, val in self.grades.items():
                result += f'Средняя оценка за домашнее задание: {key} - {round(sum(val) / len(val), 2)}\n'
            result += f'Курсы в процессе изучения: {", ".join(self.courses_in_progerss)}\n' \
                      f'Завершенные курсы: {", ".join(self.finished_courses)}\n'
            return result

    def __lt__(self, other):
        if isinstance(other, Student):
            for key1, val1 in self.grades.items():
                result = ''
                for key2, val2 in other.grades.items():
                    if key1 == key2:
                        result += f'{key1}: {(sum(val1) / len(val1)) < (sum(val2) / len(val2))}\n'
            if result == '':
                return 'Студенты изучают разные предметы, сравнение невозможно.'
            else:
                return result
        else:
            print('Указаны объекты разных классов.')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        if isinstance(self, Reviewer):
            result = f'Имя: {self.name}\n' \
                     f'Фамилия: {self.surname}\n'
            return result
        elif isinstance(self, Lecturer):
            result = ''
            result += f'Имя: {self.name}\n' \
                      f'Фамилия: {self.surname}\n'
# Т.к. один Лектор ведёт несколько лекций, то выводит среднюю оценку по всем что есть.
            for dict_grades in self.grades:
                for key, val in dict_grades.items():
                    result += f'Средняя оценка за лекции {key}: {round(sum(val) / len(val), 2)} \n'
                return result


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = [{}]
# У моих Лекторов несколько предметов и оценки по этим предметам от студентов, функция выводит результат сравнения
# по предметам который есть у обоих лекторов. Если нету совподений по предметам, выводит обрабоку такого случая.
    def __lt__(self, other):
        if isinstance(other, Lecturer):
            for dict_grades1 in self.grades:
                result = ''
                for key1, val1 in dict_grades1.items():
                    for dict_grades2 in other.grades:
                        for key2, val2 in dict_grades2.items():
                            if key1 == key2:
                                result += f'{key1}: {(sum(val1)/len(val1)) < (sum(val2)/len(val2))}\n'
            if result == '':
                return 'Лекторы ведут разные предметы, сравнение невозможно.'
            else:
                return result
        else:
            print('Указаны объекты разных классов.')


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, corses, grade):
        if isinstance(student, Student) \
                and corses in student.courses_in_progerss \
                and corses in self.courses_attached:
            if corses in student.grades:
                student.grades[corses] += [grade]
            else:
                student.grades[corses] = [grade]
        else:
            print('Error input grade.')



# Создание студентов
best_student = Student('Alexey', 'Yakovlev', 'men')
# best_student.finished_courses += ['Git']
best_student.courses_in_progerss += ['Python']
best_student.courses_in_progerss += ['SQL']

bed_student = Student('Antonio', 'Coldly', 'men')
bed_student.courses_in_progerss += ['Git']

print(best_student.__dict__)
best_student.add_finished_courses('Zumba-Umba')
best_student.add_finished_courses('Введение в программирование')
best_student.grades['Python'] = [10]
print(best_student.__dict__)


cool_mentor = Mentor('Many', 'Hoo')
cool_mentor.courses_attached += ['Python']
print(cool_mentor.__dict__)


expert = Reviewer('True', 'Expert')
expert.courses_attached += ['Python']
expert.courses_attached += ['Git']
expert.rate_hw(best_student, 'Python', 10)
expert.rate_hw(best_student, 'Python', 10)
expert.rate_hw(best_student, 'Python', 10)


print()
print(expert.__dict__)
print(best_student.__dict__)
print()

lector_one = Lecturer( 'Entony','Brock')
lector_one.courses_attached += ['Python']
print(lector_one.__dict__)
print()
lector_two = Lecturer('Frank', 'Bisher')
lector_two.courses_attached += ['Python']
lector_two.courses_attached += ['Git']
print(lector_two.__dict__)
print()

best_student.rate_lector(lector_one, 'Python', 7)
best_student.rate_lector(lector_one, 'Python', 3)
best_student.rate_lector(lector_one, 'Git', 7)
lector_one.courses_attached += ['Git']
best_student.courses_in_progerss += ['Git']
best_student.rate_lector(lector_one, 'Git', 7)
best_student.rate_lector(lector_one, 'Python', 5)
best_student.rate_lector(lector_one, 'Python', 8)
best_student.rate_lector(lector_one, 'Git', 10)

best_student.rate_lector(lector_two, 'Python', 8)
best_student.rate_lector(lector_two, 'Python', 8)
best_student.rate_lector(lector_two, 'Python', 9)
best_student.rate_lector(lector_two, 'Git', 7)
best_student.rate_lector(lector_two, 'Git', 7)

expert.rate_hw(best_student, 'Git', 8)
expert.rate_hw(best_student, 'Git', 10)
expert.rate_hw(best_student, 'Git', 5)

expert.rate_hw(bed_student, 'Git', 3)
expert.rate_hw(bed_student, 'Git', 5)
expert.rate_hw(bed_student, 'Git', 3)

print(lector_one.__dict__)
print(lector_two.__dict__)
print()
print(best_student.__dict__)
print(bed_student.__dict__)

print(lector_one)
print(lector_two)
print(expert)
print(best_student)

print(lector_one > lector_two)

print(best_student > bed_student)

print(best_student.name)