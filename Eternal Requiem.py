import pygame
import sys
import botoes
from random import randint
from prompts import mapa


def start(zona):
    global tempo, inventario, messages_index, actual_message, fade_alpha, escolhas, inicio
    fade_alpha = 255
    messages_index = 0
    actual_message = mapa[zona]


def escolha_1(zona):
    global escolheu_1, prompt_zona
    if escolheu_1 is True:
        prompt_zona = zona
    escolheu_1 = False


def escolha_2(zona):
    global escolheu_2, prompt_zona
    if escolheu_2 is True:
        prompt_zona = zona
    escolheu_2 = False


def plano_de_fundo(surface, image_path):
    janela.fill('black')
    background = pygame.image.load(image_path).convert_alpha()
    scaled_background_surface = pygame.transform.scale(background, (1280, 800))
    surface.blit(scaled_background_surface, (0, 0))


def title_and_buttons(surface):
    surface.blit(game_title_shadow_surface, game_title_shadow_rect)
    surface.blit(game_title_surface, game_title_rect)
    surface.blit(botao_start_surf, botao_start_surf.get_rect(center=(640, 650)))
    surface.blit(botao_instrucao_surf, botao_instrucao_surf.get_rect(center=(640, 580)))
    pygame.display.update()


def next_button(surface):
    global messages_index
    if botao_next.draw(surface):
        if messages_index < len(actual_message):
            messages_index += 1
            prompt(surface)


def previous_button(surface):
    global messages_index
    if botao_previous.draw(surface):
        if 0 < messages_index < len(actual_message):
            messages_index -= 1
            prompt(surface)


def prompt_key(key):
    mapa_value = mapa[key]
    return mapa_value


def prompt(n_escolhas=1, txt_escolha_1='', txt_escolha_2='', txt_continuar=''):
    global continuar, texto_1, texto_2, msg_1, msg_2
    pygame.draw.rect(janela, 'black', (175, 500, 900, 200), border_radius=20)
    global messages_index, actual_message
    y_offset = 525
    if messages_index < len(actual_message):
        for linha in actual_message[messages_index]:
            texto = text_font.render(str(linha), True, 'white')
            texto_rect = texto.get_rect(center=(625, y_offset))
            janela.blit(texto, texto_rect)
            y_offset += 35
    elif messages_index >= len(actual_message):
        global escolheu_1, escolheu_2
        if n_escolhas == 1:
            continuar = criar_continuar(txt_continuar)
            return continuar
        elif n_escolhas == 2:
            texto_1 = criar_escolha_1(txt_escolha_1)
            texto_2 = criar_escolha_2(txt_escolha_2)
            return texto_1, texto_2


def prompt_clear(surface):
    janela.fill('black')
    pygame.draw.rect(surface, 'black', (64, 350, 1140, 350), border_radius=20)


def update_screen(image_path):
    janela.fill('black')
    plano_de_fundo(janela, image_path)
    next_button(janela)
    previous_button(janela)


pygame.init()


largura, altura = 1280, 720
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Eternal Requiem")
title_font = pygame.font.Font("fontes/Ghost theory 2.ttf", 115)
subtitle_font = pygame.font.Font("fontes/Ghost theory 2.ttf", 60)
subtitle_font_2 = pygame.font.Font("fontes/Ghost theory 2.ttf", 48)
text_font = pygame.font.Font("fontes/morris-roman.black.ttf", 28)
icon_surface = pygame.image.load("background_2/game_icon.png").convert_alpha()
pygame.display.set_icon(icon_surface)
tempo = pygame.time.Clock()
fps = 60
mouse_pos = pygame.mouse.get_pos()
escolheu_1 = False
escolheu_2 = False
actual_message = mapa['introducao']
messages_index = 0
prompt_zona = ''
msg_1 = ''
msg_2 = ''
escolhas = 0

inventario = []


soundtrack_inicial = "soundtrack/epic_2.0.mp3"


game_title_surface = title_font.render("Eternal Requiem", True, (115, 0, 0))
game_title_shadow_surface = title_font.render("Eternal Requiem", True, 'black')
game_title_rect = game_title_surface.get_rect(center=(640, 150))
game_title_shadow_rect = game_title_shadow_surface.get_rect(center=(635, 153))
game_start_text = subtitle_font.render("Iniciar o Jogo", True, (115, 0, 0))
botao_start_surf = pygame.Surface((340, 60), pygame.SRCALPHA)
botao_start_rect = botao_start_surf.get_rect(center=(640, 650))
botao_start_surf.fill((0, 0, 0))
botao_start_surf.fill((0, 0, 0, 0), botao_start_surf.get_rect())
botao_start_surf.blit(game_start_text, game_start_text.get_rect(center=botao_start_surf.get_rect().center))

game_rules_text = subtitle_font_2.render("Como Jogar", True, (115, 0, 0))
botao_instrucao_surf = pygame.Surface((250, 50), pygame.SRCALPHA)
botao_instrucao_rect = botao_instrucao_surf.get_rect(center=(640, 580))
botao_instrucao_surf.fill((0, 0, 0))
botao_instrucao_surf.fill((0, 0, 0, 0), botao_instrucao_surf.get_rect())
botao_instrucao_surf.blit(game_rules_text, game_rules_text.get_rect(center=botao_instrucao_surf.get_rect().center))


background_surface = pygame.image.load("background_2/game_background.jpg").convert_alpha()
background_surface = pygame.transform.scale(background_surface, (1280, 750))


def dado():
    total = randint(1, 100)
    return total


next_surface = pygame.image.load("botoes/arrow.png").convert_alpha()
next_rect = next_surface.get_rect(center=(1090, 325))
previous_surface = pygame.image.load("botoes/arrow.png").convert_alpha()
previous_surface = pygame.transform.rotate(previous_surface, 180)
previous_rect = previous_surface.get_rect(center=(100, 325))


botao_next = botoes.Button(1045, 690, next_surface, 0.125)
botao_previous = botoes.Button(205, 690, previous_surface, 0.125)
botao_escolha_1 = botoes.TextButton2('Escolha 1', 400, 60, (150, 520), (92, 92, 92),
                                     'black')
botao_escolha_2 = botoes.TextButton2('Escolha 2', 400, 60, (720, 520), (92, 92, 92),
                                     'black')
continuar = botoes.TextButton2(text='Continuar', width=370, height=60, pos=(550, 600), bg_color=(92, 92, 92),
                               text_color='black')
texto_1 = botoes.TextButton2(text='escolha 1', width=370, height=60, pos=(150, 600), bg_color=(92, 92, 92),
                             text_color='black')
texto_2 = botoes.TextButton2(text='escolha 2', width=370, height=60, pos=(750, 600), bg_color=(92, 92, 92),
                             text_color='black')


def criar_escolha_1(button_text):
    botao_texto_1 = botoes.TextButton2(text=button_text, width=370, height=60, pos=(210, 600), bg_color=(0, 0, 0),
                                       text_color='red')
    botao_texto_1.draw(janela)
    return botao_texto_1


def criar_escolha_2(button_text):
    botao_texto_2 = botoes.TextButton2(text=button_text, width=370, height=60, pos=(650, 600), bg_color=(0, 0, 0),
                                       text_color='red')
    botao_texto_2.draw(janela)
    return botao_texto_2


def criar_continuar(button_text):
    botao_continuar = botoes.TextButton2(text=button_text, width=370, height=60, pos=(450, 600), bg_color=(0, 0, 0),
                                         text_color='red')
    botao_continuar.draw(janela)
    return botao_continuar


fade_surface = pygame.Surface((1280, 720)).convert_alpha()
fade_rect = fade_surface.get_rect()
fade_surface.fill('black')
fade_alpha = 255


def fade():
    global fade_alpha

    if fade_alpha > 0:
        fade_alpha -= 12
        fade_surface.set_alpha(fade_alpha)
    janela.blit(fade_surface, fade_rect)


musica_comeco = pygame.mixer.Sound('soundtrack/epic_2.0.mp3')
musica_castelo = pygame.mixer.Sound('soundtrack/castelo_2.1.mp3')
musica_masmorra = pygame.mixer.Sound('soundtrack/dungeon_2.0.mp3')
castelo = False
inicio = True


def main():
    global tempo, musica_comeco, musica_castelo, musica_masmorra, castelo, inicio
    click_sound = pygame.mixer.Sound("soundtrack/text_button.mp3")
    musica_comeco.set_volume(0.2)
    click_sound.set_volume(0.08)
    if inicio:
        # click_sound.set_volume(0.08)
        pygame.mixer.fadeout(3000)
        pygame.mixer.stop()
        # musica_comeco.set_volume(0.2)
        musica_comeco.play(-1)
        inicio = False
    if castelo:
        # click_sound.set_volume(0.08)
        pygame.mixer.fadeout(3000)
        pygame.mixer.stop()
        # musica_comeco.set_volume(0.2)
        musica_comeco.play(-1)
        inicio = True

    while True:
        tempo.tick(fps)
        mouse_position = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_start_rect.collidepoint(mouse_position):
                    click_sound.play()
                    introducao()
                if botao_instrucao_rect.collidepoint(mouse_position):
                    click_sound.play()
                    instrucao()

        plano_de_fundo(janela, "background_2/game_background.jpg")
        title_and_buttons(janela)
        fade()


def instrucao():
    global tempo, inventario, messages_index, actual_message, continuar, texto_1, texto_2, fade_alpha
    start('instrucao')
    messages_index = 0
    run = True
    while run:
        tempo.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_rect.collidepoint(mouse_pos):
                    next_button(janela)
                    previous_button(janela)
                if continuar.draw(janela):
                    main()
                    run = False

        update_screen("background_2/1capela2.jpg")
        prompt(1, txt_continuar='Voltar ao menu inicial')
        if messages_index < len(actual_message):
            next_button(janela)
        if 1 <= messages_index < len(actual_message):
            previous_button(janela)

        fade()
        pygame.display.update()


def introducao():
    # global tempo, inventario, messages_index, actual_message, continuar, texto_1, texto_2, fade_alpha
    # # global mus_inicial, mus_castelo, mus_masmorra
    # messages_index = 0
    start('introducao')
    run = True
    while run:
        tempo.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_rect.collidepoint(mouse_pos):
                    next_button(janela)
                    previous_button(janela)
                if continuar.draw(janela):
                    floresta_inicio()
                    run = False

        update_screen("background_2/forest3.1.jpg")
        prompt(1, txt_continuar='Iniciar a jornada')
        if messages_index < len(actual_message):
            next_button(janela)
        if 1 <= messages_index < len(actual_message):
            previous_button(janela)

        fade()
        pygame.display.update()


def floresta_inicio():
    start('floresta_inicio')
    run = True
    while run:
        tempo.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_rect.collidepoint(mouse_pos):
                    next_button(janela)
                    previous_button(janela)
                if texto_1.draw(janela):
                    floresta_plantas_carmesim()
                    run = False
                if texto_2.draw(janela):
                    floresta_bifurcacao()
                    run = False

        update_screen("background_2/forest_crimsom_flowers_2.jpg")
        prompt(2, txt_escolha_1='Investigar as plantas', txt_escolha_2='Buscar outras pistas')
        if messages_index < len(actual_message):
            next_button(janela)
        if 1 <= messages_index < len(actual_message):
            previous_button(janela)
        fade()

        pygame.display.update()


def floresta_bifurcacao():
    start('floresta_bifurcacao')
    run = True
    while run:
        tempo.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_rect.collidepoint(mouse_pos):
                    next_button(janela)
                    previous_button(janela)
                if texto_1.draw(janela):
                    caminho_fechado()
                if texto_2.draw(janela):
                    barulhos()

        update_screen("background_2/bifurcation.jpg")
        prompt(2, 'Percorrer o caminho de mata densa', 'Percorrer o caminho descendente')
        if messages_index < len(actual_message):
            next_button(janela)
        if 1 <= messages_index < len(actual_message):
            previous_button(janela)
        fade()

        pygame.display.update()


def floresta_plantas_carmesim():
    start('floresta_plantas_carmesim')
    run = True
    while run:
        tempo.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_rect.collidepoint(mouse_pos):
                    next_button(janela)
                    previous_button(janela)
                if texto_1.draw(janela):
                    pegar_ramo_carmesim()
                    run = False
                if texto_2.draw(janela):
                    floresta_bifurcacao()
                    run = False

        update_screen("background_2/forest_crimsom_flowers_4.jpg")
        prompt(2, 'Tentar cortar um ramo da planta', 'Continuar sem arriscar tocá-las')
        if messages_index < len(actual_message):
            next_button(janela)
        if 1 <= messages_index < len(actual_message):
            previous_button(janela)
        fade()

        pygame.display.update()


def pegar_ramo_carmesim():
    start('pegar_ramo_carmesim')
    run = True
    while run:
        tempo.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_rect.collidepoint(mouse_pos):
                    next_button(janela)
                    previous_button(janela)
                if continuar.draw(janela):
                    floresta_bifurcacao()
                    run = False

        update_screen("background_2/crimson_flower.jpg")
        prompt(1, txt_continuar='Buscar outras pistas')
        if messages_index < len(actual_message):
            next_button(janela)
        if 1 <= messages_index < len(actual_message):
            previous_button(janela)
        fade()

        pygame.display.update()


def caminho_fechado():
    start('caminho_fechado')
    run = True
    while run:
        tempo.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_rect.collidepoint(mouse_pos):
                    next_button(janela)
                    previous_button(janela)
                if texto_1.draw(janela):
                    encontro_urso()
                if texto_2.draw(janela):
                    encontro_urso_zumbi()

        update_screen("background_2/caminho_fechado_1.jpg")
        prompt(2, 'Seguir as pegadas no chão', 'Seguir em frente seu caminho')
        if messages_index < len(actual_message):
            next_button(janela)
        if 1 <= messages_index < len(actual_message):
            previous_button(janela)
        fade()

        pygame.display.update()


def encontro_urso():
    start('encontro_urso')
    run = True
    while run:
        tempo.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_rect.collidepoint(mouse_pos):
                    next_button(janela)
                    previous_button(janela)
                if texto_1.draw(janela):
                    caminho_fechado()
                if texto_2.draw(janela):
                    combate_urso()

        update_screen("background_2/urso_preto.jpg")
        prompt(2, 'Refugiar-se na mata densa', 'Enfrentar o urso em combate')
        if messages_index < len(actual_message):
            next_button(janela)
        if 1 <= messages_index < len(actual_message):
            previous_button(janela)
        fade()

        pygame.display.update()


def combate_urso():
    start('combate_urso')
    run = True
    while run:
        tempo.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_rect.collidepoint(mouse_pos):
                    next_button(janela)
                    previous_button(janela)
                if continuar.draw(janela):
                    sorte = dado()
                    if sorte <= 25:
                        derrota_urso()
                    else:
                        vitoria_urso()

        update_screen("background_2/zombie_bear_attack.jpg")
        prompt(1, txt_continuar='Continuar')
        if messages_index < len(actual_message):
            next_button(janela)
        if 1 <= messages_index < len(actual_message):
            previous_button(janela)
        fade()

        pygame.display.update()


def derrota_urso():
    start('derrota_urso')
    run = True
    while run:
        tempo.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_rect.collidepoint(mouse_pos):
                    next_button(janela)
                    previous_button(janela)
                if continuar.draw(janela):
                    main()

        update_screen("background_2/zombie_bear_defeat.jpg")
        prompt(1, txt_continuar='Voltar ao menu inicial')
        if messages_index < len(actual_message):
            next_button(janela)
        if 1 <= messages_index < len(actual_message):
            previous_button(janela)
        fade()

        pygame.display.update()


def vitoria_urso():
    start('vitoria_urso')
    run = True
    while run:
        tempo.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_rect.collidepoint(mouse_pos):
                    next_button(janela)
                    previous_button(janela)
                if continuar.draw(janela):
                    encontrar_toca()

        update_screen("background_2/zombie_bear_victory_2.jpg")
        prompt(1, txt_continuar='Vasculhar com cuidado os arredores')
        if messages_index < len(actual_message):
            next_button(janela)
        if 1 <= messages_index < len(actual_message):
            previous_button(janela)
        fade()

        pygame.display.update()


def encontrar_toca():
    start('encontrar_toca')
    run = True
    while run:
        tempo.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_rect.collidepoint(mouse_pos):
                    next_button(janela)
                    previous_button(janela)
                if texto_1.draw(janela):
                    entrar_na_toca()
                if texto_2.draw(janela):
                    encontro_cassius()

        update_screen("background_2/cave.jpg")
        prompt(2, 'Adentrar mais fundo a toca do urso', 'Retomar o caminho e seguir em frente')
        if messages_index < len(actual_message):
            next_button(janela)
        if 1 <= messages_index < len(actual_message):
            previous_button(janela)
        fade()

        pygame.display.update()


def entrar_na_toca():
    start('entrar_na_toca')
    inventario.append('Crucifixo')
    run = True
    while run:
        tempo.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_rect.collidepoint(mouse_pos):
                    next_button(janela)
                    previous_button(janela)
                if continuar.draw(janela):
                    encontro_cassius()

        update_screen("background_2/crucifix.jpg")
        prompt(1, txt_continuar='Sair da toca e seguir o seu caminho')
        if messages_index < len(actual_message):
            next_button(janela)
        if 1 <= messages_index < len(actual_message):
            previous_button(janela)
        fade()

        pygame.display.update()


def encontro_urso_zumbi():
    start('encontro_urso_zumbi')
    run = True
    while run:
        tempo.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_rect.collidepoint(mouse_pos):
                    next_button(janela)
                    previous_button(janela)
                if texto_1.draw(janela):
                    perseguir_zumbi()
                if texto_2.draw(janela):
                    ignorar_zumbi()

        update_screen("background_2/zombie_bear_1.jpg")
        prompt(2, 'Avançar contra o urso decrépido', 'Tentar passar sem confronto')
        if messages_index < len(actual_message):
            next_button(janela)
        if 1 <= messages_index < len(actual_message):
            previous_button(janela)
        fade()

        pygame.display.update()


def perseguir_zumbi():
    start('perseguir_zumbi')
    run = True
    while run:
        tempo.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_rect.collidepoint(mouse_pos):
                    next_button(janela)
                    previous_button(janela)
                if continuar.draw(janela):
                    encontro_cassius()

        update_screen("background_2/caminho_fechado_3.jpg")
        prompt(1, txt_continuar='Deixar a carcaça e seguir em frente')
        if messages_index < len(actual_message):
            next_button(janela)
        if 1 <= messages_index < len(actual_message):
            previous_button(janela)
        fade()

        pygame.display.update()


def ignorar_zumbi():
    start('ignorar_zumbi')
    run = True
    while run:
        tempo.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_rect.collidepoint(mouse_pos):
                    next_button(janela)
                    previous_button(janela)
                if continuar.draw(janela):
                    encontro_cassius()

        update_screen("background_2/caminho_fechado_2.jpg")
        prompt(1, txt_continuar='Avançar na floresta com cautela')
        if messages_index < len(actual_message):
            next_button(janela)
        if 1 <= messages_index < len(actual_message):
            previous_button(janela)
        fade()

        pygame.display.update()


def encontro_cassius():
    start('encontro_cassius')
    global escolhas, msg_1, msg_2
    run = True
    while run:
        tempo.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_rect.collidepoint(mouse_pos):
                    next_button(janela)
                    previous_button(janela)
                if 'Pingente Dourado' in inventario:
                    global msg_1, msg_2
                    escolhas = 2
                    msg_1 = 'Mostrar pingente de ouro'
                    msg_2 = 'Pedir direção do castelo'
                    if texto_1.draw(janela):
                        mostrar_pingente()
                        run = False
                    if texto_2.draw(janela):
                        deixar_acampamento()
                        run = False
                elif 'Pingente Dourado' not in inventario and 'Crucifixo' in inventario:
                    escolhas = 2
                    msg_1 = 'Mostrar crucifixo'
                    msg_2 = 'Pedir direção do castelo'
                    if texto_1.draw(janela):
                        mostrar_crucifixo()
                        run = False
                    if texto_2.draw(janela):
                        deixar_acampamento()
                        run = False
                else:
                    escolhas = 1
                    if continuar.draw(janela):
                        deixar_acampamento()
        update_screen("background_2/fogueira.jpg")
        prompt(escolhas, txt_escolha_1=msg_1, txt_escolha_2=msg_2, txt_continuar='Pedir direções do castelo')
        if messages_index < len(actual_message):
            next_button(janela)
        if 1 <= messages_index < len(actual_message):
            previous_button(janela)
        fade()

        pygame.display.update()


def mostrar_pingente():
    start('mostrar_pingente')
    run = True
    while run:
        tempo.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_rect.collidepoint(mouse_pos):
                    next_button(janela)
                    previous_button(janela)
                if texto_1.draw(janela):
                    entregar_pingente()
                if texto_2.draw(janela):
                    deixar_acampamento()

        update_screen("background_2/fogueira.jpg")
        prompt(2, 'Entregar o pingente ao vampiro', 'Pedir direção do castelo')
        if messages_index < len(actual_message):
            next_button(janela)
        if 1 <= messages_index < len(actual_message):
            previous_button(janela)
        fade()

        pygame.display.update()


def barulhos():
    start('barulhos')
    run = True
    while run:
        tempo.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_rect.collidepoint(mouse_pos):
                    next_button(janela)
                    previous_button(janela)
                if continuar.draw(janela):
                    corvos()

        update_screen("background_2/forest_dark.jpg")
        prompt(1, txt_continuar='Buscar com cautela a fonte dos gritos')
        if messages_index < len(actual_message):
            next_button(janela)
        if 1 <= messages_index < len(actual_message):
            previous_button(janela)
        fade()

        pygame.display.update()


def corvos():
    start('corvos')
    run = True
    while run:
        tempo.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_rect.collidepoint(mouse_pos):
                    next_button(janela)
                    previous_button(janela)
                if texto_1.draw(janela):
                    pingente_de_ouro()
                if texto_2.draw(janela):
                    vila_amaldicoada()

        update_screen("background_2/corvo.jpg")
        prompt(2, 'Investigar o brilho no buraco da árvore', 'Investigar a fumaça que sobe nas árvores')
        if messages_index < len(actual_message):
            next_button(janela)
        if 1 <= messages_index < len(actual_message):
            previous_button(janela)
        fade()

        pygame.display.update()


def pingente_de_ouro():
    start('pingente_de_ouro')
    if 'Pingente Dourado' not in inventario:
        inventario.append('Pingente Dourado')
    run = True
    while run:
        tempo.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_rect.collidepoint(mouse_pos):
                    next_button(janela)
                    previous_button(janela)
                if continuar.draw(janela):
                    vila_amaldicoada()

        update_screen("background_2/pingente.jpg")
        prompt(1, txt_continuar='Guardar o pingente e dirigir-se à fumaça')
        if messages_index < len(actual_message):
            next_button(janela)
        if 1 <= messages_index < len(actual_message):
            previous_button(janela)
        fade()

        pygame.display.update()


def vila_amaldicoada():
    start('vila_amaldicoada')
    run = True
    while run:
        tempo.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_rect.collidepoint(mouse_pos):
                    next_button(janela)
                    previous_button(janela)
                if texto_1.draw(janela):
                    floresta_bifurcacao()
                if texto_2.draw(janela):
                    explorar_vila()

        update_screen("background_2/vila_1.jpg")
        prompt(2, 'Voltar à bifurcação na floresta', 'Esgueirar-se silenciosamente na vila')
        if messages_index < len(actual_message):
            next_button(janela)
        if 1 <= messages_index < len(actual_message):
            previous_button(janela)
        fade()

        pygame.display.update()


def explorar_vila():
    start('explorar_vila')
    run = True
    while run:
        tempo.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_rect.collidepoint(mouse_pos):
                    next_button(janela)
                    previous_button(janela)
                if texto_1.draw(janela):
                    seguir_grito()
                if texto_2.draw(janela):
                    sair_da_vila()

        update_screen("background_2/vila_2.jpg")
        prompt(2, 'Investigar a origem do som', 'Tentar atravessar a vila despercebido')
        if messages_index < len(actual_message):
            next_button(janela)
        if 1 <= messages_index < len(actual_message):
            previous_button(janela)
        fade()

        pygame.display.update()


def seguir_grito():
    start('seguir_grito')
    run = True
    while run:
        tempo.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_rect.collidepoint(mouse_pos):
                    next_button(janela)
                    previous_button(janela)
                if texto_1.draw(janela):
                    sorte = dado()
                    if sorte <= 25:
                        entrar_na_casa()
                    else:
                        execucao_homem()
                if texto_2.draw(janela):
                    sair_da_vila()

        update_screen("background_2/vila_3.jpg")
        prompt(2, 'Entrar na casa para ajudá-lo', 'Aproveitar o barulho para fugir da vila')
        if messages_index < len(actual_message):
            next_button(janela)
        if 1 <= messages_index < len(actual_message):
            previous_button(janela)
        fade()

        pygame.display.update()


def execucao_homem():
    start('execucao_homem')
    run = True
    while run:
        tempo.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_rect.collidepoint(mouse_pos):
                    next_button(janela)
                    previous_button(janela)
                if continuar.draw(janela):
                    sair_da_vila()

        update_screen("background_2/casa_1.jpg")
        prompt(1, txt_continuar='Fugir da vila o mais rápido possível')
        if messages_index < len(actual_message):
            next_button(janela)
        if 1 <= messages_index < len(actual_message):
            previous_button(janela)

        pygame.display.update()
        fade()


def entrar_na_casa():
    start('entrar_na_casa')
    run = True
    while run:
        tempo.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_rect.collidepoint(mouse_pos):
                    next_button(janela)
                    previous_button(janela)
                if continuar.draw(janela):
                    main()

        update_screen("background_2/servo_wide_3.jpg")
        prompt(1, txt_continuar='Recomeçar a jornada')
        if messages_index < len(actual_message):
            next_button(janela)
        if 1 <= messages_index < len(actual_message):
            previous_button(janela)
        fade()

        pygame.display.update()


def sair_da_vila():
    start('sair_da_vila')
    run = True
    while run:
        tempo.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_rect.collidepoint(mouse_pos):
                    next_button(janela)
                    previous_button(janela)
                if continuar.draw(janela):
                    encontro_cassius()

        update_screen("background_2/vila_4.jpg")
        prompt(1, txt_continuar='Continuar em frente no caminho')
        if messages_index < len(actual_message):
            next_button(janela)
        if 1 <= messages_index < len(actual_message):
            previous_button(janela)
        fade()

        pygame.display.update()


def entregar_pingente():
    start('entregar_pingente')
    inventario.append('Adaga')
    run = True
    while run:
        tempo.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_rect.collidepoint(mouse_pos):
                    next_button(janela)
                    previous_button(janela)
                if continuar.draw(janela):
                    deixar_acampamento()

        update_screen("background_2/adaga.jpg")
        prompt(1, txt_continuar=' Guardar adaga e pedir direção do castelo')
        if messages_index < len(actual_message):
            next_button(janela)
        if 1 <= messages_index < len(actual_message):
            previous_button(janela)
        fade()

        pygame.display.update()


def mostrar_crucifixo():
    start('mostrar_crucifixo')
    run = True
    while run:
        tempo.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_rect.collidepoint(mouse_pos):
                    next_button(janela)
                    previous_button(janela)
                if continuar.draw(janela):
                    deixar_acampamento()

        update_screen("background_2/fogueira.jpg")
        prompt(1, txt_continuar='Guardar crucifixo e pedir direção do castelo')
        if messages_index < len(actual_message):
            next_button(janela)
        if 1 <= messages_index < len(actual_message):
            previous_button(janela)
        fade()

        pygame.display.update()


def deixar_acampamento():
    start('deixar_acampamento')
    run = True
    while run:
        tempo.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_rect.collidepoint(mouse_pos):
                    next_button(janela)
                    previous_button(janela)
                sorte = dado()
                if 'Adaga' in inventario:
                    if texto_1.draw(janela):
                        if sorte >= 20:
                            vitoria_servo_adaga()
                        else:
                            derrota_servo()
                elif 'Crucifixo' in inventario:
                    if texto_1.draw(janela):
                        if sorte >= 20:
                            vitoria_servo_crucifixo()
                        else:
                            derrota_servo()
                elif 'Adaga' not in inventario and 'Crucifixo' not in inventario:
                    if texto_1.draw(janela):
                        if sorte >= 30:
                            vitoria_servo_espada()
                        else:
                            derrota_servo()
                if texto_2.draw(janela):
                    esconder_servo()

        update_screen("background_2/game_background.jpg")
        prompt(2, 'Enfrentar o servo de Bertrand', 'Esconder-se', txt_continuar='')
        if messages_index < len(actual_message):
            next_button(janela)
        if 1 <= messages_index < len(actual_message):
            previous_button(janela)
        fade()

        pygame.display.update()


def derrota_servo():
    start('derrota_servo')
    run = True
    while run:
        tempo.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_rect.collidepoint(mouse_pos):
                    next_button(janela)
                    previous_button(janela)
                if continuar.draw(janela):
                    main()

        update_screen("background_2/servo_wide_1.jpg")
        prompt(1, txt_continuar='Recomeçar a jornada')
        if messages_index < len(actual_message):
            next_button(janela)
        if 1 <= messages_index < len(actual_message):
            previous_button(janela)
        fade()

        pygame.display.update()


def vitoria_servo_adaga():
    start('vitoria_servo_adaga')
    inventario.append('Chaves')
    run = True
    while run:
        tempo.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_rect.collidepoint(mouse_pos):
                    next_button(janela)
                    previous_button(janela)
                if continuar.draw(janela):
                    masmorras()

        update_screen("background_2/servo_wide_1.jpg")
        prompt(1, txt_continuar='Avançar na escuridão do castelo')
        if messages_index < len(actual_message):
            next_button(janela)
        if 1 <= messages_index < len(actual_message):
            previous_button(janela)
        fade()

        pygame.display.update()


def vitoria_servo_crucifixo():
    start('vitoria_servo_crucifixo')
    inventario.append('Chaves')
    run = True
    while run:
        tempo.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_rect.collidepoint(mouse_pos):
                    next_button(janela)
                    previous_button(janela)
                if continuar.draw(janela):
                    masmorras()

        update_screen("background_2/servo_wide_1.jpg")
        prompt(1, txt_continuar='Avançar na escuridão do castelo')
        if messages_index < len(actual_message):
            next_button(janela)
        if 1 <= messages_index < len(actual_message):
            previous_button(janela)
        fade()

        pygame.display.update()


def vitoria_servo_espada():
    start('vitoria_servo_espada')
    inventario.append('Chaves')
    run = True
    while run:
        tempo.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_rect.collidepoint(mouse_pos):
                    next_button(janela)
                    previous_button(janela)
                if continuar.draw(janela):
                    masmorras()

        update_screen("background_2/servo_wide_1.jpg")
        prompt(1, txt_continuar='Avançar na escuridão do castelo')
        if messages_index < len(actual_message):
            next_button(janela)
        if 1 <= messages_index < len(actual_message):
            previous_button(janela)
        fade()

        pygame.display.update()


def esconder_servo():
    start('esconder_servo')
    run = True
    while run:
        tempo.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_rect.collidepoint(mouse_pos):
                    next_button(janela)
                    previous_button(janela)
                if continuar.draw(janela):
                    masmorras()

        update_screen("background_2/servo_wide_1.jpg")
        prompt(1, txt_continuar='Avançar na escuridão do castelo')
        if messages_index < len(actual_message):
            next_button(janela)
        if 1 <= messages_index < len(actual_message):
            previous_button(janela)
        fade()

        pygame.display.update()


def masmorras():
    start('masmorras')
    global escolhas, castelo
    castelo = True
    pygame.mixer.fadeout(3000)
    pygame.mixer.stop()
    musica_castelo.set_volume(0.2)
    musica_castelo.play(-1)
    run = True
    while run:
        tempo.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_rect.collidepoint(mouse_pos):
                    next_button(janela)
                    previous_button(janela)
                if 'Chaves' in inventario:
                    escolhas = 2
                    if texto_1.draw(janela):
                        libertar_humanos()
                    if texto_2.draw(janela):
                        nao_libertar()
                else:
                    escolhas = 1
                    if continuar.draw(janela):
                        nao_libertar()

        update_screen("background_2/masmorra.jpg")
        prompt(escolhas, 'Libertar humanos', 'Deixar o local', txt_continuar='Deixar o local')
        if messages_index < len(actual_message):
            next_button(janela)
        if 1 <= messages_index < len(actual_message):
            previous_button(janela)
        fade()

        pygame.display.update()


def nao_libertar():
    start('nao_libertar')
    run = True
    while run:
        tempo.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_rect.collidepoint(mouse_pos):
                    next_button(janela)
                    previous_button(janela)
                if continuar.draw(janela):
                    hall_entrada()

        update_screen("background_2/masmorra.jpg")
        prompt(1, txt_continuar='Continuar para a próxima sala')
        if messages_index < len(actual_message):
            next_button(janela)
        if 1 <= messages_index < len(actual_message):
            previous_button(janela)
        fade()

        pygame.display.update()


def libertar_humanos():
    start('libertar_humanos')
    run = True
    while run:
        tempo.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_rect.collidepoint(mouse_pos):
                    next_button(janela)
                    previous_button(janela)
                if texto_1.draw(janela):
                    libertar_vampiros()
                if texto_2.draw(janela):
                    nao_libertar()

        update_screen("background_2/masmorra.jpg")
        prompt(2, 'Libertar vampiros', 'Deixar o local')
        if messages_index < len(actual_message):
            next_button(janela)
        if 1 <= messages_index < len(actual_message):
            previous_button(janela)
        fade()

        pygame.display.update()


def libertar_vampiros():
    start('libertar_vampiros')
    run = True
    while run:
        tempo.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_rect.collidepoint(mouse_pos):
                    next_button(janela)
                    previous_button(janela)
                if continuar.draw(janela):
                    hall_entrada()

        update_screen("background_2/masmorra.jpg")
        prompt(1, '', '', txt_continuar='Adentrar mais o castelo')
        if messages_index < len(actual_message):
            next_button(janela)
        if 1 <= messages_index < len(actual_message):
            previous_button(janela)
        fade()

        pygame.display.update()


def hall_entrada():
    start('hall_entrada')
    run = True
    while run:
        tempo.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_rect.collidepoint(mouse_pos):
                    next_button(janela)
                    previous_button(janela)
                if texto_1.draw(janela):
                    sala_artes()
                if texto_2.draw(janela):
                    salao_festas()

        update_screen("background_2/1hall.jpg")
        prompt(2, 'Virar à esquerda', 'Virar à direita', txt_continuar='')
        if messages_index < len(actual_message):
            next_button(janela)
        if 1 <= messages_index < len(actual_message):
            previous_button(janela)
        fade()

        pygame.display.update()


def salao_festas():
    start('salao_festas')
    run = True
    while run:
        tempo.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_rect.collidepoint(mouse_pos):
                    next_button(janela)
                    previous_button(janela)
                if texto_1.draw(janela):
                    cozinha()
                if texto_2.draw(janela):
                    sala_trono()

        update_screen("background_2/jantar.jpg")
        prompt(2, 'Seguir o cheiro de comida', 'Ir à porta grandiosa', txt_continuar='')
        if messages_index < len(actual_message):
            next_button(janela)
        if 1 <= messages_index < len(actual_message):
            previous_button(janela)
        fade()

        pygame.display.update()


def cozinha():
    start('cozinha')
    run = True
    while run:
        tempo.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_rect.collidepoint(mouse_pos):
                    next_button(janela)
                    previous_button(janela)
                if texto_1.draw(janela):
                    provar_comidas()
                if texto_2.draw(janela):
                    aposentos_criados()

        update_screen("background_2/1cozinha.jpg")
        prompt(2, 'Provar comidas e bebidas', 'Procurar outras passagens', txt_continuar='')
        if messages_index < len(actual_message):
            next_button(janela)
        if 1 <= messages_index < len(actual_message):
            previous_button(janela)
        fade()

        pygame.display.update()


def provar_comidas():
    start('provar_comidas')
    run = True
    while run:
        tempo.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_rect.collidepoint(mouse_pos):
                    next_button(janela)
                    previous_button(janela)
                if continuar.draw(janela):
                    aposentos_criados()

        update_screen("background_2/comida.jpg")
        prompt(1, '', '', txt_continuar='Deixar a comida de lado e continuar')
        if messages_index < len(actual_message):
            next_button(janela)
        if 1 <= messages_index < len(actual_message):
            previous_button(janela)
        fade()

        pygame.display.update()


def aposentos_criados():
    start('aposentos_criados')
    inventario.append('Espelho')
    run = True
    while run:
        tempo.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_rect.collidepoint(mouse_pos):
                    next_button(janela)
                    previous_button(janela)
                if texto_1.draw(janela):
                    sorte = dado()
                    if sorte >= 25:
                        espelho_vitoria()
                    else:
                        espelho_derrota()
                if texto_2.draw(janela):
                    voltar_hall()

        update_screen("background_2/1criados.jpg")
        prompt(2, 'Remover o pano negro', 'Voltar para o hall de entrada', txt_continuar='')
        if messages_index < len(actual_message):
            next_button(janela)
        if 1 <= messages_index < len(actual_message):
            previous_button(janela)
        fade()

        pygame.display.update()


def voltar_hall():
    start('voltar_hall')
    global msg_1
    run = True
    while run:
        tempo.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_rect.collidepoint(mouse_pos):
                    next_button(janela)
                    previous_button(janela)

                if continuar.draw(janela):
                    if 'Espelho' not in inventario:
                        salao_festas()
                    elif 'Lança' not in inventario:
                        sala_artes()
                    elif 'Lança' in inventario and 'Espelho' not in inventario:
                        salao_festas()
                    elif 'Caixão' not in inventario:
                        pygame.mixer.fadeout(3000)
                        pygame.mixer.stop()
                        musica_masmorra.set_volume(0.2)
                        musica_masmorra.play(-1)
                        sala_trono()
                    else:
                        aposentos_reais_2()
        update_screen("background_2/1hall2.jpg")
        prompt(1, '', '', txt_continuar='Seguir o outro caminho inexplorado')
        if messages_index < len(actual_message):
            next_button(janela)
        if 1 <= messages_index < len(actual_message):
            previous_button(janela)
        fade()

        pygame.display.update()


def espelho_vitoria():
    start('espelho_vitoria')
    run = True
    while run:
        tempo.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_rect.collidepoint(mouse_pos):
                    next_button(janela)
                    previous_button(janela)
                if continuar.draw(janela):
                    voltar_hall()

        update_screen("background_2/espelho.jpg")
        prompt(1, '', '', txt_continuar='Voltar ao hall de entrada')
        if messages_index < len(actual_message):
            next_button(janela)
        if 1 <= messages_index < len(actual_message):
            previous_button(janela)
        fade()

        pygame.display.update()


def espelho_derrota():
    start('espelho_derrota')
    run = True
    while run:
        tempo.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_rect.collidepoint(mouse_pos):
                    next_button(janela)
                    previous_button(janela)
                if continuar.draw(janela):
                    main()

        update_screen("background_2/espelho.jpg")
        prompt(1, '', '', txt_continuar='Recomeçar a jornada')
        if messages_index < len(actual_message):
            next_button(janela)
        if 1 <= messages_index < len(actual_message):
            previous_button(janela)
        fade()

        pygame.display.update()


def sala_trono():
    start('sala_trono')
    run = True
    pygame.mixer.fadeout(3000)
    pygame.mixer.stop()
    musica_masmorra.set_volume(0.2)
    musica_masmorra.play(-1)
    while run:
        tempo.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_rect.collidepoint(mouse_pos):
                    next_button(janela)
                    previous_button(janela)
                if texto_1.draw(janela):
                    afrescos_vitrais()
                if texto_2.draw(janela):
                    aposentos_reais()

        update_screen("background_2/trono.jpg")
        prompt(2, 'Examinar afrescos e vitrais', 'Examinar porta ornamentada', txt_continuar='')
        if messages_index < len(actual_message):
            next_button(janela)
        if 1 <= messages_index < len(actual_message):
            previous_button(janela)
        fade()

        pygame.display.update()


def afrescos_vitrais():
    start('afrescos_vitrais')
    run = True
    while run:
        tempo.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_rect.collidepoint(mouse_pos):
                    next_button(janela)
                    previous_button(janela)
                if continuar.draw(janela):
                    aposentos_reais()

        update_screen("background_2/vitrais.jpg")
        prompt(1, '', '', txt_continuar='Examinar porta ornamentada')
        if messages_index < len(actual_message):
            next_button(janela)
        if 1 <= messages_index < len(actual_message):
            previous_button(janela)
        fade()

        pygame.display.update()


def aposentos_reais():
    start('aposentos_reais')
    inventario.append('Caixão')
    run = True
    while run:
        tempo.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_rect.collidepoint(mouse_pos):
                    next_button(janela)
                    previous_button(janela)
                sorte = dado()
                if texto_1.draw(janela):
                    if sorte >= 25:
                        armadilha_caixao_vitoria()
                    else:
                        armadilha_caixao_derrota()
                if texto_2.draw(janela):
                    observatorio()

        update_screen("background_2/2caixao.jpg")
        prompt(2, 'Examinar o caixão negro', 'Sair da sala e subir escadas', txt_continuar='')
        if messages_index < len(actual_message):
            next_button(janela)
        if 1 <= messages_index < len(actual_message):
            previous_button(janela)
        fade()

        pygame.display.update()


def aposentos_reais_2():
    start('aposentos_reais_2')
    run = True
    while run:
        tempo.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_rect.collidepoint(mouse_pos):
                    next_button(janela)
                    previous_button(janela)
                if continuar.draw(janela):
                    observatorio()

        update_screen("background_2/2caixao.jpg")
        prompt(1, '', '', txt_continuar='Subir as escadas de pedra')
        if messages_index < len(actual_message):
            next_button(janela)
        if 1 <= messages_index < len(actual_message):
            previous_button(janela)
        fade()

        pygame.display.update()


def armadilha_caixao_vitoria():
    start('armadilha_caixao_vitoria')
    run = True
    while run:
        tempo.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_rect.collidepoint(mouse_pos):
                    next_button(janela)
                    previous_button(janela)
                if texto_1.draw(janela):
                    voltar_hall()
                if texto_2.draw(janela):
                    observatorio()

        update_screen("background_2/smoke.jpg")
        prompt(2, 'Voltar ao hall rapidamente', 'Subir as escadas rapidamente', txt_continuar='')
        if messages_index < len(actual_message):
            next_button(janela)
        if 1 <= messages_index < len(actual_message):
            previous_button(janela)
        fade()

        pygame.display.update()


def armadilha_caixao_derrota():
    start('armadilha_caixao_derrota')
    run = True
    while run:
        tempo.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_rect.collidepoint(mouse_pos):
                    next_button(janela)
                    previous_button(janela)
                if continuar.draw(janela):
                    main()

        update_screen("background_2/smoke.jpg")
        prompt(1, '', '', txt_continuar='Recomeçar a jornada')
        if messages_index < len(actual_message):
            next_button(janela)
        if 1 <= messages_index < len(actual_message):
            previous_button(janela)
        fade()

        pygame.display.update()


def sala_artes():
    start('sala_artes')
    run = True
    while run:
        tempo.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_rect.collidepoint(mouse_pos):
                    next_button(janela)
                    previous_button(janela)
                if texto_1.draw(janela):
                    sala_trono()
                if texto_2.draw(janela):
                    biblioteca()

        update_screen("background_2/artes.jpg")
        prompt(2, 'Seguir para a luz vermelha', 'Investigar porta menor', txt_continuar='')
        if messages_index < len(actual_message):
            next_button(janela)
        if 1 <= messages_index < len(actual_message):
            previous_button(janela)
        fade()

        pygame.display.update()


def biblioteca():
    start('biblioteca')
    run = True
    while run:
        tempo.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_rect.collidepoint(mouse_pos):
                    next_button(janela)
                    previous_button(janela)
                if texto_1.draw(janela):
                    livro()
                if texto_2.draw(janela):
                    capela()

        update_screen("background_2/1biblioteca.jpg")
        prompt(2, 'Examinar o livro', 'Adentrar o corredor estreito', txt_continuar='')
        if messages_index < len(actual_message):
            next_button(janela)
        if 1 <= messages_index < len(actual_message):
            previous_button(janela)
        fade()

        pygame.display.update()


def livro():
    start('livro')
    run = True
    while run:
        tempo.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_rect.collidepoint(mouse_pos):
                    next_button(janela)
                    previous_button(janela)
                if continuar.draw(janela):
                    capela()

        update_screen("background_2/tome.jpg")
        prompt(1, '', '', txt_continuar='Seguir para o corredor estreito')
        if messages_index < len(actual_message):
            next_button(janela)
        if 1 <= messages_index < len(actual_message):
            previous_button(janela)
        fade()

        pygame.display.update()


def capela():
    start('capela')
    inventario.append('Lança')
    run = True
    while run:
        tempo.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_rect.collidepoint(mouse_pos):
                    next_button(janela)
                    previous_button(janela)
                if continuar.draw(janela):
                    lisander()

        update_screen("background_2/1capela.jpg")
        prompt(1, '', '', txt_continuar='Permanecer em contemplação')
        if messages_index < len(actual_message):
            next_button(janela)
        if 1 <= messages_index < len(actual_message):
            previous_button(janela)
        fade()

        pygame.display.update()


def lisander():
    start('lisander')
    run = True
    while run:
        tempo.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_rect.collidepoint(mouse_pos):
                    next_button(janela)
                    previous_button(janela)
                if continuar.draw(janela):
                    voltar_hall()

        update_screen("background_2/spear.jpg")
        prompt(1, '', '', txt_continuar='Voltar para o hall de entrada')
        if messages_index < len(actual_message):
            next_button(janela)
        if 1 <= messages_index < len(actual_message):
            previous_button(janela)
        fade()

        pygame.display.update()


def observatorio():
    start('observatorio')
    global escolhas
    run = True
    while run:
        tempo.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_rect.collidepoint(mouse_pos):
                    next_button(janela)
                    previous_button(janela)

                escolhas = 1
                if 'Lança' not in inventario:
                    escolhas = 2
                    if texto_1.draw(janela):
                        voltar_hall()
                    if texto_2.draw(janela):
                        conde_derrota_sem_lanca()
                else:
                    if continuar.draw(janela):
                        sorte = dado()
                        if sorte >= 30:
                            conde_vitoria()
                        else:
                            conde_derrota_lanca()

        update_screen("background_2/coffin_2.jpg")
        prompt(escolhas, 'Explorar outras zonas', 'Remover a tampa do caixão',
               txt_continuar='Com a lança em mãos, abrir o caixão')
        if messages_index < len(actual_message):
            next_button(janela)
        if 1 <= messages_index < len(actual_message):
            previous_button(janela)
        fade()

        pygame.display.update()


def conde_derrota_sem_lanca():
    start('conde_derrota_sem_lanca')
    run = True
    while run:
        tempo.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_rect.collidepoint(mouse_pos):
                    next_button(janela)
                    previous_button(janela)
                if continuar.draw(janela):
                    main()

        update_screen("background_2/bertrand.jpg")
        prompt(1, '', '', txt_continuar='Recomeçar a jornada')
        if messages_index < len(actual_message):
            next_button(janela)
        if 1 <= messages_index < len(actual_message):
            previous_button(janela)
        fade()

        pygame.display.update()


def conde_derrota_lanca():
    start('conde_derrota_lanca')
    run = True
    while run:
        tempo.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_rect.collidepoint(mouse_pos):
                    next_button(janela)
                    previous_button(janela)
                if continuar.draw(janela):
                    main()

        update_screen("background_2/bertrand.jpg")
        prompt(1, '', '', txt_continuar='Recomeçar a jornada')
        if messages_index < len(actual_message):
            next_button(janela)
        if 1 <= messages_index < len(actual_message):
            previous_button(janela)
        fade()

        pygame.display.update()


def conde_vitoria():
    start('conde_vitoria')
    run = True
    while run:
        tempo.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_rect.collidepoint(mouse_pos):
                    next_button(janela)
                    previous_button(janela)
                if continuar.draw(janela):
                    fim()

        update_screen("background_2/bertrand.jpg")
        prompt(1, '', '', txt_continuar='Continuar')
        if messages_index < len(actual_message):
            next_button(janela)
        if 1 <= messages_index < len(actual_message):
            previous_button(janela)
        fade()

        pygame.display.update()


def fim():
    start('fim')
    global inicio
    pygame.mixer.fadeout(3000)
    pygame.mixer.stop()
    musica_comeco.set_volume(0.2)
    musica_comeco.play(-1)
    inicio = True

    run = True
    while run:
        tempo.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_rect.collidepoint(mouse_pos):
                    next_button(janela)
                    previous_button(janela)
                if continuar.draw(janela):
                    main()

        update_screen("background_2/1capela2.jpg")
        prompt(1, '', '', txt_continuar='Menu inicial')
        if messages_index < len(actual_message):
            next_button(janela)
        if 1 <= messages_index < len(actual_message):
            previous_button(janela)
        fade()

        pygame.display.update()


# def teste():
#     start('seguir_grito')
#     run = True
#     while run:
#         tempo.tick(fps)
#
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if next_rect.collidepoint(mouse_pos):
#                     next_button(janela)
#                     previous_button(janela)
#                 if texto_1.draw(janela):
#                     pass
#                 if texto_2.draw(janela):
#                     pass
#
#         update_screen("backgrounds/floresta_noite_background.jpg")
#         prompt(2, '', '', txt_continuar='')
#         if messages_index < len(actual_message):
#             next_button(janela)
#         if 1 <= messages_index < len(actual_message):
#             previous_button(janela)
#         fade()
#
#         pygame.display.update()


'''Para garantir que a função main() só será executada caso esse arquivo game.py seja rodado como o arquivo principal, 
definimos if __name__ == "__main__", pois, caso não estivesse assim, a função main() acima seria executada mesmo sem 
rodarmos o arquivo game.py (por exemplo, se outro arquivo importasse o arquivo game.py, a função seria rodada mesmo sem 
que desejemos isso). Isso se dá porque, quando executo o arquivo game.py, neste momento o pycharm nomeia o arquivo como 
sendo "__main__", para fins de determinar qual foi o arquivo inicial que rodou todos os outros importados (que foram 
executados, mas não são o __main__'''
if __name__ == "__main__":
    main()
