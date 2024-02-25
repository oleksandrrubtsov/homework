import time

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = [3, 5, 1, 4, 6, 2]
print("Original array:", arr)

print("Selection sort time:")
start_time = time.time()
selection_sort(arr)
end_time = time.time()
print(end_time - start_time)

print("Bubble sort time:")
start_time = time.time()
bubble_sort(arr)
end_time = time.time()
print(end_time - start_time)