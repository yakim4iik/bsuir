from lab.constants import *
from typing import List
import re


def reversed_polish_notation(formula: str) -> str:
    result = []
    stack = []
    operation_signs = ["+", "-", "*", "(", ")"]

    for element in formula:
        if element != " ":
            if element == "(":
                stack = [element] + stack
            elif element in operation_signs:
                if not stack:
                    stack = [element]
                else:
                    iconic_element(stack, element, result)
            else:
                result += [element]
    while stack:
        first_el = stack[0]
        result += [first_el]
        stack = stack[1:]
    polish_notation = "".join(result)
    return polish_notation

def iconic_element(stack, element, result):
    if element == ")":
        while True:
            first_el = stack[0]
            stack.pop(0)

            if first_el == "(":
                break
            result += [first_el]
    elif priority_search(stack[0]) < priority_search(element):
        stack.insert(0, element)
    else:
        while True:
            if not stack:
                break
            first_el = stack[0]
            result += [first_el]
            stack.pop(0)
            if priority_search(first_el) == priority_search(element):
                break
        stack.insert(0, element)

def priority_search(value: str) -> int:
    for key, v in PRIORITY.items():
        if value in v:
            return key
    return -1


def true_table(formula: str) -> (dict, List):
    formula = reversed_polish_notation(formula)
    variables = sorted(set(re.findall(r"[A-Za-z]", formula)))
    decor(variables)
    table = {}
    for i in range(pow(2, len(variables))):
        table[i] = list()
    result = ZERO
    for i in range(len(table)):
        table[i].extend(result[-len(variables):])
        table[i].append(find_result((table[i]), formula))
        result = interval(result, ONE)
        for elem in table[i]:
            print(f"  {elem}  |", end="")
        print()
    return table, variables


def find_result(table: List, formula: str) -> int:
    formula = formula.replace("a", str(table[0]))
    formula = formula.replace("b", str(table[1]))
    formula = formula.replace("c", str(table[2]))
    result = []
    for i in formula:
        if i.isdigit():
            result.append(i)
        elif i == '+':
            last_el, pre_last_el = result.pop(), result.pop()
            if int(last_el) or int(pre_last_el):
                result.append(1)
            else:
                result.append(0)
        elif i == '*':
            last_el, pre_last_el = result.pop(), result.pop()
            if int(last_el) and int(pre_last_el):
                result.append(1)
            else:
                result.append(0)
        elif i == '-':
            last_el = result.pop()
            if int(last_el):
                result.append(0)
            else:
                result.append(1)
    return result.pop()


def interval(first_el: List[int], second_el: List[int]) -> List[int]:
    result = list()
    count = 0
    for i in range(len(first_el) - 1, -1, -1):
        if int(first_el[i]) + int(second_el[i]) + count == 3:
            result.insert(0, 1)
            count = 1
        elif int(first_el[i]) + int(second_el[i]) + count == 2:
            result.insert(0, 0)
            count = 1
        elif int(first_el[i]) + int(second_el[i]) + count == 1:
            result.insert(0, 1)
            count = 0
        else:
            result.insert(0, 0)
            count = 0
    if count == 1:
        result.insert(0, 1)
    return result


def decor(variables: List):
    header = [""] * 2
    for key in variables:
        header[0] += "-" * 5 + "+"
        header[1] += f"  {key}  |"
    header[0] += "-" * 6
    header[1] += " Res |"
    print("\n".join(header + header[0:1]))
