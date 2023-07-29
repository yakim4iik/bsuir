from lab.constants import *

def conversion(number: int) -> str:
    result = ""
    number = abs(number)
    while number > 0:
        y = str(number % 2)
        result = y + result
        number = int(number / 2)

    add = BIT - 1 - len(result)
    result = add * "0" + result

    return result


def conversion_ten(x: str) -> int:
    total = 0
    step = 0
    for i in range(len(x) - 1, 0, -1):
        if x[i] == "1":
            total += pow(2, step)
        step += 1
    if x[0] == "0":
        return total
    else:
        return int("-" + str(total))


def straight_code(x: int) -> str:
    result = conversion(x)
    if x > 0:
        result = "0" + result
    if x < 0:
        result = "1" + result

    return result


def reverse_code(x: int) -> str:
    result = conversion(x)
    if x > 0:
        result = "0" + result
    if x < 0:
        total = list(result)
        for i in range(0, len(total)):
            if total[i] == "0":
                total[i] = "1"
            else:
                total[i] = "0"
        result = "1" + "".join(total)

    return result


def additional_code(x: int) -> str:
    result = conversion(x)
    if x == 0:
        result = "0" * BIT
    elif x >= 0:
        result = "0" + result
    if x < 0:
        result = reverse_code(x)
        total = list(result)
        for i in range(len(total) - 1, -1, -1):
            if total[i] == "0":
                total[i] = "1"
                break
            if total[i] == "1":
                total[i] = "0"
        result = "".join(total)

    return result
