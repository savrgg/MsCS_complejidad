import sys

def crea_matriz(size):
    matriz = []
    for i in range(size):
        matriz.append([-1 for i in range(size)])
    return matriz

def arista(m, v1,v2,p):
    if v1 == v2:
        print("v1 y v2 son el mismo %d and %d" % (v1, v2))
    m[v1][v2] = p
    m[v2][v1] = p

def buscar(i): 
    while padre[i] != i: 
        i = padre[i] 
    return i 

def union(i, j): 
    a = buscar(i) 
    b = buscar(j) 
    padre[a] = b 

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



filename = sys.argv[1]

file_t = open(filename, 'r')
n = 1

while True:
    if n == 1: 
      line = file_t.readline()  
      V = int(line)
      padre = [i for i in range(V)] 
      mat=crea_matriz(V)
      print("Imprimiendo linea: " + str(n))
      n += 1
      
    else:
      line = file_t.readline()  
      
      if not line:
        break
      
      arista(mat,int(line.split()[0]),int(line.split()[1]),int(line.split()[2]))
      print("Imprimiendo linea: " + str(n))
      n += 1

    if not line:
        break
    print(line)
file_t.close()

kruskal(mat)

