import numpy as np

votos = np.random.randint(1, 31, 5000)

votosordenados = np.bincount(votos)

candidatosordenados = np.argsort(votosordenados)[::-1]

for x in candidatosordenados:
    if x != 0:
        print("Candidato N°",x," tiene ",votosordenados[x])
    
print("Farid Camilo Rojas Vargas - ","2220051")
print("2023")