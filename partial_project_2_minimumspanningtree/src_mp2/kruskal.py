def kruskal(m_costos): 
    costomin = 0 
    dict = {}
    
    aristas = 0
    while aristas < V - 1: 
        min = float('inf')  
        for i in range(V): 
            for j in range(V): 
                if buscar(i) != buscar(j) and m_costos[i][j] < min and m_costos[i][j] != -1: 
                    min = m_costos[i][j] 
                    a = i 
                    b = j         
        union(a,b)
        dict["Arista "+ str(aristas)]= "(" + str(a)+ "," + str(b)+ ")" + " - costo: " + str(min) 
        aristas += 1
        costomin += min
    print("EL AGM ES: " + str(dict) + "\nEL COSTO MINIMO ES: " + str(costomin))
  
    
