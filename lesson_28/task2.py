import threading
import random

# Create a list of random numbers
data_list = [random.randint(1, 100) for _ in range(100)]

def process_data(data):
    # Example function: sorting the data
    data.sort()
    return data

def multi_threaded_process_data(data):
    if len(data) <= 10:
        # If the data size is small, process it without multi-threading
        return process_data(data)

    # Split the data into two halves
    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]

    # Create threads for processing each half
    left_thread = threading.Thread(target=process_data, args=(left,))
    right_thread = threading.Thread(target=process_data, args=(right,))

    # Start the threads
    left_thread.start()
    right_thread.start()

    # Wait for the threads to finish
    left_thread.join()
    right_thread.join()

    # Merge the processed results from left and right threads
    merged_result = merge(left, right)
    return merged_result

def merge(left, right):
    result = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result

if __name__ == "__main__":
    # Single-threaded processing
    result_single_threaded = process_data(data_list.copy())
    print("Single-threaded result:", result_single_threaded)

    # Multi-threaded processing
    result_multi_threaded = multi_threaded_process_data(data_list.copy())
    print("Multi-threaded result:", result_multi_threaded)