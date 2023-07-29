from lab.match_search import *
from lab.nearest_search import *
from lab.utils import *


def main():
    array_of_digits = [104, 22, 68, 108, 139, 212, 170, 7, 16, 64]
    print(array_of_digits)
    array_of_bi_digits = decimal_to_binary_list(array_of_digits)
    print(array_of_bi_digits)
    while 1:
        print("Match Search - press 1")
        print("Search nearest top (bottom) meaning - press 2")

        print("To exit - press 0")
        choose = input("Enter choise: ")
        match choose:
            case "1":
                word_to_search = decimal_to_binary(int(input("Enter the number: ")))
                print(f"You entered: {binary_to_decimal(word_to_search)}({word_to_search})")
                search_by_match(array_of_bi_digits, word_to_search)
            case "2":
                word_to_search = decimal_to_binary(int(input("Enter the number: ")))
                nearest_search(array_of_bi_digits, word_to_search)
            case "0":
                break
            case _:
                print("Invalid input")


if __name__ == '__main__':
    main()
