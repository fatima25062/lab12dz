# utils.py - вспомогательные функции
 
def add(a: float, b: float) -> float:
    """Складывает два числа."""
    return a + b
 
def subtract(a: float, b: float) -> float:
    """Вычитает два числа."""
    return a - b
 
def to_uppercase(text: str) -> str:
    """Переводит текст в верхний регистр."""
    return text.upper()

def power(a: float, b: float) -> float:
    """Возводит a в степень b."""
    return a ** b
def divide(a: float, b: float) -> float:
    """Делит два числа. Возвращает ошибку при делении на ноль."""
    if b == 0:
        raise ValueError("На ноль делить нельзя!")
    return a / b
def average(numbers: list) -> float:
    """Возвращает среднее арифметическое списка чисел."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)
def modulo(a: float, b: float) -> float:
    """Возвращает остаток от деления a на b."""
    if b == 0:
        raise ValueError("На ноль делить нельзя!")
    return a % b
