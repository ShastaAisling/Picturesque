# This module holds all of the authentication helpers and main loop for log in

def reset_password(auth):
    while (True):
        try:
            email = input("Enter email: ")
            auth.send_password_reset_email(email)
            return
        except:
            print("This email may not be associated with an account. Try again.")


def create_account(auth):
    while (True):
        email = input("Enter email: ")
        password = input("Enter password: ")
        try:
            user = auth.create_user_with_email_and_password(email, password)
            return user
        except:
            print("An error occured. Please try again.")

def authenticate(auth):
    attempt = 0
    while attempt < 3:
        try:
            email = input("Enter email: ")
            password = input("Enter password: ")
            user = auth.sign_in_with_email_and_password(email, password)
            return user
        except:
            print("Incorrect email/password. Please try again.")
            attempt += 1
    raise Exception("Out of login attempts. Please restart application.")

def auth_loop(auth):
    # Ask to create new account, login, or reset password
    print("Options: 1 - Login, 2 - Sign up, 3 - Reset Password")
    answer = input("Enter one of the options above: ")
    user = None
    if int(answer) == 1:
        # Log the user in
        try:
            user = authenticate(auth)
            print("Login successful!")
            return user
        except:
            raise SystemExit
    elif int(answer) == 2:
        user = create_account(auth)
        auth.send_email_verification(user['idToken'])
        print("Email verification set. Please restart application to log in.")
        raise SystemExit

    elif int(answer) == 3:
        reset_password(auth)
        print("Password reset email has been sent. Please restart the application to log in.")
        raise SystemExit

