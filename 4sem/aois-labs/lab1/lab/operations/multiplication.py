from lab.to_binary import *
from lab.operations.addition import *
from lab.constants import *


def multiplication(multiplier1: str, multiplier2: str) -> list[str]:
    result = ZERO
    flag_sign = multiplier1[0] == multiplier2[0]
    if multiplier2[0] == '1':
        multiplier2 = '0' + multiplier2[1:]
    while multiplier2 != ''.join(ZERO):
        additional_multiplier1 = additional_code(conversion_ten(multiplier1))
        additional_result = additional_code(conversion_ten("".join(result)))
        result = addition_additional(additional_multiplier1, additional_result)
        multiplier2 = addition_additional(additional_code(conversion_ten(multiplier2)), ''.join(ONE_ADDITION))
    if flag_sign:
        result = '0' + result[1:]
    else:
        result = '1' + result[1:]
    return result
