## edit_profile_name
## changes profile name
from utilities.utilities import get_integer_input


def edit_profile_name() -> None:
    raise NotImplementedError

## profile_remover returns none
## deletes selected profile
def profile_remover() -> None:
    raise NotImplementedError

##
##
def handle_editor_menu_choice(choice: int) -> None:
    match choice:
        case 1:
            edit_profile_name()
        case 2:
            profile_remover()
        case 0:
            exit()

##
##
def display_editor_menu() -> None:
    print("Profile editor menu")
    print("===================")
    print("1) Edit profile name")
    print("2) Delete profile")
    print("0) Exit")
    choice = get_integer_input("Enter your choice: ")
    handle_editor_menu_choice(choice)

## editor_menu
## user chooses to change profile name, delete a profile, or exit the menu
def editor_menu() -> None:
    display_editor_menu()