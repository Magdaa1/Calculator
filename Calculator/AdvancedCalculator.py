import math

from BasicCalculator import BasicCalculator


class AdvancedCalculator(BasicCalculator):
    """Derived class adding advanced operations."""
    def power(self, base, exponent):
        return base ** exponent

    def square_root(self, number):
        if number >= 0:
            return math.sqrt(number)
        else:
            return "ERROR: Square root of a negative number"

    def logarithm(self, number, base):
        if number > 0 and base > 0 and base != 1:
            return math.log(number, base)
        else:
            return "ERROR: Invalid logarithm arguments"

   # pierwiastek n-tego stopania
    def nth_root(self, number, degree):
        #1. Sprawdzenie, czy stopien pierwiastka jest zerem
        if degree == 0:
            return "ERROR: Degree cannot be zero"

        #2. Sprawdzenie pierwiastkow, ktore sa wieksze od 0

        # -> Pierwiastek stopnia n z liczby x
        # jest w rzeczywistości działaniem odwrotnym do potęgowania.
        # Szukamy liczby y, która podniesiona do potęgi n da nam x.
        # pierwiastek 3 stopnia z -8 = -2 poniewaz (-2)^3 = -8
        # To sprawdzenie zapobiega próbie obliczenia w dziedzinie
        # liczb rzeczywistych (której używamy w większości
        # podstawowych programów) wyników takich jak pierwistek 2 stopnia z -4
        # albo pierwiastek 4 stopnia z -16,
        # ktore doprowadzilyby do liczb zespolonych urojonych
        # modulo jest potrzebne dlatego, ze najlatwiej jest sprawdzic czy jest parzysta czy nie
        # parzytsa, gdzy dowolna liczbe dzielisz przez 2 => reszta 0
        # nieparzytsa, gdy liczba nieparzysta  przez 2 => reszta 1

        if number < 0 and degree % 2 == 0:
            return "ERROR: Cannot calculate an even root of a negative number"

        # 3.Główna kalkulacja (x**(1/n))
        try:
            return number ** (1 / degree)
        except OverflowError:
            return "ERROR: Result too large or small for standard float"