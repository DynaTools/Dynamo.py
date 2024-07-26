# Curso de Dynamo - Python

## INTRODUÇÃO

Modelagem da Informação da Construção (em inglês, Building Information Modeling - BIM) está cada vez mais presente e trouxe grandes mudanças na arquitetura, engenharia e construção (AEC), pois trata-se de uma representação tridimensional fiel de uma edificação (JANSSEN, 2015; WEN et al., 2021):

> Quando completo, o modelo gerado computacionalmente contém a geometria precisa e os dados relevantes, necessários para dar suporte à construção, à fabricação e ao fornecimento de insumos necessários para a realização da construção (EASTMAN et al., 2018, tradução nossa).

Os modelos BIM são desenvolvidos através de plataformas conhecidas como paramétricas, baseadas em objetos. Possuem um tipo de inteligência ou comportamento de projeto (em inglês, design behavior) (EASTMAN et al., 2018). Por exemplo, ao modelar um elemento parede, a mesma estará automaticamente identificada na lista de quantidades e nos cortes associados. Outra característica paramétrica está na inserção dos elementos, uma porta só poderá ser inserida em um elemento parede, e este, por sua vez, terá a área de material imediatamente removida dos metadados.

Este tipo de inteligência paramétrica está ausente em programas de modelagem CAD. Estes necessitam que o projetista identifique o elemento, preenchendo a propriedade associada. No exemplo citado anteriormente, a porta poderá ser inserida em qualquer ponto do modelo CAD sem que isso gere qualquer identificação de erro, assim como cortes precisarão ser atualizados quando ocorrerem mudanças na planta baixa.

Os limites e usabilidades de programas CAD e BIM podem variar em um projeto e os benefícios devem ser avaliados pela equipe envolvida. Apesar das disponibilidades de diversas ferramentas CAD e BIM, o projetista poderá ser confrontado, eventualmente, com uma necessidade de buscar o apoio da programação como solução de expansão de funcionalidade dos softwares (LANDIM, 2019). A programação visual ou visual programming language (VPL) é o nome que se dá para qualquer tipo de linguagem de programação possível de se manipular em um formato gráfico (NOONE; MOONEY, 2017). Uma das características positivas desta forma de programar é o retorno visual instantâneo do resultado ao projetista (LANDIM, 2019 apud CELANI;VAZ, 2012), sem a necessidade de compilar códigos complexos com domínio dos conceitos de programação e criação de algoritmos.

Pesquisas indicam que o uso da VPL apresenta benefícios ao projetista em relação à programação textual (NOONE; MOONEY, 2017), em especial àqueles que necessitam de mais feedbacks visuais de seu processo. A VPL melhora a capacidade de enxergar opções de parametrização dentro de projetos. Esta forma de pensar é classificada como pensamento paramétrico (WURZER; ALAÇAM; LORENZ, 2011). O projetista, ao desenvolver este raciocínio, começa de forma abstrata a conceber conexões entre elementos do projeto que pode ser traduzido em algoritmos.

Algoritmos são o conjunto de regras, operações e procedimentos definidos, ordenados e usados na solução de um problema em um número finito de etapas (ALGORITMO, 2021). Portanto, a ordem e organização de informações são cruciais para que o projetista produza bons resultados. É importante que o projetista tenha conhecimento sobre os tipos e classificações das ferramentas que utiliza no projeto, pois pode tomar decisões mais informadas sobre quando utilizar um determinado software, tecnologia ou linguagem de programação durante o desenvolvimento do projeto.

## PROBLEMA DE PESQUISA E METODOLOGIA

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

## TAXONOMIA DOS MODELOS PARAMÉTRICOS

Quando um curso de ciência da computação é bem delineado e desenvolvido, qualquer pessoa pode aprender a programar (LEITÃO, 2013). Partindo desse princípio, buscamos estruturar o curso utilizando a taxonomia proposta por Patrick Janssen e Rudi Stouffs, formando assim a primeira bibliografia que sugerimos aos alunos de Programação Visual Paramétrica (VPL) no início de seus estudos. Atualmente, existem muitos softwares de Modelagem de Informação da Construção (BIM) no mercado e, às vezes, chamá-los apenas de programa BIM, programa paramétrico ou programa de modelagem paramétrica pode não ser suficiente se quisermos compará-los e classificá-los adequadamente.

Em Types of Parametric Modelling, os autores definem um Modelo Geral Paramétrico (em inglês, General Parametric Model (GPM)) como a primeira estrutura de classificação.

O GPM é descrito utilizando um conceito matemático comum na ciência da computação, o grafo acíclico dirigido ou directed acyclic graph (DAG). Um DAG é um grafo que contém arcos direcionados sem qualquer ciclo, ou seja, não é possível retornar a um nó uma vez que ele já foi visitado (DIRECTED, 2021). Isso significa que não é possível percorrer o mesmo caminho múltiplas vezes, evitando assim recursão de dados.

### Figura 02 - Grafo Acíclico Dirigido

![Grafo Acíclico Dirigido](https://github.com/user-attachments/assets/2b17f4e8-ab94-4962-9aac-dcfadbd9a743)
**Fonte**: Extraído de Wikipédia¹

Considerando que arquitetos, engenheiros e projetistas geralmente não possuem formação formal em programação, mas estão sendo introduzidos a ela através das linguagens de programação visual (VPL), o conceito de iteração de dados pode se tornar muito abstrato e dificultar o engajamento do aluno com o conteúdo.

Os autores classificam as VPLs (que, por sua vez, são descritas como Grafos Acíclicos Dirigidos) pela maneira como iteram dados. Os tipos de iteração de dados são:

1. **Iteração simples**: O processo de repetição ocorre de forma direta e linear.
2. **Iteração múltipla implícita**: A repetição acontece dentro de estruturas de dados como listas aninhadas, de forma não explicitamente definida pelo usuário.
3. **Iteração múltipla explícita**: A repetição é definida de maneira clara e detalhada pelo usuário, permitindo maior controle sobre o processo iterativo.

Esses tipos de iteração formam a base para a taxonomia de modelos paramétricos descritos a seguir:

1. **Modelagem de Objetos**: Programas que não permitem nenhum tipo de iteração, como os programas CAD tradicionais.
2. **Modelagem de Associação**: Programas que permitem uma única rodada de iterações, como o Autodesk Revit, onde uma alteração em um componente pode refletir em outros componentes associados.
3. **Modelagem de Fluxo de Dados**: Programas que permitem iteração implícita através do uso de listas aninhadas, como o Grasshopper para Rhino3D e o Generative Components da Bentley.
4. **Modelagem com base em Procedimentos**: Programas que permitem iteração explícita, onde o usuário define claramente como a repetição ocorrerá, como o Dynamo BIM.

Esses tipos de iteração, e os tipos de modelagem que eles suportam, são fundamentais para entendermos a estrutura das VPLs utilizadas na área, bem como os tipos de modelagem suportados por programas considerados paramétricos. A seguir, vamos nos concentrar nas especificidades dos fluxos paramétricos BIM, explorando como esses conceitos são aplicados na prática e quais são suas implicações para o desenvolvimento de projetos na construção civil.

### Exemplos de Softwares de Modelagem e suas Aplicações

Para melhor entender como diferentes tipos de softwares se encaixam nos conceitos de modelagem e iteração, aqui está uma explicação de alguns dos principais programas utilizados na indústria de arquitetura, engenharia e design.

- **Revit**: O Autodesk Revit é um software de Modelagem de Informação da Construção (BIM). Ele permite a criação de modelos 3D inteligentes que incluem dados importantes sobre os componentes de construção. O Revit é um exemplo de software de Modelagem de Associação, onde uma modificação em um componente pode automaticamente atualizar outros componentes associados. Isso facilita a coordenação entre diferentes disciplinas (arquitetura, estrutura e MEP - mecânica, elétrica e hidráulica).

- **Grasshopper**: Grasshopper é um plugin para Rhino3D que permite a modelagem paramétrica. Ele é usado para criar algoritmos que geram geometrias complexas. Grasshopper exemplifica a Modelagem de Fluxo de Dados, onde iterações implícitas ocorrem através de listas e estruturas de dados aninhadas, permitindo a manipulação e a geração de formas complexas de maneira visual.

- **Dynamo**: Dynamo é um software de programação visual que se integra com o Revit, permitindo a criação de scripts para automatizar tarefas e criar geometrias paramétricas complexas. Dynamo exemplifica a Modelagem com base em Procedimentos, onde o usuário define explicitamente como a iteração e a manipulação de dados ocorrerão.

- **Rhinoceros (Rhino)**: Rhinoceros, ou Rhino, é um software de modelagem 3D baseado em NURBS (Non-Uniform Rational B-Splines), usado principalmente para criar superfícies e geometrias complexas. Embora Rhino em si seja mais focado na modelagem de objetos, quando combinado com Grasshopper, ele permite a modelagem paramétrica avançada.

- **AutoCAD**: AutoCAD é um software de desenho assistido por computador (CAD) usado para criar desenhos técnicos e plantas. Ele exemplifica a Modelagem de Objetos, pois é utilizado principalmente para criar geometrias estáticas sem iterações ou parametrizações complexas.

- **Inventor**: Autodesk Inventor é um software de modelagem CAD 3D utilizado principalmente para design mecânico. Ele permite a criação de peças, montagens e simulações. O Inventor pode ser classificado como Modelagem de Associação, pois permite que alterações em um componente reflitam nas montagens e desenhos associados.

- **SolidWorks**: SolidWorks é um software de CAD 3D utilizado para design de produtos, engenharia mecânica e simulações. Similar ao Inventor, ele suporta Modelagem de Associação com capacidades avançadas de simulação e análise.

- **ArchiCAD**: ArchiCAD é um software de BIM desenvolvido pela Graphisoft. Ele é usado principalmente para modelagem arquitetônica, permitindo a criação de modelos detalhados de edifícios. ArchiCAD também se enquadra na Modelagem de Associação, onde mudanças em um elemento do modelo podem afetar outros elementos relacionados.

- **Blender**: Blender é um software de modelagem 3D open-source que é amplamente utilizado em animação, efeitos visuais, arte 3D e design de jogos. Embora seja mais conhecido por suas capacidades artísticas e de animação, Blender também suporta Modelagem de Objetos e pode ser estendido para modelagem paramétrica através de scripts e plugins.

### Resumo

A classificação dos softwares acima em termos de seus métodos de iteração e tipos de modelagem ajuda a entender suas capacidades e aplicações específicas:

- **Modelagem de Objetos**: AutoCAD, Blender (com foco em geometria estática).
- **Modelagem de Associação**: Revit, Inventor, SolidWorks, ArchiCAD.
- **Modelagem de Fluxo de Dados**: Grasshopper (para Rhino3D).
- **Modelagem com base em Procedimentos**: Dynamo (para Revit).

Compreender esses conceitos e como eles se aplicam a diferentes softwares é crucial para escolher a ferramenta certa para cada tipo de projeto e para desenvolver fluxos de trabalho eficientes na indústria de AEC (Arquitetura, Engenharia e Construção).

## Integração de Python, Revit e Dynamo: Potencializando o Design Paramétrico

A combinação de Python, Revit e Dynamo oferece um poderoso conjunto de ferramentas para a modelagem paramétrica e automação de tarefas na arquitetura, engenharia e construção (AEC). Vamos explorar como cada componente contribui para essa integração e quais são os benefícios dessa abordagem.

### Revit

O Autodesk Revit é um software de Modelagem de Informação da Construção (BIM) que permite a criação de modelos 3D detalhados com informações ricas sobre os componentes da construção. Ele é amplamente utilizado para o design arquitetônico, estrutural e de sistemas MEP (mecânica, elétrica e hidráulica). O Revit suporta a Modelagem de Associação, onde uma alteração em um componente pode refletir automaticamente em componentes relacionados, facilitando a coordenação entre diferentes disciplinas.

### Dynamo

Dynamo é um ambiente de programação visual que se integra perfeitamente com o Revit. Ele permite aos usuários criar scripts visuais para automatizar tarefas repetitivas, gerar geometrias complexas e manipular dados de forma avançada. Dynamo é uma ferramenta de Modelagem com base em Procedimentos, onde o usuário define explicitamente os processos de iteração e manipulação de dados.

### Python

Python é uma linguagem de programação de alto nível conhecida por sua simplicidade e versatilidade. Ele é amplamente utilizado em diversos campos, incluindo a automação de tarefas, análise de dados e desenvolvimento de scripts para softwares como Revit e Dynamo. A integração de Python com Dynamo expande significativamente as capacidades do Dynamo, permitindo a criação de scripts mais complexos e personalizados.

### Integração Prática

A integração de Python, Revit e Dynamo pode ser visualizada como uma combinação de suas forças individuais, permitindo fluxos de trabalho mais eficientes e complexos. Aqui estão alguns exemplos de como essa integração pode ser utilizada:

#### Automação de Tarefas Repetitivas

- **Revit**: Configuração inicial e gerenciamento de modelos BIM.
- **Dynamo**: Criação de scripts visuais para automatizar tarefas repetitivas, como a criação de elementos padrão em um projeto.
- **Python**: Uso de scripts para automatizar processos ainda mais complexos, como a importação e manipulação de grandes volumes de dados externos.

#### Criação de Geometrias Complexas

- **Revit**: Visualização e documentação das geometrias criadas.
- **Dynamo**: Geração de formas paramétricas complexas através de nós visuais.
- **Python**: Programação de algoritmos avançados para gerar e manipular geometrias que seriam difíceis de implementar apenas com Dynamo.

#### Análise e Otimização de Projetos

- **Revit**: Repositório central para informações do projeto e visualização de resultados de análises.
- **Dynamo**: Scripts para executar análises básicas de desempenho e otimização.
- **Python**: Implementação de algoritmos de análise complexos, como otimização de energia, análise estrutural avançada e simulações de fluxo de trabalho.

#### Interoperabilidade e Manipulação de Dados

- **Revit**: Plataforma BIM que centraliza todos os dados do projeto.
- **Dynamo**: Interação com os dados do Revit para manipulação e análise.
- **Python**: Utilização de bibliotecas externas (como pandas e numpy) para análise e manipulação avançada de dados, importação e exportação de dados entre diferentes formatos e integração com outras plataformas e serviços.

### Benefícios da Integração

- **Eficiência e Produtividade**: Automatização de tarefas repetitivas e complexas, reduzindo o tempo necessário para completar projetos.
- **Precisão e Consistência**: Redução de erros humanos através da automatização de processos e validação de dados.
- **Flexibilidade e Customização**: Criação de soluções personalizadas que atendem às necessidades específicas de cada projeto.
- **Inovação**: Capacidade de explorar novas formas de design e análise que seriam difíceis ou impossíveis de realizar com ferramentas tradicionais.

### Exemplo Prático

Imagine que você está trabalhando em um projeto de grande escala que requer a colocação de milhares de luminárias em um edifício. Manualmente, isso seria extremamente demorado e sujeito a erros. Com a integração de Python, Revit e Dynamo, você pode:

1. Criar um script em Dynamo para gerar os pontos de inserção das luminárias com base em regras paramétricas (distância entre luminárias, alturas variáveis, etc.).
2. Usar Python dentro do Dynamo para ler um arquivo CSV contendo informações específicas sobre cada luminária (tipo, potência, etc.) e aplicar esses dados ao modelo.
3. Atualizar automaticamente o modelo no Revit, inserindo todas as luminárias nos locais corretos com as informações apropriadas.

Este fluxo de trabalho não só economiza tempo, mas também garante que todas as luminárias sejam colocadas de acordo com as especificações do projeto, melhorando a qualidade e a eficiência do processo de design.

A combinação de Python, Revit e Dynamo oferece um poderoso conjunto de ferramentas para qualquer profissional de AEC, permitindo a automação avançada, a criação de geometrias complexas e a análise profunda de projetos, tudo isso com uma flexibilidade e customização incomparáveis.
