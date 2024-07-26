
# Introdução ao Processing

## Resumo

Este documento introduz os conceitos básicos do Processing, uma ferramenta flexível para aprendizado de programação dentro do contexto das artes visuais. Ele cobre conceitos fundamentais como a configuração do ambiente, a compreensão do sistema de coordenadas e o desenho de formas básicas. Funções chave e seu uso são explicados, fornecendo uma base para a criação de programas visuais.

## Principais Características
- **Configuração do Ambiente**: Aprenda como configurar e configurar o ambiente do Processing.
- **Sistema de Coordenadas**: Compreenda o sistema de coordenadas 2D usado no Processing.
- **Desenho Básico**: Desenhe formas básicas como pontos, linhas, retângulos e elipses.
- **Funções de Cor**: Aplique cores às formas usando as funções `fill` e `stroke`.
- **Interatividade**: Crie esboços interativos usando entradas de mouse e teclado.

## Conteúdo

### Primeiros Passos
Para começar a usar o Processing, você precisa baixar e instalar o Ambiente de Desenvolvimento do Processing (PDE) do [site oficial](https://processing.org/download/). Uma vez instalado, você pode criar seu primeiro esboço abrindo o PDE e escrevendo um programa simples para desenhar uma forma.

### Desenho Básico
O Processing usa um sistema de coordenadas 2D onde o canto superior esquerdo da janela é a origem (0, 0). Você pode desenhar várias formas usando funções incorporadas como `point()`, `line()`, `rect()` e `ellipse()`.

```python
size(480, 120)  # Define o tamanho da janela
line(0, 0, width, height)  # Desenha uma linha do canto superior esquerdo ao canto inferior direito
ellipse(width / 2, height / 2, 60, 60)  # Desenha uma elipse no centro
```

### Funções de Cor
Você pode definir a cor das formas usando as funções `fill()` e `stroke()`. A função `fill()` define a cor interior das formas, enquanto a função `stroke()` define a cor do contorno.

```python
fill(255, 0, 0)  # Define a cor de preenchimento para vermelho
stroke(0, 255, 0)  # Define a cor do contorno para verde
rect(50, 50, 100, 100)  # Desenha um retângulo com as cores especificadas
```

### Interatividade
O Processing permite criar esboços interativos que respondem a entradas do mouse e teclado. Você pode usar variáveis integradas como `mouseX`, `mouseY`, `mousePressed` e `keyPressed` para criar esboços dinâmicos.

```python
def setup():
    size(480, 120)

def draw():
    if mousePressed:
        fill(0)
    else:
        fill(255)
    ellipse(mouseX, mouseY, 50, 50)
```

## Conceitos Ampliados

### Ambiente de Desenvolvimento do Processing (PDE)
O PDE é um IDE (Ambiente de Desenvolvimento Integrado) simplificado que facilita a escrita de código Processing. Ele oferece uma interface amigável para codificação, execução e depuração de seus esboços. Além disso, o PDE fornece acesso a uma rica documentação e exemplos que ajudam a aprender e explorar as funcionalidades do Processing.

### Sistema de Coordenadas
O sistema de coordenadas do Processing é baseado em pixels, com o ponto (0, 0) no canto superior esquerdo da tela. A coordenada X aumenta para a direita e a coordenada Y aumenta para baixo. Entender esse sistema é crucial para posicionar corretamente os elementos gráficos no seu esboço.

### Formas Básicas
Além das formas básicas mencionadas, o Processing permite desenhar arcos, curvas de Bézier e outras formas complexas. Cada função de desenho tem parâmetros específicos que controlam o tamanho, a posição e outros atributos da forma.

### Funções de Cor
As funções `fill()` e `stroke()` aceitam valores RGB para definir as cores. Além disso, você pode usar a função `noFill()` para desenhar formas sem preenchimento e `noStroke()` para desenhar formas sem contorno. O Processing também suporta transparência (alfa) nas cores, permitindo criar efeitos visuais avançados.

### Interatividade Avançada
O Processing oferece uma ampla gama de funções para criar interatividade avançada. Por exemplo, você pode detectar eventos de teclado específicos, rastrear movimentos do mouse em tempo real e responder a cliques do mouse em áreas específicas da tela. Essas funcionalidades permitem criar aplicativos interativos ricos e envolventes.

## Exercícios

1. **Configuração**:
   - Instale o Processing e crie seu primeiro esboço.
   - Configure a tela usando a função `size()` e desenhe uma forma simples como um retângulo.

2. **Sistema de Coordenadas**:
   - Experimente o sistema de coordenadas desenhando formas em diferentes coordenadas.
   - Crie um padrão de grade usando linhas e retângulos.

3. **Formas Básicas**:
   - Desenhe uma combinação de diferentes formas (elipse, retângulo, linha) para formar uma ilustração simples.
   - Use as funções `fill()` e `stroke()` para adicionar cores às suas formas.

4. **Formas Dinâmicas**:
   - Use as variáveis `mouseX` e `mouseY` para fazer com que as formas sigam o cursor.
   - Crie uma animação onde as formas se movem pela tela.

5. **Interatividade**:
   - Implemente interatividade básica usando as funções `mousePressed` e `keyPressed`.
   - Crie um esboço onde pressionar uma tecla muda a cor de uma forma.
