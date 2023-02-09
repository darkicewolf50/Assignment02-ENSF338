import json
import timeit

def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)

def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

with open("ex2.json", "r") as file:
    data = json.load(file)

timing_results = []
for input_data in data:
    start = timeit.default_timer()
    func1(input_data, 0, len(input_data) - 1)
    end = timeit.default_timer()
    timing_results.append(end - start)

# Plot the timing results

