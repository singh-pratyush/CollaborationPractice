class Calculator:
    def multiply(factor1: float, factor2: float) -> float:
        pass

    def divide(dividend: float, divisor: float) -> float:
        pass
    
    def add(number1: float, number2: float) -> float:
        pass
    
    def subtract(minuend: float, subtrahend: float) -> float:
        pass
    
    def power(base: float, exponent: int) -> float:
        pass

assert Calculator.multiply(2, 3) == 6
assert Calculator.divide(6, 2) == 3
assert Calculator.add(2, 3) == 5
assert Calculator.subtract(5, 2) == 3
assert Calculator.power(2, 3) == 8