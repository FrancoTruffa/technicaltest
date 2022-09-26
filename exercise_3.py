def def_casos(T):
    casos_valor = []
    casos_keys = []
    for i in range(T):
        value = int(input(f"Ingrese #Caso {i+1}: "))
        while(value>200 or value<0):
            value = int(input("Porfavor, ingrese un #Caso entre 0 y 200: "))    
        if(value>=0 and value<=200):
            casos_valor.append(value)
            casos_keys.append(f"Caso #{i+1}")

    return casos_keys, casos_valor

def ciclo_bleatrix(N, casos_keys):
    """
        x = []
        for i in range(0,10):
            x.append(i)
    """
    validador = [0,1,2,3,4,5,6,7,8,9]
    valores_keys = []
    print(N)

    for valor in N:
        i=0
        compara = []
        while((compara!=validador)):
            i+=1
            x = valor * i
            for digits in str(x):
                compara.append(int(digits))
            compara = list(dict.fromkeys(compara))
            compara.sort()
            if(compara == validador):
                valores_keys.append(x)
                break
            elif((valor==0)):
                valores_keys.append("INSOMNIA")
                break

    return dict(zip(casos_keys, valores_keys))
    

if __name__ == "__main__":
    T = int(input("Introducir cantidad de casos a probar: "))
    while(T is None or T>100 or T<1):
        T = int(input("Porfavor, ingrese un valor entre 1 y 100: "))

    T_par = def_casos(T)
    print(ciclo_bleatrix(T_par[1], T_par[0]))
    