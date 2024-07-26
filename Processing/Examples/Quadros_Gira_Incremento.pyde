p1 = 0.1
p2 = 0.1

def setup():
    size(600, 600)  # Define o tamanho da janela
    background(255, 200, 180)  # Define a cor de fundo inicial (uma cor de tom pastel)
    global angle, radius, r, g, b
    angle = 0
    radius = 0
    # Definir a primeira cor pastel
    r = random(100, 255)
    g = random(100, 255)
    b = random(100, 255)
    fill(r, g, b)

def quadrado(x, y):
    rect(x, y, 10, 10)  # Desenha um quadrado na posição (x, y) com tamanho 10x10

def draw():
    global angle, radius, r, g, b
    translate(width / 2, height / 2)  # Move a origem para o centro da tela
    translate(radius * cos(angle), radius * sin(angle))  # Move a posição do quadrado
    
    quadrado(-5, -5)  # Desenha o quadrado com seu centro na posição atual
    
    angle += 0.2  # Incrementa o ângulo
    radius += 0.2  # Incrementa o raio para criar a espiral
    
