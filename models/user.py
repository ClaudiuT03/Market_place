"""
Module with class representing a user/entry from Users table
"""
from exceptions import ValidationError


class User:
    """
    Class representing a user/entry from Users table
    """

    def __init__(self, id, username, password, email, is_logged=0):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
        self.is_logged = is_logged

    def validate(self):
        self.__validate_username()
        self.__validate_email()
        self.__validate_password()

    def __validate_username(self):
        """
        Check that username does not contain special characters.
        """
        invalid_chars = "!#$%^&*()+=`~/?<>,\\|\"\'|țșăîâÂÎȚȘĂ"
        if any([c in invalid_chars for c in self.username]):
            raise ValidationError("Username is not valid!")

    def __validate_email(self):
        """
        Check that email has only one @ and at least one .
        """
        # my_str = "aaabc"
        # my_str.count("a") # -> 3
        # my_str.count("b") # -> 1
        # my_str.count("e") # -> 0
        if self.email.count("@") != 1 or self.email.count(".") == 0:
            raise ValidationError("Email is not valid!")

    def __validate_password(self):
        """
        Check that password fulfills the following requirements:
        - has at least 8 characters
        - has at least one special character
        - has at least one capital letter
        - has at least one number
        """
        # Verifica daca exista cel putin o litera mare
        if not any(char.isupper() for char in self.password):
            raise ValidationError("Password is not valid!")

        # Verifica lungimea minima de 8 caractere
        if len(self.password) < 8:
            raise ValidationError("Password is not valid!")

        # Verifica daca exista cel putin un numar
        if not any(char.isdigit() for char in self.password):
            raise ValidationError("Password is not valid!")

        # Verifica daca exista cel putin un caracter special
        special_chars = "!@#$%^&*()-=_+[]{}|;':\"<>,./?\\"
        if not any(char in special_chars for char in self.password):
            raise ValidationError("Password is not valid!")
