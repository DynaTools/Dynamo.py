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
