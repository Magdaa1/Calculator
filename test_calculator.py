import unittest

from advance_calculator import AdvancedCalculator
from basic_calculator import BasicCalculator

class TestBasicCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = BasicCalculator()

    #---Add and substract---#
    def test_add_positive(self):
        # check, 2 + 3 == 5
        self.assertEqual(self.calc.add(2,3),5)

    def tst_substract_negative_result(self):
        # check, 10 - 20 == -10
        self.assertEqual(self.calc.subtract(10,20),-10)

    def test_division_standard(self):
        # check, 10 / 4 == 2.5
        self.assertEqual(self.calc.divide(2,2),1)

        # division by 0 => error
    def test_division_by_zero(self):
        expected_error = "ERROR: Division by zero is not allowed!"
        self.assertEqual(self.calc.divide(2,0), expected_error)

    #--- Modulo ---
    def test_modulo_standard(self):
        # 10 % 3 == 1; 10/2 = 9 reszta 1
        self.assertEqual(self.calc.modulo(10,3),1)

    #---- Testowanie Pamieci (Stan Kalkulatora) ---
    def test_memory_functionality(self):
        # Add worth
        self.calc.m_plus(10)
        self.assertEqual(self.calc.m_recall(),10)
        # Check if the worth was saved
        self.calc.m_plus(10)
        self.assertEqual(self.calc.m_recall(),20)
        # clears memory
        self.calc.m_clear()
        # check the memory is 0
        self.assertEqual(self.calc.m_recall(),0.0)

class TestAdvancedCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = AdvancedCalculator()
    # --- potegowanie ---
    # --- Potęgowanie ---
    def test_power_standard(self):
        # Sprawdza, czy 2^3 == 8
        self.assertEqual(self.calc.power(2, 3), 8)

        # --- Pierwiastek Kwadratowy ---

    def test_sqrt_of_four(self):
        # Sprawdza, czy sqrt(4) == 2.0
        self.assertEqual(self.calc.square_root(4), 2.0)

    def test_sqrt_of_negative(self):
        # Sprawdza, czy sqrt(-1) zwraca błąd (w dziedzinie R)
        expected_error = "ERROR: Square root of a negative number"
        self.assertEqual(self.calc.square_root(-1), expected_error)

        # --- Pierwiastek N-tego Stopnia (Nth Root) ---

    def test_nth_root_cubic(self):
        # Sprawdza, czy pierwiastek 3. stopnia z 27 jest 3.0
        self.assertAlmostEqual(self.calc.nth_root(27, 3), 3.0)  # Używamy assertAlmostEqual dla ułamków

    def test_nth_root_even_of_negative(self):
        # Sprawdza pierwiastek stopnia 4 (parzysty) z liczby ujemnej
        expected_error = "ERROR: Cannot calculate an even root of a negative number"
        self.assertEqual(self.calc.nth_root(-16, 4), expected_error)

    def test_nth_root_zero_degree(self):
        # Sprawdza, czy stopień pierwiastka jest zerem
        expected_error = "ERROR: Root degree cannot be zero"
        self.assertEqual(self.calc.nth_root(10, 0), expected_error)

        # --- Logarytm ---

    def test_logarithm_base_10(self):
        # Sprawdza, czy log10(100) == 2.0
        self.assertAlmostEqual(self.calc.logarithm(100, 10), 2.0)


if __name__ == '__main__':
    unittest.main()
