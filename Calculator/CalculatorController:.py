from BasicCalculator import BasicCalculator
from AdvancedCalculator import AdvancedCalculator


class CalculatorController:
    def __init__(self):
        self.calculator = None
        self.select_mode()

    def select_mode(self):
        """Selects the calculator mode and initializes the object."""
        while True:
            print("\n--- CALCULATOR MODE SELECTION ---")
            choice = input("Select mode (1: Basic, 2: Advanced, 3: Exit): ")

            if choice == '1':
                self.calculator = BasicCalculator()
                print("Basic mode selected.")
                self.run()
                break
            elif choice == '2':
                self.calculator = AdvancedCalculator()
                print("Advanced mode selected.")
                self.run()
                break
            elif choice == '3':
                print("Goodbye! 👋")
                break
            else:
                print("Invalid choice. Please try again.")

    def _display_menu(self):
        """Displays the menu based on the selected mode."""
        is_advanced = isinstance(self.calculator, AdvancedCalculator)

        print("\n--- MENU ---")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Modulo (%)")
        print("M. Memory Functions (M+/MR/MC)")

        if is_advanced:
            print("P. Power (^)")
            print("R. Square Root (sqrt)")
            print("L. Logarithm (log)")
            print("Z. Change Mode")

        print("W. Exit Program")

    def _handle_memory(self):
        """Submenu for memory operations."""
        while True:
            print("\n--- MEMORY MENU ---")
            # Używamy już przetłumaczonych metod m_recall i m_clear
            mem_choice = input("Select operation (M+: Add, MR: Recall, MC: Clear, W: Back to Menu): ").upper()

            if mem_choice == 'W':
                break
            elif mem_choice == 'MR':
                print(f"Memory = {self.calculator.m_recall()}")
            elif mem_choice == 'MC':
                print(self.calculator.m_clear())
            elif mem_choice == 'M+':
                try:
                    number = float(input("Enter number to add to memory: "))
                    print(self.calculator.m_plus(number))
                except ValueError:
                    print("Invalid number.")
            else:
                print("Unknown memory option.")

    def run(self):
        """Main execution loop."""
        is_advanced = isinstance(self.calculator, AdvancedCalculator)

        while True:
            self._display_menu()
            choice = input("Enter selection: ").upper()

            if choice == 'W':
                print("Session ended. Returning to mode selection...")
                self.select_mode()
                break

            if choice == 'M':
                self._handle_memory()
                continue

            if is_advanced and choice == 'Z':
                print("Changing mode...")
                self.select_mode()
                break

            # --- BASIC OPERATIONS (require 2 arguments) ---
            if choice in ('1', '2', '3', '4', '5'):
                try:
                    num1 = float(input("Enter first number: "))
                    num2 = float(input("Enter second number: "))
                except ValueError:
                    print("Invalid number. Please try again.")
                    continue

                result = None

                if choice == '1':
                    result = self.calculator.add(num1, num2)
                elif choice == '2':
                    result = self.calculator.subtract(num1, num2)
                elif choice == '3':
                    result = self.calculator.multiply(num1, num2)
                elif choice == '4':
                    result = self.calculator.divide(num1, num2)
                elif choice == '5':
                    result = self.calculator.modulo(num1, num2)

            # --- ADVANCED OPERATIONS (Power/Logarithm - 2 args.) ---
            elif is_advanced and choice in ('P', 'L'):
                try:
                    num1 = float(input("Enter base/number: "))
                    num2 = float(input("Enter exponent/base: "))
                except ValueError:
                    print("Invalid number. Please try again.")
                    continue

                if choice == 'P':
                    result = self.calculator.power(num1, num2)
                elif choice == 'L':
                    result = self.calculator.logarithm(num1, num2)

            # --- ADVANCED OPERATIONS (Square Root - 1 arg.) ---
            elif is_advanced and choice == 'R':
                try:
                    num1 = float(input("Enter number: "))
                except ValueError:
                    print("Invalid number. Please try again.")
                    continue
                result = self.calculator.square_root(num1)

            else:
                print("Invalid choice. Please try again.")
                continue

            if 'result' in locals() and result is not None:
                print(f"\n✅ Result: {result}")


if __name__ == "__main__":
    CalculatorController()