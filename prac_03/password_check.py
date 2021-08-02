def main():
    password = get_password()
    password_to_star(password)

def get_password():
    user_passwrod = input("Enter your password: ")
    return user_passwrod

def password_to_star(password):
    print("Your password:", "*" * len(password))

main()
