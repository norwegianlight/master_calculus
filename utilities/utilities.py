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


##
##
def get_number_of_profiles() -> int:
    iterator = 0
    for file_name in os.listdir("./profile"):
        if file_name.endswith(".json"):
            iterator += 1
    return iterator


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
def get_username_from_file(username: str) -> str:
    return username[:-5]


##
##
TODO: ("Figure out how to get username whenever," \
       "maybe not whenever but for starting the program")
def get_username() -> str:
    raise NotImplementedError


## get_profile_path
## returns string
## takes in profile name and returns a created file path
def get_profile_path(chosen_profile: str) -> str:
    return os.path.join('./profile', chosen_profile + '.json')


## display_profiles()
## returns none
## checks the profile directory for files ending in .json
## and display just the file name
def display_profiles() -> None:
    profiles = [p for p in os.listdir('./profile') if p.endswith(".json")]
    for index, filename in enumerate(profiles, start=1):
        print(f"{index}) {get_username_from_file(filename)}")


##
##
def get_date() -> str:
    return datetime.datetime.now().strftime("%b %-d, %Y")