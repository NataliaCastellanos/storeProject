class User: 

    def __init__(self, name, lastName, email, password):
        self.name = name
        self.lastName= lastName
        self.set_email(email)
        self.set_password(password)

    def get_email(self):
        return self._email

    def set_email(self, email):
        if (email != ""):
            self._email = email
        else: 
            raise ValueError("El correo no puede estar vacío")

    def get_password(self):
        return self._password

    def set_password(self, password):
        if password == "":
            raise ValueError("La contraseña no puede estar vacía")

        if not any(character.isupper() for character in password):
            raise ValueError("La contraseña debe tener al menos una mayúscula")

        self._password = password

    def show_info(self):
        return f"Nombre: {self.name} {self.lastName} - Correo: {self.get_email()}"

    def login(self, email, password):
        return (self.get_email() == email and self.get_password() == password)

    
