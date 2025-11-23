import json

from utilities.utilities import get_number_of_profiles, get_profile_path, get_date


## get_profile_name()
## checks if the input profile name is valid
def get_profile_name() -> str:
    while True:
        name = input("Enter profile name: ").strip()
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


## get_user_id
## returns the number of profiles
def get_user_id() -> int:
    return get_number_of_profiles() + 1


## create_profile()
## creates a new profile
def create_profile() -> str:
    profile_name = get_profile_name()

    new_profile = get_profile_path(profile_name)

    profile_id = get_user_id()

    default_profile = \
        {
            "name": profile_name,
            "date_created": get_date(),
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