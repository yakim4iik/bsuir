from typing import *
from lab.constants import *


def check_input(formula: str) -> bool:
    valid_characters = "abc+*-()"
    for i in formula:
        if valid_characters.find(i) == -1:
            return False
    return 'a' in formula and 'b' in formula and 'c' in formula


def create_sknf(table: Dict[int, list], variables: list) -> str:
    sknf = ''
    for i in range(len(table)):
        if table[i][LAST] == 0:
            sknf += '('
            for j in range(len(table[i]) - 1):
                if table[i][j] == 0:
                    sknf += f'{variables[j]}+'
                else:
                    sknf += f'-{variables[j]}+'
            sknf = sknf[:LAST]
            sknf += ')*'
        else:
            continue
    if sknf[LAST] == '*':
        sknf = sknf[:LAST]
    return sknf


def create_sdnf(table: dict[int, list], variables: list) -> str:
    sdnf = ''
    for i in range(len(table)):
        if table[i][LAST] == 1:
            sdnf += '('
            for j in range(len(table[i]) - 1):
                if table[i][j] == 0:
                    sdnf += f'-{variables[j]}*'
                else:
                    sdnf += f'{variables[j]}*'
            sdnf = sdnf[:LAST]
            sdnf += ')+'
        else:
            continue
    if sdnf[LAST] == '+':
        sdnf = sdnf[:LAST]
    return sdnf


def gluing(SNF):
    nf = []
    if len(SNF) == 1:
        return SNF
    for i in range(len(SNF)):  # Run through the SNF in search of implicants
        for j in range(i + 1, len(SNF)):
            summand1 = set(SNF[i])
            summand2 = set(SNF[j])
            implicant = list(summand1 & summand2)
            implicant.sort(key=lambda x: x[-1])
            if len(implicant) == 2:  # If the implicant fits, then add it to NF
                nf.append(implicant)
    return nf


def print_dnf(dnf):
    dnf_output = ""
    for i in dnf:
        dnf_output += f"({'*'.join(i)})+"
    print(f"DNF: {dnf_output[:-1]}")


def print_knf(knf):
    knf_output = ""
    for i in knf:
        knf_output += f"({'+'.join(i)})*"
    print(f"KNF: {knf_output[:-1]}")


def print_mdnf(mdnf):
    mdnf_output = ""
    for i in mdnf:
        mdnf_output += f"({'*'.join(i)})+"
    print(f"MDNF: {mdnf_output[:-1]}")


def print_mknf(mknf):
    mknf_output = ""
    for i in mknf:
        mknf_output += f"({'+'.join(i)})*"
    print(f"MKNF: {mknf_output[:-1]}")
