class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password  
    
    def set_password(self, new_password):
        
        self.__password = new_password
    
    def check_password(self, password):
        
        return self.__password == password


user = UserAccount("deni", "deni@mail.ru", "anypassword")


user.set_password("new_secure_password")

if(user.check_password):
    print(user.check_password("new_secure_password"))  
else:
    print(user.check_password("wrong_password"))       