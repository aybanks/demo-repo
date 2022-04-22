class Student:
    def __init__(self, name, courses_grades_and_weights):
        self.name = name
        self.courses_grades_and_weights = courses_grades_and_weights

    def __str__(self):
        return f"name: {self.name}, courses_grades_and_weights: {self.courses_grades_and_weights}"


Ayodele = Student("Ayodele", [{"course": "MEG 211", "grade": 5, "weight": 2},
                              {"course": "MEG 212", "grade": 5, "weight": 2},
                              {"course": "MEG 213", "grade": 5, "weight": 2},
                              {"course": "MEG 214", "grade": 5, "weight": 2},
                              {"course": "MEG 215", "grade": 5, "weight": 2},
                              {"course": "EEG 211", "grade": 5, "weight": 2},
                              {"course": "EEG 231", "grade": 5, "weight": 1},
                              {"course": "SSG 215", "grade": 5, "weight": 1},
                              {"course": "GEG 217", "grade": 5, "weight": 3},
                              {"course": "GEG 219", "grade": 5, "weight": 3}])

Tolani = Student("Tolani", [{"course": "MEG 211", "grade": 4, "weight": 2},
                            {"course": "MEG 212", "grade": 3, "weight": 2},
                            {"course": "MEG 213", "grade": 2, "weight": 2},
                            {"course": "MEG 214", "grade": 1, "weight": 2},
                            {"course": "MEG 215", "grade": 4, "weight": 2},
                            {"course": "EEG 211", "grade": 3, "weight": 2},
                            {"course": "EEG 231", "grade": 2, "weight": 1},
                            {"course": "SSG 215", "grade": 1, "weight": 1},
                            {"course": "GEG 217", "grade": 2, "weight": 3},
                            {"course": "GEG 219", "grade": 4, "weight": 3}])

Bolu = Student("Bolu", [{"course": "MEG 211", "grade": 2, "weight": 2},
                        {"course": "MEG 212", "grade": 1, "weight": 2},
                        {"course": "MEG 213", "grade": 1, "weight": 2},
                        {"course": "MEG 214", "grade": 1, "weight": 2},
                        {"course": "MEG 215", "grade": 3, "weight": 2},
                        {"course": "EEG 211", "grade": 1, "weight": 2},
                        {"course": "EEG 231", "grade": 1, "weight": 1},
                        {"course": "SSG 215", "grade": 1, "weight": 1},
                        {"course": "GEG 217", "grade": 1, "weight": 3},
                        {"course": "GEG 219", "grade": 1, "weight": 3}])


def rank_cgpas(student_list):
    final_student_list = []
    for student in student_list:
        total_credit_units = 0
        total_quality_points = 0
        for course in student.courses_grades_and_weights:
            total_credit_units += course["weight"]
            total_quality_points += course["grade"] * course["weight"]
        cgpa = total_quality_points / total_credit_units
        final_student_list.append({"name": student.name, "CGPA": cgpa})
    final_student_list.sort(reverse=True, key=lambda x: x["CGPA"])
    minimum_gpa = 1.5
    list = []
    for student in final_student_list:
        if student["CGPA"] < minimum_gpa:
            list.append(
                {"standing": "fail", "name": student["name"], "CGPA": student["CGPA"]})
        else:
            list.append(
                {"standing": "pass", "name": student["name"], "CGPA": student["CGPA"]})
    print(*list, sep="\n")


rank_cgpas([Ayodele, Tolani, Bolu])
