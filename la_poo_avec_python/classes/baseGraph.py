import matplotlib as mil  # pour compatibilité mac et linux
mil.use('TkAgg')
import matplotlib.pyplot as plt


# () ne se fait pas trop.
# Ceci est un mixin ?
class BaseGraph:

    def __init__(self):
        self.show_grid = True

        self.title = "Your graph title"
        self.x_label = "X-axis label"
        self.y_label = "X-axis label"

    def show(self, zones):
        x_values, y_values = self.xy_values(zones)
        self.plot(x_values, y_values)

        plt.xlabel(self.x_label)
        plt.ylabel(self.y_label)
        plt.title(self.title)
        plt.grid(self.show_grid)
        plt.show()

    def plot(self, x_values, y_values):
        """Override this method to create different kinds of graphs, such as histograms"""
        # http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.plot
        plt.plot(x_values, y_values, '.')

    def xy_values(self, zones):
        """
        Returns:
            x_values
            y_values
        """
        # You should implement this method in your children classes
        raise NotImplementedError

