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
        rotate( PI/2)
        rect(0, 0, 120, 12)
        popMatrix()    
        
    def parametros(self):
        return[self.custo, self.pot, self.lm, self.cor]
listLuminaria = []
listCusto = []
total = 0
d = 175
def setup():
    background(255)
    size(700,900)
    noLoop()
    
def draw():
    global total, d
    for i in range((width/4), width, (width/2)):
        for j in range((height/5), height, (height/5)):
            lum1 = Luminaria(i, j, 120, i) #define a posição e a marca da luminária
            lum1.inserirFamilia() #chama a função de desenho
    #       param = lum1.parametros() #chama a função de parâmetros 
    #       listLuminaria.append(lum1) #adiciona a instância lum1 a lista de luminárias
    #       listLuminaria.append(param) #adiciona na lista de luminarias os parâmetros daquela instância. 
        
    #       custos = param[0] #extrai apenas o primeiro item da lista
    #       listCusto.append(custos)
     
    #    for c in listCusto:
    #        total += c
    #    print(total)
    
