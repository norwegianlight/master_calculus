import os

from profile.profile_creator import create_profile
from profile.profile_editor import editor_menu
from utilities.utilities import get_integer_input


##
##
def handle_profile_selector_choice(input: int) -> None:
    ...

##
##
def profile_selector() -> None:
    iterator = 1
    for file_name in os.listdir("./profile"):
        if file_name.endswith(".json"):
            print(f"{iterator}) {file_name}")
            iterator += 1
    choice = get_integer_input("Enter your choice: ")
    handle_profile_selector_choice(choice)



## handle_profile_menu_choice(choice)
##
def handle_profile_menu_choice(choice: int) -> None:
    match choice:
        case 1:
            create_profile() #profile_creator
        case 2:
            profile_selector()
        case 3:
            editor_menu() #profile_editor
        case 0:
            exit()
        case _:
            print("Invalid choice")


## display_profile_menu()
## display menu for user to choose from
def display_profile_menu() -> None:
    print("====================")
    print("Profile Manager Menu")
    print("====================")
    print("1) Create new profile")
    print("2) Choose existing profile")
    print("3) Modify profile(s)")
    print("0) Exit")
    choice = get_integer_input("Enter your choice: ")
    handle_profile_menu_choice(choice)


## profile_menu()
## user creates new profile or selects existing profile
def profile_menu() -> None:
    display_profile_menu()
