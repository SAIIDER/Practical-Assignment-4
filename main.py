import numpy as np

def main():
    rows, cols = 3, 3
    arr = None
    while True:
        print("\n=== ГЛАВНОЕ МЕНЮ ===")
        print(f"1. Ввод размера массива (текущий: {rows}x{cols})")
        print("2. Создание массива")
        print("3. Просмотр созданного массива")
        print("4. Выполнение функций")
        print("5. Выход")
        choice = input("Выберите пункт меню: ")
        if choice == "5":
            print("Завершение работы.")
            break

if __name__ == "__main__":
    main()
