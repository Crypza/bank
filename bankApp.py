pin = 1234
login = False
loginA = 0


#Ifall pin inte är samma som userPin så avslutas programmet
while login == False:

    userPin = int(input("Skriv in din pinkod: "))

    if pin != userPin:
        loginA = loginA + 1
        print("Felaktigt")
        if loginA > 2:
            exit()
    else:
        login = True
    

#Öppnar filen balance.txt som variabeln balanceFile och läser av vad som står i filen. Anger sedan balance som BalanceFile. Ifall att ingen fil hittas noteras användaren och saldot blir 0.
try:
    with open("balance.txt", "r")as balanceFile:
        try:
            balance = balanceFile.readline()
            balance = float(balance)
        except (ValueError):
            print("File corrupt")
            balance = 0.0
except (FileNotFoundError):
    balance = 0.0
menu = 0
# menu 1 insättning
# menu 2 uttag
# menu 3 avsluta

#Ifall att menu inte är 0, 2 eller 3 så tas användaren direkt till insättning. Lägger till användarens input på balance
while menu != 3:
    print("Ditt saldo är: ", balance)
    menu = int(input("Skriv ditt val[1, 2, 3]: "))
    if menu == 1:
        balance = balance + float(input("Gör en instättning: "))
        try:
             with open("balance.txt", "w")as balanceFile:
              balanceFile.write(str(balance))
        except (FileNotFoundError):
                print("Ingen fil")

#Säger åt användaren att ange ett tal för att göra ett uttag och drar av det från balance, ifall att det inte är ett tal som anges spottar den ut ett Error meddelande och säger åt användaren att ange ett tal nästa gång
    elif menu == 2:
        print('''uttag
        ''')
        try:
            uttagAmount = float(input("Gör ett uttag: "))
            balance = balance - uttagAmount
            try:
                 with open("balance.txt", "w")as balanceFile:
                    balanceFile.write(str(balance))
            except (FileNotFoundError):
                print("Ingen fil")
        except (ValueError):
            print('''Error: invalid number. Vänligen angiv ett giltigt nummer
            ''')

#Avslutar och sparar variabeln balance i balance.txt filen
    else:
        print("Fel eller avslut")
        try:
            with open("balance.txt", "w")as balanceFile:
                balanceFile.write(str(balance))
        except (FileNotFoundError):
            print("Ingen fil")