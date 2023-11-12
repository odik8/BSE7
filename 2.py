#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    elements = [1.5, -3.2, 4.7, -2.1, 5.8, -6.4, 0.9]

    # 1. Найти номер максимального по модулю элемента списка
    max_abs_index = elements.index(max(elements, key=abs))
    print(f"Номер максимального по модулю элемента: {max_abs_index}")

    # 2. Найти сумму элементов после первого положительного элемента
    first_positive_index = next((i for i, x in enumerate(elements) if x > 0), None)
    if first_positive_index is not None:
        sum_after_positive = sum(elements[first_positive_index + 1:])
        print(f"Сумма элементов после первого положительного: {sum_after_positive}")
    else:
        print("В списке нет положительных элементов.")

    # Значения a и b для интервала [a, b]
    a = 0
    b = 5

    # Преобразовать список
    transformed_list = sorted(elements, key=lambda x: x // 1 if a <= x <= b else float(
        'inf'))  # float('inf') делает число бесконечно большим, что перемещает его в конец списка
    print("Преобразованный список:", transformed_list)


if __name__ == "__main__":
    main()
