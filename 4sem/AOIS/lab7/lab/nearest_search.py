from lab.utils import *


def comparison(argument, word, i):
    result = {}
    previous_result = {}
    if i == 0:
        previous_result["g"] = False
        previous_result["l"] = False
    else:
        previous_result = comparison(argument, word, i - 1)
    if previous_result["g"] or (argument[i] == "0" and word[i] == "1" and not previous_result["l"]):
        result["g"] = True
    else:
        result["g"] = False
    if previous_result["l"] or (argument[i] == "1" and word[i] == "0" and not previous_result["g"]):
        result["l"] = True
    else:
        result["l"] = False
    return result


def find_min_max(arr, flag):
    if flag == "min":
        if len(arr) != 0:
            min_val = arr[0]
            for i in range(1, len(arr)):
                comparison_result = comparison(min_val, arr[i], len(arr[i]) - 1)
                if comparison_result["l"]:
                    min_val = arr[i]
            return min_val
        else:
            return None
    else:
        if len(arr) != 0:
            max_val = arr[0]
            for i in range(1, len(arr)):
                comparison_result = comparison(max_val, arr[i], len(arr[i]) - 1)
                if comparison_result["g"]:
                    max_val = arr[i]
            return max_val
        else:
            return None


def nearest_search(data, digit_to_search):
    higher = []
    lower = []
    for index, i in enumerate(data):
        temp = comparison(digit_to_search, i, len(i) - 1)
        if temp["g"]:
            higher.append(i)
        elif temp["l"]:
            lower.append(i)
        else:
            return print(i)
    higher_min, lower_max = find_min_max(higher, 'min'), find_min_max(lower, 'max')
    if higher_min is None:
        print(f"Nearest top: -")
        print(f"Nearest bottom: {binary_to_decimal(find_min_max(lower, 'max'))}({find_min_max(lower, 'max')})")
    elif lower_max is None:
        print(f"Nearest top: {binary_to_decimal(find_min_max(higher, 'min'))}({find_min_max(higher, 'min')})")
        print(f"Nearest bottom: -")
    else:
        print(f"Nearest top: {binary_to_decimal(find_min_max(higher, 'min'))}({find_min_max(higher, 'min')})")
        print(f"Nearest bottom: {binary_to_decimal(find_min_max(lower, 'max'))}({find_min_max(lower, 'max')})")
