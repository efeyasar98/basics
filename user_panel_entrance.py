print("""
********************
Wellcome To The User Panel
********************
""")

sys_user_name = "admin"

sys_pass = "master"
entry_chance = 3

while True:
    user_name = input("User Name:")
    passw = input("Password:")
    if (user_name != sys_user_name and passw == sys_pass ):
        print("User Name is wrong!")
        entry_chance -= 1
    elif (user_name == sys_user_name and passw != sys_pass ):
        print("Password is wrong!")
        entry_chance -= 1
    elif (user_name != sys_user_name and passw != sys_pass):
        print("User Name and Password is wrong!")
        entry_chance -= 1
    else:
        print("Welcome to the system")
        break
    if (entry_chance == 0):
        print("Your entry chance is finished...")
        break