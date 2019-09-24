#Bank applikation



#Login

print("Välkommen till SwedBank")
print("Swedbank Login")

userName = "hans"
userPass = "Hej123!"

loginA = 0

login = False
while login == False:
    
    if loginA < 3:
        userNameA = str(input("Enter Username: "))
        userPassA = str(input("Enter Password: "))
        if userNameA == userName and userPassA == userPass:
            print("Välkommen till SwedBank")
            login = True
        elif userNameA != userName:
            print("Unknown User")
            userExitC = str(input("Exit? [y/n]")).lower
            if userExitC == "y":
                exit()
            else:
                loginA += 1
        else:
            print("Invalid Password")
            userExitC = str(input("Exit? [y/n]")).lower
            if userExitC == "y":
                exit()
            else:
                loginA += 1
    else:
        exit()
    
    #