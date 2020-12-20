def merge_time(n):
    start_time = time.time()
    for i in range(1):
        a = np.random.rand(n)
        b = mergeSort(a)
    elapsed_time = (time.time() - start_time)/1
    return {'desordenado': a, 'ordenado': b ,'tiempo': elapsed_time}
