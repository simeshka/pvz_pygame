import math
import random

import pygame

import enemy
import entity
import plant

pygame.init() # Инициализация pygame
clock = pygame.time.Clock()
screen_x = 1250
screen_y = 875
mode="1"
screen=pygame.display.set_mode((screen_x, screen_y))
screen_color=(117,0,0)

starY = 0
starX = random.randint(200, 900)

att3 = 0

zembies = []

time3cyc = [36000, 7000, 13000, 7000, 11000, 1000, 1000, 300, 500, 4000, 1000, 8000, 1000, 500, 1000, 2000]
time3cur = 0

zom3ord = [1, 1, 2, 3, 1, 4, 2, 1, 1, 2, 3, 2, 1, 2, 1, 2, 1, 2, 3, 1]
zom3cor = -1

button_play_rect = pygame.Rect(screen_x/20,screen_y/7,screen_x/5,screen_y/7)
button_sound_rect = pygame.Rect(screen_x/100,screen_y/(35/32),screen_x/20,screen_y/14)
button_exit_rect = pygame.Rect(screen_x/(50/47),screen_y/70,screen_x/20,screen_y/14)
button_level_one = pygame.Rect(screen_x/(6+6/9),screen_y/(2+1/3),screen_x/5,screen_y/7)
button_level_two = pygame.Rect(screen_x/(31/12),screen_y/(7/3),screen_x/5,screen_y/7)
button_level_three = pygame.Rect(screen_x/(1+48/77),screen_y/(2+1/3),screen_x/5,screen_y/7)
button_sunflower = pygame.Rect(screen_x/50, screen_y/35, screen_x/9, screen_y/12)
button_peashooter = pygame.Rect(screen_x/50, screen_y/7, screen_x/9, screen_y/12)
button_wallnut = pygame.Rect(screen_x/50, screen_y/(3+3/4), screen_x/9, screen_y/12)
button_delete = pygame.Rect(screen_x/(7+1/3), screen_y/35, screen_x/9, screen_y/12)
grids = []
lawns = []
Rect = pygame.Rect
xoffset = 0
yoffset = screen_y/(875/100)
for i in range(9):
    for z in range(6):
        grids.append(pygame.Rect((screen_x/(100/83))-xoffset, screen_y/(700/yoffset), screen_x/(11+1/9),screen_y/(8+3/4)))
        yoffset += screen_y/(875/80)
    yoffset = screen_y/(875/100)
    xoffset += screen_x/(1000/80)
for aa in range(6):
    lawns.append(Rect(screen_x/(100/15), screen_y/(700/yoffset), screen_x/(100/4), screen_y/(8+3/4)))
    yoffset += 80

track_main = pygame.mixer.Sound("sounds/02. Crazy Dave (Intro Theme).mp3")
sfx_lawnmower = pygame.mixer.Sound("sounds/SFX lawnmower.mp3")

pvz_main_img = pygame.image.load("images/pvz_main.jpg") # ШАГ 1: Загружаем изображение
pvz_peashooter = pygame.image.load("images/Peashooter.png")
pvz_sunflower = pygame.image.load("images/Sunflower.png")
pvz_wallnut = pygame.image.load("images/Wall-nut.png")
pvz_sun = pygame.image.load("images/Sun_PvZ2.png")
pvz_soundbut = pygame.image.load("images/images.png")
pvz_house = pygame.image.load("images/house.png")
pvz_shovel = pygame.image.load("images/Shovel.png")
pvz_lawnmower = pygame.image.load("images/grassremover.png")
pvz_pea = pygame.image.load("images/pea.png")
pvz_zombie = pygame.image.load("images/Zombie/Zombie_0.png")
pvz_zombie1 = pygame.image.load("images/Zombie/Zombie_1.png")
pvz_zombie2 = pygame.image.load("images/Zombie/Zombie_2.png")
pvz_zombie3 = pygame.image.load("images/Zombie/Zombie_2.png")
pvz_zombie4 = pygame.image.load("images/Zombie/Zombie_4.png")
pvz_zombie5 = pygame.image.load("images/Zombie/Zombie_5.png")
pvz_zombie6 = pygame.image.load("images/Zombie/Zombie_6.png")
pvz_zombie7 = pygame.image.load("images/Zombie/Zombie_7.png")
pvz_zombie8 = pygame.image.load("images/Zombie/Zombie_8.png")
pvz_zombie9 = pygame.image.load("images/Zombie/Zombie_9.png")
pvz_zombie10 = pygame.image.load("images/Zombie/Zombie_10.png")
pvz_zombie11 = pygame.image.load("images/Zombie/Zombie_11.png")
pvz_zombie12 = pygame.image.load("images/Zombie/Zombie_12.png")
pvz_zombie13 = pygame.image.load("images/Zombie/Zombie_13.png")
pvz_zombie14 = pygame.image.load("images/Zombie/Zombie_14.png")
pvz_bzombie = pygame.image.load("images/BucketHeadZombie/BucketheadZombie_0.png")
pvz_bzombie1 = pygame.image.load("images/BucketHeadZombie/BucketheadZombie_1.png")
pvz_bzombie2 = pygame.image.load("images/BucketHeadZombie/BucketheadZombie_2.png")
pvz_bzombie3 = pygame.image.load("images/BucketHeadZombie/BucketheadZombie_2.png")
pvz_bzombie4 = pygame.image.load("images/BucketHeadZombie/BucketheadZombie_4.png")
pvz_bzombie5 = pygame.image.load("images/BucketHeadZombie/BucketheadZombie_5.png")
pvz_bzombie6 = pygame.image.load("images/BucketHeadZombie/BucketheadZombie_6.png")
pvz_bzombie7 = pygame.image.load("images/BucketHeadZombie/BucketheadZombie_7.png")
pvz_bzombie8 = pygame.image.load("images/BucketHeadZombie/BucketheadZombie_8.png")
pvz_bzombie9 = pygame.image.load("images/BucketHeadZombie/BucketheadZombie_9.png")
pvz_bzombie10 = pygame.image.load("images/BucketHeadZombie/BucketheadZombie_10.png")
pvz_bzombie11 = pygame.image.load("images/BucketHeadZombie/BucketheadZombie_11.png")
pvz_bzombie12 = pygame.image.load("images/BucketHeadZombie/BucketheadZombie_12.png")
pvz_bzombie13 = pygame.image.load("images/BucketHeadZombie/BucketheadZombie_13.png")
pvz_bzombie14 = pygame.image.load("images/BucketHeadZombie/BucketheadZombie_14.png")
pvz_czombie = pygame.image.load("images/ConeheadZombie/ConeheadZombie_0.png")
pvz_czombie1 = pygame.image.load("images/ConeheadZombie/ConeheadZombie_1.png")
pvz_czombie2 = pygame.image.load("images/ConeheadZombie/ConeheadZombie_2.png")
pvz_czombie3 = pygame.image.load("images/ConeheadZombie/ConeheadZombie_2.png")
pvz_czombie4 = pygame.image.load("images/ConeheadZombie/ConeheadZombie_4.png")
pvz_czombie5 = pygame.image.load("images/ConeheadZombie/ConeheadZombie_5.png")
pvz_czombie6 = pygame.image.load("images/ConeheadZombie/ConeheadZombie_6.png")
pvz_czombie7 = pygame.image.load("images/ConeheadZombie/ConeheadZombie_7.png")
pvz_czombie8 = pygame.image.load("images/ConeheadZombie/ConeheadZombie_8.png")
pvz_czombie9 = pygame.image.load("images/ConeheadZombie/ConeheadZombie_9.png")
pvz_czombie10 = pygame.image.load("images/ConeheadZombie/ConeheadZombie_10.png")
pvz_czombie11 = pygame.image.load("images/ConeheadZombie/ConeheadZombie_11.png")
pvz_czombie12 = pygame.image.load("images/ConeheadZombie/ConeheadZombie_12.png")
pvz_czombie13 = pygame.image.load("images/ConeheadZombie/ConeheadZombie_13.png")
pvz_czombie14 = pygame.image.load("images/ConeheadZombie/ConeheadZombie_14.png")
pvz_czombie15 = pygame.image.load("images/ConeheadZombie/ConeheadZombie_15.png")
pvz_czombie16 = pygame.image.load("images/ConeheadZombie/ConeheadZombie_16.png")
pvz_czombie17 = pygame.image.load("images/ConeheadZombie/ConeheadZombie_17.png")
pvz_czombie18 = pygame.image.load("images/ConeheadZombie/ConeheadZombie_18.png")
pvz_czombie19 = pygame.image.load("images/ConeheadZombie/ConeheadZombie_19.png")
pvz_czombie20 = pygame.image.load("images/ConeheadZombie/ConeheadZombie_20.png")
pvz_sunflower1 = pygame.image.load("images/Sunflower/SunFlower_1.png")
pvz_sunflower2 = pygame.image.load("images/Sunflower/SunFlower_2.png")
pvz_sunflower3 = pygame.image.load("images/Sunflower/SunFlower_3.png")
pvz_sunflower4 = pygame.image.load("images/Sunflower/SunFlower_4.png")
pvz_sunflower5 = pygame.image.load("images/Sunflower/SunFlower_5.png")
pvz_sunflower6 = pygame.image.load("images/Sunflower/SunFlower_6.png")
pvz_sunflower7 = pygame.image.load("images/Sunflower/SunFlower_7.png")
pvz_sunflower8 = pygame.image.load("images/Sunflower/SunFlower_8.png")
pvz_sunflower9 = pygame.image.load("images/Sunflower/SunFlower_9.png")
pvz_sunflower10 = pygame.image.load("images/Sunflower/SunFlower_10.png")
pvz_sunflower11 = pygame.image.load("images/Sunflower/SunFlower_11.png")
pvz_sunflower12 = pygame.image.load("images/Sunflower/SunFlower_12.png")
pvz_sunflower13 = pygame.image.load("images/Sunflower/SunFlower_13.png")
pvz_sunflower14 = pygame.image.load("images/Sunflower/SunFlower_14.png")
pvz_sunflower15 = pygame.image.load("images/Sunflower/SunFlower_15.png")
pvz_sunflower16 = pygame.image.load("images/Sunflower/SunFlower_16.png")
pvz_sunflower17 = pygame.image.load("images/Sunflower/SunFlower_17.png")
pvz_sunflower18 = pygame.image.load("images/Sunflower/SunFlower_18.png")
pvz_peashooter1 = pygame.image.load("images/Peashooter/Peashooter_1.png")
pvz_peashooter2 = pygame.image.load("images/Peashooter/Peashooter_2.png")
pvz_peashooter3 = pygame.image.load("images/Peashooter/Peashooter_3.png")
pvz_peashooter4 = pygame.image.load("images/Peashooter/Peashooter_4.png")
pvz_peashooter5 = pygame.image.load("images/Peashooter/Peashooter_5.png")
pvz_peashooter6 = pygame.image.load("images/Peashooter/Peashooter_6.png")
pvz_peashooter7 = pygame.image.load("images/Peashooter/Peashooter_7.png")
pvz_peashooter8 = pygame.image.load("images/Peashooter/Peashooter_8.png")
pvz_peashooter9 = pygame.image.load("images/Peashooter/Peashooter_9.png")
pvz_peashooter10 = pygame.image.load("images/Peashooter/Peashooter_10.png")
pvz_peashooter11 = pygame.image.load("images/Peashooter/Peashooter_11.png")
pvz_peashooter12 = pygame.image.load("images/Peashooter/Peashooter_12.png")
pvz_peashooter13 = pygame.image.load("images/Peashooter/Peashooter_13.png")

plants = []
plantpos = []
pplantpos = []
sunflowerlist = []

zomie_img = [pvz_zombie, pvz_zombie1, pvz_zombie2, pvz_zombie3, pvz_zombie4, pvz_zombie5, pvz_zombie6, pvz_zombie7, pvz_zombie8, pvz_zombie9, pvz_zombie10, pvz_zombie11, pvz_zombie12, pvz_zombie13, pvz_zombie14]
bzomie_img = [pvz_bzombie, pvz_bzombie1, pvz_bzombie2, pvz_bzombie3, pvz_bzombie4, pvz_bzombie5, pvz_bzombie6, pvz_bzombie7, pvz_bzombie8, pvz_bzombie9, pvz_bzombie10, pvz_bzombie11, pvz_bzombie12, pvz_bzombie13, pvz_bzombie14]
czomie_img = [pvz_czombie, pvz_czombie1, pvz_czombie2, pvz_czombie3, pvz_czombie4, pvz_czombie5, pvz_czombie6, pvz_czombie7, pvz_czombie8, pvz_czombie9, pvz_czombie10, pvz_czombie11, pvz_czombie12, pvz_czombie13, pvz_czombie14, pvz_czombie15, pvz_czombie16, pvz_czombie17, pvz_czombie18, pvz_czombie19, pvz_czombie20]

pvz_main_img = pygame.transform.scale(pvz_main_img, [screen_x,screen_y]) # ШАГ 2: Делаем нам нужный размер
pvz_house = pygame.transform.scale(pvz_house, [screen_x, screen_y])
pvz_peashooter = pygame.transform.scale(pvz_peashooter, [screen_x/17,screen_y/12])
pvz_sunflower = pygame.transform.scale(pvz_sunflower, [screen_x/17,screen_y/12])
pvz_wallnut = pygame.transform.scale(pvz_wallnut, [screen_x/21,screen_y/15])
pvz_sun = pygame.transform.scale(pvz_sun, [screen_x/(13+1/3),screen_y/(9+1/3)])
pvz_zombie = pygame.transform.scale(pvz_zombie, [screen_x/10,screen_y/7])
pvz_soundbut = pygame.transform.scale(pvz_soundbut, [screen_x/20,screen_y/14])
pvz_shovel = pygame.transform.scale(pvz_shovel, [screen_x/9, screen_y/12])
pvz_lawnmower = pygame.transform.scale(pvz_lawnmower, [screen_x/17, screen_y/12])
pvz_pea = pygame.transform.scale(pvz_pea, [screen_x/(100/3), screen_y/(70/3)])
pvz_sunflower1 = pygame.transform.scale(pvz_sunflower1, [screen_x/17,screen_y/12])
pvz_sunflower2 = pygame.transform.scale(pvz_sunflower2, [screen_x/17,screen_y/12])
pvz_sunflower3 = pygame.transform.scale(pvz_sunflower3, [screen_x/17,screen_y/12])
pvz_sunflower4 = pygame.transform.scale(pvz_sunflower4, [screen_x/17,screen_y/12])
pvz_sunflower5 = pygame.transform.scale(pvz_sunflower5, [screen_x/17,screen_y/12])
pvz_sunflower6 = pygame.transform.scale(pvz_sunflower6, [screen_x/17,screen_y/12])
pvz_sunflower7 = pygame.transform.scale(pvz_sunflower7, [screen_x/17,screen_y/12])
pvz_sunflower8 = pygame.transform.scale(pvz_sunflower8, [screen_x/17,screen_y/12])
pvz_sunflower9 = pygame.transform.scale(pvz_sunflower9, [screen_x/17,screen_y/12])
pvz_sunflower10 = pygame.transform.scale(pvz_sunflower10, [screen_x/17,screen_y/12])
pvz_sunflower11 = pygame.transform.scale(pvz_sunflower11, [screen_x/17,screen_y/12])
pvz_sunflower12 = pygame.transform.scale(pvz_sunflower12, [screen_x/17,screen_y/12])
pvz_sunflower13 = pygame.transform.scale(pvz_sunflower13, [screen_x/17,screen_y/12])
pvz_sunflower14 = pygame.transform.scale(pvz_sunflower14, [screen_x/17,screen_y/12])
pvz_sunflower15 = pygame.transform.scale(pvz_sunflower15, [screen_x/17,screen_y/12])
pvz_sunflower16 = pygame.transform.scale(pvz_sunflower16, [screen_x/17,screen_y/12])
pvz_sunflower17 = pygame.transform.scale(pvz_sunflower17, [screen_x/17,screen_y/12])
pvz_sunflower18 = pygame.transform.scale(pvz_sunflower18, [screen_x/17,screen_y/12])
pvz_sunflower1 = pygame.transform.scale(pvz_sunflower1, [screen_x/17,screen_y/12])
pvz_peashooter1 = pygame.transform.scale(pvz_peashooter1, [screen_x/17,screen_y/12])
pvz_peashooter2 = pygame.transform.scale(pvz_peashooter2, [screen_x/17,screen_y/12])
pvz_peashooter3 = pygame.transform.scale(pvz_peashooter3, [screen_x/17,screen_y/12])
pvz_peashooter4 = pygame.transform.scale(pvz_peashooter4, [screen_x/17,screen_y/12])
pvz_peashooter5 = pygame.transform.scale(pvz_peashooter5, [screen_x/17,screen_y/12])
pvz_peashooter6 = pygame.transform.scale(pvz_peashooter6, [screen_x/17,screen_y/12])
pvz_peashooter7 = pygame.transform.scale(pvz_peashooter7, [screen_x/17,screen_y/12])
pvz_peashooter8 = pygame.transform.scale(pvz_peashooter8, [screen_x/17,screen_y/12])
pvz_peashooter9 = pygame.transform.scale(pvz_peashooter9, [screen_x/17,screen_y/12])
pvz_peashooter10 = pygame.transform.scale(pvz_peashooter10, [screen_x/17,screen_y/12])
pvz_peashooter11 = pygame.transform.scale(pvz_peashooter11, [screen_x/17,screen_y/12])
pvz_peashooter12 = pygame.transform.scale(pvz_peashooter12, [screen_x/17,screen_y/12])
pvz_peashooter13 = pygame.transform.scale(pvz_peashooter13, [screen_x/17,screen_y/12])

pvz_snfs = [pvz_sunflower1, pvz_sunflower2, pvz_sunflower3, pvz_sunflower4, pvz_sunflower5, pvz_sunflower6, pvz_sunflower7, pvz_sunflower8, pvz_sunflower9, pvz_sunflower10, pvz_sunflower11, pvz_sunflower12, pvz_sunflower13, pvz_sunflower14, pvz_sunflower15, pvz_sunflower16, pvz_sunflower17, pvz_sunflower18]
pvz_pshs = [pvz_peashooter1, pvz_peashooter2, pvz_peashooter3, pvz_peashooter4, pvz_peashooter5, pvz_peashooter6, pvz_peashooter7, pvz_peashooter8, pvz_peashooter9, pvz_peashooter10, pvz_peashooter11, pvz_peashooter12, pvz_peashooter13]

lawnmows = []
for ab in range(6):
    lawnmows.append(pvz_lawnmower)
lawndata = []
yoffsett = 0
for ad in range(6):
    lawndata.append([screen_x/(100/15), screen_y/(875/(125+yoffsett))])
    yoffsett += 100
lawntouch = []
for ae in range(6):
    lawntouch.append(0)
lawnsound = []
for af in range(6):
    lawnsound.append(0)


bullets = []
def_bullet = [10, 1, 0, 0] ## 10 - Урон, 1 - Скорость, 0 - Позиция x, 0 - Позиция y.


zembie = enemy.Enemy(100, 0.4, screen, screen_x/(1+3/17), 140, 100, 100, random.randint(1, 6))
conzembie = enemy.Enemy(200, 0.1, screen, screen_x/(1+3/17), 140, 100, 100, random.randint(1, 6))

zom3cyc = [zembie, zembie, zembie, conzembie, conzembie, conzembie, conzembie, zembie, zembie, zembie, zembie, conzembie, zembie, conzembie, zembie, zembie, zembie, conzembie]
zom3cur = 0
zemb = zom3cyc[zom3cur]


money = 100

volume = 0.1

tmv_check = 1

track_main.set_volume(volume)

# Создаем шрифт для работы с текстом - ШАГ 1
button_font = pygame.font.SysFont("Helvetica", int(48//(1000/screen_x)))

# Сохраняем параметры текста в переменную - ШАГ 2
button_play_text = button_font.render("Play", False, [0,0,0])
button_exit_x = button_font.render("X", True, [255,0,0])
text_mode_two = button_font.render("Level 1", True, [0,255,0])
text_level_two = button_font.render("Level 2", True, [255,255,0])
text_level_three = button_font.render("Level 3", True, [255,0,0])
text_ready = button_font.render("Ready...", True, [255,0,0])
text_set = button_font.render("Set...", True, [255,0,0])
text_plant = button_font.render("PLANT!!!", True, [255,0,0])
text_level1 = button_font.render("Level 1", True, [255,0,255])
text_win = button_font.render("YOU WIN!", True, [255,255,0])

track_main.play()
imgcycle_snf = -1
imgcycle_snf2 = 0
imgcycle_psh = -1
imgcycle_psh2 = 0
pss = 0
time0 = 0
time1 = 0
time2 = 0
time3 = 0
time4 = 0
time5 = 0
need_check_sf = False
need_check_ps = False
need_check_pt = False
start_time_sf = 0
start_time_ps = 0
start_time_pt = 0
counter2 = 0
cooldown_snf = 0
cooldown_psh = 0
cooldown_pot = 0
cooldown_time_passed_snf = 0
cooldown_time_passed_psh = 0
cooldown_time_passed_pot = 0
sun_hitbox = None
start_time = 0
i = 0
imgcycle = -1
current_img = pvz_zombie
p = 1
sunflowersuncheck = 0
test = 0
deletecheck = 0
rand_col = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
display = 2
c1 = 0
gri = 0
last_purchase = None
clicked_grid = None
buttoncheck1 = 0
zomcreat = False
win_time = 0
running = True
# бесконечный игровой цикл чтобы игра не заканчивалась
while running:
    # ПЕРВЫЙ ЭТАП игрового цикла проверка событий в игре
    for event in pygame.event.get():
        if event.type == 256:
            running = False

        ##############################
#       Если событие поднятие кнопки мыши
        ###############################
        if event.type == 1026:
            print("A")
            if button_play_rect.collidepoint(event.pos) and mode == "1":
                mode = "2"
            ######################################
#           Проверяем нажатие с помощью collidepoint()
            ######################################
            elif button_exit_rect.collidepoint(event.pos) and mode == "1":
                pygame.display.quit()
            elif button_sound_rect.collidepoint(event.pos):
                if tmv_check == 1:
                    volume = 0
                    tmv_check = 0
                else:
                    tmv_check = 1
                    volume = 0.1
            elif button_level_one.collidepoint(event.pos) and mode == "2":
                mode = "3"
                start_time: int = pygame.time.get_ticks()
                time0 = 3000
                time1 = 13000
                time2 = 1000
                time3 = 36000
                time4 = 13000
                time5 = 20000
            elif button_sunflower.collidepoint(event.pos) and mode == "3":
                print("Вы выбрали подсолнуха")
                if buttoncheck1 == 1:
                    buttoncheck1 = 0
                else:
                    buttoncheck1 = 1
                    clicked_grid = None
            elif button_peashooter.collidepoint(event.pos) and mode == "3":
                print("Вы выбрали горохострела")
                if 2 == buttoncheck1:
                    buttoncheck1 = 0
                else:
                    buttoncheck1 = 2
                    clicked_grid = None
            elif button_wallnut.collidepoint(event.pos) and mode == "3":
                print("wallnut")
                if buttoncheck1 == 3:
                    buttoncheck1 = 0
                else:
                    buttoncheck1 = 3
            elif button_delete.collidepoint(event.pos) and mode == "3":
                print("hello")
                buttoncheck1 = 0
                if deletecheck == 1:
                    deletecheck = 0
                else:
                    deletecheck = 1
                    clicked_grid = None
            for i in sunflowerlist:
                if i.sunclick(event.pos):
                    sunflowerlist.remove(i)
                    money += 25
            if att3 == 1:
                if sun_hitbox.collidepoint(event.pos) and mode == "3":
                    att3 = 0
                    money += 25
                    starY = 0
                    starX = random.randint(0, 900)
                    rand_col = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
                    print(f"amount of money: {money}")
            for z in grids:
                if z.collidepoint(event.pos) and mode == "3":
                    clicked_grid = [z[0]+10, z[1]+10]

    # ВТОРОЙ ЭТАП игрового цикла обновление переменных
    track_main.set_volume(volume)
    sfx_lawnmower.set_volume(volume)

    # ТРЕТИЙ ЭТАП игрового цикла отображение предметов на экране
    screen.fill(screen_color)

    text_money = button_font.render(f"Money: {money}", True, [0, 0, 0])

    current_time = pygame.time.get_ticks() - (start_time + 200)

    imgcycle_snf2 += 1
    if imgcycle_snf2 == 2:
        imgcycle_snf2 = 0
        imgcycle_snf += 1
    if imgcycle_snf == 18:
        imgcycle_snf = 0
    current_snf_img = pvz_snfs[imgcycle_snf]

    imgcycle_psh2 += 1
    if imgcycle_psh2 == 2:
        imgcycle_psh2 = 0
        imgcycle_psh += 1
    if imgcycle_psh == 12:
        imgcycle_psh = 0
    current_psh_img = pvz_pshs[imgcycle_psh]

    if need_check_sf:
        cooldown_time_passed_snf = current_time - start_time_sf
        need_check_sf = False

    if need_check_ps:
        cooldown_time_passed_psh = current_time - start_time_ps
        need_check_ps = False

    if need_check_pt:
        cooldown_time_passed_pot = current_time - start_time_pt
        need_check_pt = False

    if cooldown_snf > 0:
        need_check_sf = True
        start_time_sf = current_time
        cooldown_snf -= cooldown_time_passed_snf
        if cooldown_snf < 0:
            cooldown_snf = 0

    if cooldown_psh > 0:
        need_check_ps = True
        start_time_ps = current_time
        cooldown_psh -= cooldown_time_passed_psh
        if cooldown_psh < 0:
            cooldown_psh = 0

    if cooldown_pot > 0:
        need_check_pt = True
        start_time_pt = current_time
        cooldown_pot -= cooldown_time_passed_pot
        if cooldown_pot < 0:
            cooldown_pot = 0

    if buttoncheck1 == 1:
        if clicked_grid:
            curpos = f"{str(clicked_grid[0]*1000 + clicked_grid[1])}"
            purpos = f"S{str(clicked_grid[0]*1000 + clicked_grid[1])}"
            if curpos not in plantpos and cooldown_snf == 0:
                if money >= 50:
                    plantpos.append(curpos)
                    pplantpos.append(purpos)
                    money -= 50
                    plants.append(plant.Plant(screen, "Sunflower", 50, clicked_grid[0], clicked_grid[1], (((clicked_grid[1])-screen_y/(875/100)) // (screen_y/(875/80))), current_time+10000, current_time+19000))
                    text_money = button_font.render(f"Money: {money}", True, [0, 0, 0])
                    clicked_grid = None
                    buttoncheck1 = 0
                    cooldown_snf = 7500
    elif buttoncheck1 == 2:
        if clicked_grid:
            curpos = f"{str(clicked_grid[0] * 1000 + clicked_grid[1])}"
            purpos = f"P{str(clicked_grid[0] * 1000 + clicked_grid[1])}"
            if curpos not in plantpos and cooldown_psh == 0:
                if money >= 100:
                    plantpos.append(curpos)
                    pplantpos.append(purpos)
                    money -= 100
                    ff = plant.Plant(screen, "Peashoot", 0, clicked_grid[0], clicked_grid[1], (((clicked_grid[1])-screen_y/(875/100)) // (screen_y/(875/80))), current_time, 0)
                    plants.append(ff)
                    text_money = button_font.render(f"Money: {money}", True, [0, 0, 0])
                    clicked_grid = None
                    if ff.row < 4.0:
                        ff.row += 1.0
                    buttoncheck1 = 0
                    cooldown_psh = 10000
    elif buttoncheck1 == 3:
        if clicked_grid:
            curpos = f"{str(clicked_grid[0] * 1000 + clicked_grid[1])}"
            purpos = f"W{str(clicked_grid[0] * 1000 + clicked_grid[1])}"
            if curpos not in plantpos and cooldown_pot == 0:
                if money >= 50:
                    plantpos.append(curpos)
                    pplantpos.append(purpos)
                    money -= 50
                    plants.append(plant.Plant(screen, "Wallnut", 0, clicked_grid[0], clicked_grid[1], (((clicked_grid[1])-screen_y/(875/100)) // (screen_y/(875/80))), 0, 0))
                    text_money = button_font.render(f"Money: {money}", True, [0, 0, 0])
                    clicked_grid = None
                    buttoncheck1 = 0
                    cooldown_pot = 15000
    elif deletecheck == 1:
        if clicked_grid:
            matchx = clicked_grid[0]
            matchy = clicked_grid[1]
            for i in plants:
                if i.pos_x == matchx and i.pos_y == matchy:
                    print(matchx, matchy, plantpos)
                    plants.pop(plants.index(i))
                    pindexx = plantpos.index(f"{matchx}{matchy}")
                    plantpos.pop(pindexx)
                    pplantpos.pop(pindexx)
                    clicked_grid = None
                    deletecheck = 0
            clicked_grid = None
            deletecheck = 0

    if mode == "1":
        # Размещаем прямоугольник на экране
        screen.blit(pvz_main_img, [0,0]) # ШАГ 3: Отображаем изображение на экране
        pygame.draw.rect(screen, [255, 255, 255], button_play_rect)

        # Размещаем круг на экране
        pygame.draw.ellipse(screen, [99,95,93], button_sound_rect)
        screen.blit(pvz_soundbut, [screen_x/100,screen_y/(35/32)])

        pygame.draw.ellipse(screen, [27,42,53], button_exit_rect)

        # Отображаем текст на экране - ШАГ 3
        screen.blit(button_play_text, [screen_x/(8+16/23),screen_y/(5+5/19)])
        screen.blit(button_exit_x, [screen_x/(500/477),screen_y/35])
    elif mode == "2":
        screen.blit(pvz_main_img, [0, 0])
        screen.blit(text_mode_two, [screen_x/(5+5/7),screen_y/(7/2)])
        screen.blit(text_level_two, [screen_x/(2+23/51), screen_y/(7/2)])
        screen.blit(text_level_three, [screen_x/(1+359/641), screen_y/(7/2)])

        pygame.draw.ellipse(screen, [99, 95, 93], button_sound_rect)
        screen.blit(pvz_soundbut, [screen_x / 100, screen_y / (35 / 32)])

        pygame.draw.rect(screen,[117,117,117], button_level_one)
        pygame.draw.rect(screen, [117, 117, 117], button_level_two)
        pygame.draw.rect(screen, [117, 117, 117], button_level_three)
    elif mode == "3":
        screen.blit(pvz_house, [0, 0])
        if time1 < current_time:
            print(f"{math.floor(current_time / 1000)} seconds passed")
            time1 += 20000
            att3 = 1
            print("hiii")
        if time2 < current_time:
            if imgcycle > 13:
                imgcycle = -1
            imgcycle += 1
            time2 += 100
            current_img = bzomie_img[imgcycle]
        if time3 < current_time:
            time3 += time3cyc[time3cur]
            print(zemb.hp)
            if zom3cur < 12:
                time3cur += 1
                zom3cur += 1
                zom3cor += 1
                print("ue")
                zemb = enemy.Enemy(100, 1, screen, screen_x/(1+3/17), 140, 100, 100, random.randint(1, 6))
                zembies.append(zemb)
            zomcreat = True
        timee = 1
        coolor1 = 75
        coolor2 = 151
        for i in grids[::-1]:
            if gri == 5:
                c1 += 2
                gri = 0
            if timee == 1:
                pygame.draw.rect(screen, [coolor1-c1, coolor2-c1, coolor1-c1], i)
                timee = 2
            else:
                pygame.draw.rect(screen, [coolor1-c1-10, coolor2-c1-10, coolor1-c1-10], i)
                timee = 1
            gri += 1
        lawnc = 1
        for i in lawns:
            if lawnc == 1:
                pygame.draw.rect(screen, [coolor2, coolor1, coolor2], i)
                lawnc = 2
            else:
                pygame.draw.rect(screen, [coolor2-5, coolor1-5, coolor2-5], i)
                lawnc = 1
        for q in plants:
            if q.plant == "Sunflower":
                q.appear(current_snf_img)
                if q.time2 < current_time:
                    pss = 0
                    q.time2 += 10000
                if q.time < current_time:
                    q.time += 10000
                    pss = entity.Sun(int(q.pos_x), int(q.pos_y), screen_x, screen_y)
                    sunflowerlist.append(pss)
            if q.plant == "Peashoot":
                q.appear(current_psh_img)
                if q.time < current_time:
                    zombie_in_row = any(ag.zrng == q.row for ag in zembies)
                    if zombie_in_row:
                        print(f"hi from {q.row}")
                        print("bullet")
                        bullets.append([10, 1, (q.pos_x+screen_x/25), q.pos_y, q.row])
                    q.time = current_time + 5000
            if q.plant == "Wallnut":
                q.appear(pvz_wallnut)
        for aj in sunflowerlist:
            aj.sunappear(screen)
        for ah in bullets:
            if ah[2] == screen_x:
                bullets.pop(bullets.index(ah))
            for ai in zembies:
                if int(ai.pos_x)-10 < int(ah[2]) < int(ai.pos_x)+5 and ah[4] == ai.zrng:
                    bullets.pop(bullets.index(ah))
                    ai.hp -= 25
            screen.blit(pvz_pea, [ah[2], (ah[3]+screen_y/70)])
            ah[2] += ah[1] * screen_y/(875/1.1)
        lawntime = 0
        for ac in lawnmows:
            if lawndata[lawntime][0] >= screen_x/(10/9):
                lawndata[lawntime][0] = (2**31)-1
                lawntouch[lawntime] = 0
            if lawntouch[lawntime] == 1:
                lawndata[lawntime][0] += screen_x/1000
                for ak in zembies:
                    if ak.pos_x-10 < lawndata[lawntime][0] < ak.pos_x+5 and ak.zrng == lawntime+1:
                        zembies.pop(zembies.index(ak))
            if lawnsound[lawntime] == 1:
                sfx_lawnmower.play()
                lawnsound[lawntime] = 2
            screen.blit(ac, lawndata[lawntime])
            lawntime += 1
        if time5 < current_time:
            sunflowerlist = []
            time5 += 10000
        for n in zembies:
            n.pos_x -= 0.33 * n.speed
            n.pos_y = 80*n.zrng+(20*n.zrng)
            n.appear(current_img)
            if n.hp <= 0:
                zembies.pop(zembies.index(n))
            if n.pos_x < screen_x/(1000/100):
                lawntouch[n.zrng-1] = 1
                if lawnsound[n.zrng-1] == 0:
                    lawnsound[n.zrng-1] = 1
                zembies.pop(zembies.index(n))
                print("delete")
                print(n.zrng)
        pygame.draw.rect(screen, [209, 209, 209], button_sunflower)
        pygame.draw.rect(screen, [209, 209, 209], button_peashooter)
        pygame.draw.rect(screen, [209, 209, 209], button_wallnut)
        if deletecheck == 0:
            pygame.draw.rect(screen, [144,144,144], button_delete)
        else:
            pygame.draw.rect(screen, [173, 32, 0], button_delete)
        screen.blit(pvz_shovel, [screen_x/(7+1/3), screen_y/35])
        screen.blit(pvz_wallnut, [screen_x/(33+1/3), screen_y/(3+3/4)])
        screen.blit(pvz_peashooter, [screen_x/(33+1/3), screen_y/7])
        screen.blit(pvz_sunflower, [screen_x/(33+1/3), screen_y/50])
        if att3 == 1:
            sun_hitbox = pygame.Rect(starX, starY, screen_x/21, screen_y/15)
            screen.blit(pvz_sun, [starX, starY])
            starY += screen_y/1000
            if starY >= screen_y:
                starY = 0
                att3 = 0
                starX = random.randint(int(screen_x/10), int(screen_x/(10/9)))
                rand_col = [random.randint(150, 255), random.randint(75, 255), random.randint(0, 100)]
                print(rand_col)
        pygame.draw.ellipse(screen, [99, 95, 93], button_sound_rect)
        screen.blit(pvz_soundbut, [screen_x / 100, screen_y / (35 / 32)])
        screen.blit(text_money, [screen_x/(1000/60),screen_y/(70/65)])
        screen.blit(text_level1, [0, screen_y/(17/14)])
        if time0 > current_time:
            if 0 < current_time < 1000:
                screen.blit(text_ready, [screen_x / (2 + 23 / 51), screen_y / (7 / 2)])
            elif 1000 < current_time < 2000:
                screen.blit(text_set, [screen_x / (2 + 23 / 51), screen_y / (7 / 2)])
            elif 2000 < current_time < 3000:
                screen.blit(text_plant, [screen_x / (2 + 23 / 51), screen_y / (7 / 2)])
        if zom3cur == 12 and len(zembies) == 0:
            screen.blit(text_win, [screen_x / (2 + 23 / 51), screen_y / (7 / 2)])
            win_time = current_time
        if current_time >= win_time+5000 and win_time != 0:
            mode = "1"
    c1 = 0
    gri = 0
    pygame.display.flip()
    clock.tick(240)  # Кадры в секунду
pygame.display.quit()