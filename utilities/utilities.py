import os.path, datetime


##
##
def get_integer_input(prompt: str) -> int:
    try:
        input_integer = int(input(prompt))
        return input_integer
    except ValueError:
        print("Please enter an integer")
        return get_integer_input(prompt)


## check_profiles_exist
## returns bool
##
def check_profiles_exist() -> bool:
    files_exist = False
    for file_name in os.listdir("./profile"):
        if file_name.endswith(".json"):
            files_exist = True
    return files_exist


##
##
def get_profile_list() -> list:
    profiles = []
    for file_name in os.listdir("./profile"):
        if file_name.endswith(".json"):
            profiles.append(file_name)
    return profiles


##
##
def display_profiles(profile_list: list) -> None:
    for index, profile in enumerate(profile_list):
        print(f"{index+1}) {profile[:-5]}")


## get_profile_path
## returns string
## takes in profile name and returns a created file path
def get_profile_path(chosen_profile: str) -> str:
    if chosen_profile.endswith(".json"):
        return os.path.join('./profile', chosen_profile)
    else:
        return os.path.join('./profile', chosen_profile + '.json')


##
##
def get_date() -> str:
    return datetime.datetime.now().strftime("%b %-d, %Y")