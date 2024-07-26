
# Processing Listas

## Resumo

Este documento introduz listas no Processing, uma estrutura de dados que permite armazenar e manipular coleções de valores. Ele explica como criar, acessar e modificar listas, e fornece exemplos de uso de listas para gerenciar múltiplos elementos em um esboço.

## Principais Características
- **Criação de Listas**: Aprenda a criar listas e adicionar elementos a elas.
- **Acesso a Elementos**: Entenda como acessar elementos individuais em uma lista.
- **Modificação de Listas**: Veja como modificar elementos em uma lista e realizar operações em todos os elementos.
- **Iteração com Listas**: Use loops para iterar através de listas e realizar operações em seus elementos.

## Conteúdo

### De Variáveis a Listas
Quando um programa precisa rastrear uma ou duas coisas, não é necessário usar uma lista. No entanto, quando um programa tem muitos elementos, as listas tornam o código mais fácil de escrever e entender.

```python
x1 = -20.0
x2 = 20.0

def setup():
    size(240, 120)
    noStroke()

def draw():
    global x1, x2
    background(0)
    x1 += 0.5
    x2 += 0.5
    arc(x1, 30, 40, 40, 0.52, 5.76)
    arc(x2, 90, 40, 40, 0.52, 5.76)
```

### Muitas Variáveis
Adicionar mais variáveis pode tornar o código complicado rapidamente.

```python
x1 = -10.0
x2 = 10.0
x3 = 35.0
x4 = 18.0
x5 = 30.0

def setup():
    size(240, 120)
    noStroke()

def draw():
    global x1, x2, x3, x4, x5
    background(0)
    x1 += 0.5
    x2 += 0.5
    x3 += 0.5
    x4 += 0.5
    x5 += 0.5
    arc(x1, 20, 20, 20, 0.52, 5.76)
    arc(x2, 40, 20, 20, 0.52, 5.76)
    arc(x3, 60, 20, 20, 0.52, 5.76)
    arc(x4, 80, 20, 20, 0.52, 5.76)
    arc(x5, 100, 20, 20, 0.52, 5.76)
```

### Listas, Não Variáveis
Em vez de criar muitas variáveis, podemos usar uma lista.

```python
x = []

def setup():
    size(240, 120)
    noStroke()
    fill(255, 200)
    for i in range(3000):
        x.append(random(-1000, 200))

def draw():
    background(0)
    for i in range(len(x)):
        x[i] += 0.5
        y = i * 0.4
        arc(x[i], y, 12, 12, 0.52, 5.76)
```

### Operações com Listas
Cada item em uma lista é chamado de elemento, e cada um tem um valor de índice para marcar sua posição dentro da lista. Os valores de índice começam em 0.

```python
x = [5, 10, 15, 20]
print(x[0])  # imprime 5
print(x[1])  # imprime 10
print(x[2])  # imprime 15
print(x[3])  # imprime 20
```

### Manipulação de Listas
Após a criação da lista, você pode sobrescrever o valor de um item em um índice específico.

```python
x = [5, 10, 15, 20]
print(x[2])  # imprime 15
x[2] = 789
print(x[2])  # imprime 789
```

### Comprimento de uma Lista
Para determinar o comprimento de uma lista, use a função `len()`.

```python
x = [5, 10, 15, 20]
print(len(x))  # imprime 4
y = []
print(len(y))  # imprime 0
```

### Repetição e Listas
O loop `for` torna mais fácil trabalhar com grandes listas enquanto mantém o código conciso.

```python
gray = []

def setup():
    size(240, 120)
    for i in range(width):
        gray.append(random(0, 255))

def draw():
    for i in range(len(gray)):
        stroke(gray[i])
        line(i, 0, i, height)
```

### Rastreamento dos Movimentos do Mouse
Armazene a posição do mouse em duas listas e desenhe elipses para visualizar o movimento.

```python
x = []
y = []

def setup():
    size(240, 120)
    noStroke()

def draw():
    background(0)
    x.insert(0, mouseX)
    y.insert(0, mouseY)
    for i in range(len(x)):
        fill(i * 4)
        ellipse(x[i], y[i], 40, 40)
```

### Listas de Objetos
Crie uma lista de objetos e atualize e exiba cada um dentro de `draw()`.

```python
class JitterBug:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def move(self):
        self.x += random(-1, 1)
        self.y += random(-1, 1)

    def display(self):
        ellipse(self.x, self.y, self.r, self.r)

bugs = []

def setup():
    size(240, 120)
    for i in range(33):
        x = random(width)
        y = random(height)
        r = i + 2
        bugs.append(JitterBug(x, y, r))

def draw():
    for bug in bugs:
        bug.move()
        bug.display()
```

## Exercícios

1. **Criando Listas**:
   - Crie uma lista de números e imprima seus elementos.
   - Experimente com diferentes tipos de dados, como strings ou objetos.

2. **Acessando Elementos**:
   - Escreva um programa que itera através de uma lista e realiza uma operação em cada elemento.
   - Use uma lista para armazenar as posições de várias formas e desenhá-las na tela.

3. **Modificando Listas**:
   - Desenvolva um esboço que adiciona ou remove elementos de uma lista com base na entrada do usuário.
   - Implemente uma lista dinâmica que cresce ou encolhe durante a execução do esboço.

4. **Operações Avançadas com Listas**:
   - Crie um programa que classifica ou filtra uma lista com base em critérios específicos.
   - Use listas aninhadas para gerenciar estruturas de dados mais complexas.
