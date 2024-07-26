class Luminaria:
    def __init__(self, posx, posy, h, mark):
        self.posx = posx 
        self.posy = posy
        self.h = h
        self.custo = int(980)
        self.pot = '980VA'
        self.lm = '1100lm'
        self.cor = '3000K'
        self.mark = mark
        
    def inserirFamilia(self):
        rectMode(CENTER)
        fill('#3C3ADE')
        pushMatrix()
        translate(self.posx, self.posy)
        rotate(PI/2)
        rect(0, 0, 120, 12)
        popMatrix()    
        
    def parametros(self):
        return [self.custo, self.pot, self.lm, self.cor]

def setup():
    size(800, 800)
    background(255)
    noLoop()

def draw():
    # Definir as duas curvas (como exemplo, uso linhas retas para simplificação)
    # para coletar as curvas no Dynamo usa-se o GetIsoLines 
    curve1 = [(100, 100), (700, 100)]  # Linha horizontal no topo
    curve2 = [(100, 100), (100, 700)]  # Linha vertical à esquerda
    
    # Número de colunas
    ncolunaX = 2
    ncolunaY = 3
    
    # Obter pontos ao longo das curvas
    pointsCurve1 = get_points(curve1, ncolunaX)
    pointsCurve2 = get_points(curve2, ncolunaY)
    
    # Encontrar os pontos de interseção e desenhar
    for pt1 in pointsCurve1:
        for pt2 in pointsCurve2:
            # Cria um ponto na interseção das coordenadas X de pt1 e Y de pt2 #só funciona se as curvas possuem a mesma origem
            intersectionPoint = (pt1[0], pt2[1])
            draw_shapes(intersectionPoint)

def get_points(curve, ncolunas):
    points = []
    for i in range(ncolunas + 1):
        param = i / float(ncolunas)
        x = lerp(curve[0][0], curve[1][0], param)  #lerp(100, 700, param) equivale a [100 + (700-100) * param ], esse é o primeiro X
        y = lerp(curve[0][1], curve[1][1], param)
        points.append((x, y))
    return points

def draw_shapes(pt):
    # Criar e inserir uma instância da Luminaria no ponto de interseção
    luminaria = Luminaria(pt[0], pt[1], 0, 'Marca X')
    luminaria.inserirFamilia()

# Executar o código no Processing Python Mode
