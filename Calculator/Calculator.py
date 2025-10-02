class Kalkulator:
    """Klasa implementująca prosty kalkulator konsolowy."""

    def __init__(self):
        print("--- Prosty Kalkulator Python ---")

    def _wyswietl_menu(self):
        """Wyświetla opcje dla użytkownika."""
        print("\nWybierz opcje:")
        print("1. Dodawanie (+)")
        print("2. Odejmowanie (-)")
        print("3. Mnożenie (*)")
        print("4. Dzielenie (/)")
        print("5. Modulo (%)")
        print("6. Wyjdź z programu")

    # --- Metody obliczeniowe ---

    def dodawanie(self, a, b):
        return a + b

    def odejmowanie(self, a, b):
        return a - b

    def mnozenie(self, a, b):
        return a * b

    def dzielenie(self, a, b):
        if b != 0:
            return a / b
        else:
            return "BŁĄD: Nie dzielimy przez zero!"

    def modulo(self, a, b):
        return a % b

    # --- Główna pętla programu ---

    def run(self):
        """Główna metoda uruchamiająca kalkulator."""
        while True:
            self._wyswietl_menu()
            choice = input("Wprowadź wybór (1/2/3/4/5/6): ")

            if choice == '6':
                print("Do widzenia! 👋")
                break  # Zakończenie pętli i programu

            # Wczytywanie liczb tylko dla opcji 1-5
            if choice in ('1', '2', '3', '4', '5'):
                try:
                    num1 = float(input("Wprowadź pierwszą liczbę: "))
                    num2 = float(input("Wprowadź drugą liczbę: "))
                except ValueError:
                    print("❌ Nieprawidłowa liczba. Spróbuj ponownie.")
                    continue  # Przejście na początek pętli

                wynik = None

                if choice == '1':
                    wynik = self.dodawanie(num1, num2)
                elif choice == '2':
                    wynik = self.odejmowanie(num1, num2)
                elif choice == '3':
                    wynik = self.mnozenie(num1, num2)
                elif choice == '4':
                    wynik = self.dzielenie(num1, num2)
                elif choice == '5':
                    wynik = self.modulo(num1, num2)

                # Wyświetlenie wyniku (jeśli funkcja nie zwróciła błędu)
                print(f"\n✅ Wynik: {wynik}")
            else:
                print("⚠️ Nieprawidłowy wybór. Spróbuj ponownie.")


# --- Uruchomienie programu ---
if __name__ == "__main__":
    kalkulator = Kalkulator()  # Tworzenie instancji klasy
    kalkulator.run()  # Uruchomienie głównej pętli kalkulatora
