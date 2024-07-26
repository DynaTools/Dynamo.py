
# (PT-BR) 

# Curso de Dynamo - Python 

# INTRODUÇÃO

Modelagem da Informação da Construção (em inglês, Building Information Modeling - BIM) está cada vez mais presente e trouxe grandes mudanças na arquitetura, engenharia e construção (AEC), pois trata-se de uma representação tridimensional fiel de uma edificação (JANSSEN, 2015; WEN et al., 2021):

> Quando completo, o modelo gerado computacionalmente contém a geometria precisa e os dados relevantes, necessários para dar suporte à construção, à fabricação e ao fornecimento de insumos necessários para a realização da construção (EASTMAN et al., 2018, tradução nossa).

Os modelos BIM são desenvolvidos através de plataformas conhecidas como paramétricas, baseadas em objetos. Possuem um tipo de inteligência ou comportamento de projeto (em inglês, design behavior) (EASTMAN et al., 2018). Por exemplo, ao modelar um elemento parede, a mesma estará automaticamente identificada na lista de quantidades e nos cortes associados. Outra característica paramétrica está na inserção dos elementos, uma porta só poderá ser inserida em um elemento parede, e este, por sua vez, terá a área de material imediatamente removida dos metadados.

Este tipo de inteligência paramétrica está ausente em programas de modelagem CAD. Estes necessitam que o projetista identifique o elemento, preenchendo a propriedade associada. No exemplo citado anteriormente, a porta poderá ser inserida em qualquer ponto do modelo CAD sem que isso gere qualquer identificação de erro, assim como cortes precisarão ser atualizados quando ocorrerem mudanças na planta baixa.

Os limites e usabilidades de programas CAD e BIM podem variar em um projeto e os benefícios devem ser avaliados pela equipe envolvida. Apesar das disponibilidades de diversas ferramentas CAD e BIM, o projetista poderá ser confrontado, eventualmente, com uma necessidade de buscar o apoio da programação como solução de expansão de funcionalidade dos softwares (LANDIM, 2019). A programação visual ou visual programming language (VPL) é o nome que se dá para qualquer tipo de linguagem de programação possível de se manipular em um formato gráfico (NOONE; MOONEY, 2017). Uma das características positivas desta forma de programar é o retorno visual instantâneo do resultado ao projetista (LANDIM, 2019 apud CELANI;VAZ, 2012), sem a necessidade de compilar códigos complexos com domínio dos conceitos de programação e criação de algoritmos.

Pesquisas indicam que o uso da VPL apresenta benefícios ao projetista em relação à programação textual (NOONE; MOONEY, 2017), em especial àqueles que necessitam de mais feedbacks visuais de seu processo. A VPL melhora a capacidade de enxergar opções de parametrização dentro de projetos. Esta forma de pensar é classificada como pensamento paramétrico (WURZER; ALAÇAM; LORENZ, 2011). O projetista, ao desenvolver este raciocínio, começa de forma abstrata a conceber conexões entre elementos do projeto que pode ser traduzido em algoritmos.

Algoritmos são o conjunto de regras, operações e procedimentos definidos, ordenados e usados na solução de um problema em um número finito de etapas (ALGORITMO, 2021). Portanto, a ordem e organização de informações são cruciais para que o projetista produza bons resultados. É importante que o projetista tenha conhecimento sobre os tipos e classificações das ferramentas que utiliza no projeto, pois pode tomar decisões mais informadas sobre quando utilizar um determinado software, tecnologia ou linguagem de programação durante o desenvolvimento do projeto.

# PROBLEMA DE PESQUISA E METODOLOGIA

Os cursos existentes que se propõem a ensinar o uso das interfaces de programação visual como Grasshopper e Dynamo são excelentes meios de introduzir o projetista nas ferramentas de design paramétrico. Encontramos diversos cursos rápidos destas ferramentas disponíveis nas plataformas Linkedin Learning e Udemy, por exemplo. Esses cursos possuem conteúdos que ensinam o projetista a utilizar a interface dos programas de linguagem visual. Observamos que o conteúdo é direcionado a ensinar através de exemplos práticos que complementam funcionalidades que não estão presentes nos programas BIM por padrão (JANSSEN, 2015).

Como ilustra a figura abaixo, os cursos têm focado em ensinar os alunos a sintaxe da linguagem, ou seja, as regras que determinam quais combinações de nós geram funções úteis, como os construtores operam com os tipos de dados, quais são os símbolos e pontuações aceitas para declarar variáveis e listas de dados, etc. Desta maneira, os cursos têm se configurado como um conjunto de rotinas prontas que podem ser ensinadas para que os alunos comecem a entender o funcionamento da interface através destes exemplos.

De maneira prática, isto torna o conteúdo do curso objetivo e funcional. Entretanto, deixar o aluno focado na ferramenta ou no aprendizado da interface, não garante que entenda um arcabouço teórico-prático que fornece autonomia para que pense nos fluxos de projeto.

### Figura 01 - Curso do Linkedin Learning - Dynamo Essential Training
![image](https://github.com/user-attachments/assets/a906a0ce-2eae-4cda-8d2f-45f0fbda94d8)

O curso pode ser rico em exemplos, mas sem uma estrutura lógica, o aluno fica restrito às possibilidades que foram apresentadas em aula. Aprender sobre a estrutura das linguagens de programação para além de uma linguagem específica como Dynamo ou Grasshopper pode ajudar o projetista a entender qual pode ser a melhor estratégia de projeto computacional para resolver um determinado problema. Isso também garante que o conhecimento aprendido no percurso possa ser reaproveitado a longo prazo, pois VPLs específicas podem mudar ou se tornar obsoletas.

Se o aluno conhecer os conceitos que estruturam VPLs em um contexto mais ampliado e em diálogo com as linguagens de programação textual, ele estará melhor preparado para estas mudanças e adaptações (LEITÃO, 2013). Além disso, existem algumas diferenças fundamentais nas necessidades que um projetista mais focado em BIM precisa alcançar nos fluxos de trabalho baseados nesta tecnologia:

- Em BIM, não é frequente o uso da VPL Dynamo para testar concepção formal de projetos, sejam formas complexas, simples ou orgânicas. Esta fase de investigação formal é geralmente feita em outros programas tridimensionais ou usando a VPL Grasshopper, que possuem funções mais adaptadas para esta fase de projeto, e são posteriormente conectadas para fluxos BIM.
- Ferramentas BIM já possuem um nível de parametria incorporado por padrão. Eastman et al. (2018) chama este comportamento inteligente de design behavior:

> A gama de regras que podem ser incorporadas em um gráfico paramétrico determina a generalidade do sistema. As famílias de objetos paramétricos são definidas usando parâmetros e as relações entre os parâmetros. Uma vez que as relações restringem o comportamento do projeto de um modelo paramétrico, a modelagem paramétrica também é conhecida como modelagem de restrição (EASTMAN et al., 2018, p.39).

Isso ilustra que programadores de VPL BIM não precisam criar códigos que restrinjam as relações entre os objetos ou componentes de um modelo, como geralmente é feito por usuários de Grasshopper num primeiro momento, uma vez que o sistema BIM já traz essa solução incorporada.

# TAXONOMIA DOS MODELOS PARAMÉTRICOS

Quando um curso de ciência da computação é bem delineado e desenvolvido, qualquer um pode aprender a programar (LEITÃO, 2013). Nesta linha, buscamos estruturar o curso com base na taxonomia de Patrick Janssen e Rudi Stouffs, formando assim a primeira bibliografia proposta ao aluno de VPL no começo do seu curso. Existem muitos softwares BIM no mercado e, às vezes, chamá-los de programa BIM, programa paramétrico ou programa de modelagem paramétrica pode não ser suficiente se desejamos comparar e classificar os mesmos.

Em *Types of Parametric Modelling*, os autores determinam um Modelo Geral Paramétrico (em inglês, General Parametric Model (GPM)) como primeira estrutura da classificação.

O GPM é descrito utilizando um conceito matemático comum na ciência da computação, o grafo acíclico dirigido ou directed acyclic graph (DAG) (figura 01). DAG é um gráfico contendo grafos dirigidos sem qualquer tipo de ciclo (DIRECTED, 2021). Não é possível ir e voltar diversas vezes pelo mesmo nó, ou seja, fazer recursão de dados.

### Figura 01 - Grafo Acíclico Dirigido
![Grafo Acíclico Dirigido](https://github.com/user-attachments/assets/2b17f4e8-ab94-4962-9aac-dcfadbd9a743)
**Fonte**: Extraído de Wikipédia¹ 

Considerando que arquitetos, engenheiros e projetistas não têm educação formal em programação, mas estão sendo introduzidos nela através das linguagens de programação visual (VPL), o conceito de iteração de dados pode se tornar muito abstrato e atrapalhar o envolvimento do aluno com o assunto. Desta maneira, para atingir o entendimento do processo com exemplos mais acessíveis, o conceito pode ser simplificado se criarmos um paralelo com um moedor de carne:
¹Disponível em: <https://en.wikipedia.org/wiki/Directed_acyclic_graph>. Acesso em: 15 jul. 2021.

Os autores classificam as VPLs (que por sua vez são descritas como Grafos Acíclicos Dirigidos) pela maneira como iteram dados. Os tipos de iteração de dados são:

- **Iteração simples:** Imaginemos um sistema (figura 03) onde o operador (nó 01) insira a carne em diversos moedores de uma vez (nó 02) e o resultado cairá em um conjunto de recipientes (nó 03). Esse processo é chamado de iteração simples num modelo paramétrico geral.

- **Iteração múltipla implícita:** Caso a iteração simples não seja suficiente, podemos colocar mais uma linha (figura 04) de moedores dentro do sistema de moedores, chamamos isso de listas de listas (nested list). Esse processo é chamado de iteração múltipla implícita.

- **Iteração múltipla explícita:** Por último, se desejarmos mais um tipo de iteração (figura 05), podemos colocar um tempero especial (nó 04) para cada entrada. Esse tipo de nó especial (for each) faz parte da iteração múltipla explícita. Os autores ainda subdividem essa iteração, entretanto, para nosso propósito, paramos nessa simplificação.

As iterações formam a base para a taxonomia de modelos paramétricos descritos a seguir:

- **Modelagem de Objetos:** Programas que não permitem nenhum tipo de iteração, por exemplo, programas CAD.
- **Modelagem de Associação:** Descrição que envolve uma única rodada de iterações (figura 03), por exemplo, o programa Autodesk Revit.
- **Modelagem de Fluxo de Dados:** Programas que permitem iteração implícita utilizando listas dentro de listas, figura 04, por exemplo, o Grasshopper para Rhino3D e Generative Components da Bentley.
- **Modelagem com base em Procedimentos:** Programas que permitem iteração explícita, figura 05, por exemplo, o Dynamo BIM.

Estes tipos de iteração, e por sua vez os tipos de modelagem que as suportam, são importantes para entendermos a estrutura, tanto das VPLs usadas na área, quanto dos tipos de modelagem suportadas por programas considerados paramétricos. A seguir, nos concentraremos nas especificidades dos fluxos paramétricos BIM.

# FLUXO PARAMÉTRICO BIM

O termo fluxo paramétrico BIM (em inglês, Parametric BIM Workflow) é o nome proposto também pelo autor Patrick Janssen (2015) para identificar a conexão entre programas baseados em grafos, VPL e sistemas BIM. O autor aplica uma tarefa de modelagem para trazer à luz a necessidade de conexão entre os tipos de modelos paramétricos:

> A tarefa de modelagem consiste em gerar as placas de piso para uma torre cônica cuja forma geral é definida por uma superfície curva. Placas de piso para a torre são então geradas em intervalos regulares, até que o topo da torre seja alcançado. O perímetro das placas de piso está associado a uma superfície curva definindo a forma da torre, garantindo assim que as placas de piso se atualizem automaticamente sempre que a forma for modificada (JANSSEN, 2015, p 438. tradução nossa).

O autor utiliza este exemplo para demonstrar que existem algumas demandas em projetos que precisam de outros níveis de parametria que não são comportados pelo software BIM padrão. Através dos tipos de modelagem paramétrica apresentados anteriormente, um sistema BIM é classificado como modelagem de associação. Este tipo não comporta um fluxo de trabalho que permita um nível de iteração suficiente para que as placas de piso fossem atualizadas automaticamente sempre que a forma do edifício fosse modificada. O resultado só foi possível de ser alcançado com o uso de modelagem de procedimentos e fluxo de dados, através de programação VPL. Assim, o autor propõe duas abordagens para realizar a tarefa em modelos BIM: a abordagem incorporada (em inglês, embedded) e a abordagem acoplada (em inglês, coupled).

## Processo de Abordagem Incorporada (Embedded Approach)

Nesta opção, o programa BIM incorpora funcionalidades da linguagem VPL. Porém, identifica Janssen (2015), pela natureza dos programas BIM isto seria inviável na prática, pois quando se utiliza programas como o Grasshopper, busca-se uma ferramenta leve e responsiva para poder experimentar diversas opções de projeto. Algo que pode não ser efetivo em BIM quando o modelo se torna complexo (JANSSEN, 2015). Entretanto, ferramentas BIM ainda podem ser mais exploradas neste sentido com o uso de massa conceitual.

O programa Revit possui os mais avançados tipos de associação (JANSSEN, 2015), e a modelagem de massas pode ser uma alternativa para a modelagem conceitual de um projeto. Conforme a modelagem conceitual evolui, as formas podem ser convertidas em elementos básicos que irão compor uma arquitetura mais detalhada (AUTODESK, 2021). Conforme figura 06, esse ambiente do programa permite criação de geometrias mais desafiadoras.

### Figura 06 - Comparação entre o edifício Turning Torso Building e sua versão criada utilizando o programa Revit
![Comparação entre o edifício Turning Torso Building e sua versão criado utilizando o programa Revit](https://github.com/user-attachments/assets/d23abe61-d05f-4b7f-a952-c107f50e4aa6)
**Fonte**: Extraído da página do curso de Revit do grupo Balkan Architect²

## Processo de Abordagem Acoplada (Coupled Approach)

Neste tipo de abordagem, programas escritos em VPL são acoplados a modelos BIM para a realização de tarefas de modelagem e gerenciamento de dados (JANSSEN, 2015). O autor classifica a abordagem acoplada em duas subcategorias:

### Processo Fortemente Acoplado

Em inglês, *tightly coupled*, é a utilização de um programa VPL que utiliza a API do programa BIM para execução de tarefas, como exemplo, o Dynamo com o software Revit e Generative Components com o AecoSIM da Bentley.

#### Autodesk Dynamo

Pela taxonomia de Janssen e Stouffs (JANSSEN; STOUFFS, 2015), o programa Dynamo é classificado como um programa que suporta Modelagem com base em Procedimentos, ou seja, também suporta modelagem de fluxo de dados e todas as iterações, implícitas e explícitas. Baseado em grafos, o Dynamo está associado à ferramenta de modelagem de objetos denominada Autodesk Revit. Seu uso é difundido no meio BIM, e conforme apresentado a seguir, é um programa de linguagem VPL muito utilizado por projetistas. 


