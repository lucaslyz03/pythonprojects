class Users:
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name

    def greet_users(self):
        print('hello '+str(self.first_name))


class Admin(Users):
    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)
        self.privileges='can ban users'
    
    def show_privileges(self):
        print(self.first_name+' '+self.privileges)

    

amy=Users('wang','lm')
david=Users('zhou','hui')
amy.greet_users()
david.greet_users()

admin=Admin('kk','adm')
admin.show_privileges()