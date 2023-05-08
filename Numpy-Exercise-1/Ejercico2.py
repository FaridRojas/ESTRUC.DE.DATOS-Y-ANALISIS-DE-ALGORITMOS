import numpy as np
import random
import string
import names

def nombre():
    return names.get_full_name()

estudiantes = np.empty((6500, 5), dtype=object)

#Columna 1 = Codigo Estudiante
#Columna 2 = Nombre Estudiante
#Columna 3 = Promedio Estudiante
#Columna 4 = Codigo Carrera
#Columna 5 = Año de Ingreso 

estudiantes[:, 0] = np.random.randint(2000000, 3000000, size=6500)
estudiantes[:, 1] = [nombre() for i in range(6500)]
estudiantes[:, 2] = np.around(np.random.uniform(2.8, 5, size=6500), decimals=1)
estudiantes[:, 3] = np.random.randint(10, 69, size=6500)
estudiantes[:, 4] = np.random.randint(1980, 2024, size=6500)

codigo_carrera = input("Ingrese el código de la carrera a listar (los codigos de carreras van de 10 a 68): ")
estudiante_por_carreras = estudiantes[estudiantes[:,3].astype('str') == codigo_carrera]
estudiante_por_promedios = estudiante_por_carreras[estudiante_por_carreras[:,2].astype(float) >= 4]

print("Código y nombre de los estudiantes de la carrera ",codigo_carrera," con promedio acumulado igual o mayor a 4:")

for estudiante in estudiante_por_promedios:
    print("Código: ",estudiante[0], ", Nombre: ",estudiante[1], ", Promedio: ",estudiante[2])
    
print("Total de estudiantes: ",len(estudiante_por_promedios))

estudiantes_antes_1990 = estudiantes[estudiantes[:,4].astype(int) < 1990]
estudiantes_condicionales = estudiantes_antes_1990[estudiantes_antes_1990[:,2].astype(float) < 3]

print("Código y nombre de los estudiantes que ingresaron antes de 1990 y están condicionales:")

for estudiante in estudiantes_condicionales:
    print("Código: ",estudiante[0], ", Nombre: ",estudiante[1],", Promedio: ",estudiante[2])

