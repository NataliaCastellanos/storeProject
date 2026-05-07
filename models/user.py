class User: 

    def __init__(self, new_name, new_last_name, new_email, new_password):
        self.set_name(new_name)
        self.set_last_name(new_last_name)
        self.set_email(new_email)
        self.set_password(new_password)

    # Getter for name
    def get_name(self):
        return self._name
    
    # Setter for name
    def set_name(self, new_name):
        if( new_name != ""):
            self._name = new_name
        else:
            print("The Name can not be empty")

    # Getter for last_name
    def get_last_name(self):
        return self._last_name

    # Setter for last_name
    def set_last_name(self, new_last_name):
        if(new_last_name != ""):
            self._last_name = new_last_name
        else:
            print("The Last Name can not be empty")
    
    # Getter for email
    def get_email(self):
        return self._email
    
    # Setter for email
    def set_email(self, new_email):
        if(new_email != ""):
            self._email = new_email
        else: 
            print("The Email can not be empty")
    
    # Getter for password
    def get_password(self):
        return self._password
    
    # Setter for password
    def set_password(self, new_password):
        if(new_password != ""):
            self._password = new_password
        else:
            print("The Password can not be empty")

    # Get role
    def get_role(self):
        return ("User")
    
    # Show_info
    def show_info(self):
        return (f"Name: {self.get_name()}, Last Name: {self.get_last_name()}, Email: {self.get_email()}")
        
    # Login
    def login(self, email, password):
        if(self._email == email and self._password == password):
            return (f"Welcome {self.get_name()}")
        else:
            return ("Invalid credentials")