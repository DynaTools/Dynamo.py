
# Processing Respostas

## Resumo

Este documento discute como lidar com entrada do usuário e respostas no Processing. Inclui exemplos de uso de eventos de mouse e teclado para criar esboços interativos que respondem às ações do usuário.

## Principais Características
- **Entrada do Mouse**: Aprenda a rastrear a posição do mouse e responder a cliques.
- **Entrada do Teclado**: Veja como capturar pressionamentos de teclas e responder a eles.
- **Interatividade**: Crie esboços dinâmicos que respondem às ações do usuário em tempo real.

## Conteúdo

### A Função draw()
O código dentro do bloco `draw()` é executado de cima para baixo e depois repete até que você saia do programa clicando no botão Parar ou fechando a janela. Cada execução do `draw()` é chamada de frame. A taxa de frames padrão é de 60 frames por segundo, mas isso pode ser alterado.

```python
def draw():
    print("Estou desenhando")
    print(frameCount)
```

### Função setup()
A função `setup()` é executada apenas uma vez quando o programa inicia, e é usada para definir os valores iniciais.

```python
def setup():
    print("Estou começando")
def draw():
    print("Estou rodando")
```

### Variáveis Globais
Variáveis declaradas fora de `setup()` e `draw()` são globais e podem ser usadas em qualquer lugar do programa.

```python
x = 280
y = -100
diameter = 380

def setup():
    size(480, 120)
    fill(102)

def draw():
    background(204)
    ellipse(x, y, diameter, diameter)
```

### Rastreamento do Mouse
A variável `mouseX` armazena a coordenada X do mouse, e `mouseY` armazena a coordenada Y.

```python
def setup():
    size(480, 120)
    fill(0, 102)
    noStroke()

def draw():
    ellipse(mouseX, mouseY, 9, 9)
```

### Atualizando a Tela Continuamente
Para atualizar a tela e exibir apenas o círculo mais recente, coloque a função `background()` no início de `draw()`.

```python
def setup():
    size(480, 120)
    fill(0, 102)
    noStroke()

def draw():
    background(204)
    ellipse(mouseX, mouseY, 9, 9)
```

### Espessura Dinâmica das Linhas
As variáveis `pmouseX` e `pmouseY` armazenam a posição do mouse no frame anterior. Elas podem ser usadas para desenhar linhas contínuas.

```python
def setup():
    size(480, 120)
    strokeWeight(4)
    stroke(0, 102)

def draw():
    line(mouseX, mouseY, pmouseX, pmouseY)
```

### Suavização dos Movimentos
A técnica de easing faz com que os valores sigam o mouse de forma mais suave, criando um movimento fluido.

```python
x = 0.0
easing = 0.01

def setup():
    size(220, 120)

def draw():
    global x
    targetX = mouseX
    x += (targetX - x) * easing
    ellipse(x, 40, 12, 12)
    print(targetX, x)
```

### Modificando Variáveis Globais
Para modificar o valor de uma variável global dentro de uma função, use a palavra-chave `global`.

```python
x = 0

def draw():
    global x
    x = x + 1
    ellipse(x, height / 2, 10, 10)
```

### Verificando Cliques do Mouse
A variável `mousePressed` indica se o botão do mouse está pressionado (True) ou não (False).

```python
def setup():
    size(240, 120)
    strokeWeight(30)

def draw():
    background(204)
    stroke(102)
    line(40, 0, 70, height)
    if mousePressed:
        stroke(0)
        line(0, 70, width, 50)
```

### Detectando Diferentes Botões do Mouse
A variável `mouseButton` pode ter três valores: `LEFT`, `CENTER` ou `RIGHT`.

```python
def setup():
    size(120, 120)
    strokeWeight(30)

def draw():
    background(204)
    stroke(102)
    line(40, 0, 70, height)
    if mousePressed:
        if mouseButton == LEFT:
            stroke(255)
        else:
            stroke(0)
        line(0, 70, width, 50)
```

### Verificando a Localização do Cursor
Para verificar se o cursor está dentro de uma área específica, use expressões relacionais.

```python
x = 80
y = 30
w = 80
h = 60

def setup():
    size(240, 120)

def draw():
    background(204)
    if mouseX > x and mouseX < x + w and mouseY > y and mouseY < y + h:
        fill(0)
    else:
        fill(255)
    rect(x, y, w, h)
```

### Entrada do Teclado
A variável `keyPressed` é True quando qualquer tecla é pressionada, e `key` armazena a última tecla pressionada.

```python
def setup():
    size(240, 120)

def draw():
    background(204)
    line(20, 20, 220, 100)
    if keyPressed:
        line(220, 20, 20, 100)
```

### Mapear Valores
A função `map()` converte uma variável de uma faixa de números para outra.

```python
def setup():
    size(240, 120)
    strokeWeight(12)

def draw():
    background(204)
    stroke(102)
    line(mouseX, 0, mouseX, height)  # Linha cinza
    stroke(0)
    mx = map(mouseX, 0, width, 60, 180)
    line(mx, 0, mx, height)  # Linha preta
```

## Exercícios

1. **Entrada do Mouse**:
   - Crie um esboço que muda a cor de uma forma quando o mouse é pressionado.
   - Use `mouseX` e `mouseY` para fazer com que formas sigam o cursor.

2. **Entrada do Teclado**:
   - Escreva um programa que mova uma forma com base nas teclas de seta pressionadas.
   - Implemente controles adicionais do teclado para mudar a cor ou tamanho da forma.

3. **Desenho Interativo**:
   - Desenvolva um esboço onde os usuários podem desenhar na tela com o mouse.
   - Adicione atalhos de teclado para mudar a ferramenta ou cor de desenho.

4. **Interações Complexas**:
   - Combine entradas de mouse e teclado para criar uma aplicação interativa mais complexa.
   - Implemente um jogo simples ou uma ferramenta criativa de desenho.
