import time

import pygame
from tamagochi import tamagochi
from Background import Background
from InputBox import InputBox as imbox
import InputBox

# imported module
pygame.init()

# dict of all tamagochi
tamagochis = {"tamagochi1": "assets/tamagochi1.png", "tamagochi2": "assets/tamagochi2.png",
              "tamagochi3": "assets/tamagochi3.png"}

screensize = (700, 700)
tamagochisize = (300, 300)
Colordelete = (30, 30, 30)
Color_basic = (255, 255, 255)
delta_time = 60
RectColor = (1, 254, 104, 32)

screen = pygame.display.set_mode(screensize)

# background_image
BackGround = Background('assets/background_image.png', [0, 0])
screen.blit(BackGround.image, BackGround.rect)

# title
pygame.display.set_caption("Russian Tamagochi")

# choosing tamagochi
k = 0
for i in tamagochis.values():
    image = pygame.image.load(i)
    image = pygame.transform.scale(image, tamagochisize)
    screen.blit(image, (k, 100))
    k += 200

base_font = pygame.font.Font(None, 32)
happines_text = 'Write Profile name and press enter then chouse animal'
input_rect1 = pygame.Rect(100, 550, 200, 64)
text_surface1 = base_font.render(happines_text, True, Color_basic)
screen.blit(text_surface1, (input_rect1.x + 5, input_rect1.y + 5))

input_box1 = imbox(250, 600, 300, 64)
pygame.display.update()
Profile ="Guest"
Running = True
while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
        x = input_box1.handle_event(event)
        if x: Profile = x
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 0 <= mouse[0] <= 300 and 100 <= mouse[1] <= 400:
                winer = tamagochis["tamagochi1"]
                Running = False
            if 200 <= mouse[0] <= 500 and 100 <= mouse[1] <= 400:
                winer = tamagochis["tamagochi2"]
                Running = False
            if 400 <= mouse[0] <= 600 and 100 <= mouse[1] <= 400:
                winer = tamagochis["tamagochi3"]
                Running = False
        input_box1.update()
        pygame.draw.rect(screen, (Colordelete), input_box1.rect)
        input_box1.draw(screen)
        pygame.display.update()
    mouse = pygame.mouse.get_pos()

screen.fill([1, 254, 104])
screen.blit(BackGround.image, BackGround.rect)
# placing tamagochi picture
image = pygame.image.load(winer)
image = pygame.transform.scale(image, tamagochisize)
screen.blit(image, (100, 400))

# making text box
base_font = pygame.font.Font(None, 25)
happines_text = 'happines:'
input_rect1 = pygame.Rect(500, 600, 200, 64)
pygame.draw.rect(screen, RectColor, input_rect1)

text_surface1 = base_font.render(happines_text, True, Color_basic)

hunger_text = 'hunger:'
input_rect2 = pygame.Rect(500, 500, 200, 64)
pygame.draw.rect(screen, RectColor, input_rect2)

text_surface2 = base_font.render(hunger_text, True, Color_basic)

status_text = 'CLICK ON LIVE TO START GAME'
input_rect3 = pygame.Rect(0, 200, 300, 100)
pygame.draw.rect(screen, RectColor, input_rect3)

text_surface3 = base_font.render(status_text, True, Color_basic)

# render at position stated in arguments
screen.blit(text_surface1, (input_rect1.x + 5, input_rect1.y + 5))
screen.blit(text_surface2, (input_rect2.x + 5, input_rect2.y + 5))
screen.blit(text_surface3, (input_rect3.x + 5, input_rect3.y + 5))

# button settings
not_base_font = pygame.font.Font(None, 32)
width = 60
height = 32
pygame.display.update()
color_light = (170, 170, 170)
color_dark = (100, 100, 100)
C_text = (250, 250, 250)
# button1
text1 = not_base_font.render('feed', True, C_text)
x1 = 0
y1 = 0
# button2
text2 = not_base_font.render('Live', True, C_text)
x2 = width + 20
y2 = 0
# button3
text3 = not_base_font.render('Hug', True, C_text)
x3 = width * 2 + 40
y3 = 0

# starting event
Running = True
clickable = True


# events
def events(tamagochik, delta=None):
    global Running
    try:
        if delta != None:
            if delta > delta_time:
                tamagochik.time = time.time() - (delta - delta_time * int(delta / delta_time))
                tamagochik.hunger += 1 * int(delta / delta_time)
                tamagochik.happines -= 1 * int(delta / delta_time)
        else:
            delta = time.time() - tamagochik.time
            if delta > delta_time:
                tamagochik.time = time.time()
                tamagochik.hunger += 1
                tamagochik.happines -= 1
                if tamagochik.happines > 7 and tamagochik.hunger < 30:
                    pygame.draw.rect(screen, RectColor, input_rect3)
                    text_surface3 = base_font.render(f"status:game started", True, Color_basic)
                    text_surface4 = base_font.render(f"Masha stats will drop in a minute", True, Color_basic)
                    text_surface2 = base_font.render("It`s all okay!", True, Color_basic)
                    screen.blit(text_surface3, (input_rect3.x + 5, input_rect3.y + 5))
                    screen.blit(text_surface4, (input_rect3.x + 5, input_rect3.y + 20))
                    screen.blit(text_surface2, (input_rect3.x + 5, input_rect3.y + 40))

            if tamagochik.hunger > 40:
                pygame.draw.rect(screen, RectColor, input_rect3)
                text_surface3 = base_font.render("your Masha died ", True,
                                                 Color_basic)
                text_surface4 = base_font.render("The game will end in 5 sec", True, Color_basic)
                screen.blit(text_surface3, (input_rect3.x + 5, input_rect3.y + 5))
                screen.blit(text_surface4, (input_rect3.x + 5, input_rect3.y + 20))
                pygame.display.update()
                tamagochik.setinfo(Profile, winer, 20, 20)
                time.sleep(5)
                Running = False
            elif tamagochik.hunger > 30:
                pygame.draw.rect(screen, RectColor, input_rect3)
                text_surface3 = base_font.render(f"status:game started", True, Color_basic)
                text_surface4 = base_font.render(f"Masha stats will drop in a minute", True, Color_basic)
                text_surface2 = base_font.render("i am hungry!", True, Color_basic)
                screen.blit(text_surface2, (input_rect3.x + 5, input_rect3.y + 40))
                screen.blit(text_surface3, (input_rect3.x + 5, input_rect3.y + 5))
                screen.blit(text_surface4, (input_rect3.x + 5, input_rect3.y + 20))
            elif tamagochik.happines < 1:
                pygame.draw.rect(screen, RectColor, input_rect3)
                text_surface3 = base_font.render("Your pet died from lonliness!", True,
                                                 Color_basic)
                text_surface4 = base_font.render("The game will end in 5 sec", True,
                                                 Color_basic)
                screen.blit(text_surface3, (input_rect3.x + 5, input_rect3.y + 5))
                screen.blit(text_surface4, (input_rect3.x + 5, input_rect3.y + 20))
                pygame.display.update()
                tamagochik.setinfo(Profile, winer, 20, 20)
                time.sleep(5)
                Running = False
            elif tamagochik.happines < 5:
                pygame.draw.rect(screen, RectColor, input_rect3)
                text_surface3 = base_font.render(f"status:game started", True, Color_basic)
                text_surface4 = base_font.render(f"Masha stats will drop in a minute", True, Color_basic)
                text_surface2 = base_font.render("Nobody loves me!", True, Color_basic)
                screen.blit(text_surface2, (input_rect3.x + 5, input_rect3.y + 40))
                screen.blit(text_surface3, (input_rect3.x + 5, input_rect3.y + 5))
                screen.blit(text_surface4, (input_rect3.x + 5, input_rect3.y + 20))
            elif tamagochik.happines < 7:
                pygame.draw.rect(screen, RectColor, input_rect3)
                text_surface3 = base_font.render(f"status:game started", True, Color_basic)
                text_surface4 = base_font.render(f"Masha stats will drop in a minute", True, Color_basic)
                text_surface2 = base_font.render("I’m bored!", True, Color_basic)
                screen.blit(text_surface2, (input_rect3.x + 5, input_rect3.y + 40))
                screen.blit(text_surface3, (input_rect3.x + 5, input_rect3.y + 5))
                screen.blit(text_surface4, (input_rect3.x + 5, input_rect3.y + 20))
    except NameError:
        pass


while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            try:
                tamagochik.setinfo(Profile, winer)
            except NameError:
                pass
            Running = False
        # checks if a mouse is clicked
        if event.type == pygame.MOUSEBUTTONDOWN:

            # button hungry
            if x1 <= mouse[0] <= x1 + width and y1 <= mouse[1] <= y1 + height:
                try:
                    if tamagochik.hunger > 4:
                        tamagochik.hunger -= 3
                    else:
                        pygame.draw.rect(screen, RectColor, input_rect3)
                        text_surface3 = base_font.render(f"status:game started", True, Color_basic)
                        text_surface4 = base_font.render(f"Masha stats will drop in a minute", True, Color_basic)
                        text_surface2 = base_font.render("I am not hungry", True, Color_basic)
                        screen.blit(text_surface2, (input_rect3.x + 5, input_rect3.y + 40))
                        screen.blit(text_surface3, (input_rect3.x + 5, input_rect3.y + 5))
                        screen.blit(text_surface4, (input_rect3.x + 5, input_rect3.y + 20))
                except NameError:
                    pass
            # button live
            if x2 <= mouse[0] <= x2 + width and y2 <= mouse[1] <= y2 + height and clickable:
                clickable = False
                tamagochik = tamagochi()
                tamagochik.getinfo(Profile, winer)
                tamagochik.time = time.time()
                events(tamagochik, tamagochik.coverter(time.ctime().split()[3]) - tamagochik.date)
                # hunger
                pygame.draw.rect(screen, RectColor, input_rect2)
                text_surface2 = base_font.render(f"hunger:{tamagochik.hunger}", True, Color_basic)
                screen.blit(text_surface2, (input_rect2.x + 5, input_rect2.y + 5))
                # happines
                pygame.draw.rect(screen, RectColor, input_rect1)
                text_surface1 = base_font.render(f"happines:{tamagochik.happines}", True, Color_basic)
                screen.blit(text_surface1, (input_rect1.x + 5, input_rect1.y + 5))
                # status
                pygame.draw.rect(screen, RectColor, input_rect3)
                text_surface3 = base_font.render(f"status:game started", True, Color_basic)
                text_surface4 = base_font.render(f"Masha stats will drop in a minute", True, Color_basic)
                screen.blit(text_surface3, (input_rect3.x + 5, input_rect3.y + 5))
                screen.blit(text_surface4, (input_rect3.x + 5, input_rect3.y + 20))
            # button happy
            if x3 <= mouse[0] <= x3 + width and y3 <= mouse[1] <= y3 + height:
                try:
                    if tamagochik.happines < 18:
                        tamagochik.happines += 3
                    else:
                        pygame.draw.rect(screen, RectColor, input_rect3)
                        text_surface3 = base_font.render(f"status:game started", True, Color_basic)
                        text_surface4 = base_font.render(f"Masha stats will drop in a minute", True, Color_basic)
                        text_surface2 = base_font.render("I am not borred boss", True, Color_basic)
                        screen.blit(text_surface2, (input_rect3.x + 5, input_rect3.y + 40))
                        screen.blit(text_surface3, (input_rect3.x + 5, input_rect3.y + 5))
                        screen.blit(text_surface4, (input_rect3.x + 5, input_rect3.y + 20))
                except NameError:
                    pass

    # update game

    try:
        x = tamagochik.hunger
        pygame.draw.rect(screen, RectColor, input_rect2)
        text_surface2 = base_font.render(f"hunger:{tamagochik.hunger}", True, Color_basic)
        screen.blit(text_surface2, (input_rect2.x + 5, input_rect2.y + 5))

        pygame.draw.rect(screen, RectColor, input_rect1)
        text_surface1 = base_font.render(f"happines:{tamagochik.happines}", True, Color_basic)
        screen.blit(text_surface1, (input_rect1.x + 5, input_rect1.y + 5))
    except NameError:
        pass

    mouse = pygame.mouse.get_pos()
    try:
        events(tamagochik)
    except Exception:
        pass

    # if mouse is hovered on a button it
    # changes to lighter shade
    for x, y, text in zip([x1, x2, x3], [y1, y2, y3], [text1, text2, text3]):
        if x <= mouse[0] <= x + width and y <= mouse[1] <= y + height:
            pygame.draw.rect(screen, color_light, [x, y, width, height])

        else:
            pygame.draw.rect(screen, color_dark, [x, y, width, height])

        # superimposing the text onto our button
        screen.blit(text, (x, y))

    # updates the frames of the game
    pygame.display.update()
