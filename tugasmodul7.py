from abc import ABC, abstractmethod
import math


class Calculator(ABC):
    def __init__(self):
        self.number = [0] * 100
        self.count = 0

    def addNumber(self, num):
        self.number[self.count] = num
        self.count += 1

    def getNumber(self, index):
        return self.number[index]

    def clear(self):
        self.count = 0

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def subtract(self):
        pass

    @abstractmethod
    def multiply(self):
        pass

    @abstractmethod
    def divide(self):
        pass


class BasicCalculator(Calculator):
    def __init__(self):
        super().__init__()

    def add(self):
        result = 0
        for i in range(self.count):
            result += self.getNumber(i)
        return result

    def subtract(self):
        result = self.getNumber(0)
        for i in range(1, self.count):
            result -= self.getNumber(i)
        return result

    def multiply(self):
        result = 1
        for i in range(self.count):
            result *= self.getNumber(i)
        return result

    def divide(self):
        result = self.getNumber(0)
        for i in range(1, self.count):
            if self.getNumber(i) == 0:
                print("Cannot divide by zero")
                return 0
            result /= self.getNumber(i)
        return result


class ScientificCalculator(Calculator):
    def __init__(self):
        super().__init__()

    def squareRoot(self):
        result = math.sqrt(self.getNumber(0))
        return result

    def exponentiation(self):
        result = math.pow(self.getNumber(0), self.getNumber(1))
        return result

    def factorial(self):
        result = 1
        num = int(self.getNumber(0))
        for i in range(1, num+1):
            result *= i
        return result

    def add(self):
        result = 0
        for i in range(self.count):
            result += self.getNumber(i)
        return result

    def subtract(self):
        result = self.getNumber(0)
        for i in range(1, self.count):
            result -= self.getNumber(i)
        return result

    def multiply(self):
        result = 1
        for i in range(self.count):
            result *= self.getNumber(i)
        return result

    def divide(self):
        result = self.getNumber(0)
        for i in range(1, self.count):
            if self.getNumber(i) == 0:
                print("Cannot divide by zero")
                return 0
            result /= self.getNumber(i)
        return result


if __name__ == "__main__":
    calc = None
    choice = 0
    num1, num2 = 0, 0

    while True:
        print("Choice calculator type:")
        print("1. Basic Calculator")
        print("2. Scientific Calculator")
        choice = int(input())

        if choice == 1:
            calc = BasicCalculator()
            break
        elif choice == 2:
            calc = ScientificCalculator()
            break
        else:
            print("Invalid choice, please try again")

    while True:
        print("Choice operation:")
        print("1. Add numbers")
        print("2. Subtract numbers")
        print("3. Multiply numbers")
        print("4. Divide numbers")
        if choice == 2:
            print("5. Square root")
            print("6. Exponentiation")
            print("7. Factorial")
        print("8. Clear")
        print("9. Exit")
        operation = int(input())

        if operation == 1:
            num = int(input("Enter number of numbers to add: "))
            for i in range(num):
                calc.addNumber(int(input("Enter number: ")))
            print("Result: ", calc.add())
        elif operation == 2:
            num = int(input("Enter number of numbers to subtract: "))
            for i in range(num):
                calc.addNumber(int(input("Enter number: ")))
            print("Result: ", calc.subtract())
        elif operation == 3:
            num = int(input("Enter number of numbers to multiply: "))
            for i in range(num):
                calc.addNumber(int(input("Enter number: ")))
            print("Result: ", calc.multiply())
        elif operation == 4:
            num = int(input("Enter number of numbers to divide: "))
            for i in range(num):
                calc.addNumber(int(input("Enter number: ")))
            print("Result: ", calc.divide())
        elif operation == 5 and choice == 2:
            calc.addNumber(float(input("Enter number: ")))
            print("Result: ", calc.squareRoot())
        elif operation == 6 and choice == 2:
            calc.addNumber(float(input("Enter base: ")))
            calc.addNumber(float(input("Enter exponent: ")))
            print("Result: ", calc.exponentiation())
        elif operation == 7 and choice == 2:
            calc.addNumber(int(input("Enter number: ")))
            print("Result: ", calc.factorial())
        elif operation == 8:
            calc.clear()
            print("Cleared")
        elif operation == 9:
            break
        else:
            print("Invalid operation, please try again")
