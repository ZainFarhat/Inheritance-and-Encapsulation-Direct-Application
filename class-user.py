
class User:
    # This runs when we create a new User
    def __init__(self, name, email):
        self.__name = name        # save the name and keep it private
        self.__email = email      # save email and keep it private 

    # Method to return name and email
    def get_info(self):
        return self.__name, self.__email

    # Method to update email later on if needed.
    def set_email(self, new_email):
        self.__email = new_email

class Student(User):
    def __init__(self, name, email):
        super().__init__(name, email)   # get name and email from User 
        self.__enrolled_courses = []    # empty list for enrolled courses

    # Method to enroll in a course
    def enroll(self, course_name):
        self.__enrolled_courses.append(course_name)

class Instructor(User):
    def __init__(self, name, email):
        super().__init__(name, email)   # get name and email from User
        self.__teaching_courses = []    # empty list for teaching courses

    # Method to add a course
    def add_course(self, course_name):
        self.__teaching_courses.append(course_name)