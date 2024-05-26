def bubble_sort(array):
    comparison = 0
    swaps = 0
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            comparison += 1
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swaps += 1
    print("Bubble Sort Output:", array)
    print("Comparisons:", comparison)
    print("Swaps:", swaps)

def selection_sort(array):
    comparison = 0
    swaps = 0
    n = len(array)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            comparison += 1
            if array[j] < array[min_index]:
                min_index = j
        if min_index != i:
            array[i], array[min_index] = array[min_index], array[i]
            swaps += 1
    print("Selection Sort Output:", array)
    print("Comparisons:", comparison)
    print("Swaps:", swaps)

def insertion_sort(array):
    comparison = 0
    swaps = 0
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0:
            comparison += 1
            if key < array[j]:
                array[j+1] = array[j]
                swaps += 1
                j -= 1
            else:
                break
        array[j+1] = key
    print("Insertion Sort Output:", array)
    print("Comparisons:", comparison)
    print("Swaps:", swaps)

test_array = [2, 7, 4, 1, 5, 3, 8, 6]

bubble_sort(test_array.copy())

selection_sort(test_array.copy())

insertion_sort(test_array.copy())

# Time Complexity Analysis

# bubble sort best case time complexity is O(n) when the array is already sorted.
# bubble sort worst case time complexity is O(n^2) when the array is reverse sorted.
# bubble sort average case time complexity is O(n^2).

# selection sort best case time complexity is O(n^2) when the array is reverse sorted.
# selection sort worst case time complexity is O(n^2) when the array is already sorted.
# selection sort average case time complexity is O(n^2).

# insertion sort best case time complexity is O(n) when the array is already sorted.
# insertion sort worst case time complexity is O(n^2) when the array is reverse sorted.
# insertion sort average case time complexity is O(n^2).