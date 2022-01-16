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
        self.students = students #a container for students
        self.instructors= instructors #a container for instructors

    def add_instructor(self,new_first_name,new_last_name,new_dob,new_status):
        new_instructor=list()
        new_instructor.append(new_first_name)
        new_instructor.append(new_last_name)
        new_instructor.append(new_dob)
        new_instructor.append(new_status)
        print(new_instructor)
        if new_instructor not in self.instructors:
            Instructor.update_first_name(new_instructor[0])
            Instructor.update_last_name(new_instructor[1])
            Instructor.update_dob(new_instructor[2])
            Instructor.update_status(new_instructor[3])
            Instructor(new_instructor)
            self.instructors.append(new_instructor)
        else:
            print("New instructor already exists")

    def remove_instructor(self,instructor:list):
        if instructor in self.instructors:
            del(instructor)
        else:
            print("Instructor does not exist")

    def add_student(self, new_student:list):
        if new_student not in self.students:
            Student(new_student)
            Student.update_first_name(new_student[0])
            Student.update_last_name(new_student[1])
            Student.update_dob(new_student[2])
            Student.update_status(new_student[3])
            self.students.append(new_student)
        else:
            print("New student already exists")

    def remove_student(self, student:list):
        if student in self.students:
            del(student)
        else:
            print("Student does not exist")

    def print_instructors(self):
        print(self.instructors)

    def print_students(self):
        print(self.students)

c=Classroom([],[])
c.add_instructor("fn1","ln1","dob1",0)
c.print_instructors()
c.add_instructor("fn2","ln2","dob2",1)
c.print_instructors()
c.remove_instructor("fn1","ln1","dob1",0)
c.print_instructors()
c.remove_instructor("fn3","ln3","dob3",0)
c.print_instructors()

c.add_student("fn1","ln1","dob1",0)
c.print_students()
c.add_student("fn2","ln2","dob2",1)
c.print_students()
c.remove_student("fn1","ln1","dob1",0)
c.print_students()
c.remove_student("fn3","ln3","dob3",0)
c.print_students()