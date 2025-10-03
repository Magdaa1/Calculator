import math

# Assuming the BasicCalculator class is in a separate file
from BasicCalculator import BasicCalculator


class AdvancedCalculator(BasicCalculator):
    """Derived class adding advanced operations."""

    # You don't need __init__, it inherits the self.memory state from the parent

    def power(self, base, exponent):
        return base ** exponent

    def square_root(self, number):
        if number >= 0:
            # You can also use ** 0.5 in Python
            return math.sqrt(number)
        else:
            return "ERROR: Square root of a negative number"

    def logarithm(self, number, base):
        if number > 0 and base > 0 and base != 1:
            return math.log(number, base)
        else:
            return "ERROR: Invalid logarithm arguments"