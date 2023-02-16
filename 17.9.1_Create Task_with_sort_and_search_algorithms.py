# Напишите программу, которой на вход подается последовательность чисел через пробел, а также запрашивается
# у пользователя любое число.
# В качестве задания повышенного уровня сложности можете выполнить проверку соответствия указанному в условии ввода
# данных.
# Далее программа работает по следующему алгоритму:
# 1. Преобразование введённой последовательности в список
# 2. Сортировка списка по возрастанию элементов в нем (для реализации сортировки определите функцию)
#3. Устанавливается номер позиции элемента, который меньше введенного пользователем числа, а следующий за ним больше
# или равен этому числу.
# # При установке позиции элемента воспользуйтесь алгоритмом двоичного поиска
# Подсказка: Помните, что у вас есть числа, которые могут не соответствовать заданному условию.В
# этом случае необходимо вывести соответствующее сообщение

# # Write a program that inputs a sequence of numbers separated by a space, and requests any number from the user.
# # As an additional task, you can perform a compliance check specified in the data entry condition.
# # Next, the program works according to the following algorithm:
# # 1. Converts the entered sequence into a list
# # 2. Sorts the list in ascending order (by defined sorting function)
# # 3. Identifies an index of an element, which is less than the number entered by the user, while the following one is
# # greater. (Here use the binary search algorithm)

# This program first reads the input sequence of numbers and the target number, checks that the inputs
# are valid integers, sorts the sequence, and then uses binary search to find the position of the largest number
# less than the target number. It then checks the result and prints an appropriate message.

def binary_search(lst, x):
    """
    Performs binary search on the sorted list and returns the position of the largest number less than x
    """
    left = 0
    right = len(lst) - 1

    while left <= right:
        mid = (left + right) // 2
        if lst[mid] >= x:
            right = mid - 1
        else:
            left = mid + 1

    return right

# Read input and check validity
input_str = input("Enter a sequence of numbers separated by a space: ")
try:
    numbers = [int(x) for x in input_str.split()]
except ValueError:
    print("Invalid input, please enter a sequence of integers separated by a space.")
    exit()

num = input("Enter a number: ")
try:
    num = int(num)
except ValueError:
    print("Invalid input, please enter an integer.")
    exit()

# Sort the list and search for the item position
numbers.sort()
pos = binary_search(numbers, num)

# Check the result and print output
if pos < 0:
    print("All numbers are greater than or equal to the entered number.")
elif pos == len(numbers) - 1:
    print("All numbers are less than or equal to the entered number.")
else:
    print("The item position number is", pos + 1)