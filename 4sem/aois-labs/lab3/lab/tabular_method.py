def tabular_method(function):
    binary_literals_list = convert_to_binary_literals(function)
    karnaugh_map = create_karnaugh_map(binary_literals_list)
    print_karnaugh_map(karnaugh_map)
    minimized_boolean_function = minimize_boolean_function(binary_literals_list, karnaugh_map, function)
    return minimized_boolean_function


def convert_to_binary_literals(function):
    binary_literals_list = []
    for term in function:
        binary_literals_list.append([str(int(not literal.startswith("!"))) for literal in term])
    return binary_literals_list


def create_karnaugh_map(binary_literals_list):
    karnaugh_map = []
    meanings = [["0 0 0", "0 0 1", "0 1 1", "0 1 0"], ["1 0 0", "1 0 1", "1 1 1", "1 1 0"]]
    for meaning in meanings:
        karnaugh_map.append([j.split() in binary_literals_list for j in meaning])
    return karnaugh_map


def print_karnaugh_map(karnaugh_map):
    print(" | 00 | 01 | 11 | 10 ")
    for index, row in enumerate(karnaugh_map):
        print(f" {index} ", end="")
        for item in row:
            print(f"| {int(item)} ", end="")
        print()


def minimize_boolean_function(binary_literals_list, karnaugh_map, function):
    minimized_boolean_function = []
    meanings = [["0 0 0", "0 0 1", "0 1 1", "0 1 0"], ["1 0 0", "1 0 1", "1 1 1", "1 1 0"]]
    if karnaugh_map[0].count(True) % 2 == 1:
        for i in range(len(karnaugh_map[0])):
            verifiable_column = [j[i] for j in karnaugh_map]
            if all(verifiable_column):
                for index, binary_literals in enumerate(binary_literals_list):
                    if binary_literals == meanings[0][i].split():
                        minimized_boolean_function.append(function[index][1:])
    for index, karnaugh_map_string in enumerate(karnaugh_map):
        for iterator in range(len(karnaugh_map_string)):
            for iterator_for_comparison in range(iterator + 1, len(karnaugh_map_string)):
                if karnaugh_map_string[iterator] and karnaugh_map_string[iterator_for_comparison]:
                    check = meanings[index][iterator].split()[:-1]
                    for index_, binary_literals_item in enumerate(binary_literals_list):
                        if binary_literals_item[:-1] == check:
                            minimized_boolean_function.append(function[index_][:1] + function[index_][2:])
                    karnaugh_map_string[iterator] = karnaugh_map_string[iterator_for_comparison] = False
                    break
    return minimized_boolean_function
