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

def func_3(arr):
    indices = np.argwhere(arr < 0)
    print("\nИндексы отрицательных элементов (строка, столбец):")
    if len(indices) == 0:
        print("Отрицательных элементов нет.")
    else:
        for idx in indices:
            print(f"[{idx[0]}][{idx[1]}]")

def func_6(arr):
    print("\nСуммы по строкам:", arr.sum(axis=1))
    print("Суммы по столбцам:", arr.sum(axis=0))

def func_7(arr):
    print("\nГлавная диагональ:", np.diag(arr))
    print("Побочная диагональ:", np.diag(np.fliplr(arr)))

def func_21(arr):
    col_sums = arr.sum(axis=0)
    max_col_idx = np.argmax(col_sums)
    print(f"\nСтолбец с наибольшей суммой: индекс {max_col_idx} (сумма = {col_sums[max_col_idx]})")

def functions_menu(arr):
    if arr is None:
        print("\nСначала создайте массив!")
        return
    while True:
        print("\n--- Выполнение функций ---")
        print("а) Заменить элементы меньше 10 числом 42 (Функция 1)")
        print("б) Напечатать индексы отрицательных элементов (Функция 3)")
        print("в) Вычислить сумму элементов каждого столбца и строки (Функция 6)")
        print("г) Напечатать главную и побочную диагонали (Функция 7)")
        print("д) Найти столбец с наибольшей суммой элементов (Функция 21)")
        print("е) Назад")
        choice = input("Выберите пункт: ").lower()
        if choice == "а": func_1(arr)
        elif choice == "б": func_3(arr)
        elif choice == "в": func_6(arr)
        elif choice == "г": func_7(arr)
        elif choice == "д": func_21(arr)
        elif choice == "е": break
        else: print("Неверный пункт меню.")

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
        if choice == "1":
            rows, cols = input_size()
            arr = None
        elif choice == "2":
            new_arr = create_array(rows, cols)
            if new_arr is not None: arr = new_arr
        elif choice == "3": view_array(arr)
        elif choice == "4": functions_menu(arr)
        elif choice == "5":
            print("Завершение работы.")
            break
        else: print("Неверный ввод.")

if __name__ == "__main__":
    main()
