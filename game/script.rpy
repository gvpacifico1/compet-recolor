# ==============================================================================
# DECLARAÇÃO DE PERSONAGENS E IMAGENS
# ==============================================================================

# Definição dos Personagens com tag de imagem para atualização automática de sprite
define t = Character("Mestre Torii", color="#a39171", image="torii")
define j = Character("Joku", color="#4b86b4", image="joku")
define m = Character("Moli", color="#e8a87c", image="moli")
define z = Character("Zurie", color="#c38d9e", image="zurie")
define a = Character("Aime", color="#85dcba", image="aime")
define g = Character("Gerivaldo", color="#d3a625", image="gerivaldo")


label start:

    # --- INTRODUÇÃO DA LORE DA HISTÓRIA ---
    scene black with fade
    
    "Há muitos séculos atrás, humanos e monstros viviam em tribos separadas, mas em harmonia, dividindo o espaço sobre o mesmo chão."

    "Enquanto os humanos ainda descobriam o fogo, os monstros — sempre mais avançados — descobriram uma forma única de mover a natureza a seu favor através da canalização da alma e da mente. Chamaram isso de Unção."

    "Quando os humanos descobriram isso, dividiram-se. Uns acreditavam ser uma conexão entre o natural e o físico; outros temiam que os monstros usassem essa força para exterminá-los."

    "Os humanos fascinados pela Unção pediram para os monstros ensiná-los. Assim surgiram os primeiros humanos capazes de mover a Unção: os bruxos."

    "Ao saberem da existência dos bruxos, os outros humanos travaram uma guerra sangrenta entre humanos, monstros e bruxos."

    "Séculos se passaram e milhares de companheiros foram perdidos, até restar um único bruxo chamado Gangis."

    "Cansado da destruição, Gangis reuniu os líderes dos humanos e dos monstros para selar um acordo de divisão de terras. O mundo foi dividido, e os bruxos tornaram-se seus mediadores."

    "Para enxergar a Unção, a única forma era ser daltônico — pois os monstros também não enxergavam cores como nós. Gangis reuniu todos os humanos daltônicos e formou a Sociedade dos Bruxos."

    "Séculos depois, no ano de 1999, na quase virada para o ano 2000, surgim rumores de que os monstros invadirão o lado dos humanos e causarão o fim do mundo."

    "Em pânico, a Sociedade dos Bruxos foi acionada. Mali, Zurie, Joku e Aime foram convocadas para partir ao mundo dos monstros e resolver esse impasse como parte do treinamento para se tornarem bruxos de verdade, acompanhadas do mestre Torii."


    # --- CENA 1: SALA DE AULA ---
    scene bg sala_reservada with dissolve

    t "... Vocês quatro irão comigo resolver a pendência da briga das duas raças. Acho que já devem ter ouvido os rumores..."

    t "Além de mim, Joku também vai ficar encarregada de vocês, não é?"

    # Mostra Joku animada à esquerda
    show joku animada at left with dissolve
    j "Sim, senhor! Com todo prazer!!"

    # Mostra Moli à direita
    show moli sorrindo at right with dissolve
    t "Moli, você é uma menina excelente. Você seria uma ótima companheira para seus amigos nessa jornada."

    t "E por favor, trate de educar Zurie a ponto de ela não sair jogando feitiços em cada um..."

    # Subtitui o sprite da Moli pela Zurie emburrada
    show zurie emburrada at right with dissolve
    z "..."

    # Apresenta Aime
    show aime tímida at right with dissolve
    t "E Aime, mesmo que sua entrada seja recente, acho que irá se sair bem com os meninos."

    show aime determinada at right
    a "Claro... Irei dar meu melhor!"


    # --- CENA 2: VILAREJO ---
    scene bg vilarejo with fade

    "Os quatro escoteiros chegam ao vilarejo. O Mestre Torii conversa ao fundo com uma pessoa importante local enquanto buscam suprimentos para a longa caminhada."

    show zurie irritada at left with dissolve
    z "Eerrrgh.. Poderia estar em casa.. Por que Mestre Gangis fez com que nós tivéssemos que resolver todo problema que os monstros causam??"

    show moli seria at right with dissolve
    m "É apenas um rumor, Zurie. Não se sabe se eles vão invadir."

    show aime calada at center with dissolve
    a "..."

    show joku seria at left with dissolve
    j "Bem, se invadirem, iremos impedir. É para isso que nós, bruxos, servimos como propósito."

    show zurie braba at right with hpunch
    z "Eles deveriam resolver os problemas sozinhos, Jok-"

    hide zurie
    hide joku
    hide moli
    hide aime
    with dissolve

    "Torii se aproxima do grupo, cortando qualquer discussão que poderia se desencadear."


    # --- CENA 3: CAMINHADA PELO GRAMADO ---
    scene bg gramado with dissolve

    show zurie cansada at left with dissolve
    z "Os monstros podiam viver mais perto, né? Eu tô morrendo de cansaço!"

    show moli feliz at right with dissolve
    m "Sabia que os monstros veem diferente da gente? Enquanto a gente vê tudo cinza, eles enxergam meio amarelado.. É engraçado, visto que eles são os originários da Unção. Como será ver tudo amarelo..?"

    show joku seria at center with dissolve
    j "Fecha a boca e mexe as pernas! Vocês vão ficar pra trás assim."

    show zurie brava at left with vpunch
    z "OLHA AQUI SUA-"


    # --- CENA 4: CHEGADA AO PORTÃO DOS MONSTROS ---
    scene bg portao_monstros with fade

    "Após um longo tempo de caminhada, elas chegam à terra principal dos monstros e são paradas junto ao grande portão."

    show gerivaldo calmo at right with dissolve
    g "Ora, bruxelas. Não esperava ver vocês aqui tão cedo. Quando foi a última vez? Há.. 100 anos atrás? Meio recente."

    show moli seria at left with dissolve
    m "Novas tendências requerem novas respostas. Só queremos procurar saber e apaziguar a situação.."

    show gerivaldo curioso at right
    g "Que situação? Tenho um ouvido apurado e não escutei nenhuma notícia sobre vocês. Claro, há quem fale sobre vocês.. Mas nada fora do normal."

    show joku decidida at left with dissolve
    j "... Ainda sim, não custa nada ir resolver! Certo, gente? Somos bruxos e nosso trabalho é ajudar as duas raças."

    show gerivaldo serio at right
    g "Mas para do portão passar, um problema vocês devem decifrar. No caso, apenas detalhar. Sabem da prova, não é?"

    show zurie surpresa at left with hpunch
    z "Prova???? Que tipo de prova???"

    show joku decidida at left
    j "Para saber se realmente somos bruxos. Sabe.. por motivos de segurança, pode ter um humano com a gente ou qualquer tipo de ser e nem sabemos!"

    show aime preocupada at left with dissolve
    a "Mas.. parecemos bruxos! Acho que não precisa desse teste.."

    show gerivaldo calmo at right
    g "É necessário, pequena mariposa. Não sabemos com quem estamos lidando. Uma folha para cada um de vocês."

    "Vocês observam atentamente cada folha entregada."


    # Tela preta com efeito de folha
    scene black with fade
    "..."

    scene bg portao_monstros with dissolve

    show gerivaldo desconfiado at right with dissolve
    g "Hm.. Estranho. Um dos bruxinhos vê bem amarelo, não é?"

    show aime nervosa at left with dissolve
    a "Ah, devem ter errado na coloração da imagem…"

    show gerivaldo pensando at right
    g "Tudo bem. Deve mesmo. Certo, agora a última prova. Aqui são três pedras. A Unção de vocês não deve estar tão enferrujada, certo?"

    "Gerivaldo apresenta as três pedras no pedestal."

    g "A cor transmite a sensação de imensidão, profundidade e tranquilidade. É uma tonalidade que lembra o céu aberto, as águas dos mares e a vastidão do universo. A essência se mostrará a vocês, bruxinhos."

    # Descrições das pedras
    "1ª Pedra: Superfície irregular e fria ao toque. Em seu interior, uma essência parece se movimentar lentamente, como se estivesse viva. Sua tonalidade lembra folhas recém-nascidas, musgo úmido e a vegetação depois da chuva."

    "2ª Pedra: Pedra lisa, de aparência cristalina, que parece guardar uma pequena corrente de energia dentro de si. Sua essência possui uma tonalidade que lembra o céu em um dia sem nuvens e a profundidade tranquila do oceano. Ao se aproximar, é possível sentir uma sensação de calma e liberdade. A luz refletida parece fria e serena."

    "3ª Pedra: Pedra quente, mesmo longe de qualquer fonte de calor. Dentro dela, uma essência brilhante pulsa suavemente, lembrando a luz do sol, campos de trigo e flores iluminadas durante o verão. Transmite calor, alegria e vitalidade."


    # --- PARTE DO ARDUINO ---
    g "Posicionem a pedra correta sobre o sensor para liberar o portão..."

    # Menu de teste (caso não use Arduino na hora do teste)
    if pedra_escolhida is None:
        "(Sensor desconectado. Escolha a pedra manualmente):"
        menu:
            "Apresentar a 1ª Pedra (Musgo / Verde)":
                $ pedra_escolhida = "VERDE"
            "Apresentar a 2ª Pedra (Oceano / Azul)":
                $ pedra_escolhida = "AZUL"
            "Apresentar a 3ª Pedra (Sol / Amarelo)":
                $ pedra_escolhida = "AMARELO"

    # Verificação
    if pedra_escolhida == "AZUL":
        jump passou_teste
    else:
        jump falhou_teste

label falhou_teste:
    show gerivaldo serio at right
    g "Essa essência não corresponde ao enigma... Tente novamente."
    jump start

label passou_teste:
    show gerivaldo sorrindo at right with dissolve
    g "Tudo certo, bruxinhos. Podem passar!"
    
    "O grande portão de madeira e ferro das terras dos monstros range lentamente, abrindo passagem para a equipe."

    "CONTINUA..."
    return