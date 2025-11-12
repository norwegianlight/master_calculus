import datetime
import json

from utilities.utilities import get_number_of_profiles


## get_profile_name()
## checks if the input profile name is valid
def get_profile_name() -> str:
    name = ""
    good_name = False

    while not good_name:
        name = input("Enter profile name: ")

        if not name:
            print("Profile name can not be empty")
        elif not name.isalpha():
            print("Profile name can only contain alphabetical characters")
        elif len(name) > 10:
            print("Profile name can only contain 10 characters max")
        else:
            good_name = True

    return name


##
##
def get_user_id() -> int:
    return get_number_of_profiles() + 1


## create_profile()
## creates a new profile
def create_profile() -> None:
    profile_name = get_profile_name()

    new_profile = str(f"profile/{profile_name}.json")

    new_profile_id = get_user_id()

    default_profile =  {
        "name": profile_name,
        "date created": datetime.datetime.now().strftime("%b %-d, %Y"),
        "user_id": new_profile_id,
        "avg_correct": -1.0,
        "avg_time_quiz": -1.0,
        "best_time_quiz": -1.0,
        "quizzes_completed": -1
    }

    try:
        with open(new_profile, "x") as new_file:
            new_file.write(json.dumps(default_profile))
        print(f"Profile |{profile_name}| successfully created")

    except FileExistsError:
        print(f"Profile |{profile_name}| already exists")