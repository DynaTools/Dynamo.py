
# Processing Variáveis

## Resumo

Este documento explora o conceito de variáveis no Processing. As variáveis armazenam valores na memória para uso posterior em um programa, tornando o código mais flexível e fácil de atualizar. O documento explica como criar e usar variáveis, demonstra diferentes tipos de dados e mostra como aplicar variáveis em vários cenários de programação.

## Principais Características
- **Criação de Variáveis**: Aprenda a criar variáveis e atribuir valores a elas.
- **Tipos de Dados**: Entenda os diferentes tipos de dados que podem ser armazenados em variáveis.
- **Uso de Variáveis**: Saiba como usar variáveis para controlar elementos gráficos em um esboço.
- **Operações Matemáticas**: Realize operações matemáticas com variáveis.
- **Laços e Variáveis**: Combine laços com variáveis para criar padrões e estruturas repetitivas.

## Conteúdo

### Criando Variáveis
Uma variável armazena um valor na memória para que possa ser usado posteriormente em um programa. A variável pode ser usada várias vezes dentro de um único programa, e o valor é facilmente alterado enquanto o programa está em execução.

### Primeiras Variáveis
Uma das razões pelas quais usamos variáveis é evitar a repetição de código. Se você estiver digitando o mesmo número mais de uma vez, considere transformá-lo em uma variável para tornar seu código mais geral e fácil de atualizar.

```python
size(480, 120)
y = 60
d = 80
ellipse(75, y, d, d)    # Esquerda
ellipse(175, y, d, d)   # Centro
ellipse(275, y, d, d)   # Direita
```

### Mudança de Valores
Basta mudar as variáveis `y` e `d` para alterar todas as elipses:

```python
size(480, 120)
y = 100
d = 130
ellipse(75, y, d, d)    # Esquerda
ellipse(175, y, d, d)   # Centro
ellipse(275, y, d, d)   # Direita
```

### Tipos de Dados
Ao criar suas próprias variáveis, você determina o nome e o valor. O nome é o que você decide chamar a variável. Escolha um nome que seja informativo sobre o que a variável armazena. O tipo de dados define o tipo de valor que a variável pode armazenar, como números inteiros, números decimais, palavras, imagens, fontes, etc.

### Variáveis no Processing
O Processing possui uma série de variáveis especiais para armazenar informações sobre o programa enquanto ele está em execução. Por exemplo, a largura e a altura da janela são armazenadas nas variáveis `width` e `height`.

```python
size(480, 120)
line(0, 0, width, height)  # Linha do canto superior esquerdo ao inferior direito
line(width, 0, 0, height)  # Linha do canto superior direito ao inferior esquerdo
ellipse(width/2, height/2, 60, 60)
```

### Um Pouco de Matemática
Pessoas muitas vezes assumem que matemática e programação são a mesma coisa. Embora o conhecimento de matemática possa ser útil para certos tipos de codificação, a aritmética básica cobre as partes mais importantes.

```python
size(480, 120)
x = 25
h = 20
y = 25
rect(x, y, 300, h)        # Topo
x = x + 100
rect(x, y + h, 300, h)    # Meio
x = x - 250
rect(x, y + h*2, 300, h)  # Inferior
```

### Operadores Matemáticos
Símbolos como `+`, `-`, e `*` são chamados de operadores. Quando colocados entre dois valores, eles criam uma expressão.

```python
x = 4 + 4 * 5  # Atribui 24 a x
```

### Repetição
À medida que você escreve mais programas, perceberá que padrões ocorrem quando linhas de código são repetidas, mas com pequenas variações. Um laço `for` permite executar uma linha de código mais de uma vez para condensar esse tipo de repetição em menos linhas.

```python
size(480, 120)
strokeWeight(8)
for i in range(20, 400, 60):
  line(i, 40, i + 60, 80)
```

## Conceitos Ampliados

### Trabalhando com Variáveis
Ao trabalhar com variáveis, é importante compreender como elas são armazenadas e manipuladas na memória. As variáveis podem armazenar diferentes tipos de dados, incluindo inteiros (`int`), números de ponto flutuante (`float`), strings (`String`), e objetos (`Object`). O tipo de dados determina as operações que podem ser realizadas na variável e como ela é armazenada na memória.

### Escopo das Variáveis
O escopo de uma variável refere-se à parte do programa onde a variável pode ser acessada. Variáveis globais são definidas fora de qualquer função e podem ser acessadas em qualquer parte do programa. Variáveis locais são definidas dentro de uma função e só podem ser acessadas dentro dessa função. Entender o escopo é crucial para evitar erros de lógica e garantir que o programa funcione conforme o esperado.

### Manipulação de Dados
O Processing permite a manipulação avançada de dados usando variáveis. Você pode realizar operações matemáticas complexas, manipular strings e trabalhar com estruturas de dados como listas e dicionários. Isso permite criar programas mais dinâmicos e interativos, que podem responder a diferentes tipos de entrada do usuário e gerar saídas variadas.

### Laços e Iterações
Laços são estruturas de controle que permitem executar um bloco de código várias vezes. O Processing suporta diferentes tipos de laços, incluindo `for`, `while`, e `do-while`. Esses laços são essenciais para criar animações, processar listas de dados e repetir operações de maneira eficiente.

### Entrada do Usuário
O Processing oferece várias maneiras de capturar a entrada do usuário, incluindo o uso do mouse e teclado. Você pode usar variáveis integradas como `mouseX`, `mouseY`, `key`, e `keyCode` para criar programas interativos que respondem às ações do usuário em tempo real.

## Exercícios

1. **Criando Variáveis**:
   - Defina diferentes tipos de variáveis (`int`, `float`, `String`) e imprima seus valores.
   - Crie um esboço que usa variáveis para controlar a posição e o tamanho das formas.

2. **Usando Variáveis**:
   - Modifique um esboço existente para usar variáveis em vez de valores codificados.
   - Experimente mudar os valores das variáveis para ver como isso afeta o esboço.

3. **Matemática com Variáveis**:
   - Escreva um programa que realiza operações aritméticas básicas usando variáveis.
   - Crie um esboço dinâmico onde as variáveis são atualizadas com base em expressões matemáticas.

4. **Variáveis Especiais**:
   - Use variáveis integradas do Processing como `width`, `height`, `mouseX` e `mouseY` em um esboço.
   - Crie um esboço interativo que responda aos movimentos do mouse usando essas variáveis.

5. **Laços e Variáveis**:
   - Combine laços `for` com variáveis para criar padrões.
   - Desenvolva um esboço que use laços aninhados e variáveis para desenhar uma grade de formas.
