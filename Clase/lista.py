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
        
        
class node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

# Creamos la clase linked_list
class linked_list: 
    def __init__(self):
        self.head = None
    
    # Método para agregar elementos en el frente de la linked list
    def agregar_inicio(self, data):
        self.head = node(data=data, next=self.head)  


    # Método para agregar elementos al final de la linked list
    def agregar_final(self, data):
        if not self.head:
            self.head = node(data=data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node(data=data)
    
    # Método para eleminar nodos
    def borrar_nodo(self, key):
        curr = self.head
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
        if prev is None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next
            curr.next = None

    # Método para obtener el ultimo nodo
    def get_last_node(self):
        temp = self.head
        while(temp.next is not None):
            temp = temp.next
        return temp.data

    # Método para imprimir la lista de nodos
    def print_list( self ):
        node = self.head
        while node != None:
            print(node.data, end =" => ")
            node = node.next


s = linked_list() # Instancia de la clase
s.add_at_front(5) # Agregamos un elemento al frente del nodo
s.add_at_end(8) # Agregamos un elemento al final del nodo
s.add_at_front(9) # Agregamos otro elemento al frente del nodo

s.print_list() # Imprimimos la lista de nodos