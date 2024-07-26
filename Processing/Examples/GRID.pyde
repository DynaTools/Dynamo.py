def setup():
    size(600, 600)
    noLoop()
    background(255)  # Adiciona um fundo branco

def draw():
    lado = 20
    numBlocosHoriz = int(width / lado)
    numBlocosVert = int(height / lado)

    for i in range(numBlocosHoriz):
        for j in range(numBlocosVert):
            x = i * lado
            y = j * lado
            
            if ((i%2) + (j%3))%2 == 0:
                # Se i é par, desenha uma diagonal de cima para baixo
                line(x, y, x + lado, y + lado)
            else:
                # Se i é ímpar, desenha uma diagonal de baixo para cima
                line(x + lado, y, x, y + lado)

# Certifique-se de estar usando um ambiente que suporta Processing.py
