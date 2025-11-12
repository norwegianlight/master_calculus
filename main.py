import string

from practice.practice_module import practice_menu
from profile.profile_creator import create_profile
from profile.profile_manager import profile_menu, profile_selector
from utilities.utilities import get_integer_input, check_profiles_exist, get_user_name


##################################################################

##
##
def handle_main_menu_choice(choice: int) -> None:
    match choice:
        case 1:
            #practice_menu()
            print("Under construction")
            main_menu()
        case 2:
            #quiz_menu()
            print("Under construction")
            main_menu()
        case 3:
            #user_statistics_menu()
            print("Under construction")
            main_menu()
        case 4:
            profile_menu()
        case 0:
            print("Exiting, goodbye!")
            exit()
        case _:
            print("Invalid choice")


## main_menu()
## prints out
def main_menu() -> None:
    name = get_user_name()
    print("==========================")
    print(f"Welcome to Master Calculus, {name}")
    print("==========================")
    #print("1) Learn")
    print("1) Practice")
    print("2) Quiz")
    print("3) Stats")
    print("4) Manage profiles")
    print("0) Exit")
    choice = get_integer_input("Enter your choice: ")
    handle_main_menu_choice(choice)


## main()
## goes to the profile selector or profile creator if there are no profiles found
def main() -> None:
    file_exist = check_profiles_exist()

    if file_exist:
        profile_selector()
    else:
        create_profile()

    main_menu()


if __name__ == '__main__':
    main()