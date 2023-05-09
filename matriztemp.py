import numpy as np
import random
import pandas as pd
d = 3
h = 6
temp = np.empty((d,h), dtype = float)


print("1 - Random")
print("2 - Manual")
print("3 - Salir")

option = int(input("Ingrese una opción: "))

if option == 1:
    for i in range(d):
        for j in range(h):
            temp[i][j] = float(random.randint(20,40))

    # Creamos un dataframe de pandas a partir del array temp
    df = pd.DataFrame(temp, columns=["Hora " + str(i) for i in range(h)],  index=["Día " + str(i+1) for i in range(d)])


    # Recorremos el array temp y calculamos el valor mínimo, máximo y promedio de cada día
    for i in range(len(temp)):
        max = 0
        min= 50
        prom = 0
        for j in range(len(temp[0])):
            if temp[i][j] > max:
                max = temp[i][j]
            if temp[i][j]<min:
                min = temp[i][j]
            prom += temp[i][j]
        prom = prom/h
        print("min ",min)
        print("max ",max)
        print("prom ",prom)
    # Creamos un dataframe de pandas a partir del array temp
    df = pd.DataFrame(temp, columns=["Hora " + str(i) for i in range(h)], index=["Día " + str(i) for i in range(d)])
    print(df)
    
elif option == 2:
    #Hacemos un recorrido de las columnas
    for i in range(d):
        #Hacemos un recorrido de las horas
        for j in range(h):
            #Llenamos cada índice con los datos que ingrese el usuario
            temp[i][j] = float(input(f"Ingrese la temperatura {i} - {j}: "))

    print(temp)
    print("")


    for i in range(len(temp)):
        max = 0
        min= 50
        prom = 0
        for j in range(len(temp[0])):
            if temp[i][j] > max:
                max = temp[i][j]
            if temp[i][j]<min:
                min = temp[i][j]
            prom += temp[i][j]
        prom = prom/h
        print("min ",min)
        print("max ",max)
        print("prom ",prom)

elif option == 3:
    exit()
    


