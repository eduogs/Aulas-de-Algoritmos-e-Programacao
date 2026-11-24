# 📓 LOGBOOK AFP — Algoritmos e Programação (2026.2)

> **Como usar este arquivo:** copie-o para a raiz do **seu** repositório (ou para `logbook/LOGBOOK.md`) e preencha **direto no GitHub** (botão ✏️ *Edit this file*) ou no VS Code. Ele reúne todos os instrumentos do Protocolo AFP 2026.2 (Logbook Individual — Campos 01 a 04, 06 e 07; Registro de Revisão por Pares — Campo 05; Checkpoint Conceitual; Rubrica de Defesa Técnica).
>
> **Organização:** o Logbook está dividido em **3 grupos de entrega**, cada um com seu prazo. Dentro de cada grupo, os **ciclos de entrega (01 a 12)** continuam os mesmos, com as orientações de preenchimento. Siga a ordem: **Grupo 1 → Grupo 2 → Grupo 3 → Defesa Técnica**.
>
> O `Diario.md` do checklist passa a ser **este arquivo**: o registro de cada ciclo está na seção do ciclo correspondente.

## 📍 Navegação rápida

| Seção | Prazo |
|---|---|
| [👨‍🎓 Identificação](#-identificação) | Hoje |
| [🟢 Grupo 1](#-grupo-1--prazo-segunda-1611-às-23h59) · Registros 01–04, Campos 01 e 02 | **Segunda 16/11, 23h59** |
| [🟠 Grupo 2](#-grupo-2--prazo-sábado-2111-às-23h59) · Registros 05–08, Checkpoint, Campos 03 e 04 | **Sábado 21/11, 23h59** |
| [🔵 Grupo 3](#-grupo-3--prazo-quinta-2611-às-23h59) · Registros 09–12, Campos 05, 06 e 07 | **Quinta 26/11, 23h59** |
| [🏁 Defesa Técnica](#-defesa-técnica--quarta-1811) | **Quarta 18/11** |
| [🆘 Estou atrasado](#-estou-atrasado-no-logbook-e-agora) | — |

---

## 👨‍🎓 Identificação

| Campo | Preencha |
|---|---|
| **Nome do estudante** | Eduardo Oliveira Gomes|
| **Curso / Módulo** |: ENG. DE SOFTWARE · 2º período_ |
| **Unidade curricular** | Algoritmos e Programação — UnDB 2026.2 |
| **Professor** | Rondineli Seba Salomão |
| **App-base do meu CRUD** | um app de lista de compras |
| **Link do meu repositório** |https://github.com/eduogs/Aulas-de-Algoritmos-e-Programacao/blob/97875fda5670002c98739cc34088743b79385a8f/crud.py |
| **Dupla de revisão (Campo 05)** | Samuel Denzel / Samuel Denzel |
| **Função neste ciclo** |Eduardo Oliveira Gomes · Revisor do CRUD de um colega_ |

---

## 🧭 Regras de ouro (leia antes de preencher)

1. **Processo, não resultado.** O Logbook mostra *como você pensou*, não só o que funcionou. Registre erros, desvios e dúvidas reais.
2. **Vocabulário técnico.** Use os termos da área (ex.: "laço de repetição", "validação de entrada", "estrutura de dados"). Respostas genéricas ("aprendi Python") não são aceitas.
3. **Todo registro relevante tem 3 âncoras:** o **objeto de conhecimento** mobilizado + a **justificativa técnica** + a **referência/fonte**. *Decisão sem objeto de conhecimento e sem referência é considerada não rastreável e não conta para a avaliação formativa.*
4. **Coerência entre campos.** O Campo 02 deve ser coerente com o Campo 01. *Incoerência é evidência de autoria externa.* O Campo 07 retoma o Campo 01.
5. **IA é permitida e avaliada (Campo 04).** *Print sem análise crítica = devolução imediata. Reproduzir a IA sem questionamento = reprovado.* Você precisa mostrar o que aceitou **e** o que questionou/descartou, com argumento técnico.
6. **O histórico do Git é a sua evidência.** Faça commits pequenos e frequentes. Nunca reescreva o histórico (`force push`) do arquivo do Logbook.
7. **Campo 01 e Checkpoint são "sem consulta".** Preencha em um bloco contínuo, sem internet, sem material e sem colegas, no tempo indicado (Campo 01: durante o laboratório; Checkpoint: 20 min). Depois **não edite** esses campos — se perceber um erro, corrija em um campo posterior (Campo 03 ou 07), explicando.
8. **Os prazos dos grupos (16/11, 21/11 e 26/11, às 23h59)** valem para o commit no GitHub. O horário do commit é o registro oficial.

### ✅ Padrão de commit do Logbook

```text
docs(logbook): campo 01 — ciclo 02
docs(logbook): registro do ciclo 05
docs(logbook): campo 05 — revisão do CRUD de <colega>
```

---

## 🗓️ Calendário de entregas e Defesa

Os grupos têm **5 dias entre um prazo e outro**. O horário do commit no GitHub é o registro oficial.

| Grupo | Janela de preenchimento | **Prazo** | O que entregar |
|:--:|---|---|---|
| **1** | Qua 11/11 → seg 16/11 | **Segunda 16/11, 23h59** | Identificação · Registros dos Ciclos 01 a 04 · Campo 01 · Campo 02 |
| **2** | Seg 16/11 → sáb 21/11 | **Sábado 21/11, 23h59** | Registros dos Ciclos 05 a 08 · Checkpoint Conceitual · Campo 03 · Campo 04 |
| **3** | Sáb 21/11 → qui 26/11 | **Quinta 26/11, 23h59** | Registros dos Ciclos 09 a 12 · Campo 05 (2 revisões) · Campo 06 · Campo 07 |
| 🏁 | — | **Quarta 18/11** | **Defesa Técnica individual** (Rubrica) |

### Linha do tempo

| Data | Evento |
|---|---|
| Qua 11/11 | **Hoje:** começa o Grupo 1 |
| Seg 16/11 | ✅ Prazo do **Grupo 1** |
| **Qua 18/11** | 🏁 **Defesa Técnica** |
| Sáb 21/11 | ✅ Prazo do **Grupo 2** |
| Qua 25/11 | Avaliação P2 |
| Qui 26/11 | ✅ Prazo do **Grupo 3** |
| Qua 02/12 | Avaliação Substitutiva |
| Qua 09/12 | Avaliação Final |

> ⚠️ **Atenção:** a Defesa Técnica (18/11) acontece **antes** dos prazos dos Grupos 2 e 3. Na defesa você será arguido sobre **o que já estiver registrado e commitado**. Veja a seção [Defesa Técnica](#-defesa-técnica--quarta-1811) para saber o que priorizar até 18/11.

### Ciclos de entrega por grupo

| Ciclo | Data da aula | Tema do ciclo | Grupo | O que preencher |
|:--:|:--:|---|:--:|---|
| 01 | 12/08 | Preparação do laboratório e escolha do projeto | **1** | Registro do Ciclo |
| 02 | 19/08 | Variáveis, tipos de dados, entrada/saída | **1** | Registro + **Campo 01** + **Campo 02** |
| 03 | 26/08 | Operadores, fluxogramas, paradigmas | **1** (registro) · **2** (campos) | Registro (G1) · **Checkpoint**, **Campo 03**, **Campo 04** (G2) |
| 04 | 02/09 | Condicionais: `if`, `elif`, `else` | **1** | Registro do Ciclo |
| 05 | 09/09 | Condicionais aninhadas e operadores lógicos | **2** | Registro do Ciclo |
| 06 | 30/09 | Repetição: `for`, `while`, `break`, `continue` | **2** | Registro do Ciclo (inclui devolutiva da P1) |
| 07 | 07/10 | Listas: armazenamento e iteração | **2** | Registro do Ciclo |
| 08 | 14/10 | Busca e introdução a dicionários/matrizes | **2** | Registro do Ciclo |
| 09 | 21/10 | Atualização e exclusão: CRUD completo | **3** | Registro + **Campo 05** (revisão nº 1) |
| 10 | 28/10 | Modularização: funções | **3** | Registro do Ciclo |
| 11 | 04/11 | Recursividade | **3** | Registro + **Campo 06** |
| 12 | 11/11 | Refatoração e qualidade de código | **3** | Registro + **Campo 05** (revisão nº 2) + **Campo 07** |

---

## 📊 Painel de acompanhamento

Atualize a cada commit (troque ⬜ por ✅).

| Grupo | Item | Prazo | Preenchido | Commit |
|:--:|---|---|:--:|:--:|
| 1 | Identificação | 16/11 | ✅ | ✅ |
| 1 | Registros dos Ciclos 01, 02, 03 e 04 | 16/11 | ✅ | ✅ |
| 1 | Campo 01 — Instrumento de entrada | 16/11 |✅ | ✅ |
| 1 | Campo 02 — Aprofundamento | 16/11 | ✅ | ✅ |
| 2 | Registros dos Ciclos 05, 06, 07 e 08 | 21/11 | ✅ | ✅ |
| 2 | Checkpoint Conceitual | 21/11 | ✅ | ✅ |
| 2 | Campo 03 — Execução e desvios | 21/11 | ✅ | ✅ |
| 2 | Campo 04 — Interação com IA | 21/11 | ✅ | ✅ |
| 3 | Registros dos Ciclos 09, 10, 11 e 12 | 26/11 | ✅ | ✅ |
| 3 | Campo 05 — Revisão por pares nº 1 e nº 2 | 26/11 | ✅ | ✅ |
| 3 | Campo 06 — Próximos passos | 26/11 | ✅ | ✅ |
| 3 | Campo 07 — Evolução conceitual | 26/11 | ✅ | ✅ |
| 🏁 | Defesa Técnica | 18/11 | ✅ | — |

---

## ❓ A questão-problema da AFP

**Título:** *O sistema em produção: diagnosticando as falhas do CRUD que você mesmo construiu.*

> **Enunciado completo (Apêndice A):** _professor(a): cole aqui o enunciado e os anexos liberados conforme o cronograma._

A questão-problema é **a mesma durante todo o semestre**: ela se aplica ao **seu** CRUD, que cresce a cada ciclo. Os **dados com defeito** do seu app chegam em um **lote cumulativo único** e vão expondo problemas diferentes conforme sua estrutura evolui. Seu trabalho é diagnosticar, ajustar o CRUD para tratar cada falha e **registrar o raciocínio** neste Logbook.

---

# 🔁 REGISTRO DO CICLO — modelo (copie em cada ciclo)

Cada ciclo tem sua própria seção abaixo, já com o modelo. Se precisar de espaço extra, acrescente linhas.

```markdown
### Registro do Ciclo NN — DD/MM
1. **Desafio do ciclo (em 1 frase):**
2. **O que implementei (commits / arquivos / links):**
3. **Objeto(s) de conhecimento mobilizado(s) (vocabulário técnico):**
4. **Desvio ou erro encontrado + causa técnica:**
5. **Decisão de ajuste + fonte (livro, doc, vídeo, colega, IA):**
6. **Feedback recebido (professor/colega) e o que mudei por causa dele:**
7. **Próximo passo:**
```

**Como preencher bem:** escreva como se explicasse a um colega que não esteve na aula. O item 3 e o item 5 são os mais importantes: eles ligam o que você fez ao **conteúdo** e à **fonte**.

| ❌ Fraco | ✅ Forte |
|---|---|
| "Aprendi a usar `if`." | "Usei estrutura condicional aninhada para validar a idade antes de cadastrar. Meu erro foi comparar `str` com `int` (resultado de `input()`); corrigi com `int()` (Pense em Python, cap. 2)." |
| "Deu erro e consertei." | "O programa quebrou com `ZeroDivisionError` ao calcular a média de um item sem avaliações. Causa: divisão por `len(lista)` com lista vazia. Ajuste: testar `if len(lista) > 0`." |

---

# 🟢 GRUPO 1 — prazo segunda 16/11 às 23h59

> **Janela:** quarta 11/11 → segunda 16/11. **O que entregar:** Identificação · Registros dos Ciclos 01, 02, 03 e 04 · Campo 01 · Campo 02.
>
> **Sugestão de ordem:** (1) Identificação → (2) **Campo 01 primeiro, sem consulta** → (3) Registros dos Ciclos 01 a 04 → (4) Campo 02, com pesquisa.

**Checklist do Grupo 1**
- [x] Identificação preenchida (app-base, link do repositório, dupla de revisão)
- [x] Campo 01: 3 objetos de conhecimento, 3 lacunas, hipótese de até 5 linhas
- [x] Registros dos Ciclos 01, 02, 03 e 04 com os 7 itens
- [x] Campo 02: 2 referências com contribuição, hipótese revisada, 3 recursos
- [x] Commits no GitHub e painel atualizado

## 🟢 CICLO 01 — 12/08 — Preparação do laboratório e escolha do projeto

<details>
<summary>📘 Orientações do Ciclo 01</summary>

- **Hoje não há Campo do Protocolo.** O foco é preparar o ambiente: criar o repositório, configurar o VS Code e escolher o **app-base** do seu CRUD (e, portanto, o *schema* dos seus dados).
- Preencha a **Identificação** (no início deste arquivo) e o **Registro do Ciclo 01**.
- No item 3, registre **o que você já sabia** e o que era novo (Git, GitHub, VS Code). Isso será útil para o Campo 07.
- No item 4, registre qualquer problema de instalação ou configuração e como o resolveu — isso conta como desvio.
- Faça o primeiro commit: `docs(logbook): registro do ciclo 01`.
</details>

#### Registro do Ciclo 01 — 12/08
1. **Desafio do ciclo (em 1 frase):** Planejamento da ideia e escolha do projeto
2. **O que implementei (commits / arquivos / links):** Houve implementação das váriaveis e dos `print`, arquivos disponíveis `aula1208.py`.
3. **Objeto(s) de conhecimento mobilizado(s):** Variavéis guardam valores na qual você atribiu a ele, podendo alterar o resultado dele seja para `int`, `float` ou `str`.
4. **Desvio ou erro encontrado + causa técnica:** Uma variaável não pode conter caracteres específicos, pois alguns deles tem valor em Python como `@`,`-`, `!`, `%`.
5. **Decisão de ajuste + fonte:** A decisão foi baseada nos conceitos de sintaxe da linguagem, dada em sala de aula após uma breve explicação sobre *caracteres especiais*.
6. **Feedback recebido e o que mudei:** O que foi alterado foi de `nome-da-mensagem` para `nome`, isso nos resultou em uma melhor vizualização da variável e um nome bem mais fácil de entender.
7. **Próximo passo:** Aprender os tipos de dados e entrada e saída.

## 🟢 CICLO 02 — 19/08 — Variáveis, tipos de dados e entrada/saída

<details>
<summary>📘 Orientações do Ciclo 02 — Campo 01 (sem consulta) e Campo 02 (pesquisa)</summary>

**Campo 01 — Instrumento de entrada** · *sem consulta · faça primeiro*
- Preencha **antes de tudo**, em um bloco contínuo de cerca de 15 minutos, sem internet, sem material, sem IA e sem colegas, depois de conhecer a questão-problema e a primeira amostra de dados do seu app. Depois do Campo 01 você pode consultar o que quiser.
- **1a.** Liste pelo menos **3 objetos de conhecimento** que você acha que precisa dominar para resolver o problema. Use o vocabulário técnico da área. *Não precisa acertar tudo — o Campo 07 vai mostrar o quanto você evoluiu.*
- **1b.** Liste pelo menos **3 lacunas**: o que você **não sabe** e precisa descobrir, com precisão (ruim: "não sei programar"; bom: "não sei como validar a entrada para impedir que o usuário digite texto onde espero número").
- **1c.** Escreva sua **hipótese inicial** em até 5 linhas: o que você acha que está causando as falhas do CRUD e por quê.
- Faça o commit **logo ao terminar**. Depois, **não edite** o Campo 01.

**Campo 02 — Aprofundamento** · *AV Qualis · segunda 16/11, 23h59*
- Preencha **depois do Campo 01, com pesquisa real**, e seja coerente com ele.
- **2a.** Pelo menos **2 referências** (livro, documentação, vídeo, artigo), cada uma com a **contribuição** concreta para a sua solução. Não basta listar o título.
- **2b.** **Hipótese revisada:** o que mudou em relação ao Campo 01 e **por quê**. Se não mudou nada, explique por que a pesquisa confirmou a hipótese.
- **2c.** **Dimensionamento inicial de recursos** (mínimo 3 itens), com quantidade estimada e justificativa técnica. Exemplos de recursos no seu contexto: horas de estudo, número de casos de teste, módulos/arquivos do projeto, dados de teste, bibliotecas.
</details>

### 🧩 CAMPO 01 — Instrumento de entrada
*Grupo 1 | Prazo segunda 16/11, 23h59 | SEM CONSULTA*

**1a. Objetos de conhecimento identificados (mínimo 3, com vocabulário técnico):**
1. Dados do tipo `float`, `int` e `str`.
2. Entrada e saída de dados 
3. Processamento do `input` do usuário.

**1b. Lacunas — o que não sei e preciso descobrir (mínimo 3, com precisão técnica):**
1. Dados do tipo `bool` .
2. Alterar resultado da entrada.
3. Atribuições de valores das variáveis.

**1c. Hipótese inicial em até 5 linhas — com lógica da área de formação:**

> A hipótese inicial era fazer apenas uma lista simples de compras, mostrando apenas o que o usuário dejeja comprar, com funções domente de `append` e `remove`. Perante isso, passei a usar laços de repetição `while`, pois ele continua rodando enquanto a condição programada pelo desenvolvedor continua sendo verdadeira. Notei que ultilizar `if`, `elif` e `else`, facilitaria demasiadamente, pois ele quando uma condição passa de ser verdadeira, ou o elif ou o else, dá continuidade no processo de adicionar ou remover coisas da lista. 

### 🧩 CAMPO 02 — Aprofundamento pós-aula
*AV Qualis — Grupo 1 | Segunda 16/11, 23h59*

> **Preenchido depois do Campo 01, com pesquisa real. Deve ser coerente com o Campo 01. Incoerência = evidência de autoria externa.**

**2a. Aprofundamento dos objetos de conhecimento (mínimo 2 referências com síntese da contribuição para a solução):**

- Documentação oficial do Python, função `input()` (https://docs.python.org/3/library/functions.html#input) — **Contribuição:** mostra que `input()` lê uma linha digitada pelo usuário e devolve sempre `str`. Por isso o valor precisa ser guardado em uma variável e convertido com `int()` ou `float()` antes de qualquer cálculo.
 
- Curso de Python, canal Curso em Vídeo (Gustavo Guanabara), (https://youtu.be/S9uPNppGsGo?si=OugKR7HMBC0uPtq8) — **Contribuição:** Um dado de uma varável do tipo `input` deve-se usar `f```string`.

**2b. Hipótese revisada — o que mudou em relação ao Campo 01 e por quê:**

> No Campo 01 eu previa uma lista simples, só com `append` e `remove`. Ao usar o laço `while` com `if`, `elif` e `else`, o código ficou menor e mais legível, porque o laço repete o menu sem eu reescrever as mesmas linhas, e as condicionais escolhem a ação (adicionar ou remover).

**2c. Dimensionamento inicial de recursos (recurso, quantidade estimada, justificativa técnica — mínimo 3 itens):** 

| RECURSO / MATERIAL / INSUMO | QUANTIDADE ESTIMADA | JUSTIFICATIVA TÉCNICA |
|---|---|---|
| Horas de estudo | 2 horas | Tempo estimado para dominar variáveis, tipos de dados, `input()` e conversão de tipos, com prática em casa. |
| Arquivos do projeto (.py) | 5 (`aula1208.py`, `aula1908pa.py`, `aula2008.py`, `misto2.py`, `crud.py`) | Cada arquivo isola um conceito da aula, o que facilita testar e localizar erros. |
| Casos de teste | 5 | Verificar entradas válidas, entrada em branco, texto onde se espera número, item inexistente na lista e valor negativo. |
| Documentação oficial do Python | 1 | Fonte de referência para o comportamento de `input()` e dos tipos `str`, `int` e `float`. |

#### Registro do Ciclo 02 — 19/08
1. **Desafio do ciclo (em 1 frase):** Aprender a declarar variáveis de tipos diferentes e receber dados do usuário com `input()`.
2. **O que implementei (commits / arquivos / links):** `aula1908pa.py`, com a variável numero1 = 'x', uma chamada de `input()` e variáveis comentadas `(alimento, recheio1, recheio2)`.
3. **Objeto(s) de conhecimento mobilizado(s):** variável, atribuição, tipo `str`, comentário (#), entrada de dados com `input()`.
4. **Desvio ou erro encontrado + causa técnica:** o `input()` foi chamado sem guardar o resultado em uma variável, então o valor digitado se perde. Além disso, `input()` sempre devolve `str`, então, para fazer cálculo, seria preciso converter com `int()` ou `float()`.
5. **Decisão de ajuste + fonte:**  Passei a guardar o retorno do `input()` em uma variável (atribuição) e a converter o tipo com `int()` ou `float()` quando preciso calcular, pois `input()` sempre devolve `str`. A decisão veio da explicação do professor em sala e da documentação oficial do Python (https://docs.python.org/3/library/functions.html#input), consolidada com prática em casa e em sala.
6. **Feedback recebido e o que mudei:** Um colega de turma avaliou que o código estava bom, mas poderia melhorar na estrutura para simplificar. Por causa disso,passei a repetir o menu dentro de um único laço `while`.
7. **Próximo passo:** Estudar operadores aritméticos, relacionais e lógicos e montar fluxogramas
## 🟢 CICLO 03 — 26/08 — Operadores, fluxogramas e paradigmas

<details>
<summary>📘 Orientações do Ciclo 03 — Registro (Grupo 1)</summary>

- Neste grupo você preenche **apenas o Registro do Ciclo 03**. O **Checkpoint Conceitual** e os **Campos 03 e 04** deste ciclo estão no **Grupo 2**.
- Item 3: nomeie os **operadores** (aritméticos, relacionais, lógicos) e os **tipos** que usou. Se montou fluxogramas, cite o que o fluxograma ajudou a perceber.
- Item 4: registre erros de precedência de operadores, divisão por zero ou confusão entre `=` e `==`, com a causa técnica.
</details>

#### Registro do Ciclo 03 — 26/08
1. **Desafio do ciclo (em 1 frase):** Saber como e quando utilizar laços de repetições e diferenciar valores de atribuição e comparação.
2. **O que implementei (commits / arquivos / links):** `aula2608.py`
3. **Objeto(s) de conhecimento mobilizado(s):**  Aprendi que conseguimos de maneira prática fazer uma comparação em valores utilizando o algorítmos de operações aritméticas.
4. **Desvio ou erro encontrado + causa técnica:** Um erro encontrado foi que aspas é dado com string, e nisso quando atribuí no exercício 3, apresentava erro de sintaxe.
5. **Decisão de ajuste + fonte:** A decisão de ajuste foi corrijida perante a explicação em https://docs.python.org/3/tutorial/datastructures.html, pois um sempre é recebido com string, a menos que altere o tipo de recepção dele.
6. **Feedback recebido e o que mudei:** Mudei de "30" para 30, notei que ficou muito mais fácil de entender pois a sintaxe estava correta.
7. **Próximo passo:** Aprender a como manusear corretamente as condições do `while`.
## 🟢 CICLO 04 — 02/09 — Estruturas condicionais: `if`, `elif`, `else`

<details>
<summary>📘 Orientações do Ciclo 04</summary>

- **Sem Campo do Protocolo hoje.** Preencha o Registro do Ciclo 04.
- Conecte **cada condicional** do seu CRUD a uma **regra de negócio** (ex.: "preço não pode ser negativo").
- Se já recebeu o lote de dados com defeito, procure **qual registro quebra qual condição** e registre o item 4 com a **causa técnica** (ex.: valor `None`, texto vazio, número negativo, divisão por zero).
- No item 5, cite a fonte da decisão: livro (*Pense em Python*), documentação ou exercício que você resolveu.
- Compare com o **Campo 02**: o desvio de hoje já estava previsto no seu dimensionamento?
</details>

#### Registro do Ciclo 04 — 02/09
1. **Desafio do ciclo (em 1 frase):** Compreender como usar corretamente `if`, `elif` e `else`.  
2. **O que implementei (commits / arquivos / links):** `misto2.py`
3. **Objeto(s) de conhecimento mobilizado(s):** Aprendi que enquando o `if` continua sendo verdadeiro ele continua rodando, caso passe a deixar de ser uma condição verdadeira o `else`, é a segunda opção de rodar o código, caso passe a deixar de ser verdadeira, o `elif` é a terceira opção, até o laço `while` terminar o seu processo.
4. **Desvio ou erro encontrado + causa técnica:** Percebi que as condições devem estar identadas a um linha verticalmente para que as condições interajam entre si, se elas não estiverem alinhadas, a sintaxe do ligueagem Pyhton passa a estar incoerente.
5. **Decisão de ajuste + fonte:** O ajuste foi feito de maneira bem prática já que as linhas estavam em lugares onde não haviam possibilidade de ter uma interação com o propósito do código.
6. **Feedback recebido e o que mudei:** Corriji o erro de identação das linhas de interação do laço `while`, e deixei de forma que tanto o `if`, `elif` e `else` interajam entre si.
7. **Próximo passo:** Aprender condicionais aos operadores lógicos.

---

# 🟠 GRUPO 2 — prazo sábado 21/11 às 23h59

> **Janela:** segunda 16/11 → sábado 21/11. **O que entregar:** Registros dos Ciclos 05, 06, 07 e 08 · Checkpoint Conceitual · Campo 03 · Campo 04.
>
> ⚠️ O prazo cai num **sábado**: planeje terminar na sexta. Os campos do Ciclo 03 (Checkpoint, 03 e 04) aparecem **primeiro**, porque são a base da investigação.

**Checklist do Grupo 2**
- [x] Checkpoint Conceitual feito conforme orientação do professor (20 min, sem consulta)
- [x] Campo 03: 2 achados com objeto, 1 desvio com causa técnica, 1 decisão com fonte
- [x] Campo 04: ferramenta, pergunta íntegra, resumo, o que aceitei e o que questionei
- [x] Registros dos Ciclos 05, 06, 07 e 08 com os 7 itens (devolutiva da P1 no ciclo 06)
- [x] Commits no GitHub e painel atualizado

## 🟠 CICLO 03 (campos) — 26/08 — Checkpoint, Campo 03 e Campo 04

<details>
<summary>📘 Orientações — Checkpoint, Campo 03 e Campo 04 (referentes ao Ciclo 03)</summary>

**Checkpoint Conceitual** · *20 min · sem consulta · conforme orientação do professor*
- Verifica o **seu domínio individual** do conteúdo — não avalia a sua solução. São **3 questões dissertativas**. Quem investiu por conta própria responde com segurança.
- Respostas **genéricas, sem ancoragem técnica, não são aceitas**. Defina o objeto **e** relacione-o ao problema do seu CRUD, explicitando as implicações.
- Critérios: *precisão conceitual*, *relação conteúdo-problema*, *qualidade do raciocínio*.
- Se for insatisfatório, você recebe **feedback escrito em até 48h** e deve ajustar a investigação antes da avaliação somativa.
- Se o professor aplicar o Checkpoint via GitHub, use o arquivo abaixo **só durante os 20 minutos**, com um único commit ao final.
- **3a.** Percebi que a busca linear precisa guardar o item encontrado antes do `break`. No `aula0411.py`, o `break` está antes de qualquer atribuição a encontrado; por isso, a variável permanece None e a busca nunca devolve o registro. No `crud.py`, a mesma ideia funciona porque a flag `encontrado = True` é marcada dentro do `if` e a condição `not encontrado` encerra o laço `while`.
- Percebi que o `crud.py` mantém três listas paralelas (`nomes`, `quantidades`, `preços`) sincronizadas apenas pelo índice. Por isso a remoção exige três operações (`quantidades.pop(i)`, `precos.pop(i) e nomes.remove(busca)), misturando acesso por posição e por valor.
**Campo 03 — Execução e desvios** · *sábado 21/11, 23h59*
  
- **3b.** No dimensionamento (Campo 02c), planejei 5 casos de teste: entrada válida, entrada em branco, texto onde se espera número, item inexistente e valor negativo. O `crud.py` atende apenas 3: a entrada válida, a entrada em branco (aviso `AVISO_VAZIO` e nova leitura) e o item inexistente (mensagem "Item não encontrado."). Testei "abc" como quantidade e "-5" como preço: ambos foram aceitos e a listagem exibiu `- leite (qtd: abc) - R$ -5`. 
-**Causa técnica:** O `input()` sempre devolve `str`, e eu gravo `quantidade` e `preço` nas listas sem converter com `int()` ou `float()`. A validação `while campo == ""` verifica apenas se a string é vazia (presença do dado); ela não verifica o tipo nem o domínio do valor (número maior que zero). Faltou tratamento de `ValueError` na conversão e uma comparação de limite (`> 0`).
  
- **3c.** **Decisão:** Validar e converter `quantidade` e `preco` no momento da leitura: um laço `while` True que lê o `input()`, converte com `int()` (quantidade) ou `float()` (preço) dentro de `try/except ValueError`, rejeita valores `<= 0` e só executa `break` quando o dado é válido. Descartei o método `str.isdigit()` porque ele recusa decimais (`"3.50"`) e negativos (`"-5"`), o que não distingue "texto inválido" de "número decimal válido". Com a conversão feita na entrada, `quantidades` passa a guardar `int` e `precos` guarda `float`, e a listagem formata o preço com `f"{preco:.2f}"`.
**Fonte:** Documentação oficial do Python — int() (https://docs.python.org/3/library/functions.html#int), conversão de tipos `(int()` e `float())`, validação de entrada.

**Campo 04 — Interação com IA** · *sábado 21/11, 23h59 · obrigatório e avaliado*
- Registre ** Print sem análise crítica = devolução imediata. Reproduzir a IA sem questionamento = reprovado.
- **4b.**  Presciso de uma ajuda para o aviso de campo vazio e para a refatoração com `append`, `pop` e `remove`]
- **4c.** A IA me orientou, de forma guiada, a repetir a leitura com `input()` dentro de um laço `while` enquanto o campo for uma string vazia, exibindo a mensagem de aviso a cada tentativa. Depois, ajudou a reorganizar o CRUD usando `append`, `pop` e `remove` sobre listas, a incluir o preço e a perguntar `"Você comprou tudo?"` ao sair, com despedida ou exibição da lista conforme a resposta.
- **4d.** Aceitei guardar a mensagem na constante `AVISO_VAZIO`, que elimina a repetição do mesmo em vários pontos do código (uma variável com um único ponto de alteração). Por fim, aceitei o uso de `append` para inserir e de `pop(i)` e `remove()` para excluir.
- **4e.** Questionei a suficiência da validação. Executei o `crud.py` com quantidade `abc` e preço `-5`; o programa aceitou os dois valores e a listagem exibiu `- leite (qtd: abc) - R$ -5`. O motivo é que `input()` devolve `str` e a comparação`== ""` só detecta vazio; ela não verifica tipo nem faixa de valores (documentação de `input()`: https://docs.python.org/3/library/functions.html#input). Por isso, não considerei o código "pronto" e registrei no Campo 03 a decisão de converter com `nint()`/`float()` e tratar `ValueError` .
</details>

### 🧩 CHECKPOINT CONCEITUAL INDIVIDUAL
*20 minutos · sem consulta a qualquer fonte, material ou colega · conforme orientação do professor.*

| | |
|---|---|
| **Nome do estudante** |Eduardo Oliveira Gomes|
| **Data de realização** | 20/11/2026 |
| **Unidade curricular** | Algoritmos e Programação |
| **Professor(a)** | Rondineli Seba Salomão |

> **INSTRUÇÕES:** Responda individualmente, sem consulta. Você tem 20 minutos. As questões avaliam seu domínio dos objetos de conhecimento do componente — não sua solução para o problema. Respostas genéricas sem ancoragem técnica não são aceitas.

**QUESTÃO 1** — Objeto de conhecimento: _…_
> _(Questão elaborada pelo professor na Proposta — Apêndice A, item 6)_

**RESPOSTA:**

> _…_

**QUESTÃO 2** — Objeto de conhecimento: _…_
> _(Questão elaborada pelo professor na Proposta — Apêndice A, item 6)_

**RESPOSTA:**

> _…_

**QUESTÃO 3** — Objeto de conhecimento: _…_
> _(Questão elaborada pelo professor na Proposta — Apêndice A, item 6)_

**RESPOSTA:**

> _…_

<details>
<summary>🔒 Uso do professor — critérios de avaliação do Checkpoint</summary>

| CRITÉRIO | SATISFATÓRIO | INSATISFATÓRIO |
|---|---|---|
| **Precisão conceitual** | Domínio do objeto de conhecimento, com vocabulário técnico adequado e sem erros conceituais relevantes. | Resposta vaga, com erros conceituais ou sem ancoragem nos objetos de conhecimento do componente. |
| **Relação conteúdo-problema** | Conecta o objeto de conhecimento ao problema trabalhado na AFP. | Responde o objeto de forma isolada, sem relação com o problema do ciclo. |
| **Qualidade do raciocínio** | Raciocínio técnico articulado: relaciona o objeto ao problema e explicita implicações para a investigação. | Apenas define o objeto, sem articular raciocínio ou relação com o problema investigado. |

**RESULTADO:** ☐ Satisfatório ☐ Insatisfatório
**AÇÃO DO PROFESSOR:** Checkpoint insatisfatório gera feedback escrito individualizado até 48h — o aluno ajusta a investigação antes da avaliação somativa.
</details>

### 🧩 CAMPO 03 — Execução e desvios
*AV Qualis — Grupo 2 | Sábado 21/11, 23h59*

**3a. O que descobri que mudou minha compreensão do problema (mínimo 2 achados, com objeto de conhecimento associado):**
1. _…_ — *Objeto de conhecimento:* _…_
2. _…_ — *Objeto de conhecimento:* _…_
3. _…_ *(opcional)*

**3b. Desvio em relação ao Campo 02 (ao menos 1 — causa técnica):**
- **Desvio:** _…_
- **Causa técnica:** _…_

**3c. Decisão de ajuste (ao menos 1) com justificativa e fonte:**
- **Decisão:** _…_
- **Fonte:** _…_

**Objeto de conhecimento mobilizado nesta decisão:** _…_

### 🧩 CAMPO 04 — Interação com IA
*AV Qualis — Grupo 2 | Sábado 21/11, 23h59 | OBRIGATÓRIO*

> **Obrigatório e avaliado. Print sem análise crítica = devolução imediata. Reproduzir a IA sem questionamento = reprovado.**

**4a. Ferramenta:** _…_  **Data:** _DD/MM/AAAA_

**4b. Pergunta formulada (transcrita integralmente):**

> _…_

**4c. Resposta da IA (resumida em parágrafo):**

> _…_

**4d. O que aceitei — com referência ao objeto de conhecimento do componente:**

> _…_

**4e. O que questionei ou descartei — com argumento técnico ou fonte:**

> _…_

## 🟠 CICLO 05 — 09/09 — Condicionais aninhadas e operadores lógicos

<details>
<summary>📘 Orientações do Ciclo 05</summary>

- **Sem Campo do Protocolo hoje.** Preencha o Registro do Ciclo 05.
- Registre **qual combinação de condições** (`and`, `or`, `not`) você precisou e **por que** uma condicional aninhada ou um operador lógico foi a melhor escolha.
- Descreva **pelo menos um caso de teste** que você usou para provar a lógica (entrada → resultado esperado → resultado obtido).
- **Atenção à P1 (23/09):** reveja o Logbook até aqui. Complete itens em branco e confirme se os commits estão em dia.
- Na semana de 16/09 (Nivelamento / Peer Instruction), reserve 10 minutos para atualizar este arquivo.
</details>

#### Registro do Ciclo 05 — 09/09
1. **Desafio do ciclo (em 1 frase):** Entender como o `for ... in range()` gera a sequência do contador e por que atribuir um valor a `i` antes do laço não altera o resultado.
2. **O que implementei (commits / arquivos / links):** `aula0909.py`, com o enunciado "FOR IN RANGE com i = 0 e i = 5": a versão com `i = 0` ficou comentada e a versão ativa usa `i = 5` seguido de `for i in range(10): print(i)`.
3. **Objeto(s) de conhecimento mobilizado(s):** Laço `for`, função `range()` (limite superior exclusivo), variável de controle e atribuição. Os operadores lógicos e as estruturas aninhadas desta etapa aparecem em `aula2608ap.py (x > 10 and y <= 4)` e, depois, no `crud.py: while i < len(nomes) and not encontrado` (com um `if` aninhado dentro do while) e `while resposta != "1" and resposta != "2"`. Em ambos, usei `and` porque as duas condições precisam ser verdadeiras ao mesmo tempo para o laço continuar.
4. **Desvio ou erro encontrado + causa técnica:** O programa imprimiu os valores de 0 a 9 (10 valores), e não de 0 a 5. Causa: `range(10)` equivale a `range(0, 10)`, com `stop` exclusivo, e o `for` reatribui `i` a cada iteração, descartando o `i = 5` (ou `i = 0`) declarado antes.
**Causa técnica**: `for i in range(10)` → esperado: 0 a 5 → obtido: 0 a 9 ✗. Com `range(0, 6)` → 0 a 5 ✓; com `range(5, 10)` → começa em 5 ✓.
5. **Decisão de ajuste + fonte:** Passei a definir `start` e `stop` explicitamente em `range()`, sem depender de atribuição prévia à variável de controle. Fonte: documentação oficial do Python, tipo range (https://docs.python.org/3/library/stdtypes.html#range) e instrução for (https://docs.python.org/3/tutorial/controlflow.html#for-statements).
6. **Feedback recebido e o que mudei:** Retorno da execução: a saída de 0 a 9 mostrou que o intervalo estava errado; a mudança definida é usar `range(0, 6)` para 0 a 5. Feedback de professor/colega: sem feedback externo neste ciclo.
7. **Próximo passo:**Estudar `while`, `break` e `continue` e escolher quando usar `for` ou `while`.
## 🟠 CICLO 06 — 30/09 — Devolutiva da P1 + repetição: `for`, `while`, `break`, `continue`

<details>
<summary>📘 Orientações do Ciclo 06</summary>

- **Sem Campo do Protocolo hoje.** Preencha o Registro do Ciclo 06.
- Use o item 6 para registrar a **devolutiva da P1**: o que errou e **qual conceito** estava faltando. Esses erros alimentam o **Campo 07c** (conceitos corrigidos). *Anote já, para não esquecer.*
- Registre **por que escolheu `for` ou `while`** em cada laço do seu CRUD (cadastro em lote, listagem, menu).
- Item 4: se um laço ficou infinito ou pulou itens, descreva a **causa técnica** (condição de parada, incremento, `break` fora de lugar).
</details>

#### Registro do Ciclo 06 — 30/09
1. **Desafio do ciclo (em 1 frase):** Percorrer listas com `for` e `enumerate()` e validar um valor digitado dentro de um laço `while True`.
2. **O que implementei (commits / arquivos / links):** `aula3009.py`, com as listas `animais` e `animais_permitidos`, um `while True`, `for` com `enumerate()` e a `verificação nome_animal in animais_permitidos`.
3. **Objeto(s) de conhecimento mobilizado(s):** laço `while` com `True` como condição, laço `for` sobre `lista`, `enumerate()` (par índice/valor), operador de pertinência `in`, `len()`, concatenação `+=` em lista, atribuição e escopo de variáveis. No CRUD, escolhi cada laço assim: o `for` na listagem (`for i in range(len(nomes`))), porque percorro todos os itens existentes; o `while` no menu (`while opcao != "5"`), na revalidação de campos (`while campo == ""`) e na busca (`while i < len(nomes) and not encontrado`), porque o número de repetições depende de uma condição, e não de um tamanho conhecido.
4. **Desvio ou erro encontrado + causa técnica:** `while True` sem nenhum `break`: o laço nunca termina, mesmo sem o erro acima. **Causa:** não defini condição de saída.
 -A verificação `if nome_animal in animais_permitidos` ficou dentro do `for`, repetindo o teste a cada elemento em vez de uma única vez. **Causa:** indentação (bloco errado).
5. **Decisão de ajuste + fonte:** Usar nomes distintos (`for animal in animais_permitidos`) para preservar a lista `animais`; validar `nome_animal` uma única vez, antes de percorrer as listas; inserir com `animais.append(nome_animal)`; inicializar o contador fora do laço (ou usar `enumerate()`); e incluir uma condição de saída com `break`. **Fontes:** instrução `for` (https://docs.python.org/3/tutorial/controlflow.html#for-statements), `enumerate()` (https://docs.python.org/3/library/functions.html#enumerate) 
6. **Feedback recebido (inclui devolutiva da P1) e o que mudei:** Retorno da execução: o `traceback` apontou a linha 16 e levou à descoberta da reatribuição do nome `animais`; a mudança definida é renomear a variável de laço. Feedback de professor/colega: sem feedback externo neste ciclo.
7. **Próximo passo:** Estudar listas em profundidade (`índice`, `fatiamento` e `append`) e evitar reutilizar nomes de variáveis.

## 🟠 CICLO 07 — 07/10 — Listas: armazenamento e iteração

<details>
<summary>📘 Orientações do Ciclo 07</summary>

- **Sem Campo do Protocolo hoje.** Preencha o Registro do Ciclo 07.
- Justifique **por que seus dados cabem em uma lista** e como você os percorre (iteração).
- Item 4: erros típicos — índice fora do intervalo, alterar a lista enquanto percorre, confundir cópia com referência. Registre qual deles aconteceu e a causa técnica.
- Item 3: nomeie as **operações de lista** que usou (adicionar, remover, ordenar, fatiar…).
</details>

#### Registro do Ciclo 07 — 07/10
1. **Desafio do ciclo (em 1 frase):** Armazenar valores em uma list, acessá-los por índice positivo e negativo, fatiá-los e acrescentar novos itens
2. **O que implementei (commits / arquivos / links):** `aula2110.py`, com a lista `lista_de_carros` de 10 elementos de tipos mistos (`str`, `int`, `bool` e `float`), `len()`, indexação (`[0]` e `[-1]`), fatiamento (`[3:6:]` e `[2:-1:3]`) e `append()` com valor lido por `input()`.
3. **Objeto(s) de conhecimento mobilizado(s):** `list` (estrutura ordenada, mutável e heterogênea), índice iniciado em 0 e índice negativo, fatiamento `[início:fim:passo]` com fim exclusivo, `len()`, `append()`, `input()` devolvendo` str`.
4. **Desvio ou erro encontrado + causa técnica:** Escrevi `lista = []` e, na linha seguinte, `lista = (input("Digite aqui: "))`. A segunda atribuição sobrescreve a lista vazia por uma str (os parênteses apenas agrupam a expressão, não criam lista nem tupla), então a linha `lista = []` ficou sem utilidade. Além disso, o valor digitado entra na lista como `str`: com a entrada `70`, o elemento adicionado foi `'70'`, enquanto 67 e 69 são `int`, e a lista passou a guardar tipos diferentes para o mesmo tipo de dado.
5. **Decisão de ajuste + fonte:** Usar uma variável com nome próprio, `novo_item = input("Digite aqui: ")`, sem reatribuir o nome da lista, e converter com `int()` quando o item for numérico antes do `append`. Fonte: documentação oficial do Python, métodos de lista (https://docs.python.org/3/tutorial/datastructures.html#more-on-lists) e `input()` (https://docs.python.org/3/library/functions.html#input).
6. **Feedback recebido e o que mudei:** Retorno da execução: a saída `'70'` entre aspas evidenciou o tipo `str`; a mudança definida é a variável `novo_item` com conversão. Feedback de professor/colega: sem feedback externo neste ciclo.
7. **Próximo passo:** Estudar dicionários para representar um item com campos nomeados, em vez de listas paralelas.

## 🟠 CICLO 08 — 14/10 — Busca/consulta e introdução a dicionários e matrizes

<details>
<summary>📘 Orientações do Ciclo 08</summary>

- **Sem Campo do Protocolo hoje.** Preencha o Registro do Ciclo 08.
- Explique **por que cada item do seu catálogo virou um dicionário** (chave → valor) em vez de uma lista de valores soltos.
- Item 4: registre **qual busca falhou** (item inexistente, tipo diferente — `"2"` ≠ `2`, chave com maiúscula errada) e a causa técnica.
- Se usou o lote de dados defeituoso, registre **qual registro** quebrou a busca.
- Item 5: cite a fonte (*Pense em Python*, cap. 11, ou outra).
</details>

#### Registro do Ciclo 08 — 14/10
1. **Desafio do ciclo (em 1 frase):** Representar cada registro como um dicionário (chave → valor) dentro de uma lista (catálogo)
2. **O que implementei (commits / arquivos / links):** `aula0411.py`, com a lista `catalogo` de dicionários com as chaves `"pessoa"`, `"tipo"` e `"peso"`, o contador `proximo_codigo = 3`, o acesso `catalogo[0]["tipo"]` e uma busca por `for` com `if` `item["pessoa"] == codigo`.
3. **Objeto(s) de conhecimento mobilizado(s):** `dict` (pares chave → valor), lista de dicionários, acesso por chave, `append()`, conversão `float(input(...))`, busca linear com variável sentinela (`encontrado = None`) e `break`. Cada registro virou um dicionário porque cada campo passa a ter nome (`item["peso"]`) em vez de depender da posição, o que evita as listas paralelas que usei no `crud.py` (`nomes`, `quantidades`, `precos`).
4. **Desvio ou erro encontrado + causa técnica:** `TypeError: unsupported operand type(s) for +=: 'builtin_function_or_method' and 'int'` na linha `catalogo.append += 1` (verificado ao executar). **Causa técnica:** `append` é um método, e  `+=` tentou somar 1 a ele; a intenção era chamar `catalogo.append(novo)` e incrementar `proximo_codigo += 1`.Com os códigos 1 e 2, ambos existentes no catálogo, encontrado permaneceu `None` (verificado em teste isolado)
5. **Decisão de ajuste + fonte:** Trocar por `catalogo.append(novo)` seguido de `proximo_codigo += 1`; escrever `encontrado = item` antes do `break`; testar `if` encontrado `is not None` depois do laço; e ler o tipo com `tipo = input("Tipo: ")`. Fontes: dicionários (https://docs.python.org/3/tutorial/datastructures.html#dictionaries), métodos de lista (https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
6. **Feedback recebido e o que mudei:** Retorno da execução: o `traceback` da linha 16 e a busca devolvendo `None` mostraram os dois defeitos; as mudanças definidas estão no item 5. Feedback de professor/colega:sem feedback externo neste ciclo.
7. **Próximo passo:** Estudar atualização e exclusão (CRUD completo) e avaliar migrar o `crud.py` de três listas paralelas para uma lista de dicionários.
---

# 🔵 GRUPO 3 — prazo quinta 26/11 às 23h59

> **Janela:** sábado 21/11 → quinta 26/11. **O que entregar:** Registros dos Ciclos 09, 10, 11 e 12 · Campo 05 (duas revisões por pares) · Campo 06 · Campo 07.
>
> ⚠️ O prazo vem **um dia depois da P2 (25/11)**. Os Campos 06 e 07 dependem de todo o Logbook: deixe-os para o final, mas **adiante o rascunho do 6c e do 7a/7b antes da Defesa (18/11)**.

**Checklist do Grupo 3**
- [ ] Registros dos Ciclos 09, 10, 11 e 12 com os 7 itens
- [ ] Campo 05: duas revisões (Ciclos 09 e 12), blocos 5a a 5e
- [ ] Campo 06: decisão autônoma, lacuna com plano, pergunta da banca com 5 linhas ou mais
- [ ] Campo 07: 7a a 7e, com 3 objetos, 2 equívocos corrigidos e transferência
- [ ] Coerência entre Campo 01 e Campo 07
- [ ] Painel de acompanhamento completo

## 🔵 CICLO 09 — 21/10 — Atualização e exclusão: CRUD completo

<details>
<summary>📘 Orientações do Ciclo 09 — Registro + Campo 05 (revisão por pares nº 1)</summary>

- Neste ciclo seu CRUD ficou **completo** (Create, Read, Update, Delete). Preencha o Registro do Ciclo 09.
- **Item 4:** *atualizar* ou *excluir* item inexistente, e excluir durante um laço (a lista muda de tamanho e itens são pulados) são erros comuns.
- **Campo 05 — Registro de Revisão por Pares.** Você passa a ser **revisor** do CRUD de um colega.
  - Cada revisão tem **um registro** (copie a seção do Campo 05) com o nome e o link do repositório revisado.
  - **Revise o processo, não só o código:** o que foi decidido, em que objeto de conhecimento se apoia, com que fonte.
  - **5a:** liste as etapas da revisão (ex.: rodar o CRUD, testar com o lote de dados com defeito, ler o código, registrar achados, devolver feedback).
  - **5b:** liste os insumos que usou (lote de dados, casos de teste, `requisitos.md`) com quantidade planejada, utilizada e variação.
  - **5c:** diga se a solução do colega atende ao critério (Sim/Parcialmente/Não) e **qual critério** usou (ex.: requisito do `requisitos.md`).
  - **5d:** riscos da revisão (ex.: não conseguir rodar o código do colega) e como mitigou.
  - **5e:** registre **cada decisão técnica** da revisão com **data, responsável, objeto de conhecimento e fundamentação/referência**. *Sem objeto e sem referência, não é rastreável.*
  - Feedback ao colega: **específico e respeitoso** (o que está bom, o que quebrou, como reproduzir, sugestão).
</details>

#### Registro do Ciclo 09 — 21/10
1. **Desafio do ciclo (em 1 frase):**Completar o CRUD com **atualização** e **exclusão** de itens, tratando o item inexistente e evitando alterar a lista de forma incorreta durante a busca.
2. **O que implementei (commits / arquivos / links):** `crud.py` (link na Identificação): opções **3 – Atualizar item** e **4 – Remover item** do menu. As duas buscam o item pelo nome com `while i < len(nomes) and not encontrado`.
3. **Objeto(s) de conhecimento mobilizado(s):** CRUD (Create, Read, Update, Delete); `list` (atribuição por índice `nomes[i] = novo_nome`, `pop(i)`, `remove()`, `len()`) busca linear com variável sentinela do tipo `bool` (`encontrado = False` → `True`); laço `while` com condição composta (`and`, `not`); validação de entrada (`while campo == ""`). Usei `while` com índice manual, e não `for` com remoção dentro do laço, porque remover elementos de uma lista enquanto ela é percorrida desloca os índices e faz o laço pular itens.
4. **Desvio ou erro encontrado + causa técnica:** **Nomes duplicados:** a busca e a exclusão atuam só na **primeira ocorrência**. Teste: cadastrei `leite (qtd 1)` e `leite (qtd 2)`, removi "leite" e a lista ficou com `leite (qtd: 2)`. Causa: busco por **nome**, que é um valor não único, e encerro o laço na primeira correspondência (`not encontrado`).
5. **Decisão de ajuste + fonte:** Mantive a busca com *flag* e parada na primeira ocorrência, porque ela evita alterar a lista durante a iteração e, com `pop(i)` em duas listas, mantém as três listas paralelas alinhadas (o `remove(busca)` remove o primeiro valor igual, que é justamente o elemento do índice `i`). (https://docs.python.org/3/tutorial/datastructures.html#more-on-lists).
6. **Feedback recebido e o que mudei:** Retorno da execução: os testes acima confirmaram atualização e exclusão corretas para nomes únicos e evidenciaram o problema dos nomes duplicados. Sem feedback externo neste ciclo
7. **Próximo passo:** Dividir o CRUD em funções (Ciclo 10), eliminando a repetição dos blocos de validação.

### 🧩 CAMPO 05 — Registro de Revisão por Pares
*Adaptação do **Logbook do Time** (Apêndice C) para o CRUD individual. Documento atualizado pelo **revisor**. Cada decisão técnica relevante deve ter associado o objeto de conhecimento correspondente.*

> ⚠️ **Nota de adaptação:** o Apêndice C original prevê Gestor, Responsável Técnico, Analista de Qualidade e Comunicador. Como o CRUD é **individual** e os alunos atuam como **revisores**, mantive os blocos 5a a 5e e troquei os papéis por **Autor** (dono do CRUD) e **Revisor** (você). *Pendente de validação do professor/NDE.*

> **O Logbook de revisão é um registro de conhecimento em ação.** Cada decisão técnica relevante deve estar associada ao objeto de conhecimento que a fundamenta, à justificativa técnica e à referência utilizada. Registros sem esse vínculo não são aceitos.

#### Revisão nº 1

| | |
|---|---|
| **Autor do CRUD revisado** | Samuel DEnzel de Castro Serra |
| **Repositório revisado** | [_link_](https://github.com/denzelsxz/denzel) |
| **Revisor** | Eduardo Oliveira Gomes |
| **Unidade curricular / Semestre** | Algoritmos e Programação · 2026.2 |
| **Ciclo / data** | _Ciclo 09 · 24/11_ |

**5a. AVANÇO DO PROCESSO DE REVISÃO — análise técnica de cada etapa:**

| ETAPA DO PROCESSO | RESPONSÁVEL | PRAZO | STATUS | DESVIO / JUSTIFICATIVA |
|---|---|---|---|---|
| 1. Clonar/abrir o repositório do colega e executar o CRUD  | Eduardo / Samuel | _24/11 | x Concluída ☐ Em andamento ☐ Com desvio | _…_ |
| 2. Rodar os 7 casos de teste planejados (5b) | Eduardo / Samuel | _24/11_ | x Concluída ☐ Em andamento ☐ Com desvio | _…_ |
| 3. Ler o código e conferir laços, condicionais e estruturas de dados | Eduardo / Samue  | _24/11_ | x Concluída ☐ Em andamento ☐ Com desvio | _…_ |
| 4. Registrar os achados (o que está bom, o que quebrou e como reproduzir) | Eduardo / Samuel | _D2411_ | x Concluída ☐ Em andamento ☐ Com desvio | _…_ |
| 5. Devolver o feedback ao autor | Eduardo / Samuel | _24/11_ | x Concluída ☐ Em andamento ☐ Com desvio | _…_ |

**5b. ANÁLISE DE INSUMOS E CRITÉRIOS DE QUALIDADE:**

| RECURSO | QTDE PLANEJADA | QTDE UTILIZADA | VARIAÇÃO | JUSTIFICATIVA TÉCNICA |
|---|---|---|---|---|
| Horas de estudo | 2 Horas | 1:47h | _…_ | Tempo estimado para dominar, itens inexistentes, `def` e `return` e com prática em casa. |
| Horas de prática | 1 hora e 30 min | 1 Hora | _…_ |Tempo para poder botar a mão na massa e compreender o uso da função e suas regras.  |
| Exercícios | 30 min | 30 min | _…_ | Tempo médio para aprender como usar e onde usar as funções `def` e `return`.|

**5c. CONTROLE DE QUALIDADE:**
- **Critério ou norma técnica:** Requisitos da `aula0411.py`
- **A solução atende?** ☐ Sim x Parcialmente ☐ Não

**5d. GESTÃO DE RISCOS:**
- **Risco:** Devido as configurações do sistema de leitura da linguagem Python, o risco de haver desavenças entre uma versão recente e outra cuja pode ser mais ultrapassada, aumenta em mais linhas de código ou funções novas que podem dificultar a compreensão do mesmo.
- **Estratégia de mitigação:** Estar sempre atento aos lançamentos de novas versões para que os modelos do mesmo sejam compreendidos pelo o revisor/autor.

**5e. RASTREABILIDADE DAS DECISÕES TÉCNICAS — COM VÍNCULO AO CONTEÚDO:**

| DATA | DECISÃO TÉCNICA | RESP. | OBJETO DE CONHECIMENTO MOBILIZADO | FUNDAMENTAÇÃO / REFERÊNCIA |
|---|---|---|---|---|
| _24/11/2026_ | Eduardo | O uso de `def` e `return` | Python.org |


> **IMPORTANTE:** Decisão registrada sem objeto de conhecimento associado e sem referência é considerada **não rastreável** e não conta para a avaliação formativa. O vínculo entre processo e conteúdo é obrigatório em todas as decisões relevantes.

## 🔵 CICLO 10 — 28/10 — Modularização: funções

<details>
<summary>📘 Orientações do Ciclo 10</summary>

- **Sem Campo do Protocolo hoje.** Preencha o Registro do Ciclo 10.
- Explique **como dividiu** o CRUD em funções (`cadastrar()`, `buscar()`, `alterar()`, `excluir()`, `listar()`, `menu()`) e **por que** cada função tem aquela responsabilidade.
- Item 4: erros típicos — variável fora de escopo, função sem `return`, parâmetro na ordem errada.
- Compare o código **antes e depois** da refatoração: o que ficou mais claro? Registre no item 6 o feedback do colega que fez a *peer review*.
</details>

#### Registro do Ciclo 10 — 28/10
1. **Desafio do ciclo (em 1 frase):** Dividir o CRUD em funções com uma responsabilidade cada (por exemplo, ler campo, buscar, listar, menu)
2. **O que implementei (commits / arquivos / links):** `crud.py`
3. **Objeto(s) de conhecimento mobilizado(s):** _…_
4. **Desvio ou erro encontrado + causa técnica:** Diagnóstico do `crud.py` atual: as variáveis `busca`, `encontrado` e `i` são reutilizadas nas opções 3 e 4 no mesmo escopo global. Hoje não há erro, porque cada opção reinicializa `encontrado = False` e `i = 0`, mas o estado compartilhado é um risco: esquecer uma reinicialização faria a busca seguinte começar com o valor da anterior. Causa: ausência de funções, que isolariam o escopo de cada operação.
5. **Decisão de ajuste + fonte:** Dividi um programa grande em blocos menores, independentes e reutilizáveis, onde cada bloco executa uma única tarefa bem definida. (https://docs.python.org/3/tutorial/datastructures.html#more-on-lists).
6. **Feedback recebido e o que mudei:** Recebi o apontamento de que manter variáveis de controle (busca, encontrado, i) no escopo global aumenta o acoplamento temporal e o risco de efeitos colaterais entre fluxos.
7. **Próximo passo:** Concluir a extração das funções restantes (`ler_campo`, `buscar_registro`, `listar_registros` e `exibir_menu`), garantindo que todas recebam dependências por parâmetro e retornem valores em vez de depender de variáveis globais.

## 🔵 CICLO 11 — 04/11 — Recursividade

<details>
<summary>📘 Orientações do Ciclo 11 — Registro + Campo 06 (Grupo 3)</summary>

- Preencha o Registro do Ciclo 11 (caso base, chamada recursiva, pilha de execução).
- **Campo 06 — Próximos passos para a defesa** · *individual · quinta 26/11, 23h59*. Prepare-se para a **Defesa Técnica de quarta 18/11**: como o prazo é posterior à defesa, **adiante pelo menos o 6c** (pergunta da banca e resposta) e leve-o para a arguição.
  - **6a.** Uma **decisão técnica que você defende com plena autonomia**: algo que aprendeu e **é exclusivamente seu**, que nenhum colega consegue explicar por você.
  - **6b.** Uma **lacuna técnica real** e um **plano de ação** com passos e datas para saná-la antes da defesa.
  - **6c.** Uma **pergunta que a banca pode fazer** (nível de Avaliação ou Criação) e a sua **resposta fundamentada em, no mínimo, 5 linhas**, com o objeto de conhecimento e a fonte.
  - Dica: leia a **Rubrica de Defesa Técnica** (no Encerramento) e escolha uma pergunta que teste *aplicação*, *evolução* ou *transferência*.
</details>

#### Registro do Ciclo 11 — 04/11
1. **Desafio do ciclo (em 1 frase):** Estruturar um catálogo em memória com lista de dicionários, cadastro incremental por código e consulta de registro por identificador.
2. **O que implementei (commits / arquivos / links):** Rascunho inicial de catálogo em Python (em `crud.py` / anotações da aula de 04/11).
3. **Objeto(s) de conhecimento mobilizado(s):** Listas (`list´` ), dicionários (`dict`), acesso e indexação por chave, laços de repetição (`for`,` while`), variáveis de controle e entrada/saída (`input`, `print`).
4. **Desvio ou erro encontrado + causa técnica:** Há falhas de sintaxe, lógica e semântica no código: `print(len(catalogo))`, "`tipo`" deixa "tipo" solto fora da chamada; `tipo = ("Tipo:")` atribui uma `str` literal em vez de ler a entrada com `input(); catalogo.append += 1` tenta somar 1 a um método em vez de usar `catalogo.append(novo)` e incrementar `proximo_codigo += 1`; no laço de busca, o break ocorre sem atribuir `encontrado = item`, e o `if encontrado:` está indentado dentro do `for` em vez de fora. **Causa:** mistura de rascunho de chamadas, operadores incompatíveis e erro de fluxo/indentação na busca.
5. **Decisão de ajuste + fonte:** Corrigi a leitura de tipo com `input()`, substituí `catalogo.append += 1` por `catalogo.append(novo)` com atualização de `proximo_codigo`, atribui  `encontrado = item` antes do `break` e a verificação de encontrado para fora do laço, (https://docs.python.org/3/tutorial/datastructures.html).
6. **Feedback recebido e o que mudei:** Durante a revisão do rascunho em aula, identifiquei que a busca não armazenava o item localizado nem exibia o resultado após o término do laço, além de o cadastro não inserir o dicionário novo na lista. Ajustei a atribuição de `encontrado`, a posição do `if` e a inserção via `append`.
7. **Próximo passo:** Integrar a manipulação da lista de dicionários às funções com responsabilidade única iniciadas no Ciclo 10 (cadastro, busca e listagem) e testar entradas inválidas e códigos inexistentes.

### 🧩 CAMPO 06 — Próximos passos para a defesa
*AV Qualis — Grupo 3 | Individual | Quinta 26/11, 23h59*

**6a. Decisão técnica que defendo com plena autonomia — o que aprendi que é exclusivamente meu e não consigo transferir para nenhum colega:**

> Defendo a decisão de buscar, atualizar e remover itens com um laço `while` controlado por um índice manual `i` e por uma variável sentinela booleana (`while i < len(nomes) and not encontrado`), em vez de um `for` com `remove()` dentro do laço. A razão técnica é que remover elementos de uma lista enquanto ela é percorrida por `for` encolhe a lista e desloca os índices, e o laço pula o elemento seguinte. Com o `while`, eu controlo o `i`, paro na primeira ocorrência e a condição `i < len(nomes)` impede que o corpo acesse `nomes[i]` fora do intervalo (`IndexError`). Na exclusão, uso `pop(i)` nas listas `quantidades` e `precos` e `remove(busca)` em `nomes`; as três operações atingem o mesmo item porque `remove()` apaga a primeira ocorrência do valor e o laço parou justamente no primeiro índice em que `nomes[i] == busca`. Sei que essa decisão tem um limite: com nomes repetidos, só a primeira ocorrência é afetada (testei com dois "leite"), e que a solução seria um identificador único.
**6b. Lacuna técnica e plano de ação para saná-la:**

- **Lacuna:** Ainda não apliquei funções (`def`, parâmetros e `return`) nem recursividade em nenhum arquivo do repositório: o `crud.py` tem 148 linhas no escopo global, com 9 blocos repetidos de revalidação `while campo == ""` e a listagem escrita duas vezes. Também não converto as entradas com `int()`/`float()` (Campo 03b).
- **Plano de ação (passos e datas):** 24/11: extrair uma função `ler_texto(mensagem)` para os 9 blocos de revalidação e uma função `listar()` para as duas listagens, com um commit por extração. 25/11, depois da P2: estudar `def`, parâmetros, `return` e escopo na documentação (https://docs.python.org/3/tutorial/controlflow.html#defining-functions). 26/11 até a tarde: criar `buscar()` retornando o índice (ou -1) e `ler_numero_positivo()` com `try/except ValueError`, rodar os 7 casos de teste e fazer o commit final, para depois registrar os Ciclos 10 e 12.

**6c. Pergunta que a banca pode fazer — com resposta fundamentada (mínimo 5 linhas):**

- **Pergunta:** Seu CRUD guarda nome, quantidade e preço em três listas paralelas. Avalie essa escolha: em que situação ela falha e por que uma lista de dicionários seria melhor?
- **Resposta:**

> Escolhi três listas porque era a estrutura que eu dominava no Ciclo 07: cada `append` no cadastro mantém os índices alinhados, e a listagem lê `nomes[i]`, `quantidades[i]` e `precos[i]` com o mesmo `i`. O problema é que a relação entre nome, quantidade e preço existe só pela **posição**, e não na estrutura de dados. Qualquer operação que altere uma lista e esqueça as outras desalinha tudo: na exclusão eu preciso de `pop(i)` em duas listas e `remove(busca)` na terceira, e se eu omitir uma delas o preço de um item passa a aparecer no item vizinho; ordenar apenas a lista `nomes` teria o mesmo efeito. Hoje o código funciona porque cada operação encerra na primeira ocorrência e `remove()` apaga o primeiro valor igual, que é o elemento do índice `i` (testei com dois "leite"). Com uma lista de dicionários, como no `aula0411.py` (`{"pessoa": 1, "tipo": "ectomorfo", "peso": 80.6}`), cada item é uma unidade só: a exclusão vira um único `pop(i)`, o acesso é por chave (`item["preco"]`) e posso acrescentar um campo novo sem criar uma quarta lista. A limitação da minha resposta é que o dicionário sozinho não resolve nomes duplicados: eu ainda precisaria de um identificador único, como o `proximo_codigo`, e essa refatoração ainda não foi aplicada no repositório.

**Objeto de conhecimento mobilizado:** `list` (índice, `pop()`, `remove()`), `dict` (chave → valor), lista de dicionários, busca linear.
**Fonte:** Documentação oficial do Python, estruturas de dados — métodos de lista e dicionários (https://docs.python.org/3/tutorial/datastructures.html).

## 🔵 CICLO 12 — 11/11 — Refatoração e qualidade de código

<details>
<summary>📘 Orientações do Ciclo 12 — Registro + Campo 05 (revisão nº 2) + início do Campo 07</summary>

- Preencha o Registro do Ciclo 12. Registre o que revisou: código duplicado, nomes ruins, funções grandes, comentários desnecessários, lógica confusa.
- **Campo 05 — Revisão por pares nº 2.** Foque em **qualidade**: o CRUD do colega resiste aos casos de teste (mínimos, máximos, inválidos, entradas vazias) e ao **lote de dados com defeito**? Use a seção abaixo (copie o bloco *Revisão nº 1* do Ciclo 09 e preencha novamente).
- **Campo 07 — Evolução conceitual** · *individual · quinta 26/11, 23h59.* Comece agora, enquanto a memória do semestre está fresca; leve o rascunho de 7a e 7b para a Defesa de 18/11. Dicas por item:
  - **7a.** Releia o **Campo 01** e resuma o que você *pensava* e *achava que sabia*. Seja honesto, mesmo se o Campo 01 estiver "errado".
  - **7b.** Pelo menos **3 objetos de conhecimento** na tabela: o que você *não dominava*, o que *aprendeu e consegue demonstrar* e a **evidência** (em qual Campo ou ciclo do Logbook aparece).
  - **7c.** Pelo menos **2 equívocos corrigidos**, dizendo **o que os corrigiu** (Fechamento Teórico, pesquisa, *Peer Review*, arguição, devolutiva da P1).
  - **7d.** **Transferência:** um exemplo concreto de aplicar o que aprendeu em um **contexto diferente** do CRUD (outra área do seu curso ou outro tipo de sistema).
  - **7e.** Avaliação honesta do que **ainda não domina** e vai aprofundar.
</details>

#### Registro do Ciclo 12 — 11/11
1. **Desafio do ciclo (em 1 frase):** _…_
2. **O que implementei (commits / arquivos / links):** _…_
3. **Objeto(s) de conhecimento mobilizado(s):** _…_
4. **Desvio ou erro encontrado + causa técnica:** _…_
5. **Decisão de ajuste + fonte:** _…_
6. **Feedback recebido e o que mudei:** _…_
7. **Próximo passo:** _…_

### 🧩 CAMPO 05 — Registro de Revisão por Pares (revisão nº 2)

| | |
|---|---|
| **Autor do CRUD revisado** | _nome_ |
| **Repositório revisado** | _link_ |
| **Revisor** | _seu nome_ |
| **Ciclo / data** | _Ciclo 12 · 11/11_ |

**5a. AVANÇO DO PROCESSO DE REVISÃO:**

| ETAPA DO PROCESSO | RESPONSÁVEL | PRAZO | STATUS | DESVIO / JUSTIFICATIVA |
|---|---|---|---|---|
| 1. _…_ | Revisor / Autor | _DD/MM_ | ☐ Concluída ☐ Em andamento ☐ Com desvio | _…_ |
| 2. _…_ | Revisor / Autor | _DD/MM_ | ☐ Concluída ☐ Em andamento ☐ Com desvio | _…_ |
| 3. _…_ | Revisor / Autor | _DD/MM_ | ☐ Concluída ☐ Em andamento ☐ Com desvio | _…_ |
| 4. _…_ | Revisor / Autor | _DD/MM_ | ☐ Concluída ☐ Em andamento ☐ Com desvio | _…_ |
| 5. _…_ | Revisor / Autor | _DD/MM_ | ☐ Concluída ☐ Em andamento ☐ Com desvio | _…_ |

**5b. ANÁLISE DE INSUMOS E CRITÉRIOS DE QUALIDADE:**

| RECURSO | QTDE PLANEJADA | QTDE UTILIZADA | VARIAÇÃO | JUSTIFICATIVA TÉCNICA |
|---|---|---|---|---|
| _…_ | _…_ | _…_ | _…_ | _…_ |
| _…_ | _…_ | _…_ | _…_ | _…_ |
| _…_ | _…_ | _…_ | _…_ | _…_ |

**5c. CONTROLE DE QUALIDADE:**
- **Critério ou norma técnica:** _…_
- **A solução atende?** ☐ Sim ☐ Parcialmente ☐ Não

**5d. GESTÃO DE RISCOS:**
- **Risco:** _…_
- **Estratégia de mitigação:** _…_

**5e. RASTREABILIDADE DAS DECISÕES TÉCNICAS — COM VÍNCULO AO CONTEÚDO:**

| DATA | DECISÃO TÉCNICA | RESP. | OBJETO DE CONHECIMENTO MOBILIZADO | FUNDAMENTAÇÃO / REFERÊNCIA |
|---|---|---|---|---|
| _DD/MM/AA_ | _…_ | _…_ | _…_ | _…_ |
| _DD/MM/AA_ | _…_ | _…_ | _…_ | _…_ |
| _DD/MM/AA_ | _…_ | _…_ | _…_ | _…_ |
| _DD/MM/AA_ | _…_ | _…_ | _…_ | _…_ |
| _DD/MM/AA_ | _…_ | _…_ | _…_ | _…_ |

### 🧩 CAMPO 07 — Evolução conceitual
*AV Qualis — Grupo 3 | Individual | Quinta 26/11, 23h59*

*Evidência rastreável de aprendizagem entre o início e o encerramento do ciclo AFP.*

**7a. O que eu pensava no início do ciclo (com base no Campo 01 — registrar a hipótese inicial e os objetos de conhecimento que achava conhecer):**

> No início do ciclo, eu acreditava que teria que desenvolver o front-end do projeto para poder mostrar à uma banca, na qual iria avaliar o nosso sistema com base nos fundamentos dado em sala de aula e estudos internos, acreditava também que além das funções `append` e `remove`, ia aprender sobre importações de bibliotecas e implementação de outros códigos.

**7b. O que aprendi — conceitos, princípios ou relações técnicas que não dominava no início e que agora consigo explicar com precisão (mínimo 3 objetos de conhecimento):**

| OBJETO DE CONHECIMENTO | O QUE EU NÃO DOMINAVA | O QUE APRENDI E CONSIGO DEMONSTRAR | EVIDÊNCIA (campo do Logbook onde aparece) |
|---|---|---|---|
| Funções |Como usar `append` e `remove` e quando estruturar trechos em funções reutilizáveis  | Diferenciar funções de métodos de lista, adicionar itens ao final com `append()`, remover elementos específicos com `remove()` e organizar operações em funções | `crud.py` |
| Listas e pilhas | O funcionamento interno de listas e pilhas e o critério para escolher cada estrutura |Listas permitem acesso/manipulação por indíce e `append()` insere no fim; pilhas seguem a lógica LIFO (Last-In, First-Out), removendo sempre o último elemento inserido | `aula2110.py`|
| Laaços de repetição | As regras de parada e quando aplicar `while` ou `for` | Usar `for` para percorrer sequências/iterações definidas e `while` para repetir blocos enquanto uma condição permanecer verdadeira, evitando loops infinitos | `aula0909.py` e `aula3009.py`|

**7c. Conceitos que precisei corrigir ao longo do ciclo — onde eu estava equivocado e o que o corrigiu (Fechamento Teórico, pesquisa, Peer Review, arguição):**

1. **Equívoco:** Achar que `append` e `remove` eram funções soltas ou que podiam ser usados indistintamente sem entender o efeito no índice/posição da lista.— **Correção:** `append` insere apenas no final da lista e `remove` apaga a primeira ocorrência do valor informado, alterando o tamanho e os índices seguintes.
   **O que corrigiu:** Fechamento Teórico e testes práticos em `crud.py` 
2. **Equívoco:** Confundir o uso de `while` e `for`, ou assumir que uma condição em `while` se atualiza sozinha a cada iteração. — **Correção:** `for` é mais indicado quando há um iterável ou quantidade conhecida de passos;` whil`e exige que a condição mude dentro do laço para não travar a execução
   **O que corrigiu:** Exercícios e revisão em `aula0909.py`,  `aula3009.py` e Peer Review.

**7d. Transferência — como este aprendizado se aplica a um contexto diferente do problema trabalhado (ao menos 1 exemplo concreto da área de formação):**

> A lógica de laços de repetição e estruturas como listas e pilhas se aplica diretamente ao processamento de dados e automação de tarefas na área de computação/desenvolvimento: por exemplo, percorrer registros vindos de um arquivo ou API com `for`, validar entradas até uma condição válida com `while`, ou usar uma pilha para controlar histórico de ações (desfazer/undo) e chamadas em execução.

**7e. Avaliação honesta do próprio percurso — o que ainda não domino e preciso aprofundar após este ciclo:**

> Ainda não domino com segurança o tratamento de erros (como tentar remover um item que não existe na lista), a decomposição de problemas maiores em várias funções pequenas e bem testadas, e a escolha da estrutura de dados mais eficiente quando o volume de dados cresce. No próximo ciclo, quero focar em escrever códigos mais legíveis, prever casos de borda e praticar mais resolução de problemas sem depender de tentativa e erro.

---

# 🏁 DEFESA TÉCNICA — quarta 18/11

<details>
<summary>📘 Orientações para a Defesa Técnica e preparação</summary>

**A Defesa é antes dos prazos dos Grupos 2 e 3.** Você será arguido sobre o que já estiver registrado e commitado. Priorize, até **terça 17/11**:
- [x] **Grupo 1 entregue** (prazo 16/11): Identificação, Registros 01 a 04, Campos 01 e 02.
- [x] **Campo 04 (IA)** e **Campo 03** ao menos em rascunho, para sustentar as perguntas sobre decisões (critérios 2 e 5).
- [x] **Campo 06c** (pergunta da banca e resposta) e **rascunho de 7a e 7b**, para sustentar a evolução conceitual (critério 3).
- [x] Registros dos Ciclos já feitos, mesmo que ainda não "entregues" no prazo do grupo.
- [x] `README.md`, `docs/` e CRUD rodando.
- [x] Você consegue explicar **cada linha** do seu código e **cada decisão** registrada.
- Os demais itens seguem com os prazos dos grupos (21/11 e 26/11). A banca pode consultar o histórico do Git.

**A Defesa Técnica é individual.** Você será arguido sobre o que registrou. Cada aluno recebe pelo menos **1 questão** nos níveis de **Avaliação** ou **Criação** (taxonomia de Bloom).

**Como a Rubrica se liga ao seu Logbook:**

| Critério da Rubrica | Onde você prepara a evidência |
|---|---|
| 1. Domínio dos objetos de conhecimento | Campos 01, 02 e 07b |
| 2. Aplicação do conteúdo à solução ⚠️ *inegociável* | Registros dos ciclos (itens 3 e 5), Campo 03c e Campo 05e |
| 3. Evolução conceitual ⚠️ *inegociável* | Campo 01 → Campo 07 (7a, 7b e 7c; leve o rascunho) |
| 4. Capacidade de transferência | Campo 07d |
| 5. Argumentação sob pressão | Campo 06c e Campo 04e |
| 6. Autonomia intelectual e coerência com o Logbook | Todo o Logbook (principalmente Campos 04 e 06a) |

**Treino:** peça a um colega que faça 3 perguntas "imprevistas" sobre o seu CRUD e responda **sem consultar** o Logbook. Se não conseguir, volte ao Campo 06b.
</details>

## 🧩 RUBRICA DE DEFESA TÉCNICA (revisada)
*Avaliação individual de cada membro na Semana 16. Cada membro recebe ao menos 1 questão nos níveis de Avaliação ou Criação da Taxonomia de Bloom. Critérios revisados para medir aprendizagem, aplicação, evolução e transferência do conteúdo.*

| | |
|---|---|
| **Nome** | _…_ |
| **Curso / Time / Função** | _…_ |

<details>
<summary>🔒 Uso do professor — rubrica completa</summary>

| CRITÉRIO | EXCELENTE (4,0) | SATISFATÓRIO (3,0) | INSATISFATÓRIO (2,0) | AUSENTE (0) |
|---|---|---|---|---|
| **1. DOMÍNIO DOS OBJETOS DE CONHECIMENTO** — Responde com precisão técnica, sem apoio dos colegas, demonstrando aprendizagem do conteúdo. | Responde com precisão e profundidade, nomeando os objetos de conhecimento mobilizados sem hesitação. | Responde com precisão, com imprecisões pontuais que não comprometem o raciocínio. | Responde de forma vaga, com erros conceituais relevantes ou dependendo dos colegas. | Não responde ou demonstra desconhecimento total. |
| **2. APLICAÇÃO DO CONTEÚDO À SOLUÇÃO** — Demonstra como os objetos de conhecimento fundamentaram as decisões do processo. | Explicita com precisão qual objeto de conhecimento fundamentou cada decisão relevante do processo investigativo, citando referência e demonstrando por que aquele conhecimento era o mais adequado. | Estabelece a relação conteúdo-decisão na maioria das perguntas, com alguma imprecisão pontual. | Não consegue explicitar a relação entre o conteúdo e as decisões do processo investigativo com clareza. | Não demonstra nenhuma relação entre os objetos de conhecimento e as decisões tomadas. |
| **3. EVOLUÇÃO CONCEITUAL** — Demonstra aprendizagem em relação ao que sabia no início do ciclo. | Identifica com precisão o que aprendeu, o que corrigiu e como o conhecimento evoluiu ao longo do ciclo. | Demonstra evolução em parte dos conceitos trabalhados, com alguma dificuldade de articular a trajetória. | Dificuldade em identificar diferenças entre o que sabia no início e o que domina agora. | Não demonstra nenhuma percepção de evolução conceitual ao longo do ciclo. |
| **4. CAPACIDADE DE TRANSFERÊNCIA** — Aplica o conhecimento a um contexto diferente do problema trabalhado. | Consegue transferir o aprendizado para um contexto novo com fundamentação técnica precisa. | Realiza a transferência com imprecisões que não comprometem a lógica do raciocínio. | Demonstra dificuldade em aplicar o conhecimento a contextos diferentes do problema original. | Não consegue realizar nenhuma transferência do conhecimento para contexto diferente. |
| **5. ARGUMENTAÇÃO SOB PRESSÃO** — Mantém coerência técnica diante de questionamentos imprevistos. | Mantém raciocínio coerente, reconhece limites com honestidade e reformula com fundamentação. | Mantém coerência na maior parte, com hesitações pontuais sem perda do fio técnico. | Fragilidade técnica diante de questionamentos imprevistos. | Não sustenta argumentação técnica diante de nenhum questionamento. |
| **6. AUTONOMIA INTELECTUAL E COERÊNCIA COM O LOGBOOK** — Defende o que registrou com consciência e sem depender do grupo. | Defende com precisão as decisões do Logbook, demonstrando autoria plena e independência intelectual. | Defende a maioria das decisões com coerência, com alguma imprecisão ou apoio pontual. | Depende dos colegas ou demonstra desconhecimento de parte do que registrou no próprio Logbook. | Não reconhece o que registrou ou não demonstra autonomia intelectual durante a arguição. |

**PONTUAÇÃO:** _____ / 24,0 **CONCEITO:** _____________

**Conversão:** 20–24 = Excelente (4,0) | 14–19 = Satisfatório (3,0) | 8–13 = Insatisfatório (2,0) | < 8 = Ausente (0)

> ⚠️ **Critérios 2 (Aplicação) e 3 (Evolução Conceitual) são inegociáveis — AUSENTE em qualquer um deles implica nota máxima de 2,0 na Defesa, independentemente do desempenho nos demais.**

**OBSERVAÇÕES:** _…_

**Professor(a):** _________________  **Data:** ___________
</details>

### Registro do Encerramento — 18/11
1. **O que apresentei/defendi (em 1 frase):** _…_
2. **Objeto(s) de conhecimento que a banca mais explorou:** _…_
3. **Pergunta que mais me desafiou e como respondi:** _…_
4. **O que levo deste semestre para o próximo módulo:** _…_

---

# 🆘 Estou atrasado no Logbook. E agora?

1. **Não apague nem "retroescreva" o passado.** Preencha agora e **escreva a data real** do preenchimento (ex.: *"preenchido com atraso em 12/11"*).
2. **Campo 01 e Checkpoint (sem consulta):** se perdeu a janela, registre **o que sabe hoje, sem consultar nada**, marcando-o como *preenchimento tardio*. Combine o tratamento com o professor.
3. **Priorize a ordem dos grupos:** Grupo 1 (16/11) → Defesa (18/11) → Grupo 2 (21/11) → Grupo 3 (26/11). Dentro de cada grupo, os Campos vêm antes dos Registros.
4. **Use o histórico do Git** (`git log --oneline`) para reconstruir o que fez em cada ciclo — ele é uma evidência melhor que a memória.
5. **Fale com o professor** antes do prazo, não depois.
