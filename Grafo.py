from Nodo import *
from Arista import *

'Clase Grafo'
class Grafo: 
    def __init__(self):
        self.nodos = []         # Lista para almacenar los nodos del grafo
        self.aristas = []       # Lista para almacenar las aristas como pares de nodos
        self.atributos = {}     # Diccionario para atributos adicionales (opcional, no se usa aquí)

    def agregar_Nodo(self, n):
        # Agrega un nodo al grafo si no está ya presente
        if n not in self.nodos:
            nodo = Nodo(n)                          # Crea una instancia de Nodo (se espera que exista esta clase)
            self.nodos.append(nodo.identificador)   # Agrega el identificador del nodo a la lista de nodos

    def agregar_Arista(self, origen, destino):
        #Agrega una arista entre dos nodos si ambos están en el grafo
        if origen in self.nodos and destino in self.nodos:
            aristas_id = Arista(origen, destino)    # Crea una instancia de Arista (se espera que exista esta clase)
            self.aristas.append([
                aristas_id.arista[0].identificador, 
                aristas_id.arista[1].identificador
            ])  # Agrega la arista como una lista de dos nodos

    def mostrar_grafo(self):
        # Imprime los nodos del grafo
        print("Nodos:")
        for nodo in self.nodos:
            print(f"  Nodo {nodo}")

        # Imprime las aristas del grafo
        print("\nAristas:")
        for arista in self.aristas:
            print(f"  {arista[0]} -> {arista[1]}")

    def exportar_a_gv(self, nombre_archivo):
        # Exporta el grafo a un archivo en formato Graphviz (.gv)
        with open(nombre_archivo, 'w') as f:
            f.write('graph G {\n')                   # Inicio de un grafo no dirigido
            
            usadas = set()                           # Conjunto para evitar duplicar aristas
            for arista in self.aristas:
                n1, n2 = arista
                if (n2, n1) not in usadas:           # Evita escribir aristas duplicadas
                    f.write(f'    {n1} -- {n2};\n')  # Sintaxis de grafo no dirigido
                    usadas.add((n1, n2))

            # Agrega nodos que no tienen ninguna arista
            for i in range(len(self.nodos)):
                b = False
                while not b:
                    for j in range(len(self.aristas)):
                        if self.nodos[i] in self.aristas[j]:
                            b = True                 # El nodo tiene al menos una arista
                    if not b:
                        ns = str(self.nodos[i])
                        f.write(f'    {ns};\n')      # Nodo aislado
                    b = True                         # Salir del while (se ejecuta solo una vez)

            f.write('}\n')                           # Cierra el bloque del grafo

        
    

    



        
