from lab.operations.addition import *
from lab.to_binary import *


def float_to_bi(num: str) -> tuple:
    integer, float1 = num.split('.')
    fraction = abs(float(num) - int(integer))
    result = ''
    integer = straight_code(int(integer))
    integer = integer[integer.find('1') - 1:]
    index = -1
    while fraction > 0:
        if fraction - pow(2, index) >= 0:
            result += '1'
            fraction -= pow(2, index)
        else:
            result += '0'
        index -= 1

    return integer, result


def float_addition(number1, number2) -> str:
    number1_copy, number2_copy = number1, number2
    num1_int, num1_fl = float_to_bi(number1)
    num2_int, num2_fl = float_to_bi(number2)
    max_fl, max_int = max(len(num1_fl), len(num2_fl)), max(len(num1_int), len(num2_int))
    num1_fl, num2_fl = num1_fl + (max_fl - len(num1_fl)) * '0', num2_fl + (max_fl - len(num2_fl)) * '0'
    num1_int, num2_int = (max_int - len(num1_int)) * '0' + num1_int, (max_int - len(num2_int)) * '0' + num2_int
    number1, number2 = num1_int + num1_fl, num2_int + num2_fl
    result = addition_additional(additional_code(conversion_ten(number1)), additional_code(conversion_ten(number2)))
    answer = ''.join(result[:-max_fl]) + ',' + ''.join(result[-max_fl:])
    index = conversion(max_fl)
    if float(number1) + float(number2) > 0:
        print(f'{result[0]}.{result[result.find("1", 1):]}*2^1.{index[index.find("1"):]}')
        return f'{number1_copy} + {number2_copy} = {bi_to_float(answer)} = {answer[0]}.{answer[answer.find("1", 1):]}'
    else:
        print(f'{result[0]}.{result[result.find("1", 1):]}*2^1.{index[index.find("1"):]}')
        return f'{number1_copy} + {number2_copy} = {bi_to_float(answer)} = {answer[0]}.{answer[answer.find("1", 1):]}'


def bi_to_float(num: str) -> float:
    integer, float1 = num.split(',')
    integer = conversion_ten(integer)
    total = integer
    index = -1
    for i in range(0, len(float1)):
        if float1[i] == "1":
            total += pow(2, index)
        index -= 1
    return total
