from utilities.utilities import get_integer_input


def derivative_practice_module() -> None:
    print("What would you like to practice?")
    print("1) Power rule")
    print("2) Product rule")
    print("3) Chain rule")
    print("4) Quotient rule")
    print("5) All of the above")



def handle_practice_menu_choice(choice: int) -> None:
    match choice:
        case 1:
            derivative_practice_module()


def display_practice_menu() -> None:
    print(f"Practice Module")
    print(f"===============")
    print(f"1) Derivatives")
    print(f"2) Integrals")
    print(f"3) Limits")
    print(f"4) Exit")
    choice = get_integer_input("Enter your choice: ")
    handle_practice_menu_choice(choice)


def practice_menu() -> None:
    display_practice_menu()