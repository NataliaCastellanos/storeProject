class User:
    # Constructor for the User class
    def __init__(self, new_name, new_last_name, new_email, new_password):
        self.set_name(new_name)
        self.set_last_name(new_last_name)
        self.set_email(new_email)
        self.set_password(new_password)

    # Getter for the user name
    def get_name(self):
        return self._name
    
    # Setter for the user name
    def set_name(self, new_name):
        if(new_name != ""):
            self._name = new_name
        else:
            print("The user name cannot be empty")

    # Getter for the user last name
    def get_last_name(self):
        return self._last_name

    # Setter for the user last name
    def set_last_name(self, new_last_name):
        if(new_last_name != ""):
            self._last_name = new_last_name
        else:
            print("The user last name cannot be empty")

    # Getter for the user email
    def get_email(self):
        return self._email

    # Setter for the user email
    def set_email(self, new_email):
        if(new_email != ""):
            self._email = new_email
        else:
            print("The user email cannot be empty")

    # Getter for the user password
    def get_password(self):
        return self._password
    
    # Setter for the user password
    def set_password(self, new_password):
        if(new_password != ""):
            self._password = new_password
        else:
            print("The user password cannot be empty")

    # Show_info
    def show_info(self):
        return(f"Name: {self.get_name()} {self.get_last_name()} \n"
               f"Email: {self.get_email()}")
    
    # Get role
    def get_role(self):
        return "User"
    
    # Login
    def login(self, email, password):
        if( self.get_email() == email and self.get_password() == password):
            return (f"{self.get_role()} bienvenido")
        else:
            return ("Invalid credetials")
        