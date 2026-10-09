# Resumo Técnico e Narrativo: Projeto Recolor

## 1. Visão Geral do Projeto
**Projeto Recolor** é uma Visual Novel (VN) desenvolvida na engine **Ren'Py** (versão 8.5.3). O jogo mistura a estrutura clássica de narrativa interativa com uma mecânica de hardware customizado, indicando forte intenção de integração com um **Arduino** ou sensores externos para a resolução de puzzles físicos acoplados ao jogo.

## 2. Tecnologias e Arquitetura
- **Engine:** Ren'Py 8.5.3 (Python 3 baseado)
- **Linguagens:** Ren'Py Script (`.rpy`) e Python
- **Integração de Hardware:** Planejada integração com Arduino para leitura de sensores físicos (provavelmente sensores de cor, RFID ou botões) que interagem diretamente com o fluxo do jogo através de variáveis.

## 3. Estrutura do Código e Variáveis
O script principal (`game/script.rpy`) está dividido de forma linear com labels de controle de fluxo.

### Personagens Definidos
- `t`: Mestre Torii (Cor: #a39171)
- `j`: Joku (Cor: #4b86b4)
- `m`: Moli (Cor: #e8a87c)
- `z`: Zurie (Cor: #c38d9e)
- `a`: Aime (Cor: #85dcba)
- `g`: Gerivaldo (Cor: #d3a625)

### Labels Principais
- `label start`: Início do jogo, contém toda a introdução da lore e a progressão até o puzzle do portão.
- `label passou_teste`: Caminho de sucesso do puzzle do Arduino, o portão se abre.
- `label falhou_teste`: Caminho de falha do puzzle do Arduino, reinicia o loop mandando o jogador de volta ao início (não recomendado para fluxo real, pois recomeça toda a história).

## 4. Lore e Narrativa
O mundo é dividido entre Humanos e Monstros. No passado, uma guerra foi evitada graças à criação da "Sociedade dos Bruxos" por Gangis. 
- **A Unção:** É a força vital mágica que permeia o mundo. 
- **Mecânica de Visão:** Para enxergar a "Unção", um humano precisa ser daltônico. Por isso, a Sociedade dos Bruxos é formada exclusivamente por humanos daltônicos.
- **O Enredo:** Em 1999, rumores de uma invasão dos monstros fazem com que aprendizes de bruxos (Moli, Zurie, Joku e Aime), guiados pelo Mestre Torii, viagem até o mundo dos monstros.
- **O Desafio:** Ao chegar no portão dos monstros, o guardião Gerivaldo exige que eles passem por um teste físico e sensitivo com três pedras de essências e cores diferentes (1ª Musgo/Verde, 2ª Oceano/Azul, 3ª Sol/Amarelo).

## 5. Mecânicas de Jogo e Puzzle de Hardware
A parte final do script atual exige a resolução de um enigma onde o jogador precisa colocar a "pedra correta" sobre um sensor físico.

- O enigma pede a cor que transmite "imensidão, profundidade e tranquilidade... céu aberto, águas dos mares" (A resposta correta é a **2ª Pedra - Azul**).
- Há um fallback (menu no jogo) projetado para o caso do sensor estar desconectado, permitindo a escolha manual da pedra mudando a variável `pedra_escolhida`.

## 6. Estado Atual e Bugs Conhecidos (Contexto para IA)
A partir da análise estrutural do código em `script.rpy`, o projeto apresenta os seguintes pontos de atenção:

1. **Bug Crítico de Variável Ausente (`script.rpy`):**
   - No momento do puzzle, a variável `pedra_escolhida` é verificada (`if pedra_escolhida is None:`) sem ter sido declarada ou inicializada previamente, o que causará um `NameError`.
   - **Solução necessária:** Adicionar a declaração `default pedra_escolhida = None` no topo do arquivo ou no escopo de variáveis globais.

2. **Fluxo do Puzzle Incorreto:**
   - O label `falhou_teste` redireciona para o `start`, fazendo o jogador reviver toda a história inicial se errar a pedra. Deve ser corrigido para voltar apenas ao início do enigma do portão.

3. **Progresso da Integração com Arduino:**
   - O script não possui, no momento, os blocos `init python:` necessários para estabelecer a comunicação serial com o Arduino. A lógica atual está aguardando a implementação dessa ponte (provavelmente usando bibliotecas Python ou polling contínuo via telas e timers no Ren'Py).

## 7. Diretrizes para Desenvolvimento Assistido por IA
- O projeto exige cuidados ao sobrescrever blocos de script para **não perder a lógica da narrativa linear**.
- Na implementação da parte do hardware (Arduino), certificar-se de utilizar métodos thread-safe caso o polling de hardware ocorra fora da main loop do Ren'Py.
- **Imagens:** O script assume sprites nomeados exatamente como nas tags de Character (ex: `torii`, `joku animada`). Esses arquivos devem estar corretos em `/game/images`.
