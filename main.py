"""Automates score calculation for the board game Targi and records the results.

Authors: Bruce Truong, Olivia Sausville
Date Created: July 29th, 2024
"""

# Imports
from __future__ import annotations

import os

from welcome_message import welcome


def calculate_score() -> None:
    """Calculate the score for the given player Class."""
    print("Calculating score...")  # noqa: T201
    # Implementation here
    print("Score calculation completed.") # noqa: T201


def display_score_history() -> None:
    """Display the saved score history."""
    print("Displaying score history...")  # noqa: T201
    # Implementation here
    print("Score history displayed.")  # noqa: T201


def display_menu(menu_list: list[str]) -> None:
    """Display the menu."""
    print("Please select from the following or press any other key to exit:\n")  # noqa: T201
    for i, menu_option in enumerate(menu_list):
        print(f"{i+1}. {menu_option}")  # noqa: T201


def get_user_choice(menu_list: list[str]) -> str:
    """Menu choice."""
    return input(f"\nEnter your choice (1-{len(menu_list)}): ")


def main() -> None:
    """Begin the Calculator."""
    os.system("cls" if os.name == "nt" else "clear")  # OS-based clear # noqa: S605
    welcome()

    menu_list = ["Calculate Score",
                 "Display Score History"]

    while True:
        display_menu(menu_list)
        choice = get_user_choice(menu_list)

        if choice:
            match choice:
                case "1":
                    calculate_score()
                case "2":
                    display_score_history()
                case _:
                    print("\nExiting...")  # noqa: T201
                    break
        else:
            print("\nInvalid choice. Please try again.")  # noqa: T201

if __name__ == "__main__":
    main()
