"""
Nome: Pedro Henrique Ikeda
TIA: 32016344

Nome: Luiz Szajnbok
TIA: 32086083
"""

import pygame as pg

pg.init()
pg.mixer.init()

# Display Settings
WIDTH = 732
HEIGHT = 400
TITLE = "Arduino Cook"
screen = pg.display.set_mode([WIDTH, HEIGHT])

# Game Settings
PROJECTILE_FREQ = 2200
MAX_NUM_PROJECTILE = 13
ITEM_FREQ = 1300
MAX_NUM_ITEM = 8

# Files
SCORE_FILE = "highscore.txt"

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Backgrounds e Icone
BGMENU = pg.image.load("img\\menu\\main_menu\\restaurante.jpg")
BGIMAGE = pg.image.load("img\\game\\map\\mapa_03.png")
BGIMAGE = pg.transform.scale(BGIMAGE, [732, 400])
gameIcon = pg.image.load("img\\menu\\icon.png")
gameIcon = pg.transform.scale(gameIcon, [32, 32])
GOIMAGE = pg.image.load("img\\menu\\game_over\\tela_gameover.png")
HSIMAGE = pg.image.load("img\\menu\\game_over\\score.png")
pg.display.set_icon(gameIcon)


def make_rect(group, path, l, t, w, h,scale=False, nW=0, nH=0):
    temp = pg.sprite.Sprite(group)
    temp.image = pg.image.load(path).convert_alpha()
    temp.rect = pg.Rect(l, t, w, h)
    if scale == True:
        temp.image = pg.transform.scale(temp.image, [nW, nH])

    return temp


# Draw Groups

## Menu
mm_draw_group1 = pg.sprite.Group()
mm_start = pg.sprite.Group()
mm_option = pg.sprite.Group()
mm_inst = pg.sprite.Group()
mm_quit = pg.sprite.Group()
## option
option_draw_group = pg.sprite.Group()
snd_add_hover = pg.sprite.Group()
snd_minus_hover = pg.sprite.Group()
snd_on_button = pg.sprite.Group()
snd_on_hover = pg.sprite.Group()
snd_off_button = pg.sprite.Group()
snd_off_hover = pg.sprite.Group()
## Instruction
inst_draw_group = pg.sprite.Group()
# Close Button
close_draw_group = pg.sprite.Group()
close_hover = pg.sprite.Group()
start_draw_group = pg.sprite.Group()

## Game Over
go_draw_group = pg.sprite.Group()
go_quit = pg.sprite.Group()
go_retry = pg.sprite.Group()

#  * Menu *

# mm_draw_group
start_btn1 = make_rect(mm_draw_group1, "img\\menu\\main_menu\\start1.png", 60, 80, 200, 50)
start_btn2 = make_rect(mm_start, "img\\menu\\main_menu\\start2.png", 60, 80, 200, 50)
start_btn3 = pg.image.load("img\\menu\\main_menu\\start3.png")
option_btn1 = make_rect(mm_draw_group1, "img\\menu\\main_menu\\options1.png", 60, 140, 200, 50)
option_btn2 = make_rect(mm_option, "img\\menu\\main_menu\\options2.png", 60, 140, 200, 50)
option_btn3 = pg.image.load("img\\menu\\main_menu\\options3.png")
inst_btn1 = make_rect(mm_draw_group1, "img\\menu\\main_menu\\instrucao1.png", 60, 200, 200, 50)
inst_btn2 = make_rect(mm_inst, "img\\menu\\main_menu\\instrucao2.png", 60, 200, 200, 50)
inst_btn3 = pg.image.load("img\\menu\\main_menu\\instrucao3.png")
exit_btn1 = make_rect(mm_draw_group1, "img\\menu\\main_menu\\sair1.png", 60, 260, 200, 50)
exit_btn2 = make_rect(mm_quit, "img\\menu\\main_menu\\sair2.png", 60, 260, 200, 50)
exit_btn3 = pg.image.load("img\\menu\\main_menu\\sair3.png")
title = make_rect(mm_draw_group1, "img\\menu\\main_menu\\title.png", 330,20, 360, 140)
jacquin = make_rect(mm_draw_group1, "img\\menu\\main_menu\\jacquin.png", 310, 184, 0, 0, True, 400, 215) # Scale 2.4
# start_draw_group
# start_screen = make_rect(start_draw_group, "img\\menu\\no_game.png", 0, 0, 732, 400)
# inst_draw_group
inst_pag1 = make_rect(inst_draw_group, "img\\menu\\instructions\\inst_pag1.jpg", 0, 0, 732, 400)
# close_draw_group
close_btn1 = make_rect(close_draw_group, "img\\menu\\botao_sair.png", 670, 4, 50, 50)
close_btn2 = make_rect(close_hover, "img\\menu\\botao_sair2.png", 670, 4, 50, 50)
# option_draw_group
option_pag1 = make_rect(option_draw_group, "img\\menu\\options\\options_pag1.jpg", 0, 0, 732, 400)
snd_on = make_rect(snd_on_button, "img\\menu\\options\\botao_som_on_02.png", (WIDTH/2)-25, (HEIGHT/2), 50, 50)
snd_on_h = make_rect(snd_on_hover, "img\\menu\\options\\botao_som_on_03.png", (WIDTH/2)-25, (HEIGHT/2), 50, 50)
snd_on_c = pg.image.load("img\\menu\\options\\botao_som_on.png")
snd_minus = make_rect(option_draw_group, "img\\menu\\options\\botao_som_down_02.png", (WIDTH/2)-125, (HEIGHT/2), 50, 50)
snd_minus_h = make_rect(snd_minus_hover, "img\\menu\\options\\botao_som_down_03.png", (WIDTH/2)-125, (HEIGHT/2), 50, 50)
snd_minus_c = pg.image.load("img\\menu\\options\\botao_som_down.png")
snd_add = make_rect(option_draw_group, "img\\menu\\options\\botao_som_up_02.png", (WIDTH/2)+75, (HEIGHT/2), 50, 50)
snd_add_h = make_rect(snd_add_hover, "img\\menu\\options\\botao_som_up_03.png", (WIDTH/2)+75, (HEIGHT/2), 50, 50)
snd_add_c = pg.image.load("img\\menu\\options\\botao_som_up.png")
snd_mute = make_rect(snd_off_button, "img\\menu\\options\\botao_som_off_02.png", (WIDTH/2)-25, (HEIGHT/2), 50, 50)
snd_mute_h = make_rect(snd_off_hover, "img\\menu\\options\\botao_som_off_03.png", (WIDTH/2)-25, (HEIGHT/2), 50, 50)
snd_mute_c = pg.image.load("img\\menu\\options\\botao_som_off.png")

# * In-Game *
bottle = [pg.image.load("img\\game\\projectiles\\garrafa_01.png"), pg.image.load("img\\game\\projectiles\\garrafa_02.png"), pg.image.load("img\\game\\projectiles\\garrafa_03.png"), pg.image.load("img\\game\\projectiles\\garrafa_04.png")]
spoon = [pg.image.load("img\\game\\projectiles\\spoon_01.png"), pg.image.load("img\\game\\projectiles\\spoon_02.png"), pg.image.load("img\\game\\projectiles\\spoon_03.png"), pg.image.load("img\\game\\projectiles\\spoon_04.png")]
hearts = [pg.image.load("img\\game\\player\\vida_cheia.png"), pg.image.load("img\\game\\player\\vida.png")]

# * Game Over *

retry_btn1 = make_rect(go_draw_group, "img\\menu\\game_over\\restart1.png", 80, 260, 200, 50)
retry_btn2 = make_rect(go_retry, "img\\menu\\game_over\\restart2.png", 80, 260, 200, 50)
retry_btn3 = pg.image.load("img\\menu\\game_over\\restart3.png")
quit_btn1 = make_rect(go_draw_group, "img\\menu\\main_menu\\sair1.png", 480, 260, 200, 50)
quit_btn2 = make_rect(go_quit, "img\\menu\\main_menu\\sair2.png", 480, 260, 200, 50)
quit_btn3 = pg.image.load("img\\menu\\main_menu\\sair3.png")
enemy_idle = pg.image.load("img\\game\\enemy\\oponente_01.png")
enemy_idle_go = pg.transform.scale(enemy_idle, (64, 80))
enemy_left = pg.image.load("img\\game\\enemy\\oponente_03.png")
enemy_left_go = pg.transform.scale(enemy_left, (48, 80))
enemy_right = pg.image.load("img\\game\\enemy\\oponente_04.png")
enemy_right_go = pg.transform.scale(enemy_right, (48, 80))

# * Map *

# table1 = make_rect(map_draw_group, "img\\game\\table1.png", 120, 135, 80, 120, True, 80, 150)
# table2 = make_rect(map_draw_group, "img\\game\\table1.png", 315, 135, 80, 120, True, 80, 150)
# table3 = make_rect(map_draw_group, "img\\game\\table3.png", 512, 135, 80, 120, True, 80, 150)
# wall_right = make_rect(map_draw_group, "img\\game\\inv.png", 702, 0, 30, 400, True, 30, 400)
# wall_top = make_rect(map_draw_group, "img\\game\\inv.png", 702, 0, 30, 83, True, 30, 27)
# wall_left = make_rect(map_draw_group, "img\\game\\inv.png", 702, 0, 30, 83, True, 18, 400)
# wall_down = make_rect(map_draw_group, "img\\game\\inv.png", 0, 372, 30, 83, True, 732, 27)
# walls = [table1, table2, table3]

vol = 0.5
vol_msc = 0.05
# Sound
click_snd = pg.mixer.Sound("snd\\btn_click.ogg")
click_snd.set_volume(vol)
door_snd = pg.mixer.Sound("snd\\door.ogg")
fall_snd = pg.mixer.Sound("snd\\fall.ogg")
ds3_snd = pg.mixer.Sound("snd\\ds3_norm.ogg")
profission_snd = pg.mixer.Sound("snd\\profission.ogg")
profission_snd.set_volume(0.8)
cala_snd = pg.mixer.Sound("snd\\cala.ogg")
cala_snd.set_volume(0.5)

music = pg.mixer.music.load("snd\\music\\02.mp3")
pg.mixer.music.set_volume(vol_msc)

hit_snd = [pg.mixer.Sound("snd\\panela_batendo.ogg"), pg.mixer.Sound("snd\\vidro_quebrando.ogg")]
hit_snd[0].set_volume(vol)
hit_snd[1].set_volume(vol)
item_snd = pg.mixer.Sound("snd\\item.ogg")
item_snd.set_volume(vol)
