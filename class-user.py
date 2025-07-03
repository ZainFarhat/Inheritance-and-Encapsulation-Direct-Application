
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