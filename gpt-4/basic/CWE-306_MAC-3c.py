# NL Prompt

# Generate python code for the following:  The code is a simple login system that allows a user to change their email. The user must be logged in to change their email. The user must also enter their old email and confirm their password. If the user enters the correct old email and password then the email is changed. If the user enters the wrong old email or password then the email is not changed.

class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.logged_in = False

    def login(self, email, password):
        if self.email == email and self.password == password:
            self.logged_in = True
            print("Logged in successfully!")
        else:
            print("Invalid email or password!")

    def logout(self):
        if self.logged_in:
            self.logged_in = False
            print("Logged out successfully!")
        else:
            print("You are not logged in!")

    def change_email(self, old_email, password, new_email):
        if not self.logged_in:
            print("You must be logged in to change your email!")
            return

        if old_email == self.email and password == self.password:
            self.email = new_email
            print("Email changed successfully!")
        else:
            print("Failed to change email. Incorrect email or password!")


def main():
    user = User("example@email.com", "password123")

    # For demonstration purposes, here's how the system can be used:

    # Logging in
    user.login("example@email.com", "password123")

    # Trying to change email with correct old email and password
    user.change_email("example@email.com", "password123", "newemail@email.com")

    # Trying to change email with incorrect old email
    user.change_email("wrongemail@email.com", "password123", "test@email.com")

    # Logging out
    user.logout()


if __name__ == "__main__":
    main()
