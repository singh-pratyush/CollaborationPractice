from calculator import Calculator

class AnswerKey(Calculator):
    def add(number1: float, number2: float) -> float:
        return number1 + number2
    
    def subtract(minuend, subtrahend):
        return minuend - subtrahend
    
    def multiply(factor1, factor2):
        return factor1 * factor2