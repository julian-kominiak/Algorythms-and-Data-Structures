import random
import time
import numpy as np


def insertSort(array):
    for i in range(1, len(array)):
        temp = array[i]
        j = i - 1
        while j >= 0 and temp < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = temp
    return array


def bubbleSort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j + 1] < array[j]:
                array[j + 1], array[j] = array[j], array[j + 1]
    return array


def quickSort(array):
    def partition(array, start, stop):
        i = start - 1
        pivot = array[stop]
        for j in range(start, stop):
            if array[j] < pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[stop] = array[stop], array[i + 1]
        return i + 1

    def recursion(array, start, stop):
        if start < stop:
            partitionPoint = partition(array, start, stop)
            recursion(array, start, partitionPoint - 1)
            recursion(array, partitionPoint + 1, stop)

    recursion(array, 0, len(array) - 1)
    return array


def heapSort(array):
    def heap(array, n, i):
        biggest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and array[biggest] < array[left]:
            biggest = left
        if right < n and array[biggest] < array[right]:
            biggest = right
        if biggest != i:
            array[i], array[biggest] = array[biggest], array[i]
            heap(array, n, biggest)

    for i in range(len(array) // 2 - 1, -1, -1):
        heap(array, len(array), i)
    for i in range(len(array) - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heap(array, i, 0)


def mergeSort(array):
    def merge(array, left, medium, right):
        leftElement = array[left:(medium + 1)]
        rightElement = array[(medium + 1):(right + 1)]
        i = left
        while len(leftElement) > 0 and len(rightElement) > 0:
            if leftElement[0] <= rightElement[0]:
                array[i] = leftElement.pop(0)
            else:
                array[i] = rightElement.pop(0)
            i += 1
        while len(leftElement) > 0:
            array[i] = leftElement.pop(0)
            i += 1
        while len(rightElement) > 0:
            array[i] = rightElement.pop(0)
            i += 1

    def recursion(arr, left, right):
        if left < right:
            medium = (left + right) // 2
            recursion(arr, left, medium)  # Lewa połowa
            recursion(arr, medium + 1, right)  # Prawa połowa
            merge(arr, left, medium, right)
    recursion(array, 0, len(array) - 1)
    return array


def createRandomTable(size):
    table = []
    for i in range(size):
        table.append(random.randint(1, 100))
    return table


table100 = createRandomTable(100)
table10000 = createRandomTable(10000)

print("Sorting Algorithms Analysis\n".center(130))
timesString = ""
for i in range(3):
    timesString += ("[ms] Time " + str(i + 1)).rjust(20)
print("Name".center(15) + "Array Size".center(15) + timesString + "Average Time".rjust(25))


def testAlgorithm(array, function):
    line = ""
    times = []
    line += function.__name__.center(15) + str(len(array)).rjust(10) + "     "
    for sortingTrial in range(3):
        arrayCopy = array.copy()
        start = time.time()
        function(arrayCopy)
        stop = time.time()
        times.append(round((stop - start) * 1000, 5))
        line += str(round((stop - start) * 1000, 5)).rjust(20)
    line += str(round(sum(times) / 3, 5)).rjust(25)
    print(line)

testAlgorithm(table100, insertSort)
testAlgorithm(table10000, insertSort)
testAlgorithm(table100, bubbleSort)
testAlgorithm(table10000, bubbleSort)
testAlgorithm(table100, quickSort)
testAlgorithm(table10000, quickSort)
testAlgorithm(table100, heapSort)
testAlgorithm(table10000, heapSort)
testAlgorithm(table100, mergeSort)
testAlgorithm(table10000, mergeSort)
