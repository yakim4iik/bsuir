from lab.my_task import *
from lab.general import *


def main():
    my_hash_table = HashTable(20)
    task(my_hash_table)
    while 1:
        print("Add - press 1")
        print("Delete - press 2")
        print("Search - press 3")
        print("Print - press 4")

        print("To exit - press 0")
        choose = input("Enter choise: ")
        match choose:
            case "1":
                key = input("Enter key: ")
                data = input("Enter data: ")
                my_hash_table.insert(key, data)
            case "2":
                word = input("Enter key: ")
                my_hash_table.delete(word)
            case "3":
                word = input("Enter key: ")
                print(my_hash_table.find(word))
            case "4":
                my_hash_table.print_table()
            case "0":
                break
            case _:
                print("Invalid input")


if __name__ == '__main__':
    main()
