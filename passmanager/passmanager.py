from cryptography.fernet import Fernet

#def write_key():
#    key = Fernet.generate_key()
#    with open ("key.key", "wb") as key_file:
#        key_file.write(key)

def load_key():
    file = open("key.key" , "rb")
    key = file.read()
    file.close()
    return key



while 1 == 1:
    master_pwd = input("Enter the master password or press 'Q' to quit: ").lower()
    if master_pwd == "q":
        quit()

    elif master_pwd == "fret":
        key = load_key() + master_pwd.encode()
        fer = Fernet(key)

        def add():
            acc = input("Account name: ")
            pwd = input("Password: ")
            with open("passwords.txt", "a") as a:
                a.write(acc + "|" + str(fer.encrypt(pwd.encode()).decode()) + "\n")

        def view():
            with open("passwords.txt" , "r") as a:
                for lines in a.readlines():
                    data = lines.rstrip()
                    acc, pwd = data.split("|")
                    print("Account name:",acc," Password:",str(fer.decrypt(pwd.encode()).decode()))

        while 1 == 1:
            choice = input("Enter 'V' to view a password, 'A' to add a password or 'Q' to quit the program: ").casefold()
            if choice == "q":
                quit()
            elif choice == "v":
                view()
            elif choice == "a":
                add()
            else:
                print("Your choice is invalid, please try again")
                continue

    else:
        print("You entered the wrong master password!")
        continue
