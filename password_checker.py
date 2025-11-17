import string
# password= input("Enter your password: ")

while True:
    password= input("Enter your password : ")

    
    if len(password) < 8:
        print("Password must be at least 8 characters long.")
        print("Enter a valid password.")
        
    elif len(password) >=8 and len(password) <=16:
            print("Your password: ",password)
            break
#     elif len(password) >10 and len(password) <=14:  
#             print("Password strength: Moderate")
#             print("Your password: ",password)
        #     break
#     elif len(password) >14 and len(password) <=16:
#             print("Password strength: Strong")
#             print("Your password: ",password)
        #     break
    else:
            print("Password must not exceed 16 characters.")
            print("Enter a valid password.")

# print("Lowercase: " ,password.islower())
# print("Uppercase: ", password.isupper())
# print("Digit:     " ,password.isalpha())
# has_symbol = any(char in string.punctuation for char in password)
# print("Symbol:    ",has_symbol)

score = 0
if len(password)>=8:
       score+=2                         #if true score = 2
if len(password)>10:
       score+=2                         #if  both true score = 4
if len(password)>14 and len(password)<=16:
       score+=2                          #if all true score = 6
if any(char.islower() for char in password):
       score+=1                                #if all true score = 7s
if any(char.isupper()for char in password):
       score+=1                  #if all true score = 8
if any( char.isdigit() for char in password ):
       score+=1                          #if all true score = 9
if any(char in string.punctuation for char in password):
       score+=1                         #if all true score = 10

if score>0 and score<=4:
       print(" Password Strength: Weak")
elif score>4 and score<=7:
       print(" Password Strength: Moderate")
elif score>7:
       print(" Password Strength: Strong!")
       

    


    