pin = 1234

userPin = int(input("Skriv in din pinkod: "))

if pin != userPin:
    exit()

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
    elif menu == 2:
        print('''uttag
        ''')
        try:
            uttagAmount = int(input("Gör ett uttag: "))
            balance = balance - uttagAmount
            try:
                 with open("balance.txt", "w")as balanceFile:
                    balanceFile.write(str(balance))
            except (FileNotFoundError):
                print("Ingen fil")
        except (ValueError):
            print('''Error: invalid number. Vänligen angiv ett giltigt nummer
            ''')

    else:
        print("Fel eller avslut")
        try:
            with open("balance.txt", "w")as balanceFile:
                balanceFile.write(str(balance))
        except (FileNotFoundError):
            print("Ingen fil")