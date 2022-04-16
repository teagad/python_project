import profile
import time

import pygame
from tamagochi import tamagochi

# imported module
pygame.init()
pg = pygame


COLOR_INACTIVE = pg.Color('green')
COLOR_ACTIVE = pg.Color('dodgerblue2')
FONT = pg.font.Font(None, 32)
Profile = ""

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.image = pygame.transform.scale(self.image, (700, 700))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event, used):
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    global Profile
                    Profile = self.text
                    used = False
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect, 2)


# dict of all tamagochi
tamagochis = {"tamagochi1": "tamagochi1.png", "tamagochi2": "tamagochi2.png", "tamagochi3": "tamagochi3.png"}

screen = pygame.display.set_mode((700, 700))



# background_image
BackGround = Background('background_image.png', [0, 0])
screen.fill([1, 254, 104])
screen.blit(BackGround.image, BackGround.rect)

# title
pygame.display.set_caption("Russian Tamagochi")

# choosing tamagochi
k = 0
for i in tamagochis.values():
    image = pygame.image.load(i)
    image = pygame.transform.scale(image, (300, 300))
    screen.blit(image, (k, 100))
    k += 200

base_font = pygame.font.Font(None, 32)
happines_text = 'Write Profile name and press enter then chouse animal'
input_rect1 = pygame.Rect(100, 550, 200, 64)
text_surface1 = base_font.render(happines_text, True, (255, 255, 255))
screen.blit(text_surface1, (input_rect1.x + 5, input_rect1.y + 5))

input_box1 = InputBox(250, 600, 300, 64)
pygame.display.update()
clock = pg.time.Clock()
Running = True
used = True
while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
        if used:
            input_box1.handle_event(event,used)
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
        input_box1.draw(screen)
        pg.display.flip()
        clock.tick(30)
    mouse = pygame.mouse.get_pos()

screen.fill([1, 254, 104])
screen.blit(BackGround.image, BackGround.rect)
# placing tamagochi picture
image = pygame.image.load(winer)
image = pygame.transform.scale(image, (300, 300))
screen.blit(image, (100, 400))

# making text box
base_font = pygame.font.Font(None, 25)
happines_text = 'happines:'
input_rect1 = pygame.Rect(500, 600, 200, 64)
pygame.draw.rect(screen, (1, 254, 104, 32), input_rect1)

text_surface1 = base_font.render(happines_text, True, (255, 255, 255))

hunger_text = 'hunger:'
input_rect2 = pygame.Rect(500, 500, 200, 64)
pygame.draw.rect(screen, (1, 254, 104, 32), input_rect2)

text_surface2 = base_font.render(hunger_text, True, (255, 255, 255))

status_text = 'CLICK ON LIVE TO START GAME'
input_rect3 = pygame.Rect(0, 200, 300, 100)
pygame.draw.rect(screen, (1, 254, 104, 32), input_rect3)

text_surface3 = base_font.render(status_text, True, (255, 255, 255))

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
# button1
text1 = not_base_font.render('feed', True, (250, 250, 250))
x1 = 0
y1 = 0
# button2
text2 = not_base_font.render('Live', True, (250, 250, 250))
x2 = width + 20
y2 = 0
# button3
text3 = not_base_font.render('Hug', True, (250, 250, 250))
x3 = width * 2 + 40
y3 = 0

# starting event
Running = True
clickable = True
while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            try:
                tamagochik.setinfo(Profile,winer)
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
                        pygame.draw.rect(screen, (1, 254, 104, 32), input_rect3)
                        text_surface3 = base_font.render(f"status:game started", True, (255, 255, 255))
                        text_surface4 = base_font.render(f"Masha stats will drop in a minute", True, (255, 255, 255))
                        text_surface2 = base_font.render("I am not hungry", True, (255, 255, 255))
                        screen.blit(text_surface2, (input_rect3.x + 5, input_rect3.y + 40))
                        screen.blit(text_surface3, (input_rect3.x + 5, input_rect3.y + 5))
                        screen.blit(text_surface4, (input_rect3.x + 5, input_rect3.y + 20))
                except NameError:
                    pass
            # button live
            if x2 <= mouse[0] <= x2 + width and y2 <= mouse[1] <= y2 + height and clickable:
                clickable = False
                tamagochik = tamagochi()
                tamagochik.getinfo(Profile,winer)
                tamagochik.time = time.time()
                events(tamagochik.coverter(time.ctime().split()[3]) - tamagochik.date)
                # hunger
                pygame.draw.rect(screen, (1, 254, 104, 32), input_rect2)
                text_surface2 = base_font.render(f"hunger:{tamagochik.hunger}", True, (255, 255, 255))
                screen.blit(text_surface2, (input_rect2.x + 5, input_rect2.y + 5))
                # happines
                pygame.draw.rect(screen, (1, 254, 104, 32), input_rect1)
                text_surface1 = base_font.render(f"happines:{tamagochik.happines}", True, (255, 255, 255))
                screen.blit(text_surface1, (input_rect1.x + 5, input_rect1.y + 5))
                # status
                pygame.draw.rect(screen, (1, 254, 104, 32), input_rect3)
                text_surface3 = base_font.render(f"status:game started", True, (255, 255, 255))
                text_surface4 = base_font.render(f"Masha stats will drop in a minute", True, (255, 255, 255))
                screen.blit(text_surface3, (input_rect3.x + 5, input_rect3.y + 5))
                screen.blit(text_surface4, (input_rect3.x + 5, input_rect3.y + 20))
            # button happy
            if x3 <= mouse[0] <= x3 + width and y3 <= mouse[1] <= y3 + height:
                try:
                    if tamagochik.happines < 18:
                        tamagochik.happines += 3
                    else:
                        pygame.draw.rect(screen, (1, 254, 104, 32), input_rect3)
                        text_surface3 = base_font.render(f"status:game started", True, (255, 255, 255))
                        text_surface4 = base_font.render(f"Masha stats will drop in a minute", True, (255, 255, 255))
                        text_surface2 = base_font.render("I am not borred boss", True, (255, 255, 255))
                        screen.blit(text_surface2, (input_rect3.x + 5, input_rect3.y + 40))
                        screen.blit(text_surface3, (input_rect3.x + 5, input_rect3.y + 5))
                        screen.blit(text_surface4, (input_rect3.x + 5, input_rect3.y + 20))
                except NameError:
                    pass

    # update game

    try:
        x = tamagochik.hunger
        pygame.draw.rect(screen, (1, 254, 104, 32), input_rect2)
        text_surface2 = base_font.render(f"hunger:{tamagochik.hunger}", True, (255, 255, 255))
        screen.blit(text_surface2, (input_rect2.x + 5, input_rect2.y + 5))

        pygame.draw.rect(screen, (1, 254, 104, 32), input_rect1)
        text_surface1 = base_font.render(f"happines:{tamagochik.happines}", True, (255, 255, 255))
        screen.blit(text_surface1, (input_rect1.x + 5, input_rect1.y + 5))
    except NameError:
        pass

    mouse = pygame.mouse.get_pos()


    # events
    def events(delta=None):
        try:
            global Running
            if delta != None:
                if delta > 60:
                    tamagochik.time = time.time() - (delta - 60 * int(delta / 60))
                    tamagochik.hunger += 1 * int(delta / 60)
                    tamagochik.happines -= 1 * int(delta / 60)
            else:
                delta = time.time() - tamagochik.time
                if delta > 60:
                    tamagochik.time = time.time()
                    tamagochik.hunger += 1
                    tamagochik.happines -= 1
                    if tamagochik.happines > 7 and tamagochik.hunger < 30:
                        pygame.draw.rect(screen, (1, 254, 104, 32), input_rect3)
                        text_surface3 = base_font.render(f"status:game started", True, (255, 255, 255))
                        text_surface4 = base_font.render(f"Masha stats will drop in a minute", True, (255, 255, 255))
                        text_surface2 = base_font.render("It`s all okay!", True, (255, 255, 255))
                        screen.blit(text_surface3, (input_rect3.x + 5, input_rect3.y + 5))
                        screen.blit(text_surface4, (input_rect3.x + 5, input_rect3.y + 20))
                        screen.blit(text_surface2, (input_rect3.x + 5, input_rect3.y + 40))

                if tamagochik.hunger > 40:
                    pygame.draw.rect(screen, (1, 254, 104, 32), input_rect3)
                    text_surface3 = base_font.render("your Masha died ", True,
                                                     (255, 255, 255))
                    text_surface4 = base_font.render("The game will end in 5 sec", True, (255, 255, 255))
                    screen.blit(text_surface3, (input_rect3.x + 5, input_rect3.y + 5))
                    screen.blit(text_surface4, (input_rect3.x + 5, input_rect3.y + 20))
                    pygame.display.update()
                    tamagochik.setinfo(Profile,winer, 20, 20)
                    time.sleep(5)
                    Running = False
                elif tamagochik.hunger > 30:
                    pygame.draw.rect(screen, (1, 254, 104, 32), input_rect3)
                    text_surface3 = base_font.render(f"status:game started", True, (255, 255, 255))
                    text_surface4 = base_font.render(f"Masha stats will drop in a minute", True, (255, 255, 255))
                    text_surface2 = base_font.render("i am hungry!", True, (255, 255, 255))
                    screen.blit(text_surface2, (input_rect3.x + 5, input_rect3.y + 40))
                    screen.blit(text_surface3, (input_rect3.x + 5, input_rect3.y + 5))
                    screen.blit(text_surface4, (input_rect3.x + 5, input_rect3.y + 20))
                elif tamagochik.happines < 1:
                    pygame.draw.rect(screen, (1, 254, 104, 32), input_rect3)
                    text_surface3 = base_font.render("Your pet died from lonliness!", True,
                                                     (255, 255, 255))
                    text_surface4 = base_font.render("The game will end in 5 sec", True,
                                                     (255, 255, 255))
                    screen.blit(text_surface3, (input_rect3.x + 5, input_rect3.y + 5))
                    screen.blit(text_surface4, (input_rect3.x + 5, input_rect3.y + 20))
                    pygame.display.update()
                    tamagochik.setinfo(Profile,winer, 20, 20)
                    time.sleep(5)
                    Running = False
                elif tamagochik.happines < 5:
                    pygame.draw.rect(screen, (1, 254, 104, 32), input_rect3)
                    text_surface3 = base_font.render(f"status:game started", True, (255, 255, 255))
                    text_surface4 = base_font.render(f"Masha stats will drop in a minute", True, (255, 255, 255))
                    text_surface2 = base_font.render("Nobody loves me!", True, (255, 255, 255))
                    screen.blit(text_surface2, (input_rect3.x + 5, input_rect3.y + 40))
                    screen.blit(text_surface3, (input_rect3.x + 5, input_rect3.y + 5))
                    screen.blit(text_surface4, (input_rect3.x + 5, input_rect3.y + 20))
                elif tamagochik.happines < 7:
                    pygame.draw.rect(screen, (1, 254, 104, 32), input_rect3)
                    text_surface3 = base_font.render(f"status:game started", True, (255, 255, 255))
                    text_surface4 = base_font.render(f"Masha stats will drop in a minute", True, (255, 255, 255))
                    text_surface2 = base_font.render("I’m bored!", True, (255, 255, 255))
                    screen.blit(text_surface2, (input_rect3.x + 5, input_rect3.y + 40))
                    screen.blit(text_surface3, (input_rect3.x + 5, input_rect3.y + 5))
                    screen.blit(text_surface4, (input_rect3.x + 5, input_rect3.y + 20))



        except NameError:
            pass


    events()

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
