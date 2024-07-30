# Authors: Bruce Truong, Olivia Sausville
# Date Created: July 29th, 2024
# Description:  This program would automate the score calculation for the
#               board game Targi and record the results

# Imports
from welcome_message import welcome
import os

def calculate_score():
    # TODO: Implement the score calculation logic here
    pass

def display_score_history():
    # TODO: This will save scores to a file
    pass

def display_menu(menu_list):
    print("Please select from the following or press any other key to exit:\n")
    for i, menu_option in enumerate(menu_list):
        print(f"{i+1}. {menu_option}")

def get_user_choice(menu_list):
    choice = input(f"\nEnter your choice (1-{len(menu_list)}): ")
    return choice

def main():
    os.system('cls' if os.name == 'nt' else 'clear') # clear screen depending on OS
    welcome()

    menu_list = ["Calculate Score",
                 "Display Score History",]

    while True:
        display_menu(menu_list)
        choice = get_user_choice(menu_list)

        match choice:
            case "1":
                calculate_score()
            case "2":
                display_score_history()
            case _:
                print("\nExiting...")
                break

if __name__ == "__main__":
    main()
