def calcularTerminanAntes_ai(s, f, i):
    S_i = []
    F_i = []
    
    for l in range(len(s)):
        if s[i] >= f[l]:  
            S_i.append(s[l])
            F_i.append(f[l])
    
    return S_i, F_i

def calcularInicianDespues_ai(s, f, i):
    S_i = []
    F_i = []
    
    for l in range(len(s)):
        if s[l] >= f[i]:  
            S_i.append(s[l])
            F_i.append(f[l])
    
    return S_i, F_i

    
def SeleccionActividades_valorOpt(s, f):
    if len(s) == 0:
        return 0
    
    n = len(s)
    q = -1
    for k in range(n):        
        ST_k, FT_k = calcularTerminanAntes_ai(s, f, k)
        SD_k, FD_k = calcularInicianDespues_ai(s, f, k)
        
        p = 1 + SeleccionActividades_valorOpt(ST_k, FT_k)
        + SeleccionActividades_valorOpt(SD_k, FD_k)
            
        if p > q:
            q = p
    
    return q
    
