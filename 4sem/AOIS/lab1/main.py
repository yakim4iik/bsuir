
from lab.operations.multiplication import *
from lab.operations.division import *
from lab.operations.float_addition import *


def main():

    a = int(input("Введите 1 число: "))
    b = int(input("Введите 2 число: "))

    print(f"X1 = {a}", straight_code(a), reverse_code(a), additional_code(a), sep="\n")
    print(f"-X1 = {-a}", straight_code(-a), reverse_code(-a), additional_code(-a), sep="\n")
    print(f"X2 = {b}", straight_code(b), reverse_code(b), additional_code(b), sep="\n")
    print(f"X2 = {-b}", straight_code(-b), reverse_code(-b), additional_code(-b), sep="\n")

    print("_" * 60)
    print("_" * 26 + "ADDITION" + "_" * 26)
    print("_" * 60)

    print(f"X1 + X2 = {a + b}")
    print(addition_additional(additional_code(a), additional_code(b)))
    print(f"X1 - X2 = {a - b}")
    print(addition_additional(additional_code(a), additional_code(-b)))
    print(f"-X1 + X2 = {-a + b}")
    print(addition_additional(additional_code(-a), additional_code(b)))
    print(f"-X1 - X2 = {-a - b}")
    print(addition_additional(additional_code(-a), additional_code(-b)))

    print("_" * 60)
    print("_" * 23 + "MULTIPLICATION" + "_" * 23)
    print("_" * 60)

    print(f"X1 * X2 = {a * b}")
    print(multiplication(straight_code(a), straight_code(b)))
    print(f"X1 * (-X2) = {a * (-b)}")
    print(multiplication(straight_code(a), straight_code(-b)))
    print(f"(-X1) * X2 = {(-a) * b}")
    print(multiplication(straight_code(-a), straight_code(b)))
    print(f"(-X1) * (-X2) = {(-a) * (-b)}")
    print(multiplication(straight_code(-a), straight_code(-b)))

    print("_" * 60)
    print("_" * 26 + "DIVISION" + "_" * 26)
    print("_" * 60)

    print(f"X1 / X2 = {a / b}")
    print(division(straight_code(a), straight_code(b)))
    print(f"X1 / (-X2) = {a / (-b)}")
    print(division(straight_code(a), straight_code(-b)))
    print(f"(-X1) / X2 = {(-a) / b}")
    print(division(straight_code(-a), straight_code(b)))
    print(f"(-X1) / (-X2) = {(-a) / (-b)}")
    print(division(straight_code(-a), straight_code(-b)))

    print("_" * 60)
    print("_" * 23 + "FLOAT_ADDITION" + "_" * 23)
    print("_" * 60)

    a_float = input("Введите 1 число(формата *.*): ")
    b_float = input("Введите 2 число(формата *.*): ")

    print(float_addition(a_float, b_float))


if __name__ == "__main__":
    main()
