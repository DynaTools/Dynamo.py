def setup():
    size(800, 800)
    background(255)
    
    # Criando uma forma personalizada (um retângulo com bordas arredondadas)
    shape1 = createShape(RECT, 150, 150, 200, 100, 20, 20, 20, 20)
    shape1.setFill(color(255, 0, 0))  # Cor de preenchimento vermelho
    shape1.setStroke(color(0))  # Cor da borda preta
    shape1.setStrokeWeight(2)  # Espessura da borda
    
    # Criando uma forma personalizada (um triângulo)
    shape2 = createShape()
    shape2.beginShape()
    shape2.vertex(500, 150)
    shape2.vertex(550, 250)
    shape2.vertex(450, 250)
    shape2.endShape(CLOSE)
    shape2.setFill(color(0, 255, 0))  # Cor de preenchimento verde
    shape2.setStroke(color(0))  # Cor da borda preta
    shape2.setStrokeWeight(2)  # Espessura da borda

    # Exibindo as formas na tela
    shape(shape1)
    shape(shape2)
