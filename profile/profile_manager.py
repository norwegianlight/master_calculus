import json, os, datetime

from utilities.utilities import get_integer_input, get_profile_path, check_profiles_exist


def get_profile_list() -> list:
    profiles = []
    for file_name in os.listdir("./profile"):
        if file_name.endswith(".json"):
            profiles.append(file_name)
    return profiles


def display_profiles(profile_list: list) -> None:
    for index, profile in enumerate(profile_list):
        print(f"{index+1}) {profile[:-5]}")


def load_profile(path: str) -> dict:
    try:
        with open(path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def get_profile_name() -> str:
    while True:
        name: str = input("Enter profile name: ").strip()
        if not name:
            print("Profile name can not be empty, try again")
        elif not name.isalpha():
            print("Profile name can only contain alphabetical characters, try again")
        elif len(name) > 10:
            print("Profile name can only contain 10 characters max, try again")
        elif name.lower() == "default":
            print("Profile name cannot be 'default', try again")
        else:
            return name


def get_number_of_profiles() -> int:
    iterator = 0
    for file_name in os.listdir("./profile"):
        if file_name.endswith(".json"):
            iterator += 1
    return iterator


def create_profile() -> str:
    profile_name: str = get_profile_name()

    new_profile: str = get_profile_path(profile_name)

    profile_id: int = get_number_of_profiles() + 1

    default_profile = \
        {
            "name": profile_name,
            "date_created": datetime.datetime.now().strftime("%b %-d, %Y"),
            "user_id": profile_id,
            "avg_correct_answers": -1.0,
            "avg_quiz_time": -1.0,
            "best_quiz_time": -1.0,
            "quizzes_completed": -1
        }

    try:
        with open(new_profile, "x") as new_file:
            new_file.write(json.dumps(default_profile))
        print(f"SUCCESS: profile |{profile_name}| has been created")

    except FileExistsError:
        print(f"FAIL: profile |{profile_name}| already exists")

    return profile_name


def profile_selector() -> str:
    profile_list: list = get_profile_list()
    display_profiles(profile_list)
    print("0) Create new profile")

    choice: int = get_integer_input("Choose profile: ")

    if choice == 0:
        path = get_profile_path(create_profile())
        return path

    else:
        selected_profile = profile_list[choice - 1]
        path = get_profile_path(selected_profile)
        if not os.path.exists(path):
            print(f"Profile |{selected_profile}| does not exist")
            return profile_selector()
        return path


def rename_profile() -> None:
    profile_list: list = get_profile_list()
    display_profiles(profile_list)

    choice: int = get_integer_input("Which profile to rename: ")
    profile_to_rename = profile_list[choice - 1]
    old_path = get_profile_path(profile_to_rename)

    new_name: str = get_profile_name()
    new_path: str = get_profile_path(new_name)

    if os.path.exists(new_path):
        print(f"FAIL: Profile with name |{new_name}| already exists")
        return

    os.rename(old_path, new_path)

    with(open(new_path, "r")) as file:
        data = json.load(file)

    data["name"] = new_name

    with open(new_path, "w") as file:
        json.dump(data, file)


TODO: 'Update the user if current profile is deleted'
def profile_remover() -> None:
    profile_list = get_profile_list()
    display_profiles(profile_list)

    choice = get_integer_input("Which profile to delete: ")
    profile_to_delete = profile_list[choice - 1]

    try:
        os.remove(get_profile_path(profile_to_delete))
        print(f"SUCCESS: Profile |{profile_to_delete[:-5]}| deleted")
    except FileNotFoundError:
        print(f"FAIL: Profile |{profile_to_delete[:-5]}| does not exist")

    if not check_profiles_exist():
        profile_selector()


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


def display_profile_menu() -> None:
    print("====================")
    print("Profile Manager Menu")
    print("====================")
    print("Profiles:")
    display_profiles(get_profile_list())
    print("====================")
    print("1) Create new profile")
    print("2) Switch profile")
    print("3) Rename a profile")
    print("4) Delete a profile")
    print("0) Exit")

    choice = get_integer_input("Enter your choice: ")
    handle_profile_menu_choice(choice)


def profile_menu() -> None:
    display_profile_menu()