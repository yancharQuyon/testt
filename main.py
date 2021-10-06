import os
import random
import getpass
import json


class User:
    def __init__(self,name=None,login=None,password=None,age=None,file_name="user.txt"):
        self.clear_everything()
        self.username=name
        self.login=login
        self.password=password
        self.age=age
        self.file_name=file_name
        self.init_input_option=["1","2"]
        self.all_users=[]
        self.get_all_users()
        self.password_min_len=6
        self.user_logged_in = True
        self.current_login=None
        self.current_password=None
        self.current_ID=None
        print("shunchaki print")


    def entering_system(self):
        self.clear_everything()
        self.init_massage()


        while reg_or_login not in self.init_input_option:
            self.clear_everything()
            print("Invalid input. Please select one of the options bellow")
            self.init_massage()
            reg_or_login = input("[1/2]:").strip()

        if reg_or_login==self.init_input_option[0]:
            self.register()
        else:
            self.log_in()

    def init_massage(self):
        print(f"""
        Entering the system:
        Register    [{self.init_input_option[0]}]
        Log in       [{self.init_input_option[1]}]
        """)

    def register(self):
        self.clear_everything()

        input_name=input("Name: ").strip().capitalize()
        while not input_name.isalpha():
            self.clear_everything()
            print("Invalid input. Please enter only letters:")
            input_name=input("Name: ").strip().capitalize()

        input_login=input("Login: ").strip()
        while not input_login.isalnum() or self.user_exists(input_login):
            self.clear_everything()
            print("Invalid input. Possible errors:")
            print("-Login should contain only letters or/and numbers")
            print("-This user exists")
            input_login = input("Login: ").strip()

        input_password=getpass.getpass("Password (hidden): ").strip()
        check_password=getpass.getpass("Confirm Password (hidden): ").strip()
        while self.is_string_empty(input_password) or len(input_password)<self.password_min_len or \
                input_password !=check_password:
            self.clear_everything()
            print("Invalid input. Possible errors:")
            print("-You've entered an empty password")
            print("-Passwords don't match")
            print(f"-Password should contain at least {self.password_min_len} characters")
            input_password = getpass.getpass("Password (hidden): ").strip()
            check_password = getpass.getpass("Confirm Password (hidden): ").strip()

        input_age=input("Age: ").strip()
        while not input_age.isnumeric():
            self.clear_everything()
            print("Invalid input. Please enter number")
            input_age = input("Age: ").strip()
        self.assign_user_values(input_name,input_login,input_password,input_age)
        self.write_to_json_file()
        self.main_menu()



    def assign_user_values(self,input_name,input_login,input_password,input_age):
        self.username=input_name
        self.login=input_login
        self.password=input_password
        self.age=input_age


    def get_all_users(self):
        if not self.is_file_empty():
            file=open(self.file_name)
            text=file.read()
            file.close
            text=text.strip()
            lines=text.split("\n")
            for line in lines:
                self.all_users.append(json.loads(line))



    def user_exists(self,current_input_login):
        for user in self.all_users:
            if current_input_login == user["login"]:
                return True
        return False

    def user_password(self,current_input_password):
        for user in self.all_users:
            if current_input_password == user["password"]:
                return user["password"]
        return False

    def log_in(self):
        login__=input("Your login: ").strip()
        while not login__.isalnum() or not self.user_exists(login__):
            self.clear_everything()
            print("Invalid input. Possible errors:")
            print("-Login should contain only letters or/and numbers")
            print("-This user does not exists")
            login__ = input("Your login: ").strip()
        self.current_login=login__

        password__ = getpass.getpass("Your password: ").strip()
        while self.is_string_empty(password__) or len(password__)<self.password_min_len or \
                password__ !=self.user_password(password__):
            self.clear_everything()
            print("Invalid input. Possible errors:")
            print("-You've entered an empty password")
            print("-Passwords don't match")
            print(f"-Password should contain at least {self.password_min_len} characters")
            password__ = getpass.getpass("Your password: ").strip()
        self.current_password=password__

        self.main_menu()

    def main_menu(self):
        self.clear_everything()
        for i in range(len(self.all_users)):
            if self.current_login == self.all_users[i]["login"]:
                print(f'Salom {self.all_users[i]["name"]}')


        print("""
                Main Menu""")


        print("""
    1. Friends
    2. Massages
    3. Quiz
    4. Settings
    5. Log out""")





        page=int(input("choose one of bellow: "))
        if page == 4:
            self.settings()

        elif page == 5:
            self.ask()


        # if self.user_logged_in == False:
        #     print("yoqole")
    def log_out(self):
        self.entering_system()

    def ask(self):
        self.clear_everything()
        print(f"""
                Choose one:
                Sign in       [{self.init_input_option[0]}]
                Log out       [{self.init_input_option[1]}]
                """)

        signIn_or_logout = input("[1/2]:").strip()

        while signIn_or_logout not in self.init_input_option:
            self.clear_everything()
            print("Invalid input. Please select one of the options bellow")
            self.init_massage()
            signIn_or_logout = input("[1/2]:").strip()


        if signIn_or_logout==self.init_input_option[0]:
            self.main_menu()
        else:
            self.log_out()


    def settings(self):
        page=0
        self.clear_everything()
        print(f""" Settings:
    1.Update login  
    2.Update password
    3.Delete password""")
        page=int(input())
        if page == 1:
            self.update_login()

        elif page == 2:
            self.update_password()

        elif page == 3:
            self.delete_account()

        else:
            self.settings()




    def update_login(self):
        self.clear_everything()
        tekshir=input("Input your current login:")
        if tekshir == self.current_login:
            # file=open(self.file_name,"w")

            for i in range(0,self.accaunt_ID()):
                print(self.all_users[i])

            print(self.all_users[self.accaunt_ID()])

            for i in range(self.accaunt_ID()+1,len(self.all_users)):
                print(self.all_users[i])


            # file.close

        else:
            print("Invalid login")


    def update_password(self):
        self.clear_everything()
        print("parol",self.accaunt_ID())

    def delete_account(self):
        self.clear_everything()
        print("delete acc",self.accaunt_ID())

    @staticmethod
    def clear_everything():
        os.system("clear")

    @staticmethod
    def is_string_empty(str_):
        """String bo'sh bo'lsa True qaytaradi\n
        Aks holda False qaytaradi"""
        return not str_

    def write_to_json_file(self)-> None:
        file=open(self.file_name,"a")
        user_info={
            "name":self.username,
            "login":self.login,
            "password":self.password,
            "age":self.age
        }
        user_info=json.dumps(user_info)
        file.write(user_info +"\n")
        file.close

    def is_file_empty(self):
        file=open(self.file_name)
        text=file.read()
        file.close()
        return self.is_string_empty(text)

    def accaunt_ID(self):
        for i in range(len(self.all_users)):
            if self.current_login == self.all_users[i]["login"]:
                return i
            else:
                continue
        self.accaunt_ID=i











person=User()
person.entering_system()


















