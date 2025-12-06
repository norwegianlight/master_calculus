import os.path


def get_integer_input(prompt: str) -> int:
    try:
        input_integer = int(input(prompt))
        return input_integer
    except ValueError:
        print("Please enter an integer")
        return get_integer_input(prompt)


def get_profile_path(chosen_profile: str) -> str:
    if chosen_profile.endswith(".json"):
        return os.path.join('./profile', chosen_profile)
    else:
        return os.path.join('./profile', chosen_profile + '.json')


def check_profiles_exist() -> bool:
    files_exist: bool = False
    for file_name in os.listdir("./profile"):
        if file_name.endswith(".json"):
            files_exist = True
    return files_exist