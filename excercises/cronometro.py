contador_hora = 0
contador_min = 0
contador_seg = 0

while contador_hora <= 24:
    while contador_min < 60:
        while contador_seg < 60:
            print(contador_hora, contador_min, contador_seg)
            contador_seg +=1
        print(contador_hora, contador_min, contador_seg)    
        contador_seg = 0
        contador_min +=1
    print(contador_hora, contador_min, contador_seg)
    contador_min =0
    contador_hora +=1