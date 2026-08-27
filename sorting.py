def bubble_sort(numbers):
    n = len(numbers)

    for i in range(n - 1):
        swapped = False

        for j in range(n - 1 - i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swapped = True

        if not swapped:
            break

    return numbers


numbers = [5, 9, 12, 5, 2, 14, 3, 6, 11]

sorted_numbers = bubble_sort(numbers)
print("Sorted numbers:", sorted_numbers)
