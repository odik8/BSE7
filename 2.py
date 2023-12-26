#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    elements = list(map(float, input("Введите числа через пробел: ").split()))

    max_abs_index = elements.index(max(elements, key=abs))
    print(f"Номер максимального по модулю элемента: {max_abs_index}")

    first_positive_index = next((i for i, x in enumerate(elements) if x > 0), None)
    if first_positive_index is not None:
        sum_after_positive = sum(elements[first_positive_index + 1:])
        print(f"Сумма элементов после первого положительного: {sum_after_positive}")
    else:
        print("В списке нет положительных элементов.")

    a = 0
    b = 5

    transformed_list = sorted(elements, key=lambda x: x // 1 if a <= x <= b else float(
        'inf'))
    print("Преобразованный список:", transformed_list)


if __name__ == "__main__":
    main()