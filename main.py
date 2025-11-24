from profile.profile_creator import create_profile
from profile.profile_manager import profile_selector, load_profile, display_profile_menu
from utilities.utilities import get_integer_input, get_profile_path, check_profiles_exist


##
##
def display_stats(profile: dict) -> None:
    print(f"{profile['name']}'s stats:")
    print(f"Profile created: {profile['date_created']}")
    print(f"Quizzes completed: {profile['quizzes_completed']}")
    print(f"Average correct answers: {profile['avg_correct_answers']}")
    print(f"Average quiz time: {profile['avg_quiz_time']}")
    print(f"Best quiz time: {profile['best_quiz_time']}")


##
##
def handle_main_menu_choice(choice: int, profile: dict) -> None:
    match choice:
        case 1:
            print("meep")
        case 2:
            print("moop")
        case 3:
            display_stats(profile)
        case 4:
            display_profile_menu()
        case 0:
            print("Exiting program, goodbye!")
            exit(0)
        case _:
            print("Invalid choice")


## main_menu
## returns none
## display main menu
def main_menu(profile: dict) -> None:
    print("==========================")
    print(f"Welcome to Master Calculus, " + profile["name"] + "!")
    print("==========================")
    print("1) Practice")
    print("2) Quiz")
    print("3) Statistics")
    print("4) Manage profiles")
    print("0) Exit")
    choice = get_integer_input("Enter your choice: ")
    handle_main_menu_choice(choice, profile)


##
##
def new_user() -> dict:
    username = create_profile()
    return load_profile(get_profile_path(username))


##
##
def startup_wizard() -> dict:
    if not check_profiles_exist():
        return new_user()
    else:
        username = profile_selector()
        return load_profile(username)


## main
## returns none
##
def main() -> None:
    profile = startup_wizard()

    while True:
        main_menu(profile)


if __name__ == '__main__':
    main()
