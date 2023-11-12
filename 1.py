#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    A = [int(input(f"Введите {i + 1}-й элемент списка: ")) for i in range(10)]

    sum_negative_multiples_of_7 = 0
    count_negative_multiples_of_7 = 0

    for num in A:
        if num < 0 and num % 7 == 0:
            sum_negative_multiples_of_7 += num
            count_negative_multiples_of_7 += 1

    print("С использованием циклов:")
    print(f"Сумма отрицательных элементов, кратных 7: {sum_negative_multiples_of_7}")
    print(f"Количество отрицательных элементов, кратных 7: {count_negative_multiples_of_7}")

    sum_negative_multiples_of_7 = sum(num for num in A if num < 0 and num % 7 == 0)
    count_negative_multiples_of_7 = sum(1 for num in A if num < 0 and num % 7 == 0)

    print("\nС использованием List Comprehensions:")
    print(f"Сумма отрицательных элементов, кратных 7: {sum_negative_multiples_of_7}")
    print(f"Количество отрицательных элементов, кратных 7: {count_negative_multiples_of_7}")

if __name__ == "__main__":
    main()
