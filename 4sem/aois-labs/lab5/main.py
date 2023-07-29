from lab5.calculated_tabular import *
from lab5.utils import *


def main():

    table_q1 = create_sdnf_table(H1)
    short_form_y1, sign_y1 = array_form(get_shortened_form(table_q1), 'sdnf')
    table_q2 = create_sdnf_table(H2)
    short_form_y2, sign_y2 = array_form(get_shortened_form(table_q2), 'sdnf')
    table_q3 = create_sdnf_table(H3)
    short_form_y3, sign_y3 = array_form(get_shortened_form(table_q3), 'sdnf')
    table_q4 = create_sdnf_table(H4)
    short_form_y4, sign_y4 = array_form(get_shortened_form(table_q4), 'sdnf')
    print(LINE)
    print("H1 SDNF:", create_sdnf(H1))
    print("H2 SDNF:", create_sdnf(H2))
    print("H3 SDNF:", create_sdnf(H3))
    print("H4 SDNF:", create_sdnf(H4))
    print(LINE)
    print("H1 min:", deadlock_calculated_tabular(create_sdnf(H1), print_tdnf(short_form_y1), sign_y1))
    print("H2 min:", deadlock_calculated_tabular(create_sdnf(H2), print_tdnf(short_form_y2), sign_y2))
    print("H3 min:", deadlock_calculated_tabular(create_sdnf(H3), print_tdnf(short_form_y3), sign_y3))
    print("H4 min:", deadlock_calculated_tabular(create_sdnf(H4), print_tdnf(short_form_y4), sign_y4))
    print(LINE)


if __name__ == '__main__':
    main()
