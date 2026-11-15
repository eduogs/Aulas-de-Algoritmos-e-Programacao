# LOGBOOK — CRUD Lista de Compras

# PARTE 1 — CICLOS DE DESENVOLVIMENTO

## Ciclo 1 — Planejamento e levantamento de requisitos

**Data:** 15/11/2026

Nesta etapa, defini as informações que seriam armazenadas para cada item da lista: nome e quantidade.

Também defini as operações do sistema: adicionar item, ver a lista, atualizar item e remover item.

Delimitei os tipos de dados de cada atributo e estabeleci regras para o cadastro do item: impedir nomes vazios e exigir uma quantidade maior ou igual a 1.

Defini Python como linguagem do projeto, com funcionamento via terminal e sem necessidade de internet.

**Resultado:** atributos, operações, tipos de dados, regras de cadastro e linguagem definidos.

**Arquivos e documentação relacionados:** `crud.py` e `ideia para o CRUD`.

## Ciclo 2 — Primeira implementação do CRUD

**Data:** 15/11/2026

Desenvolvi a primeira versão do CRUD utilizando duas listas de tamanho fixo (50 posições), `nomes` e `quantidades`, para armazenar os dados da lista. Cada posição representa um item, e uma posição livre é marcada com texto vazio (`""`).

Implementei um menu interativo em que é possível escolher entre adicionar, ver, atualizar e remover itens, ou sair do programa. Para controlar a execução, utilizei estruturas condicionais e de repetição.

No decorrer dessa etapa, notei que a lista apresentava falhas: a pessoa podia deixar o nome do item e a quantidade em branco, e o programa aceitava esses campos como se algo tivesse sido escrito, ocupando uma posição da lista sem conteúdo.

Também identifiquei que algumas validações definidas no planejamento ainda não estavam implementadas no código.

Não fiz os registros no Logbook durante esse ciclo, por uma falha minha na organização e no acompanhamento da documentação. Reconstruí as atividades depois, com base no código e nos arquivos disponíveis.

**Resultado:** primeira versão do CRUD com menu e as quatro operações, ainda com as falhas de validação descritas acima.

**Arquivos e documentação relacionados:** `crud`

## Ciclo 3 — Teste de uma lista de dicionários

**Data:** 15/11/2026

Comecei uma refatoração do CRUD para corrigir e melhorar o código, testando uma mudança na estrutura de armazenamento.

Primeiro, criei uma lista chamada `nomes` para armazenar os produtos. Em seguida, organizei os atributos de cada item em um dicionário, utilizando os nomes dos atributos como chaves e os respectivos valores como dados.

Utilizei o método `append()` para adicionar cada novo dicionário à lista `itens`.

Depois, adaptei a opção de ver a lista para percorrer `itens` com um laço `for` e apresentar individualmente os atributos de cada item.

Durante a implementação, cometi um erro ao utilizar uma variável diferente daquela que representava o elemento percorrido pelo laço. Corrigi o problema usando a variável correta.

Inicialmente, também utilizei `print(nomes)` para exibir os registros. Embora essa instrução apresentasse os dados, decidi exibir cada atributo separadamente, para tornar a saída mais organizada e compreensível.

Testei o cadastro de mais de um item e confirmei que a listagem apresentava os registros corretamente.

**Resultado:** As opções de adicionar e de ver a lista funcionaram com a nova estrutura. As opções de atualizar e de remover ficaram pendentes de adaptação. s ciclos seguintes.]**

**Arquivos e documentação relacionados:**  REF02 e REF05 em `ideia para o CRUD`

## Ciclo 4 — Refatoração do código com listas e validação de campos vazios

**Data:** 15/11/2026

Refatorei o CRUD da primeira versão (duas listas de tamanho fixo), mantendo as mesmas opções do menu. Nesta etapa, defini as restrições: sem funções `append`, `pop` e `remove`. Contei com o apoio da IA, como detalho no Campo 2.

As principais mudanças foram:

- Troquei o tamanho fixo por uma constante, `TAMANHO`, e guardei o texto do aviso em `AVISO_VAZIO`, para alterar cada um em um único lugar.
- Implementei a validação de campo vazio. Depois de cada `input()`, um `while` repete a pergunta e mostra o aviso "Você não digitou nada, tente novamente." enquanto a pessoa não digitar nada. Apliquei isso no menu, no nome e na quantidade (adicionar), na busca, no novo nome e na nova quantidade (atualizar) e na busca (remover).
- Na opção de ver a lista, substituí o contador manual por `for i in range(TAMANHO)` e usei `f-string` na exibição de cada item.
- Simplifiquei as condições, trocando `== True` e `== False` por `if variavel` e `if not variavel`.
- Removi do final do `else` um bloco que sobrou da opção de remover e que mostrava uma mensagem sem sentido para opções inválidas.
- Padronizei a formatação e os comentários, que agora seguem o nome de cada opção do menu. O programa também passou a ter mensagem de saída e de opção inválida.

Durante a validação, percebi que um campo contendo apenas espaços ainda é aceito. Deixei esse caso de fora porque tratá-lo exigiria um método de texto, como `strip()`.

**Resultado:** todos os campos de entrada passaram a validar o campo vazio e a pedir a informação de novo.

**Testes:** **[ testes que fiz no meu computador, por exemplo: Enter vazio em cada campo, item inexistente, opção inválida e lista cheia.]**

**Arquivos e documentação relacionados:** `lista_de_compras.py`.

## Ciclo 5 — Preço, listas dinâmicas e pergunta final

**Data:** 15/11/2026

Criei uma nova versão do CRUD com três mudanças principais. **[PREENCHER: por que nesta versão passei a poder usar `append`, `pop` e `remove`, que eram restrições no Ciclo 4.]**

- **Preço:** incluí o preço como novo atributo do item, guardado em uma terceira lista, `precos`, que usa o mesmo índice de `nomes` e `quantidades`. O preço é pedido ao adicionar e ao atualizar, com a mesma validação de campo vazio, e aparece na listagem no formato `R$`.
- **Listas dinâmicas:** as listas passaram a começar vazias e a crescer com `append()`, o que eliminou a constante `TAMANHO` e as posições marcadas com texto vazio. Para remover um item, usei `pop()` nas listas de quantidades e de preços e `remove()` na lista de nomes, mantendo as três listas alinhadas. A listagem passou a usar `len()` para saber se a lista está vazia.
- **Pergunta final:** ao escolher sair, o programa pergunta "Você comprou tudo?" (1 para sim, 2 para não), repetindo a pergunta se a resposta for vazia ou inválida. Se a resposta for 1, exibe "Ok, muito obrigado, até mais!". Se for 2, exibe "Vamos comprar!" e mostra a lista.

Também padronizei as mensagens do programa com acentos.

**Limitações conhecidas:** o preço é guardado como texto, o que não permite calcular o total da compra, e campos com apenas espaços ainda são aceitos.

**Resultado:** o CRUD passou a ter preço, lista sem limite de itens e o fechamento com a pergunta final.

**Testes:** **[ fiz no meu computador nesta versão, incluindo as respostas 1 e 2 na pergunta final.]**

**Arquivos e documentação relacionados:** `lista_de_compras_v2.py`.

---

# PARTE 2 — CAMPO 1: ENTRADA

## O que acredito saber

Tenho conhecimentos iniciais de lógica de programação e de Python, adquiridos durante as aulas e aplicados no desenvolvimento da primeira versão do CRUD.

### 1. Fundamentos de lógica de programação

Acredito compreender o conceito básico de algoritmo como uma sequência de instruções organizadas para resolver determinado problema.

Conheço a estrutura IPO (Entrada, Processamento e Saída) e consigo identificar esses elementos na construção de um algoritmo.

Também conheço as representações de algoritmos por meio de linguagem natural, pseudocódigo e fluxogramas, e compreendo a relação entre essas etapas e a implementação em uma linguagem de programação.

Tenho conhecimento inicial sobre programação procedural e sobre a organização de instruções em uma sequência lógica.

### 2. Variáveis e tipos de dados

Sei declarar e utilizar variáveis para armazenar informações durante a execução de um programa.

Conheço os principais tipos de dados de Python:

- `int`: números inteiros; ex: "10"
- `float`: números decimais; ex: "10,67"
- `str`: textos; ex: "Olá mundo!"
- `bool`: valores booleanos (`True` e `False`). ex: "sim" ou "não"

Também sei converter entre tipos de dados com `int()`, `float()` e `str()`.

Compreendo a diferença entre o operador de atribuição (`=`) e o operador de comparação (`==`).

### 3. Operadores

Conheço e consigo utilizar operadores aritméticos, relacionais e lógicos:

- Aritméticos: `+`, `-`, `*`, `/`, `//`, `%` e `**`;
- Relacionais: `==`, `!=`, `>`, `<`, `>=` e `<=`;
- Lógicos: `and`, `or` e `not`.

Também sei utilizar operadores de atribuição composta, como `+=`, e compreendo o uso do operador módulo (`%`) em operações matemáticas.

### 4. Estruturas condicionais

Sei utilizar as estruturas `if`, `elif` e `else` para controlar o fluxo de execução de um programa de acordo com determinadas condições.

Consigo combinar condições com operadores lógicos e aplicar estruturas condicionais em situações como validação de dados e seleção de opções de um menu.

### 5. Estruturas de repetição

Conheço e consigo utilizar as estruturas `while` e `for`.

Compreendo que o `while` executa instruções enquanto uma condição for verdadeira e que o `for` permite percorrer sequências de elementos.

Também conheço o uso de `range()` para gerar sequências numéricas e das instruções `break` e `continue` para controlar a execução dos laços.

Já apliquei essas estruturas no CRUD para manter o menu em execução, percorrer os registros armazenados e repetir perguntas quando um campo está vazio.

### 6. Estruturas de dados

Tenho conhecimento inicial sobre listas e dicionários em Python.

**Listas:**

- Sei criar listas e armazenar vários elementos;
- Sei acessar elementos por meio de índices;
- Compreendo que os índices começam em zero;
- Sei utilizar o método `append()` para adicionar elementos;
- Consigo percorrer listas com estruturas de repetição;
- Sei utilizar `len()` para obter a quantidade de elementos.

**Dicionários:**

- Sei criar dicionários com pares de chave e valor;
- Sei acessar valores por meio de suas chaves;
- Compreendo que um dicionário permite organizar informações relacionadas a um mesmo registro;
- Sei que diferentes tipos de dados podem ser armazenados em um dicionário.

Já apliquei listas no CRUD, usando uma lista para os nomes e outra para as quantidades dos itens, relacionadas pela posição. Também comecei a testar uma lista para armazenar vários dicionários, cada um representando um item da lista de compras.

### 7. Funções

Tenho conhecimento básico sobre a criação e a utilização de funções em Python.

Apesar de conhecer esses conceitos, ainda preciso praticar a aplicação deles na organização e na divisão de programas em partes menores.

### 8. Funções nativas e métodos

Conheço e já utilizei algumas funções nativas e métodos de Python, como:

- `print()`: exibir informações;
- `input()`: receber dados do usuário;
- `len()`: obter a quantidade de elementos;
- `append()`: adicionar elementos a uma lista.

Consigo aplicar esses recursos em situações simples, mas ainda preciso ampliar meu conhecimento sobre os métodos disponíveis para listas e dicionários.

### 9. Aplicação prática dos conhecimentos

Já apliquei parte desses conhecimentos no desenvolvimento de um CRUD em Python.

Na primeira versão, implementei um menu interativo com as operações de adicionar, ver, atualizar e remover itens, usando duas listas de tamanho fixo.

Na refatoração, testei uma estrutura composta por uma lista e dicionários e, na versão mais recente, passei a usar três listas relacionadas pela posição (nomes, quantidades e preços), com os métodos `append()`, `pop()` e `remove()`.

Acredito conseguir desenvolver programas simples utilizando variáveis, operadores, condicionais, laços de repetição e estruturas de dados básicas, embora ainda preciso me consolidar esses conhecimentos por meio da prática.

## O que ainda preciso compreender melhor

- Remover elementos de uma lista;
- Atualizar valores armazenados em um dicionário;
- Aplicar validações de entrada de maneira consistente;
- Percorrer uma lista e localizar um registro específico;
- Combinar listas e dicionários para organizar conjuntos de registros;
- Adaptar todas as operações do CRUD à nova estrutura de armazenamento;
- Utilizar funções para dividir o programa em partes menores e organizadas;
- Compreender melhor como utilizar parâmetros e retornos na construção de funções.

## Hipótese inicial

Acredito que uma lista contendo dicionários seja uma estrutura adequada para armazenar vários itens da lista de compras.

Cada dicionário representa um item e contém seus atributos. A lista reúne todos os itens cadastrados.

Essa organização deve permitir que as operações de adicionar, ver, atualizar e remover trabalhem com vários registros, sem depender de variáveis individuais para cada item.

---

# PARTE 3 — CAMPO 2: APROFUNDAMENTO

## Objeto de conhecimento

Estruturas de dados em Python, principalmente listas e dicionários, e sua aplicação na organização de registros.

## Justificativa técnica

A primeira versão do CRUD armazenava os itens em duas listas de tamanho fixo, `nomes` e `quantidades`, relacionadas pelo mesmo índice. Uma posição livre era marcada com texto vazio, o que limitava o programa a 50 itens e fazia com que um nome vazio fosse confundido com uma posição livre.

A utilização de uma lista de dicionários permite agrupar os atributos de cada item em um único registro e armazenar vários registros em uma única estrutura.

Na versão mais recente, o CRUD usa três listas dinâmicas (`nomes`, `quantidades` e `precos`), que crescem com `append()` e diminuem com `pop()` e `remove()`. A posição `i` continua ligando os três atributos do mesmo item, e por isso as três listas precisam ser alteradas juntas.

## Comparação entre a hipótese e o resultado

**A hipótese inicial era uma lista de dicionários, mas a versão mais recente usa três listas relacionadas pela posição. Na comparação das duas estruturas, percebi que nos dicionários, fica um código mais limpo e muito mais fácil de ser localizados por meio dos índices, já na lista, é como se fosse um grupo só e ela é mutável, assim dificultando ainda mais a busca por meio visual ou até mesmo pelo código e a versão final ficou assim porque tem é perceptível que a leitura dele fica mais rápido e prática.**

## Referência de estudo

Documentação oficial do Python — Estruturas de dados:

https://docs.python.org/3/tutorial/datastructures.html

## Análise crítica do auxílio da IA

Durante a refatoração, utilizei a IA (Claude) como apoio para esclarecer dúvidas, avaliar alternativas e revisar o código. Registro aqui como foi esse uso, o que aceitei e o que não aceitei.

**O que pedi.** Pedi sugestões para melhorar o código mantendo as mesmas opções do menu, com a explicação de como e por que cada mudança foi feita. Informei as restrições do Ciclo 4: sem funções (`def` e `return`) e sem `append`, `pop` e `remove`. Mais tarde, pedi uma nova versão com `append`, `pop` e `remove`, o preço e a pergunta final "Você comprou tudo?" (Ciclo 5).

**O que não aceitei.** A primeira versão sugerida pela IA usava funções (`def` e `return`), o que não era permitido. Percebi o problema e pedi uma nova versão que respeitasse as restrições.

**O que aceitei.** Na versão seguinte, aceitei as melhorias de legibilidade: uso de constantes (`TAMANHO` e `AVISO_VAZIO`), laço `for` com `range` na listagem, simplificação das comparações com `True` e `False`, `f-strings` no lugar da concatenação e comentários padronizados com o nome de cada opção do menu. Na tentativa com dicionários (Ciclo 3), aceitei a lista de dicionários e o laço `for` para percorrer os registros, porque atendiam à necessidade de armazenar vários itens e organizar seus atributos.

**Validação de campos vazios.** Ao perceber que campos vazios eram aceitos, pedi ajuda sem receber a resposta direta. A IA me orientou com dicas, entre elas usar um `while` que repete a pergunta enquanto o campo estiver vazio. Fiz o sistema sozinho, ele completo com todas as funções, só que apresntava muito problema devido ao alinhamento das condições e lógicas da linguagem, após pedir a versão completa e com o auxlio da IA, percebi que muitas linhas do código estava fora de contexto, pois uma não conversava direito com a outra, assim fazendo que a sua execução não saisse proporcional á minha ideia. Depois, enviei meu código e pedi a versão final, com o aviso "Você não digitou nada, tente novamente." em todos os campos.

**Revisão feita pela IA.** A IA apontou um bloco de código sobrando no final do `else` da opção inválida, restante da opção de remover, que exibiria uma mensagem sem sentido e poderia causar erro.

**Nova versão (Ciclo 5).** A IA elaborou a versão com `append`, `pop` e `remove`, o preço e a pergunta final, e avisou sobre duas limitações: o preço é guardado como texto, sem permitir somar o total, e o trecho que mostra a lista aparece duas vezes, porque o programa não usa funções. Revisei o todo o código novamente para que se houvesse algum erro, detectaria tentaria resolve-lo imediatamente, e testei ele via terminal, resultando em todas as funções saindo como planejado.

**Questionamentos.** Questionei a utilização de `print(nomes)` como forma de listagem. Embora a instrução funcionasse, considerei que apresentar cada atributo separadamente tornaria a saída mais organizada.

**Documentação das alterações.** Também procurei compreender onde documentar as alterações realizadas, diferenciando as decisões técnicas, o histórico de mudanças no código e os registros pessoais de aprendizagem.

**Limites e cuidados.** A IA testou os programas com entradas simuladas, mas essa validação não substitui meus próprios testes, que descrevi nos ciclos. Os programas validam apenas campos totalmente vazios; um campo contendo somente espaços ainda é aceito. Não tratei esse caso porque exigiria um método de texto como `strip()`. 

**Observação:** este logbook ainda está em desenvolvimento. O Campo 2 e os ciclos ainda não estão completos na data desta alteração (15/11/2026).
