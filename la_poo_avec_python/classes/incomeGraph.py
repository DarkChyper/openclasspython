from classes.baseGraph import *
from collections import defaultdict  # for income graph


class IncomeGraph(BaseGraph):
    # Inheritance, yay!

    def __init__(self):
        # Call base constructor
        super(IncomeGraph, self).__init__()

        self.title = "Older people have more money"
        self.x_label = "age"
        self.y_label = "income"

    def xy_values(self, zones):
        income_by_age = defaultdict(float)
        population_by_age = defaultdict(int)
        for zone in zones:
            for inhabitant in zone.inhabitants:
                income_by_age[inhabitant.age] += inhabitant.income
                population_by_age[inhabitant.age] += 1

        x_values = range(0, 100)
        # list comprehension (listcomps)
        y_values = [income_by_age[age] / (population_by_age[age] or 1) for age in range(0, 100)]
        return x_values, y_values

