
# Insertion sort

def insertionSort(array):
    for i in range(1,len(array)):
        current = array[i]
        while i>0 and array[i-1]>current:
            array[i] = array[i-1]
            i = i-1
            array[i] = current
    return array
