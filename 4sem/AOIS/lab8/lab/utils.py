def print_matrix(matrix):
    for row in matrix:
        for element in row:
            if element:
                print("1", end=' ')
            else:
                print("0", end=' ')
        print()


def print_list(row):
    for i in range(len(row)):
        if row[i]:
            print("1", end=' ')
        else:
            print("0", end=' ')
    print()
    return row
