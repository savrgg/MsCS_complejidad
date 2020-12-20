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
        
        if (ST_k, FT_k) in sel_actividades:
            out_1 = sel_actividades[(ST_k, FT_k)]
        else:
            sel_actividades[(ST_k, FT_k)] = SeleccionActividades_valorOpt(ST_k, FT_k)
            out_1 = sel_actividades[(ST_k, FT_k)]
            
        if (SD_k, FD_k) in sel_actividades:
            out_2 = sel_actividades[(SD_k, FD_k)]
        else:
            sel_actividades[(SD_k, FD_k)] = SeleccionActividades_valorOpt(SD_k, FD_k)
            out_2 = sel_actividades[(SD_k, FD_k)]

        p = 1 + out_1 + out_2
            
        if p > q:
            q = p
    
    return q
    

sel_actividades = {}    
print(SeleccionActividades_valorOpt([1,3,0,5,3,5,6,8,8,2,12,20,19],[2,5,6,7,9,9,10,11,12,14,16,22,24]))
