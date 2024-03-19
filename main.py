from src.user_input import user_input
from src.converter import persian_number_to_integer

def main():
    text = user_input()
    result = persian_number_to_integer(text)

    print(result)


main()