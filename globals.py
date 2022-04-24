import pygame
from Background import Background
from InputBox import InputBox as imbox


class Globals:
    # dict of all tamagochi
    tamagochis = {"tamagochi1": "assets/tamagochi1.png", "tamagochi2": "assets/tamagochi2.png",
                  "tamagochi3": "assets/tamagochi3.png"}
    winer = 0

    screensize = (700, 700)
    tamagochisize = (300, 300)
    Colordelete = (30, 30, 30)
    Color_basic = (255, 255, 255)
    delta_time = 60
    RectColor = (1, 254, 104, 32)
    screen = pygame.display.set_mode(screensize)
    # background_image
    BackGround = Background('assets/background_image.png', [0, 0])
    base_font = pygame.font.Font(None, 32)
    Profile_array_rect = pygame.Rect(0, 0, 200, 64)
    Profile_text = 'Write Profile name and press enter then chouse animal'
    Profile_rect = pygame.Rect(100, 550, 200, 64)
    Profile_text_surface = base_font.render(Profile_text, True, Color_basic)
    Profile = "Guest"
    input_box1 = imbox(250, 600, 300, 64)
    tmagochi_coordinates = (100, 400)
    base_font = pygame.font.Font(None, 25)
    happines_text = 'happines:'
    happines_rect = pygame.Rect(500, 600, 200, 64)
    happines_text_surface = base_font.render(happines_text, True, Color_basic)
    hunger_text = 'hunger:'
    hunger_rect = pygame.Rect(500, 500, 200, 64)
    hunger_text_surface = base_font.render(hunger_text, True, Color_basic)
    status_text = 'CLICK ON LIVE TO START GAME'
    status_rect = pygame.Rect(0, 200, 300, 100)
    status_text_surface = base_font.render(status_text, True, Color_basic)
    # button settings
    not_base_font = pygame.font.Font(None, 32)
    width = 60
    height = 32
    color_light = (170, 170, 170)
    color_dark = (100, 100, 100)
    C_text = (250, 250, 250)
    # button1
    button_text1 = not_base_font.render('feed', True, C_text)
    button_x1 = 0
    button_y1 = 0
    # button2
    button_text2 = not_base_font.render('Live', True, C_text)
    button_x2 = width + 20
    button_y2 = 0
    # button3
    button_text3 = not_base_font.render('Hug', True, C_text)
    button_x3 = width * 2 + 40
    button_y3 = 0
    hunger_limit = 40
    vary_hungry = 30
    happines_limit = 1
    vary_bored = 5
    bored = 7
    basic_hunger = 20
    basic_happines = 20
    hunger_decrease = 1
    happines_decrease = 1
    hunger_decrease_by_click = 3
    happines_increase_by_click = 3
    first_tamagochi_coordinate_x = 0
    second_tamagochi_coordinate_x = 200
    third_tamagochi_coordinate_x = 400
    coordinate_y = 100
    first_line_x = 5
    first_line_y = 5
    second_line_x = 5
    second_line_y = 20
    third_line_x = 5
    third_line_y = 40
    time_sleep = 5
    tamagochi_coords = [(first_tamagochi_coordinate_x, coordinate_y), (second_tamagochi_coordinate_x, coordinate_y),
                        (third_tamagochi_coordinate_x, coordinate_y)]
    Running = True
    clickable = True
