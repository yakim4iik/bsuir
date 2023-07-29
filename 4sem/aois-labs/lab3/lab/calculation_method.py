from copy import deepcopy


def calculation_method(function, is_dnf=False):
    implicants = deepcopy(function)
    for i, implicant in enumerate(implicants):
        implicants_copy = deepcopy(implicants)
        implicant_to_check = implicants_copy.pop(i)
        variables = set_variables(implicant_to_check, is_dnf)
        implicants_copy = substitute_variables(implicants_copy, variables)
        implicants, implicant_to_check = simplify_implicants(implicants, implicants_copy, implicant_to_check)
    return implicants


def set_variables(implicant, is_dnf):
    variables = {}
    for variable in implicant:
        variables[variable] = is_dnf
    return variables


def substitute_variables(implicants, variables):
    for implicant in implicants:
        for j, variable in enumerate(implicant):
            if variable in variables:
                implicant[j] = variables[variable]
            elif variable[-1] in variables:
                implicant[j] = not variables[variable[-1]]
            elif f"!{variable}" in variables:
                implicant[j] = not variables[f"!{variable}"]
    return implicants


def simplify_implicants(implicants, implicants_copy, implicant_to_check):
    for j in range(len(implicants_copy)):
        for k in range(j + 1, len(implicants_copy)):
            result = set(implicants_copy[j]).symmetric_difference(set(implicants_copy[k]))
            if len(result) == 2 and 1 not in result:
                if implicant_to_check in implicants:
                    implicants.remove(implicant_to_check)
                return simplify_implicants(implicants, implicants_copy[:j] + implicants_copy[j+1:], implicant_to_check)
    return implicants, implicant_to_check
