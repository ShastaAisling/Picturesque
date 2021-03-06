# This module holds all of the authentication helpers and main loop for log in

def reset_password(auth):
    while True:
        try:
            email = input("Enter email: ")
            auth.send_password_reset_email(email)
            return
        except:
            print("This email may not be associated with an account. Try again.")


def create_account(auth):
    while True:
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
    raise PermissionError


def auth_loop(auth):
    while True:
        # Ask to create new account, login, or reset password
        print("Options: 1 - Login, 2 - Sign up, 3 - Reset Password, 4 - Quit")
        answer = input("Enter one of the options above: ")
        int_answer = None

        try:
            int_answer = int(answer)
        except ValueError:
            print("Only numeric input is allowed.")

        if int_answer == 1:
            # Log the user in
            try:
                user = authenticate(auth)
                print("Login successful!")
                return user
            except PermissionError:
                print("Out of login attempts. Please restart application.")
                raise SystemExit
        elif int_answer == 2:
            user = create_account(auth)
            auth.send_email_verification(user['idToken'])
            print("Email verification set. Please restart application to log in.")
            raise SystemExit
        elif int_answer == 3:
            reset_password(auth)
            print("Password reset email has been sent. Please restart the application to log in.")
            raise SystemExit
        elif int_answer == 4:
            print("Exiting.")
            raise SystemExit
        else:
            print("Please enter one of the options (1, 2, 3, or 4).")
