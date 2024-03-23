from school_db import con, cur
import os
import bcrypt

status_menu = True
global status_op

def hash_password(passwd):
    return bcrypt.hashpw(passwd.encode(), bcrypt.gensalt())

def create_user(op):
    #Create a new user
    os.system('clear')

    print("::: Signup form :::")
    idusers = input("Your id_users: ")
    email = input("Your email: ")
    passwd = input("Your password: ")
    passwd_hashed = hash_password(passwd)
    status = input("Your status: ")
    created= input("Your created_at: ")
    updated= input("Your updated_at ")
    deleted= input("Your deleted_at: ")
  
    new_user = f'''
        INSERT INTO 
            Users ( id_users,  email, password, status, created_at,updated_at,deleted_at) 
            VALUES('{idusers}', '{email}', "{passwd_hashed}", '{status}', '{created}', '{updated}', '{deleted}')
    '''
    con.execute(new_user)
    con.commit()

    print("::: New user has been created sucessfully :::")
    os.system('pause')
    menu()

def create_student(op):
    #Create a new user
    os.system('clear')

    print("::: Signup form :::")
    idstuds = input("Your id_Students: ")
    code= input("your code : ")
    id_persons=input("your id_persons : ")
    status = input("Your status: ")
    created= input("Your created_at: ")
    updated= input("Your updated_at ")
    deleted= input("Your deleted_at: ")
  
    new_student = f'''
        INSERT INTO 
            Students ( id_Student, code, status, created_at,updated_at,deleted_at) 
            VALUES('{idstuds}', '{code}','{status}', '{created}', '{updated}', '{deleted}')
    '''
    con.execute(new_student)
    con.commit()

    print("::: New user has been created sucessfully :::")
    os.system('pause')
    menu()
