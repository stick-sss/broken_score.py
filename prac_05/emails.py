def main():
    dict_email = {}
    email = input("Email: ")
    while email != "":
        username = get_username(email)
        verification = input("Is your name {}? (Y/n) ".format(username)).upper()
        if verification != "Y" and verification != "":
            username = input("Name: ")
        dict_email[email] = username
        email = input("Email: ")
    for email,name in dict_email.items():
        print("{} ({})".format(name,email))

def get_username(email):
    splitemail = email.split("@")
    splitname = splitemail[0].split(".")
    linkname = " ".join(splitname)
    name = linkname.title()
    return name

if __name__ == '__main__':
    main()