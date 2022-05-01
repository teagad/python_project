import time
import pickle
import pygame
from src.background import Background
from src.events import Event
from src.globals import Globals
from src.tamagochi import Tamagochi


# imported module
pygame.init()


class Game_logic():
    """Хранит в себе логику самой игры
    
    1)Имеет методы
    update_screen

    print_all_profiles (Печатает профили игрока)

    check_choosing_tamagochi (Смотрит на какой тамагочи кликнул игрок)

    draw_background (Рисует задний фон)

    place_tamagochi_picture (Располагает картинку тамагочи который выиграл на экран)

    making_textbox (Создание текстбоксов)

    render_textboxes (Вывод текст боксов на экран)

    hunger_button_pressed (При нажатия на кнопку покормить опускает голод на 3)

    live_button_pressed (При нажати на кнопку live начинает игру)

    button_happy (При нажатия на кнопку обнять опускает голод на 3)

    update_game(Обновляет экран(меняет голод и радость))

    mouse_is_hovered_on_button (При наводки на кнопку меняет цвет)
    
    """

    def update_screen(self):
        """Обновляет экран"""
        pygame.display.update()

    def print_all_profiles(self):
        """Печатает профили игрока

                Возвращаемое значение:
                    Возвращает 1 если существуют старые аккаунты,иначе 0
        """
        profiles_str = []
        black = (0, 0, 0)
        profile_array_rect = pygame.Rect(0, 0, 200, 64)
        try:
            with open('data.pickle', 'rb') as f:
                dic = pickle.load(f)
                print(dic)
                for profile in dic.items():
                    if profile[0][0] not in profiles_str:
                        profiles_str += [profile[0][0]]
                str = ",".join(profiles_str)
                profile_array = f'Profiles : {str}'
                profile_array_text_surface = Globals.profile_text_font.render(
                    profile_array, True,
                    black
                )
                Globals.screen.blit(
                    profile_array_text_surface,
                    profile_array_rect
                )
            return 1
        except Exception:
            profile_array = f'Profiles : it`s empty now'
            profile_array_text_surface = Globals.profile_text_font.render(
                profile_array, True,
                Globals.color_basic
            )
            Globals.screen.blit(
                profile_array_text_surface,
                profile_array_rect
            )
            return 0

    def check_choosing_tamagochi(self, mouse):
        """Смотрит на какой тамагочи кликнул игрок

                Параметры: 
                     mouse: Позиция мышки

                Возвращаемое значение:
                    running(bool): True если тамагочи не выбрали иначе False
        
        """
        running = True
        first_tamagochi_coordinate_x = 0
        second_tamagochi_coordinate_x = 200
        third_tamagochi_coordinate_x = 400
        coordinate_y = 100
        if first_tamagochi_coordinate_x <= mouse[0] <= \
                first_tamagochi_coordinate_x + \
                Globals.tamagochisize[0] and coordinate_y <= \
                mouse[1] <= \
                coordinate_y + Globals.tamagochisize[1]:
            Globals.winer = Globals.tamagochis["tamagochi1"]
            running = False
        if second_tamagochi_coordinate_x <= mouse[0] <= \
                second_tamagochi_coordinate_x + \
                Globals.tamagochisize[0] and coordinate_y <= \
                mouse[1] <= coordinate_y + Globals.tamagochisize[1]:
            Globals.winer = Globals.tamagochis["tamagochi2"]
            running = False
        if third_tamagochi_coordinate_x <= mouse[0] <= \
                third_tamagochi_coordinate_x + \
                Globals.tamagochisize[0] and coordinate_y <= \
                mouse[1] <= \
                coordinate_y + Globals.tamagochisize[1]:
            Globals.winer = Globals.tamagochis["tamagochi3"]
            running = False
        return running

    def draw_background(self):
        """Рисует задний фон"""
        back_ground = Background('assets/background_image.png', [0, 0])
        Globals.screen.blit(back_ground.image, back_ground.rect)

    def place_tamagochi_picture(self):
        """Располагает картинку тамагочи который выиграл на экран"""
        tmagochi_coordinates = (100, 400)
        image = pygame.image.load(Globals.winer)
        image = pygame.transform.scale(image, Globals.tamagochisize)
        Globals.screen.blit(image, tmagochi_coordinates)

    def making_textbox(self):
        """Создание текстбоксов"""
        pygame.draw.rect(
            Globals.screen,
            Globals.rectColor,
            Globals.happines_rect
        )
        pygame.draw.rect(
            Globals.screen,
            Globals.rectColor,
            Globals.hunger_rect
        )
        pygame.draw.rect(
            Globals.screen,
            Globals.rectColor,
            Globals.status_rect
        )

    def render_textboxes(self):
        """Вывод текст боксов на экран"""
        Globals.screen.blit(
            Globals.happines_text_surface, (
                Globals.happines_rect.x + Globals.first_line_x,
                Globals.happines_rect.y + Globals.first_line_y
            )
        )
        Globals.screen.blit(Globals.hunger_text_surface, (
            Globals.hunger_rect.x + Globals.first_line_x,
            Globals.hunger_rect.y + Globals.first_line_y))
        Globals.screen.blit(Globals.status_text_surface, (
            Globals.status_rect.x + Globals.first_line_x,
            Globals.status_rect.y + Globals.first_line_y))

    def hunger_button_pressed(self, tamagochik):
        """При нажатия на кнопку покормить опускает голод на 3
        
            Параметры: 
                tamagochik(Tamagochi): Наш тамагочи
        """
        try:
            hunger_decrease_by_click = 3
            if tamagochik.hunger >= hunger_decrease_by_click:
                tamagochik.hunger -= hunger_decrease_by_click
            else:
                pygame.draw.rect(
                    Globals.screen,
                    Globals.rectColor,
                    Globals.status_rect
                )
                text_surface3 = Globals.base_font.render(
                    f"status:game started",
                    True, Globals.color_basic
                )
                text_surface4 = Globals.base_font.render(
                    f"Masha stats will drop in a minute", True,
                    Globals.color_basic
                )
                Globals.hunger_text_surface = Globals.base_font.render(
                    "I am not hungry",
                    True, Globals.color_basic
                )
                Globals.screen.blit(Globals.hunger_text_surface, (
                    Globals.status_rect.x + Globals.third_line_x,
                    Globals.status_rect.y + Globals.third_line_y
                )
                                    )
                Globals.screen.blit(text_surface3, (
                    Globals.status_rect.x + Globals.first_line_x,
                    Globals.status_rect.y + Globals.first_line_y
                )
                                    )
                Globals.screen.blit(text_surface4, (
                    Globals.status_rect.x + Globals.second_line_x,
                    Globals.status_rect.y + Globals.second_line_y
                )
                                    )
        except NameError:
            pass

    def live_button_pressed(self):
        """При нажати на кнопку live начинает игру И создаёт тамагочи

            Возвращаемое значение:
                tamagochik(Tamagochi): Наш тамагочи
        """
        tamagochik = Tamagochi()
        tamagochik.getinfo(Globals.profile, Globals.winer)
        tamagochik.time = time.time()
        eve = Event()
        eve.events(tamagochik,
                   tamagochik.coverter(time.ctime().split()[3]) - tamagochik.date)
        # hunger
        pygame.draw.rect(Globals.screen,
                         Globals.rectColor, Globals.hunger_rect)
        Globals.hunger_text_surface = Globals.base_font.render(
            f"hunger:{tamagochik.hunger}",
            True, Globals.color_basic)
        coords = (Globals.hunger_rect.x + Globals.first_line_x,
                  Globals.hunger_rect.y + Globals.first_line_y)
        Globals.screen.blit(Globals.hunger_text_surface, coords)

        # happines
        pygame.draw.rect(Globals.screen,
                         Globals.rectColor, Globals.happines_rect)
        Globals.happines_text_surface = Globals.base_font.render(
            f"happines:{tamagochik.happines}", True,
            Globals.color_basic)
        Globals.screen.blit(Globals.happines_text_surface, (
            Globals.happines_rect.x + Globals.first_line_x,
            Globals.happines_rect.y + Globals.first_line_y))
        # status
        pygame.draw.rect(Globals.screen,
                         Globals.rectColor, Globals.status_rect)
        text_surface3 = Globals.base_font.render(
            f"status:game started", True, Globals.color_basic)
        text_surface4 = Globals.base_font.render(
            f"Masha stats will drop in a minute", True, Globals.color_basic)
        Globals.screen.blit(text_surface3, (
            Globals.status_rect.x + Globals.first_line_x,
            Globals.status_rect.y + Globals.first_line_y))
        Globals.screen.blit(text_surface4, (
            Globals.status_rect.x + Globals.second_line_x,
            Globals.status_rect.y + Globals.second_line_y))
        return tamagochik

    def button_happy(self, tamagochik):
        """При нажатия на кнопку обнять опускает голод на 3
            Параметры: 
                tamagochik(Tamagochi): Наш тамагочи
        
        """
        try:
            happines_limit_top = 20
            happines_increase_by_click = 3
            if tamagochik.happines <= \
                    happines_limit_top - happines_increase_by_click:
                tamagochik.happines += happines_increase_by_click
            else:
                pygame.draw.rect(Globals.screen,
                                 Globals.rectColor, Globals.status_rect)
                text_surface3 = Globals.base_font.render(
                    f"status:game started",
                    True, Globals.color_basic)
                text_surface4 = Globals.base_font.render(
                    f"Masha stats will drop in a minute",
                    True, Globals.color_basic)
                Globals.hunger_text_surface = Globals.base_font.render(
                    "I am not borred boss", True,
                    Globals.color_basic)
                Globals.screen.blit(Globals.hunger_text_surface, (
                    Globals.status_rect.x + Globals.third_line_x,
                    Globals.status_rect.y + Globals.third_line_y))
                Globals.screen.blit(text_surface3, (
                    Globals.status_rect.x + Globals.first_line_x,
                    Globals.status_rect.y + Globals.first_line_y))
                Globals.screen.blit(text_surface4, (
                    Globals.status_rect.x + Globals.second_line_x,
                    Globals.status_rect.y + Globals.second_line_y))
        except NameError:
            pass

    def update_game(self, tamagochik):
        """Обновляет экран(меняет голод и радость)
            Параметры: 
                tamagochik(Tamagochi): Наш тамагочи
        """
        pygame.draw.rect(Globals.screen,
                         Globals.rectColor, Globals.hunger_rect)
        Globals.hunger_text_surface = Globals.base_font.render(
            f"hunger:{tamagochik.hunger}", True, Globals.color_basic)
        Globals.screen.blit(Globals.hunger_text_surface, (
            Globals.hunger_rect.x + Globals.first_line_x,
            Globals.hunger_rect.y + Globals.first_line_y))

        pygame.draw.rect(Globals.screen,
                         Globals.rectColor, Globals.happines_rect)
        Globals.happines_text_surface = Globals.base_font.render(
            f"happines:{tamagochik.happines}", True,
            Globals.color_basic)
        Globals.screen.blit(Globals.happines_text_surface, (
            Globals.happines_rect.x + Globals.first_line_x,
            Globals.happines_rect.y + Globals.first_line_y))

    def mouse_is_hovered_on_button(self, mouse):
        """При наводки на кнопку меняет цвет

            Параметры: 
                mouse: Позиция мышки
        """
        for x, y, text in zip(
                [Globals.button_x1, Globals.button_x2, Globals.button_x3],
                [Globals.button_y1, Globals.button_y2, Globals.button_y3],
                [Globals.button_text1, Globals.button_text2, Globals.button_text3]):
            if x <= mouse[0] <= x + Globals.width and y <= mouse[1] <= \
                    y + Globals.height:
                color_light = (170, 170, 170)
                pygame.draw.rect(
                    Globals.screen, color_light,
                    [x, y, Globals.width, Globals.height])

            else:
                color_dark = (100, 100, 100)
                pygame.draw.rect(
                    Globals.screen,
                    color_dark, [x, y, Globals.width, Globals.height])
            # superimposing the text onto our button
            Globals.screen.blit(text, (x, y))
