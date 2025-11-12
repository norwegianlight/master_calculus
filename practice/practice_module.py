from utilities.utilities import get_integer_input


##
##
def handle_practice_menu_choice(choice: int) -> None:
    raise NotImplementedError


##
##
def display_practice_menu() -> None:
    print(f"Practice Module")
    print(f"===============")
    print(f"1) Derivatives")
    print(f"2) Integrals")
    print(f"3) Limits")
    print(f"4) Exit")
    choice = get_integer_input("Enter your choice: ")
    handle_practice_menu_choice(choice)


##
##
def practice_menu() -> None:
    display_practice_menu()

