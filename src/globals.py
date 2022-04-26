import pygame
pygame.init()

class Globals:
    tamagochis = {"tamagochi1": "assets/tamagochi1.png",
                  "tamagochi2": "assets/tamagochi2.png",
                  "tamagochi3": "assets/tamagochi3.png"}
    winer = 0
    tamagochisize = (300, 300)
    Color_basic = (255, 255, 255)
    RectColor = (1, 254, 104, 32)
    screen = pygame.display.set_mode((700, 700))    
    base_font = pygame.font.Font(None, 32)
    profile_text_font = pygame.font.Font(None, 48)
    Profile_text = 'Write Profile name and press enter then chouse animal'
    Profile_rect = pygame.Rect(100, 550, 200, 64)
    Profile_text_surface = base_font.render(Profile_text, True, Color_basic)
    Profile = "Guest"
    base_font = pygame.font.Font(None, 25)
    happines_rect = pygame.Rect(500, 600, 200, 64)
    happines_text_surface = base_font.render('happines:', True, Color_basic)
    hunger_rect = pygame.Rect(500, 500, 200, 64)
    hunger_text_surface = base_font.render('hunger:', True, Color_basic)
    status_text = 'CLICK ON LIVE TO START GAME'
    status_rect = pygame.Rect(0, 200, 300, 100)
    status_text_surface = base_font.render(status_text, True, Color_basic)
    not_base_font = pygame.font.Font(None, 32)
    width = 60
    height = 32
    C_text = (250, 250, 250)
    button_text1 = not_base_font.render('feed', True, C_text)
    button_x1 = 0
    button_y1 = 0
    button_text2 = not_base_font.render('Live', True, C_text)
    button_x2 = width + 20
    button_y2 = 0
    button_text3 = not_base_font.render('Hug', True, C_text)
    button_x3 = width * 2 + 40
    button_y3 = 0
    first_line_x = 5
    first_line_y = 5
    second_line_x = 5
    second_line_y = 20
    third_line_x = 5
    third_line_y = 40
    Running = True
    new_profile_C = (170, 100, 200, 100)
    old_profile_C = (170, 220, 200, 100)
    top_C = (170, 340, 200, 100)
