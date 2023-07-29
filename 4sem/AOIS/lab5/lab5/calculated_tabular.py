def create_table(formula, short_form):
    operator = '+'
    table = {}
    for col in formula:
        table[col] = {}
        col_terms = set(col[1:-1].split(operator))
        for row in short_form:
            row_terms = row[1:-1].split(operator)
            if set(row_terms).issuperset(col_terms) and len(row) > 2:
                table[col][row] = 1
            else:
                table[col][row] = 0
    return table


def get_covered_constituents(formula, short_form, table):
    covered_constituents = []
    for term in formula:
        for row in short_form:
            if table[term][row] == 1 and term not in covered_constituents:
                covered_constituents.append(term)
                break
    return covered_constituents


def get_uncovered_constituents(formula, covered_constituents):
    uncovered_constituents = set(formula) - set(covered_constituents)
    return list(uncovered_constituents)


def get_new_terms(formula, short_form, table, terms):
    for term in formula:
        count_of_one = sum(table[term].values())
        if count_of_one == 1:
            for row in short_form:
                if table[term][row] == 1 and row not in terms:
                    terms.append(row)
    return terms


def get_new_implicates(formula, short_form, table, terms):
    result = []
    uncovered_constituents = get_uncovered_constituents(formula, terms)
    short_form.reverse()
    for term in uncovered_constituents:
        for row in short_form:
            if table[term][row] == 1 and row not in terms:
                result.append(row)
                break
    return result


def deadlock_calculated_tabular(formula_str, short_form_str, sign=None):
    short_form = short_form_str.split(sign)
    formula = formula_str.split(sign)
    if len(short_form) == 1:
        return ''.join(short_form)
    terms = [i for i in short_form if len(i) <= 5]
    table = create_table(formula, short_form)
    covered_constituents = get_covered_constituents(formula, short_form, table)
    terms = get_new_terms(formula, short_form, table, terms + covered_constituents)
    new_implicates = get_new_implicates(formula, short_form, table, terms)
    terms = get_new_terms(formula, short_form, table, terms + new_implicates)
    return sign.join(terms)
