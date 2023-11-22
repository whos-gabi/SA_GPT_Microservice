import json


class Subject:
    def __init__(self, title, key):
        self.title = title
        self.key = key


class Grade:
    def __init__(self, title, grade):
        self.title = title
        self.grade = grade


class LessonType:
    def __init__(self, title, key):
        self.title = title
        self.key = key


class Lesson:
    def __init__(
        self, title, description, subject, grade, lesson_type, date, cdn, filename
    ):
        self.title = title
        self.description = description
        self.subject = subject  # This should be an instance of the Subject class
        self.grade = grade  # This should be an instance of the Grade class
        self.lesson_type = (
            lesson_type  # This should be an instance of the LessonType class
        )
        self.date = date  # Assuming that Date is a class or a valid data type
        self.cdn = cdn
        self.filename = filename

    def to_json(self):
        lesson_dict = {
            "title": self.title,
            "description": self.description,
            "subject": {"title": self.subject.title, "key": self.subject.key},
            "grade": {"title": self.grade.title, "grade": self.grade.grade},
            "type": {"title": self.lesson_type.title, "key": self.lesson_type.key},
            "date": str(self.date),  # Convert date to string for JSON serialization
            "cdn": self.cdn,
            "filename": self.filename,
        }
        return json.dumps(lesson_dict, indent=2)


# Example usage:
# Create instances of Subject, Grade, and LessonType
math_subject = Subject("Mathematics", "math")
grade_10 = Grade("Grade 10", 10)
lecture_type = LessonType("Lecture", "lecture")

# Create an instance of Lesson using the created instances
math_lecture = Lesson(
    "Introduction to Algebra",
    "Basic algebraic concepts",
    math_subject,
    grade_10,
    lecture_type,
    "2023-11-20",
    "example_cdn",
    "example_filename",
)

# Print the Lesson instance as JSON
print(math_lecture.to_json())
