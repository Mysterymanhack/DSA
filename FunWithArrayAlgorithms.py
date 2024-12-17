import random
def LinearSearch(array,goal):
    for index,element in enumerate(array):
        if element == goal:
            return index
    return "Wasn't found in array"
nums2 = []
def BinSearch(sortedArray,goal):
    low = 0
    high = len(sortedArray) - 1
    mid = (low + high) // 2
    while low < high:
        mid = (low + high) // 2
        if sortedArray[mid] < goal:
            low = mid + 1
        if sortedArray[mid] > goal:
            high = mid - 1
        if sortedArray[mid] == goal:
            return mid
    return -1
def deCircularize(circularArray):
    low = 0
    high = len(circularArray) - 1
    mid = (low + high) // 2
    while circularArray[mid] > circularArray[mid - 1]:
        mid = (low + high) // 2
        if circularArray[mid] < circularArray[low]:
            high = mid
        if circularArray[mid] > circularArray[high]:
            low = mid
    return circularArray[mid:] + circularArray[:mid]

def MergeSort(array):
    if len(array) == 1:
        return array
    array1 = MergeSort(array[:(len(array)//2)])
    array2 = MergeSort(array[(len(array)//2):])
    index1 = 0
    index2 = 0
    sortedArray = []
    while index1 <= len(array1) and index2 < len(array2):
        if index1 == len(array1):
            sortedArray.append(array2[index2])
            index2 += 1
        elif index2 == len(array2) - 1:
            sortedArray.append(array1[index1])
            index1 += 1
        elif array1[index1] <= array2[index2]:
            sortedArray.append(array1[index1])
            index1 +=1
        else:
            sortedArray.append(array2[index2])
            index2 +=1
    return sortedArray
testList = []
for i in range(100):
    testList.append(random.random())
print(MergeSort(testList))