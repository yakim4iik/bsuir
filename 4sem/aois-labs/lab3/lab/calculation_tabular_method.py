def calculation_tabular_method(prime_implicants, subsumed_implicants, key=None):

    table = create_table(prime_implicants, subsumed_implicants)
    filled_columns = [False] * len(table[0])
    minimized_implicants = get_minimized_implicants(prime_implicants, table, filled_columns)

    print_table(prime_implicants, subsumed_implicants, table, key)

    if len(subsumed_implicants) and len(prime_implicants) == 1:
        return subsumed_implicants
    return minimized_implicants


def create_table(prime_implicants, subsumed_implicants):
    table = []
    for implicant in prime_implicants:
        table.append([len(set(implicant) & set(pi)) == 2 for pi in subsumed_implicants])
    return table


def get_minimized_implicants(prime_implicants, table, filled_columns):
    minimized_implicants = []
    for i in range(len(table[0])):
        column = [row[i] for row in table]
        if column.count(True) == 1:
            implicant = prime_implicants[column.index(True)]
            if implicant not in minimized_implicants:
                minimized_implicants.append(implicant)
            filled_columns = [f or t for f, t in zip(filled_columns, table[column.index(True)])]
    return minimized_implicants


def print_table(prime_implicants, subsumed_implicants, table, key):
    implicant_width = max(len(' '.join(implicant)) for implicant in prime_implicants)
    header_width = 12 if key == "sdnf" else 11
    column_width = max(header_width, implicant_width + 2)
    print(' ' * column_width, end='')
    sign = "*" if key == "sdnf" else "+"
    for implicant in subsumed_implicants:
        print(f"| {sign.join(implicant).ljust(column_width - 1)} ", end='')
    print()
    for index, row in enumerate(table):
        print(f" {sign.join(prime_implicants[index]).ljust(column_width)} ", end='')
        for column in row:
            if column:
                print(f"| {'x'.center(column_width - 2)} ", end='')
            else:
                print(f"| {' '.center(column_width - 2)} ", end='')
        print("|")
