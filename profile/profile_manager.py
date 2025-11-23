import json
import os

from profile.profile_creator import create_profile
from profile.profile_editor import editor_menu
from utilities.utilities import get_integer_input, display_profiles, get_profile_path


##
##
def load_profile(path: str) -> dict:
    try:
        with open(path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


##
##
TODO: "add more security for checking profile"


def profile_selector() -> str:
    display_profiles()
    chosen_profile = input("Enter profile name: ").strip()

    path = get_profile_path(chosen_profile)
    if not os.path.exists(path):
        print(f"Profile |{chosen_profile}| does not exist")
        return profile_selector()

    return path


## handle_profile_menu_choice(choice)
##
def handle_profile_menu_choice(choice: int) -> None:
    match choice:
        case 1:
            #create_profile()  # -> profile_creator
            raise NotImplementedError
        case 2:
            profile_selector()
        case 3:
            editor_menu()  # -> profile_editor
        case 0:
            return
        case _:
            print("Invalid choice")


## display_profile_menu()
## display menu for user to choose from
def display_profile_menu() -> None:
    print("====================")
    print("Profile Manager Menu")
    print("====================")
    print("1) Create new profile")
    print("2) Switch profile")
    print("3) Modify profile(s)")
    print("0) Exit")
    choice = get_integer_input("Enter your choice: ")
    handle_profile_menu_choice(choice)


## profile_menu()
## user creates new profile or selects existing profile
def profile_menu() -> None:
    display_profile_menu()
