def arista(m, v1,v2,p):
    if v1 == v2:
        print("v1 y v2 son el mismo %d and %d" % (v1, v2))
    m[v1][v2] = p
    m[v2][v1] = p

