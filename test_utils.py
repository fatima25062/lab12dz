# test_utils.py - простые тесты для функций
import utils

def test_modulo():
    print("Тестируем modulo:", "OK" if utils.modulo(10, 3) == 1 else "FAIL")

def test_average():
    print("Тестируем average:", "OK" if utils.average([1,2,3,4,5]) == 3 else "FAIL")

if __name__ == "__main__":
    test_modulo()
    test_average()
