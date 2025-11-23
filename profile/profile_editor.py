import os, json

from profile.profile_creator import get_profile_name
from utilities.utilities import get_integer_input, get_profile_path, display_profiles


## edit_profile_name
## changes profile name
TODO: "Add more security for input"
def edit_profile_name() -> None:
    display_profiles()

    old_name = input("Enter profile name: ")
    old_path = get_profile_path(old_name)
    new_name = get_profile_name()
    new_path = get_profile_path(new_name)

    if os.path.exists(new_path):
        print(f"FAIL: Profile with name |{new_name}| already exists")
        return

    os.rename(old_path, new_path)

    with(open(new_path, "r")) as file:
        data = json.load(file)

    data["name"] = new_name

    with open(new_path, "w") as file:
        json.dump(data, file)

## profile_remover returns none
## deletes selected profile
def profile_remover() -> None:
    display_profiles()
    profile_to_delete = input("Enter which profile to delete: ")
    try:
        os.remove(get_profile_path(profile_to_delete))
        print(f"SUCCESS: Profile |{profile_to_delete}| deleted")
    except FileNotFoundError:
        print(f"FAIL: Profile |{profile_to_delete}| does not exist")


##
##
def handle_editor_menu_choice(choice: int) -> None:
    match choice:
        case 1:
            edit_profile_name()
        case 2:
            profile_remover()
        case 0:
            return
        case _:
            print("Invalid choice")


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
