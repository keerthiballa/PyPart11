import enum
from typing import Dict
import uuid

class AliveStatus(enum.Enum):

    def __init__(self,status):
        self.status=status
        Deceased = 0
        Alive = 1

class Person:
    """
    Attributes: first_name, last_name, dob (date of birth), alive (of type AliveStatus)
    """

    def __init__(self, first_name, last_name, dob, alive:AliveStatus):
        self.first_name=first_name
        self.last_name=last_name
        self.dob=dob
        self.alive=alive

    def update_first_name(self,new_first_name):
        self.first_name=new_first_name

    def update_last_name(self,new_last_name):
        self.last_name=new_last_name

    def update_dob(self,new_dob):
        self.dob=new_dob

    def update_status(self,new_status):
        self.status=new_status

class Instructor(Person):
    """
    Additional attribute: instructor_id that must start with the string "Instructor_" followed by a UUID value
    Hint: Use super class calls
    """
    
    def __init__(self, first_name, last_name, dob, alive: AliveStatus):
        super().__init__(first_name, last_name, dob, alive)
        self.instructor_id=f"Instructor_{uuid.uuid4()}"

class Student(Person):
    """
    Additional attribute: student_id that much start with the string "Student_" followed by a UUID value
    """

    def __init__(self, first_name, last_name, dob, alive: AliveStatus):
        self.student_id=f"Student_{uuid.uuid4()}"
        super().__init__(first_name, last_name, dob, alive)

class ZipCodeStudent(Student):
    """
    Declare a class called ZipCodeStudent.

    This class must inherit from the Student class.
    """

    def __init__(self, first_name, last_name, dob, alive: AliveStatus, student_id):
        super().__init__(first_name, last_name, dob, alive, student_id)

class CollegeStudent(Student):
    """
    Declare another type of student (prek, middle-school, college, etc).

    This class must inherit from the Student class.
    """
    def __init__(self, first_name, last_name, dob, alive: AliveStatus, student_id):
        super().__init__(first_name, last_name, dob, alive, student_id)

class Classroom:

    """
    Declare a class called Classroom:

    Classroom class must have the following attributes:

    students - a container for students
    instructors - a container for instructors
    Classroom class must also have the following methods:

    add_instructor
    remove_instructor
    add_student
    remove_student
    print_instructors
    print_students
    """

    def __init__(self, students:list, instructors: list):
        self.students = {} #a container for students
        self.instructors= {} #a container for instructors

    def add_instructor(self,instructor):
        if instructor.instructor_id not in self.instructors:
            self.instructors[instructor.instructor_id]=instructor
        else:
            print("Instructor already exists")

    def remove_instructor(self,instructor):
        if instructor.instructor_id not in self.instructors:
            del self.instructors[instructor.instructor_id]
        else:
            print("Instructor already exists")

    def add_student(self, student):
        if student.student_id not in self.students:
            self.students[student.student_id]=student
        else:
            print("Student already exists")

    def remove_student(self, student):
        if student.student_id not in self.students:
            del self.student[student.student_id]
        else:
            print("Student does not exist")

    def print_instructors(self):
        for k,v in self.instructors.items():
            print(f"{k}:{v}")

    def print_students(self):
        for k,v in self.students.items():
            print(f"{k}:{v}")