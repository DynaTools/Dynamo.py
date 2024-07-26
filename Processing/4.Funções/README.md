
# Processing Funções

## Resumo

Este documento foca nas funções no Processing, explicando como definir e usar funções para organizar e reutilizar código. Ele cobre a sintaxe para criar funções, passar parâmetros e retornar valores.

## Principais Características
- **Definição de Funções**: Aprenda a criar funções e definir seu comportamento.
- **Passagem de Parâmetros**: Entenda como passar parâmetros para funções para aumentar a flexibilidade.
- **Retorno de Valores**: Veja como funções podem retornar valores para o programa principal.

## Conteúdo

### Conceitos Básicos de Funções
As funções são os blocos básicos de construção para programas em Processing. Elas permitem modularidade, abstração e reutilização de código. Funções são independentes e podem ser usadas para construir programas mais complexos.

```python
def setup():
    print("Pronto para rolar!")
    rollDice(20)
    rollDice(20)
    rollDice(6)
    print("Terminou.")

def rollDice(numSides):
    d = 1 + int(random(numSides))
    print("Rolando...", d)
```

### Exemplo: Rolando os Dados
Este exemplo ilustra como uma função pode ser usada para gerar um número aleatório como se estivesse rolando um dado com um número específico de lados.

### Exemplo: Outra Maneira de Rolar
Se um programa equivalente fosse escrito sem a função `rollDice()`, ele poderia parecer assim:

```python
def setup():
    print("Pronto para rolar!")
    d1 = 1 + int(random(20))
    print("Rolando...", d1)
    d2 = 1 + int(random(20))
    print("Rolando...", d2)
    d3 = 1 + int(random(6))
    print("Rolando...", d3)
    print("Terminou.")
```

### Criando Funções
Funções podem ser usadas para desenhar formas complexas repetidamente. Por exemplo, podemos desenhar uma coruja definindo uma função específica para isso.

```python
def setup():
    size(480, 120)

def draw():
    background(176, 204, 226)
    owl(110, 110)
    owl(180, 110)

def owl(x, y):
    pushMatrix()
    translate(x, y)
    stroke(138, 138, 125)
    strokeWeight(70)
    line(0, -35, 0, -65)  # Corpo
    noStroke()
    fill(255)
    ellipse(-17.5, -65, 35, 35)  # Olho esquerdo
    ellipse(17.5, -65, 35, 35)  # Olho direito
    arc(0, -65, 70, 70, 0, PI)  # Queixo
    fill(51, 51, 30)
    ellipse(-14, -65, 8, 8)  # Olho esquerdo
    ellipse(14, -65, 8, 8)  # Olho direito
    quad(0, -58, 4, -51, 0, -44, -4, -51)  # Bico
    popMatrix()
```

### Funções com Parâmetros
Adicionar parâmetros às funções aumenta a flexibilidade, permitindo que a mesma função seja usada para diferentes entradas.

```python
def setup():
    size(480, 120)

def draw():
    background(176, 204, 226)
    for x in range(35, width + 70, 70):
        owl(x, 110)

def owl(x, y):
    pushMatrix()
    translate(x, y)
    stroke(138, 138, 125)
    strokeWeight(70)
    line(0, -35, 0, -65)  # Corpo
    noStroke()
    fill(255)
    ellipse(-17.5, -65, 35, 35)  # Olho esquerdo
    ellipse(17.5, -65, 35, 35)  # Olho direito
    arc(0, -65, 70, 70, 0, PI)  # Queixo
    fill(51, 51, 30)
    ellipse(-14, -65, 8, 8)  # Olho esquerdo
    ellipse(14, -65, 8, 8)  # Olho direito
    quad(0, -58, 4, -51, 0, -44, -4, -51)  # Bico
    popMatrix()
```

### Retornando Valores
Funções também podem realizar cálculos e retornar valores para o programa principal.

```python
def setup():
    yourWeight = 132.0
    marsWeight = calculateMars(yourWeight)
    print(marsWeight)

def calculateMars(w):
    newWeight = w * 0.38
    return newWeight
```

## Exercícios

1. **Definindo Funções**:
   - Escreva uma função que desenha uma forma específica e a chame em seu esboço.
   - Experimente mudar os parâmetros da função para desenhar diferentes variações da forma.

2. **Usando Parâmetros**:
   - Crie uma função que aceita parâmetros para controlar a posição e tamanho de uma forma.
   - Chame a função várias vezes com diferentes argumentos para criar um padrão.

3. **Retornando Valores**:
   - Escreva uma função que realiza um cálculo e retorna o resultado.
   - Use o valor retornado em seu esboço para controlar um aspecto do desenho.

4. **Organizando Código**:
   - Refatore um esboço existente, dividindo-o em várias funções.
   - Certifique-se de que cada função tenha um propósito claro e seja usada para simplificar o laço principal `draw()`.
