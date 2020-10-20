def simular_arreglos(tam):
    times_insertion = np.empty(int(len(range(tam))/10))
    times_merge = np.empty(int(len(range(tam))/10))
    for i in range(tam):
        if(i%500 == 0.0):
            print(i)
        if(i%10 == 0.0):
            times_insertion[int(i/10)] = insertion_time(i+1)["tiempo"]
            times_merge[int(i/10)] = merge_time(i+1)["tiempo"]
    
    return {'insertion': times_insertion, 'merge': times_merge}
    
