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
