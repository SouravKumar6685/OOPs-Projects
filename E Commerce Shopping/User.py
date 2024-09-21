class User:

    def __init__(self, username, email, password, address):
        self.username = username
        self.email = email
        self.password = password
        self.address = address
    
    # login 
    def login(self, username, password):
        if self.username == username and self.password == password:
            print(f"Welcome, {self.username}! \n")
            return True
        else:
            print("Invalid login credentails.\n")
            return False
    
    # Logout
    def logout(self):
        print(f"{self.username} has logged out.\n")
    
    # view profile
    def view_profile(self):
        print(f"Username: {self.username}, Email: {self.email},\n Address: {self.address} \n")
        