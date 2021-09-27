import sys
import logging
from registration import Register
from login import LoginToAccount

logging.basicConfig(level=logging.INFO,
                    filename='selecting_units.log',
                    filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')


class MainMenu:
    """Display a menu and respond to choices when run."""

    def __init__(self):
        self.choices = {
            "1": self.registration,
            "2": self.login_to_account,
            "3": self.quit
        }

    @staticmethod
    def display_menu():
        print("""
*Menu*

1. Registration
2. Login to account
3. Quit
        """)

    def run_main(self):
        """Display the menu and respond to choices."""
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print(f'{choice}is not a valid choice!')
                logging.warning("invalid choice")

    def registration(self):
        Register()

    def login_to_account(self):
        LoginToAccount()

    def quit(self):
        sys.exit(0)


MainMenu().run_main()
