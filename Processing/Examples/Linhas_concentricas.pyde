def setup():
    size(300, 300)  # Define o tamanho da janela
    background(255)  # Define o fundo branco
    noFill()  # Desabilita o preenchimento das formas
    noLoop()  # Desenha apenas uma vez

def draw():
    x = 0
    y = 0
    lado = 0
    contador = 0
    while contador < 50:
        lado += 5
        x = width / 2 - lado / 2
        y = height / 2 - lado / 2
        rect(x, y, lado, lado)
        contador += 1  # Incrementa o contador corretamente

# Certifique-se de estar usando um ambiente que suporta Processing.py
