import json
import os

from profile.profile_creator import create_profile, get_profile_name
from utilities.utilities import get_integer_input, get_profile_path, display_profiles, get_profile_list


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
def profile_selector() -> str:
    profile_list = get_profile_list()
    display_profiles(profile_list)
    choice = get_integer_input("Choose profile: ")
    selected_profile = profile_list[choice - 1]

    path = get_profile_path(selected_profile)
    if not os.path.exists(path):
        print(f"Profile |{selected_profile}| does not exist")
        return profile_selector()

    return path


## edit_profile_name
## changes profile name
def rename_profile() -> None:
    profile_list = get_profile_list()
    display_profiles(profile_list)

    choice = get_integer_input("Which profile to rename: ")
    profile_to_rename = profile_list[choice - 1]
    old_path = get_profile_path(profile_to_rename)

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
    profile_list = get_profile_list()
    display_profiles(profile_list)

    choice = get_integer_input("Which profile to delete: ")
    profile_to_delete = profile_list[choice - 1]

    try:
        os.remove(get_profile_path(profile_to_delete))
        print(f"SUCCESS: Profile |{profile_to_delete}| deleted")
    except FileNotFoundError:
        print(f"FAIL: Profile |{profile_to_delete}| does not exist")


## handle_profile_menu_choice(choice)
##
def handle_profile_menu_choice(choice: int) -> None:
    match choice:
        case 1:
            create_profile()
        case 2:
            profile_selector()
        case 3:
            rename_profile()
        case 4:
            profile_remover()
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
    print("3) Rename a profile")
    print("4) Delete a profile")
    print("0) Exit")

    choice = get_integer_input("Enter your choice: ")
    handle_profile_menu_choice(choice)


## profile_menu()
## user creates new profile or selects existing profile
def profile_menu() -> None:
    display_profile_menu()
