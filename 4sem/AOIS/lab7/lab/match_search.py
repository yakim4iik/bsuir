from lab.nearest_search import *
#Чем ассоциативная память отличается от адрессной

def search_by_match(data, search_arg):
    counters = [0] * len(data)
    for i in range(len(search_arg)):
        for j in range(len(data)):
            if data[j][i] == search_arg[i]:
                counters[j] += 1
    max_index = max(counters)
    same_number = []
    for i in range(len(counters)):
        if counters[i] == max_index:
            same_number.append(data[i])
    return print(f"Result: {binary_to_decimal(find_min_max(same_number, 'max'))}({find_min_max(same_number, 'max')})")

