# Análise de Integração: Joystick vs Porta Serial (ESP32)

## 1. O jogo atual tenta se comunicar via Porta Serial?
**Não.** Após análise completa dos arquivos fonte do projeto (especialmente o `script.rpy`), **não há nenhuma linha de código atualmente que tente abrir ou ler uma porta Serial (COM)**. 

O comentário `# --- PARTE DO ARDUINO ---` no `script.rpy` indica a intenção de integração, mas a implementação técnica não foi feita. O jogo atual depende exclusivamente de um menu de múltipla escolha (fallback) que é acionado se a variável `pedra_escolhida` for nula (o que atualmente causa um erro no jogo por falta de inicialização prévia da variável).

## 2. A Estratégia do ESP32 como Joystick (HID)
Você mencionou que a ideia é que o ESP32 faça a leitura de cores e **envie comandos de joystick**, e não texto via porta serial.

**Esta é uma excelente decisão de design arquitetural.** 
Se o ESP32 for programado para atuar como um dispositivo HID (Human Interface Device) simulando um controle de videogame (Joystick/Gamepad USB ou Bluetooth), a integração com o Ren'Py torna-se **muito mais simples, nativa e livre de travamentos.**

### Vantagens do Joystick em relação à Porta Serial no Ren'Py:
- **Zero bibliotecas extras:** A leitura de Serial (`pyserial`) exige configurações de Python e multithreading para não "congelar" a interface do Ren'Py. O suporte a Joystick (via SDL2/Pygame) já é 100% nativo no Ren'Py.
- **Estabilidade:** O Ren'Py processa botões de joystick automaticamente na sua fila de eventos.
- **Plug-and-Play:** Não é necessário descobrir em qual porta "COM" o dispositivo está conectado; o sistema operacional o reconhece como um controle padrão.

## 3. O projeto atual ESTÁ funcionando dessa maneira?
**Ainda não.** Para garantir que o jogo responda aos comandos de joystick enviados pelo ESP32 (ex: Botão 1, Botão 2, Botão 3), será necessário implementar um código de escuta no Ren'Py, que atualmente não existe.

## 4. Como implementar a leitura de Joystick no Ren'Py (Guia)
Quando o ESP32 estiver configurado para "apertar um botão do controle" ao detectar uma cor, você deverá mapear esses botões no código do jogo. 

A forma mais recomendada é criar uma **Screen (Tela)** no Ren'Py que aguarde o input do controle na hora do enigma.

**Exemplo Prático de Implementação no `script.rpy`:**

```renpy
# 1. Definimos a tela que vai escutar os botões invisivelmente
screen aguardar_pedra():
    # Supondo que o ESP32 envie os botões do Xbox/PlayStation padrão
    # pad_a (Verde), pad_b (Azul), pad_x (Amarelo)
    
    key "pad_a" action [SetVariable("pedra_escolhida", "VERDE"), Return()]
    key "pad_b" action [SetVariable("pedra_escolhida", "AZUL"), Return()]
    key "pad_x" action [SetVariable("pedra_escolhida", "AMARELO"), Return()]

    # Opcional: Permitir teclado para testes no PC
    key "K_1" action [SetVariable("pedra_escolhida", "VERDE"), Return()]
    key "K_2" action [SetVariable("pedra_escolhida", "AZUL"), Return()]
    key "K_3" action [SetVariable("pedra_escolhida", "AMARELO"), Return()]
```

No fluxo da história, você chamaria essa tela no lugar do menu:

```renpy
    g "Posicionem a pedra correta sobre o sensor para liberar o portão..."

    # Garante que a variável está limpa antes da leitura
    $ pedra_escolhida = None 

    # Chama a tela e congela o jogo até que um botão (ESP32) seja pressionado
    call screen aguardar_pedra
    
    # Após a tela retornar (botão pressionado), checamos o resultado
    if pedra_escolhida == "AZUL":
        jump passou_teste
    else:
        jump falhou_teste
```

### Resumo para a Eletrônica (ESP32):
O código no ESP32 precisa usar bibliotecas como `BleGamepad` (se for Bluetooth) ou as bibliotecas de HID USB nativas (se for via cabo num ESP32-S2 ou S3), mapeando:
- **Cor Verde detectada:** Disparar pressionamento do `BUTTON_1` (`pad_a` no Ren'Py)
- **Cor Azul detectada:** Disparar pressionamento do `BUTTON_2` (`pad_b` no Ren'Py)
- **Cor Amarela detectada:** Disparar pressionamento do `BUTTON_3` (`pad_x` no Ren'Py)
