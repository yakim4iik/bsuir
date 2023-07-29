from typing import List
from lab.constants import *


def addition_straight(a: str, b: str) -> str:
    term1, term2 = list(a), list(b)
    result = interval(term1, term2)
    return "".join(result)


def addition_reverse(a: str, b: str) -> str:
    term1, term2 = list(a), list(b)
    addition_result = interval(term1, term2)
    result = addition_result
    if len(addition_result) > BIT:
        result.pop(0)
        result = interval(addition_result, ONE)
    if result[0] == "1":
        for i in range(1, len(result)):
            if result[i] == "0":
                result[i] = "1"
            else:
                result[i] = "0"
    return "".join(result)


def addition_additional(a: str, b: str) -> str:
    term1, term2 = list(a), list(b)
    addition_result = interval(term1, term2)
    if len(addition_result) > BIT:
        addition_result.pop(0)
    """  if addition_result[0] == "1":
        for i in range(1, len(addition_result)):
            if addition_result[i] == "0":
                addition_result[i] = "1"
            else:
                addition_result[i] = "0"
        for i in range(len(addition_result) - 1, -1, -1):
            if addition_result[i] == "0":
                addition_result[i] = "1"
                break
            if addition_result[i] == "1":
                addition_result[i] = "0"""
    return "".join(addition_result)


def interval(first_el: List[str], second_el: List[str]) -> List[str]:
    result = list()
    count = 0
    for i in range(len(first_el) - 1, -1, -1):
        if int(first_el[i]) + int(second_el[i]) + count == 3:
            result.insert(0, "1")
            count = 1
        elif int(first_el[i]) + int(second_el[i]) + count == 2:
            result.insert(0, "0")
            count = 1
        elif int(first_el[i]) + int(second_el[i]) + count == 1:
            result.insert(0, "1")
            count = 0
        else:
            result.insert(0, "0")
            count = 0
    if count == 1:
        result.insert(0, "1")
    return result
