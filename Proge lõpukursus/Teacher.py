class Grade:
    """Grade."""

    def __init__(self, grade, weight: int, assignment: str, date: str):
        """Constructor."""
        self.assignment = assignment
        self.value = grade
        self.weight = weight
        self.date = date
        self.previous_grades = {}

    def change_grade(self, new_grade: int, date: str):
        self.previous_grades[self.date] = self.value
        self.value = new_grade
        self.date = date



class Student:
    """Student."""

    def __init__(self, name: str):
        """Constructor."""
        self.name = name
        self.grades = {}

    def grade(self, grade: Grade):
        self.grades[grade.assignment] = grade

    def redo_assignment(self, new_grade: int, assignment: str, date: str):
        self.grades[assignment].change_grade(new_grade,date)

    def calculate_weighted_average(self):
        summer = 0
        divider = 0
        print(self.grades.keys())
        for x in self.grades.keys():
            print(self.grades[x].value)
            if self.grades[x].value == "!":
                summer += 1 * self.grades[x].weight
            else:
                summer += int(self.grades[x].value) * self.grades[x].weight
            divider += self.grades[x].weight
        return(round(summer/divider))


class Class:
    """Class."""

    def __init__(self, teacher: str, students: list):
        """Constructor."""
        self.teacher = teacher
        self.students = students

    def add_student(self, student: Student):
        self.students += [student]

    def add_students(self, students: list):
        self.students += students

    def remove_student(self, student: Student):
        self.students.remove(student)
        pass

    def get_grade_sheet(self):
        length_name = max([len(i.name) for i in self.students] + [len("Name")])
        length_grade = len("Final grade")
        grade_sheet = f"{'-'*(7+length_grade+length_name)}\n| Name{' '*(length_name - 4)} | Final grade |\n{'-'*(7+length_grade+length_name)}\n"
        for i in self.students:
            grade_sheet += f"| {i.name}{' '*(length_name - len(i.name))} |      {i.calculate_weighted_average()}      |\n"
        grade_sheet += f"{'-'*(7+length_grade+length_name)}"
        return(grade_sheet)


if __name__ == '__main__':
    # Teacher, grade, student
    mari = Student("Mari Maa")
    jyri = Student("Jyri Jogi")
    teele = Student("Teele Tee")
    cl = Class("Anna", [mari, jyri, teele])
    mari.grade(Grade(5, 3, "KT", "01/09/2020"))
    gr = Grade("!", 3, "KT", "01/09/2020")
    jyri.grade(gr)
    teele.grade(Grade(4, 3, "KT", "01/09/2020"))

    print(f"Jyri keskmine hinne on {jyri.calculate_weighted_average()}.")  # 1

    jyri.redo_assignment(3, "KT", "14/09/2020")
    print(len(gr.previous_grades))  # 1

    print(f"Jyri keskmine hinne on nyyd {jyri.calculate_weighted_average()}.")  # 3
    print()

    mari.grade(Grade(5, 1, "TK", "30/11/2020"))
    jyri.grade(Grade(4, 1, "TK", "30/11/2020"))
    teele.grade(Grade(3, 1, "TK", "30/11/2020"))

    print(f"Teele keskmine hinne on {teele.calculate_weighted_average()}.")  # 4
    print(cl.get_grade_sheet())
    print()

    tuuli = Student("Tuuli Karu")
    cl.add_student(tuuli)
    print(len(cl.students))  # 4
    print(cl.get_grade_sheet())