import json
import timeit
import matplotlib.pyplot as plt
import sys
sys.setrecursionlimit(20000)

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

if __name__ == "__main__":
    with open("ex2.json", "r") as f:
        data = json.load(f)

    x = []
    y = []
    for input_data in data:
        time = timeit.timeit(lambda: func1(input_data, 0, len(input_data) - 1), number=1)
        x.append(len(input_data))
        y.append(time)

    plt.plot(x, y, 'ro')
    plt.xlabel('Input Size')
    plt.ylabel('Time (seconds)')
    plt.title('QuickSort Timing Results')

    plt.show()

