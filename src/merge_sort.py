def mergeSort(array): 
     
    current_size = 1
     
    while current_size < len(array) - 1: 
         
        left = 0

        while left < len(array)-1: 
             
            mid = min((left + current_size - 1),(len(array)-1))
             
            right = ((2 * current_size + left - 1, 
                    len(array) - 1)[2 * current_size 
                        + left - 1 > len(array)-1]) 
                             
            merge(array, left, mid, right) 
            left = left + current_size*2
             
        current_size = 2 * current_size 
    return array
 
def merge(array, l, m, r): 
    n1 = m - l + 1
    n2 = r - m 
    L = [0] * n1 
    R = [0] * n2 
    for i in range(0, n1): 
        L[i] = array[l + i] 
    for i in range(0, n2): 
        R[i] = array[m + i + 1] 
 
    i, j, k = 0, 0, l 
    while i < n1 and j < n2: 
        if L[i] > R[j]: 
            array[k] = R[j] 
            j += 1
        else: 
            array[k] = L[i] 
            i += 1
        k += 1
 
    while i < n1: 
        array[k] = L[i] 
        i += 1
        k += 1
 
    while j < n2: 
        array[k] = R[j] 
        j += 1
        k += 1
