#!/usr/bin/python3
"""
A module that defines a class Student
"""


class Student:
    """
    a class Student that defines a student by
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of a Student instance
        If attrs is a list of strings, only attribute names contained
        in this list must be retrieved
        Otherwise, all attributes must be retrieved
        """
        if type(attrs) == list and all(type(ele) == str for ele in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__


# if __name__ == "__main__":
#     students = [Student("John", "Doe", 23), Student("Bob", "Dylan", 27)]

#     for student in students:
#         j_student = student.to_json()
#         print(type(j_student))
#         print(j_student['first_name'])
#         print(type(j_student['first_name']))
#         print(j_student['age'])
#         print(type(j_student['age']))
