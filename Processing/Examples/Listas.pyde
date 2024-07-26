class Circulo:  # Classe (#família no Revit)
    def __init__(self, x, y, w, h):  # Método __init__ (inicializador)
        self.x = x  # Atributo (#Parâmetros no Revit)
        self.y = y  # Atributo (#Parâmetros no Revit)
        self.w = w  # Atributo (#Parâmetros no Revit)
        self.h = h  # Atributo (#Parâmetros no Revit)
        
    def desenhe(self):  # Método (#criar família no Revit)
        ellipse(self.x, self.y, self.w, self.h)  # Função para desenhar a elipse (necessita de um ambiente gráfico como Processing)
        
def setup():  # Função de configuração
    size(400, 400) 
        
def draw():  # Função de desenho
    circ1 = Circulo(20, 30, 40, 60)  # Instância de Circulo
    circ2 = Circulo(60, 70, 40, 60)  # Instância de Circulo

    circ1.desenhe()  # Chamada ao método desenhe da instância circ1 (#Load and place no Revit)
    circ2.desenhe()  # Chamada ao método desenhe da instância circ2 (#Load and place no Revit)
    
    
#SLICE#
minhaLista = [1,2,3,4,5] #slice ou GetItemAtIndex - Dynamo
print(minhaLista[3:])

print(minhaLista[::2]) #first item

novaLista = list(range(100))

print(novaLista[::10])

print(novaLista[::2])

# Modificando Lista
minhalista = [1, 2, 3, 4]

# Adicionando um elemento ao final da lista
minhalista.append(5)
print(minhalista)  # Saída: [1, 2, 3, 4, 5]

# Inserindo um elemento na posição 3
minhalista.insert(0, 0)  # Inserindo o valor 6 na posição 3
print(minhalista)  # Saída: [1, 2, 3, 6, 4, 5]

minhalista.remove(2)
print(minhalista)

minhalista.pop()
print(minhalista)
minhalista.pop()
print(minhalista)

# Lista inicial
minhalista = [1, 2, 3, 4, 5, 6]

# Loop para remover e imprimir cada item da lista até que ela esteja vazia
while len(minhalista):
    print(minhalista.pop())  # Remove e imprime o último item da lista

# Depois que o loop termina, a lista estará vazia
print(minhalista)  # Saída: []
