
# password= input("Enter your password: ")

while True:
    password= input("Enter your password : ")

    
    if len(password) < 8:
        print("Password must be at least 8 characters long.")
        print("Enter a valid password.")

    elif len(password) >=8 and len(password) <=10:
            print("Password strength: Weak")
            print("Your password: ",password)
            break
    elif len(password) >10 and len(password) <=14:  
            print("Password strength: Moderate")
            print("Your password: ",password)
            break
    elif len(password) >14 and len(password) <=16:
            print("Password strength: Strong")
            print("Your password: ",password)
            break
    else:
            print("Password must not exceed 16 characters.")
            print("Enter a valid password.")



    


    