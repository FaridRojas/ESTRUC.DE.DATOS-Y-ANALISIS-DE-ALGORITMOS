class Nodo:
    #Constructor Nodo
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        
    #Metodo Ver el valor    
    def devolver_valor(self):
        print(self.valor)

    #Metodo Asignar el siguiente
    def asignar_siguiente(self,nodo):
        self.siguiente = nodo
        
    #Metodo Cambiar el valor    
    def cambiar_valor(self,nuevo_valor):
        self.valor = nuevo_valor
            
Nodo1 = Nodo("A")
Nodo2 = Nodo("C")

#print(Nodo1.valor) 

#Nodo1.devolver_valor()

#Nodo.devolver_valor(Nodo1)

Nodo1.cambiar_valor("B")

Nodo1.devolver_valor()

Nodo1.asignar_siguiente(Nodo2)

Nodo1.siguiente.devolver_valor()

