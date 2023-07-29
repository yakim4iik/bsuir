import re
from prettytable import PrettyTable
from lab5.constants import *


def print_table_one():
    header = ["q4", "q3", "q2", "q1", "v", "h4", "h3", "h2", "h1"]
    x = PrettyTable()
    x.field_names = header

    for row in ALL_TABLE:
        x.add_row(row)

    print(x)


def array_form(snf, flag):
    variables = sorted(set(re.findall(r"[A-Za-z]", snf)))
    if flag == "sdnf":
        snf = snf.split("+")
        sign = "+"
    else:
        snf = snf.split("*")  # changed from empty string to "*"
        sign = "*"
    for i in range(len(snf)):
        interval = []
        for j in range(len(snf[i])):
            if snf[i][j] in variables:
                if snf[i][j - 1] == "!":
                    interval.append(snf[i][j-1: j+1])
                else:
                    interval.append(snf[i][j])
        snf[i] = interval
    return snf, sign


def get_shortened_form(table, form_type=None):
    result = table
    for i in range(len(table[0])):
        glued_table = start_glued(result)
        result = delete_duplicates(glued_table)
        short_t = delete_duplicates(result)
    if form_type == 'sknf':
        return exit(0)
    else:
        return create_short_sdnf_form(short_t)


def start_glued(table):
    short_table = []
    index = []
    for i, vector in enumerate(table):
        is_not_gluing = False
        for j in range(i+1, len(table)):
            false_index = get_gluing_index(vector, table[j])
            if false_index >= 0:
                is_not_gluing = True
                index.append(j)
                new_vector = vector.copy()
                new_vector[false_index] = None
                short_table.append(new_vector)
        if not is_not_gluing and i not in index:
            short_table.append(vector)
    return short_table if short_table else table


def delete_duplicates(table):
    new_table = []
    for vector in table:
        if vector not in new_table:
            new_table.append(vector)
    return new_table


def get_gluing_index(first_vector, second_vector):
    result_vector = []
    for i in range(len(first_vector)):
        result_vector.append(first_vector[i] == second_vector[i])
    if result_vector.count(False) == 1:
        return result_vector.index(False)
    return -1


def create_sdnf_table(table):
    sdnf_table = []
    for i in range(len(table)):
        if table[i][5] == 1:
            sdnf_table.append([table[i][0], table[i][1], table[i][2], table[i][3], table[i][4]])
    return sdnf_table


def create_short_sdnf_form(table):
    short_form = ""
    elements = {'0': 'a', '1': 'b', '2': 'c', '3': 'd', '4': 'v'}
    for i in range(len(table)):
        if short_form:
            short_form += '*'
        short_form += '('
        for j in range(len(table[i])):
            if table[i][j] is not None:
                short_form += '!' + elements[str(j)] if table[i][j] == 0 else elements[str(j)]
        short_form += ')'
    return short_form


def print_tdnf(tdnf):
    tdnf_output = ""
    for i in tdnf:
        tdnf_output += f"({'*'.join(i)})+"
    return f"{tdnf_output[:-1]}"


def create_sdnf(table) -> str:
    sdnf = ''
    for i in range(len(table)):
        if table[i][5] == 1:
            if sdnf:
                sdnf += '+'
            sdnf += '(!a*' if table[i][0] == 0 else '(a*'
            sdnf += '!b*' if table[i][1] == 0 else 'b*'
            sdnf += '!c*' if table[i][2] == 0 else 'c*'
            sdnf += '!d*' if table[i][3] == 0 else 'd*'
            sdnf += '!v)' if table[i][4] == 0 else 'v)'
    return sdnf if sdnf else "Не существует"
