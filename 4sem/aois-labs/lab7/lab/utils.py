def decimal_to_binary_list(decimal_list):
    binary_list = []
    for decimal_number in decimal_list:
        binary_number = bin(decimal_number)[2:].zfill(8)
        binary_list.append(binary_number)
    return binary_list


def decimal_to_binary(decimal_number):
    binary_number = bin(decimal_number)[2:].zfill(8)
    return binary_number


def binary_to_decimal(binary_number):
    decimal_number = int(binary_number, 2)
    return decimal_number
