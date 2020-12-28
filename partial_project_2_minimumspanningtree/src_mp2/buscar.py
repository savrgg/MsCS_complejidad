def buscar(i): 
    while padre[i] != i: 
        i = padre[i] 
    return i 

