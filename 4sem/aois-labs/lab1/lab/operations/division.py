from lab.to_binary import *
from lab.operations.addition import *
from lab.constants import *


def division(numerator: str, denominator: str) -> str:
    integer = "".join(ZERO)
    flag_sign = numerator[0] != denominator[0]
    numerator = '0' + numerator[1:]
    denominator = '1' + denominator[1:]
    additional_numerator = additional_code(conversion_ten(numerator))
    additional_denominator = additional_code(conversion_ten(denominator))
    check_type_fraction = addition_additional(additional_numerator, additional_denominator)
    if check_type_fraction[0] == '0':
        while numerator[0] != '1':
            numerator = addition_additional(numerator, additional_code(conversion_ten(denominator)))
            if numerator[0] != '1':
                integer = addition_additional("".join(integer), "".join(ONE))
    if list(integer) == ZERO:
        return integer
    if flag_sign:
        return '1' + integer[1:]
    else:
        return integer
