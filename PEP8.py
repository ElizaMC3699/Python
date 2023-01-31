# Guía de codificacion de Python PEP 8

# CamelCase para nombres de clases


class UserAdmin():

    def __init__(self, username, password=''):  # para parámetros no hay espacio
        self.username = username
        self.password = password
    
    def set_password(self):
        pass

# snake_case para nombres de variables, métodos, funciones

cody_user = UserAdmin('Cody')

# https://www.pythonchecker.com

# el archivo principal se denomina 'main.py'