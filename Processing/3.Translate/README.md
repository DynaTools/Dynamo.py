
# Processing Tradução, Rotação e Escalonamento

## Resumo

Este documento explora as transformações no Processing, como translação, rotação e escalonamento de formas. Modificando o sistema de coordenadas, você pode criar vários efeitos e animações. O documento fornece exemplos de como aplicar essas transformações em seus esboços.

## Principais Características
- **Translação**: Movimente formas ao longo do eixo X e Y.
- **Rotação**: Rotacione formas em torno de um ponto.
- **Escalonamento**: Altere o tamanho das formas de maneira proporcional.

## Conteúdo

### Translação
Trabalhar com transformações pode ser complicado, mas a função `translate()` é a mais direta, então começaremos com ela. Esta função pode deslocar o sistema de coordenadas para a esquerda, direita, cima e baixo.

```python
def setup():
    size(120, 120)

def draw():
    translate(mouseX, mouseY)
    rect(0, 0, 30, 30)
```

### Rotação
A função `rotate()` rotaciona o sistema de coordenadas. Ela possui um parâmetro que é o ângulo (em radianos) para rotacionar. Sempre rotaciona em relação ao ponto (0,0).

```python
def setup():
    size(120, 120)

def draw():
    rotate(mouseX / 100.0)
    rect(40, 30, 160, 20)
```

### Escalonamento
A função `scale()` estica as coordenadas na tela. Como as coordenadas expandem ou contraem à medida que a escala muda, tudo o que é desenhado na janela de exibição aumenta ou diminui de dimensão.

```python
def setup():
    size(120, 120)

def draw():
    translate(mouseX, mouseY)
    scale(mouseX / 60.0)
    rect(-15, -15, 30, 30)
```

## Conceitos Ampliados

### Sistema de Coordenadas Modificadas
Ao modificar o sistema de coordenadas padrão, você pode criar várias transformações, incluindo translação, rotação e escalonamento. Isso permite que você mova, gire e escale formas de maneira mais intuitiva e flexível.

### Combinação de Transformações
As transformações podem ser combinadas para criar efeitos complexos. A ordem das transformações é importante e pode afetar o resultado final. Por exemplo, se você mover o sistema de coordenadas e depois rotacionar, o resultado será diferente de rotacionar e depois mover.

```python
def setup():
    size(120, 120)

def draw():
    translate(mouseX, mouseY)
    rotate(radians(45))
    rect(0, 0, 50, 50)
```

### Uso de `pushMatrix()` e `popMatrix()`
Para isolar os efeitos de uma transformação para que não afetem comandos subsequentes, você pode usar as funções `pushMatrix()` e `popMatrix()`. Isso é útil quando transformações são necessárias para uma forma, mas não desejadas para outra.

```python
def setup():
    size(120, 120)

def draw():
    pushMatrix()
    translate(mouseX, mouseY)
    rect(0, 0, 30, 30)
    popMatrix()
    translate(35, 10)
    rect(0, 0, 15, 15)
```

## Exercícios

1. **Translação**:
   - Crie um esboço que mova uma forma pela tela usando a função `translate()`.
   - Experimente transladar várias formas em diferentes direções.

2. **Rotação**:
   - Escreva um programa que rotacione uma forma ao redor de seu centro usando a função `rotate()`.
   - Crie uma animação onde as formas rotacionam continuamente.

3. **Escalonamento**:
   - Desenvolva um esboço que escalona uma forma para cima e para baixo usando a função `scale()`.
   - Combine escalonamento com translação para criar efeitos visuais dinâmicos.

4. **Transformações Combinadas**:
   - Use `translate()`, `rotate()` e `scale()` juntos em um único esboço.
   - Crie uma animação complexa que envolva todas as três transformações.
