# main.py - главный файл приложения
 
import utils
import config
 
def main():
    print(f"Запуск {config.APP_NAME} версии {config.VERSION}")
    print(f"Автор: {config.AUTHOR}")
    print("-" * 30)
    
    # Демонстрация работы функций
    a, b = 10, 5
    print(f"{a} + {b} = {utils.add(a, b)}")
    print(f"{a} - {b} = {utils.subtract(a, b)}")
    
    text = "hello world"
    print(f"Текст в верхнем регистре: {utils.to_uppercase(text)}")

    # Деление
    try:
        print(f"{a} / {b} = {utils.divide(a, b)}")
    except ValueError as e:
        print(f"Ошибка: {e}")

 
if __name__ == "__main__":
    main()
