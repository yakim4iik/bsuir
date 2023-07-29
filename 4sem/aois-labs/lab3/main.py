from lab.utils import *
from lab.true_table import *
from lab.calculation_method import *
from lab.calculation_tabular_method import *
from lab.tabular_method import *


def main():

        formula = input("Введите логическую формулу")
        if not check_input(formula):
            raise Exception('Invalid input!')

        table, variables = true_table(formula)

        print("_" * 60)

        SDNF = create_sdnf(table, variables)
        SDNF = SDNF.replace('-', '!')
        print(SDNF)
        SKNF = create_sknf(table, variables)
        SKNF = SKNF.replace('-', '!')
        print(SKNF)
        SDNF = [i.split("*") for i in SDNF[1:-1].split(")+(")]
        SKNF = [i.split("+") for i in SKNF[1:-1].split(")*(")]

        print("Gluing")
        dnf = gluing(SDNF)
        knf = gluing(SKNF)
        print_dnf(dnf)
        print_knf(knf)

        print("Calculation-tabular method:")
        mdnf = calculation_tabular_method(dnf, SDNF, "sdnf")
        print_mdnf(mdnf)
        mknf = calculation_tabular_method(knf, SKNF, "sknf")
        print_mknf(mknf)

        print("Calculation method:")
        mdnf = calculation_method(dnf, "dnf")
        mknf = calculation_method(knf, "knf")
        print_mdnf(mdnf)
        print_mknf(mknf)

        print("Tabular method:")
        mdnf = tabular_method(SDNF)
        print_mdnf(mdnf)
        mknf = tabular_method(SKNF)
        print_mknf(mknf)


if __name__ == '__main__':
    main()
"""
-((-a+c)*(-(b*c)))
((a+c)*(-(b*c)))
-((-(a+c))*(b+c))
"""