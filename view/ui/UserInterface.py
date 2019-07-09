#######################################################
# 
# UserInterface.py
# Python implementation of the Class UserInterface
# Created on:      23-jun.-2019 6:56:37
# Original author: Betacode
# 
#######################################################
from controllers.UserChangeObserver import UserChangeObserver
import re

class UserInterface:
    MAX_PASSWORD = 20
    MIN_PASSWORD = 8

    def checkLength(length):
        """checkLength(length: int): bool
        """
        return UserInterface.MIN_PASSWORD <= length <= UserInterface.MAX_PASSWORD, UserInterface.suggest(1)

    def isPasswordCorrect(pwd):
        """isPasswordCorrect(pwd: str): bool
        """
        return bool(pwd) and isinstance(pwd, str) and re.match(r"\w", pwd), UserInterface.suggest(2)

    def isUsernameCorrect(username):
        """isUsernameCorrect(username: str): bool
        """
        return bool(username) and isinstance(username, str) and not bool(re.findall(r"[^\w\-\_]", username)), UserInterface.suggest(3)

    def suggest(idseggest):
        """suggest(idseggest: int): str
        """
        msg = {
            1: "Revise la longitud del password.",
            2: "Los caracteres especiales son invalidos.",
            3: "Se permiten letras, numeros y los caracteres especiales '_' y '-'."
        }
        return msg.get(idseggest)
