import math

class BasicCalculator:
    """Base class implementing basic operations and memory state."""

    def __init__(self):
        self.memory = 0.0

    # --- BASIC OPERATIONS ---
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "ERROR: Division by zero is not allowed!"

    def modulo(self, a, b):
        if b != 0:
            return a % b
        else:
            return "ERROR: Division by zero in modulo operation!"

    # --- MEMORY FUNCTIONS ---
    # Using lowercase letters, as per Python convention (PEP 8)
    def m_plus(self, number):
        self.memory += number
        return f"Added {number} to memory. Memory: {self.memory}"

    def m_recall(self):
        return self.memory

    def m_clear(self):
        self.memory = 0.0
        return "Memory cleared (MC)."