from lab.general import *
from lab.true_table import *


def main():

    print("Введите логическую формулу")
    formula = input("Введите логическую формулу")

    if not check_input(formula):
        raise Exception('Invalid input!')

    table, variables = true_table(formula)

    print("_" * 60)

    print(f'SKNF: {create_sknf(table, variables)}')
    print(f'SDNF: {create_sdnf(table, variables)}')

    print("_" * 60)

    print(f'SKNF in binary form:{binary_num_sknf(table, variables)}')
    print(f'SKNF in decimal form:{decimal_num_sknf(table, variables)}')

    print("_" * 60)

    print(f'SDNF in binary form:{binary_num_sdnf(table, variables)}')
    print(f'SDNF in decimal form:{decimal_num_sdnf(table, variables)}')

    print("_" * 60)
    print(f'INDEX:{index(table)}')


if __name__ == "__main__":
    main()


