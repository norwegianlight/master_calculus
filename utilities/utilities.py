import os

##
##
def check_if_string_length_over_ten(input_string) -> bool:
    if input_string > 10:
        return True
    else:
        return False


##
##
def get_integer_input(prompt):
    try:
        integer = int(input(prompt))
        return integer
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


##
##
def check_profiles_exist() -> bool:
    files_exist = False
    for file_name in os.listdir("./profile"):
        if file_name.endswith(".json"):
            files_exist = True

    return files_exist


##
##
def get_user_name() -> str:
    iterator = 0
    #for file_name in os.listdir("./profile"):

    return "meep"