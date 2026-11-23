import numpy as np

def input_size():
    rows = int(input("Введите количество строк (высоту): "))
    cols = int(input("Введите количество столбцов (ширину): "))
    return rows, cols

def create_array(rows, cols):
    while True:
        print("\n--- Создание массива ---")
        print("1. Вручную")
        print("2. Автоматически (случайные числа от 0 до 100)")
        print("3. Назад")
        choice = input("Выберите вариант: ")
        if choice == "1":
            arr = np.zeros((rows, cols), dtype=int)
            for i in range(rows):
                for j in range(cols):
                    arr[i, j] = int(input(f"Введите элемент [{i}][{j}]: "))
            print("Массив успешно создан!")
            return arr
        elif choice == "2":
            arr = np.random.randint(0, 101, size=(rows, cols))
            print("Массив успешно сгенерирован!")
            return arr
        elif choice == "3":
            return None
        else:
            print("Неверный ввод.")

def view_array(arr):
    if arr is None:
        print("\nМассив еще не создан!")
    else:
        print("\nТекущий массив:")
        print(arr)

def func_1(arr):
    res = arr.copy()
    res[res < 10] = 42
    print("\nРезультат (элементы < 10 заменены на 42):")
    print(res)
