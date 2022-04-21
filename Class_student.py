gpa_minimum_value = 1.5

class Student:
    def __init__(self, name, courses_grades_and_weights):
        self.name = name
        self.courses_grades_and_weights = courses_grades_and_weights

    def __str__(self):
        return f"Student(name:{self.name},courses_grades_and_weights: {self.courses_grades_and_weights})"

Ayodeji = Student("Ayodeji", [
    {"name": "MEG 211", "grade": 4, "weight": 2},
    {"name": "MEG 212", "grade": 5, "weight": 2},
    {"name": "MEG 213", "grade": 5, "weight": 2},
    {"name": "MEG 214", "grade": 5, "weight": 2},
    {"name": "MEG 215", "grade": 5, "weight": 2},
    {"name": "EEG 211", "grade": 5, "weight": 2},
    {"name": "EEG 231", "grade": 5, "weight": 1},
    {"name": "GEG 219", "grade": 5, "weight": 2},
    {"name": "GEG 217", "grade": 5, "weight": 2},
    {"name": "SSG 215", "grade": 5, "weight": 1}])
Bola = Student("Bola", [
    {"name": "MEG 211", "grade": 4, "weight": 2},
    {"name": "MEG 212", "grade": 3, "weight": 2},
    {"name": "MEG 213", "grade": 5, "weight": 2},
    {"name": "MEG 214", "grade": 4, "weight": 2},
    {"name": "MEG 215", "grade": 3, "weight": 2},
    {"name": "EEG 211", "grade": 5, "weight": 2},
    {"name": "EEG 231", "grade": 4, "weight": 1},
    {"name": "GEG 219", "grade": 3, "weight": 2},
    {"name": "GEG 217", "grade": 5, "weight": 2},
    {"name": "SSG 215", "grade": 4, "weight": 1}])

Chukwueze = Student("Chukwueze", [
  {"name": "MEG 211", "grade": 4, "weight": 2},
    {"name": "MEG 212", "grade": 0, "weight": 2},
    {"name": "MEG 213", "grade": 4, "weight": 2},
    {"name": "MEG 214", "grade": 1, "weight": 2},
    {"name": "MEG 215", "grade": 0, "weight": 2},
    {"name": "EEG 211", "grade": 1, "weight": 2},
    {"name": "EEG 231", "grade": 0, "weight": 1},
    {"name": "GEG 219", "grade": 1, "weight": 2},
    {"name": "GEG 217", "grade": 0, "weight": 2},
    {"name": "SSG 215", "grade": 3, "weight": 1}])


def compute_stand(student_info):
    if student_info["GPA"] < gpa_minimum_value:
        return {"standing": "fail", **student_info}
    return {"standing": "pass", **student_info}


def rank_cgpas(student_list):
    final_student_list_with_gpas = []
    for student in student_list:
        total_credits = 0
        total_grade_points = 0
        for course in student.courses_grades_and_weights:
            total_credits += course["weight"]
            total_grade_points += course["weight"] * course["grade"]
        final_student_list_with_gpas.append(
            {"name": student.name, "GPA": total_grade_points / total_credits})
    final_student_list_with_gpas.sort(key=lambda x: x["GPA"], reverse=True)
    standing_with_gpa = list(
        map(compute_stand, final_student_list_with_gpas))
    print(*standing_with_gpa, sep='\n')


rank_cgpas([Ayodeji, Bola, Chukwueze])
