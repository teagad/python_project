import time
import pickle
import pygame
from src.tamagochi import Tamagochi
from src.globals import Globals

# imported module
pygame.init()


class Game_logic():
    def update_screen(self):
        pygame.display.update()

    def print_all_profiles(self):
        profiles_str = []
        black = (0, 0, 0)
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
                    Globals.Profile_array_rect
                )
            return 1
        except Exception:
            profile_array = f'Profiles : it`s empty now'
            profile_array_text_surface = Globals.profile_text_font.render(
                profile_array, True,
                Globals.Color_basic
            )
            Globals.screen.blit(
                profile_array_text_surface,
                Globals.Profile_array_rect
            )
            return 0

    def check_choosing_tamagochi(self, mouse):
        running = True
        if Globals.first_tamagochi_coordinate_x <= mouse[0] <= \
                Globals.first_tamagochi_coordinate_x + \
                Globals.tamagochisize[0] and Globals.coordinate_y <= \
                mouse[1] <= \
                Globals.coordinate_y + Globals.tamagochisize[1]:
            Globals.winer = Globals.tamagochis["tamagochi1"]
            running = False
        if Globals.second_tamagochi_coordinate_x <= mouse[0] <= \
                Globals.second_tamagochi_coordinate_x + \
                Globals.tamagochisize[0] and Globals.coordinate_y <= \
                mouse[1] <= Globals.coordinate_y + Globals.tamagochisize[1]:
            Globals.winer = Globals.tamagochis["tamagochi2"]
            running = False
        if Globals.third_tamagochi_coordinate_x <= mouse[0] <= \
                Globals.third_tamagochi_coordinate_x + \
                Globals.tamagochisize[0] and Globals.coordinate_y <= \
                mouse[1] <= \
                Globals.coordinate_y + Globals.tamagochisize[1]:
            Globals.winer = Globals.tamagochis["tamagochi3"]
            running = False
        return running

    def draw_background(self):
        Globals.screen.blit(Globals.BackGround.image, Globals.BackGround.rect)

    def place_tamagochi_picture(self):
        image = pygame.image.load(Globals.winer)
        image = pygame.transform.scale(image, Globals.tamagochisize)
        Globals.screen.blit(image, Globals.tmagochi_coordinates)

    def making_textbox(self):
        pygame.draw.rect(
            Globals.screen,
            Globals.RectColor,
            Globals.happines_rect
        )
        pygame.draw.rect(
            Globals.screen,
            Globals.RectColor,
            Globals.hunger_rect
        )
        pygame.draw.rect(
            Globals.screen,
            Globals.RectColor,
            Globals.status_rect
        )

    def render_textboxes(self):
        Globals.screen.blit(
            Globals.happines_text_surface, (
                Globals.happines_rect.x + Globals.first_line_x,
                Globals.happines_rect.y + Globals.first_line_y
            )
        )
        Globals.screen.blit(Globals.hunger_text_surface,
                            (
                                Globals.hunger_rect.x + Globals.first_line_x,
                                Globals.hunger_rect.y + Globals.first_line_y))
        Globals.screen.blit(Globals.status_text_surface,
                            (
                                Globals.status_rect.x + Globals.first_line_x,
                                Globals.status_rect.y + Globals.first_line_y))

    def hunger_button_pressed(self, tamagochik):
        try:
            if tamagochik.hunger >= Globals.hunger_decrease_by_click:
                tamagochik.hunger -= Globals.hunger_decrease_by_click
            else:
                pygame.draw.rect(
                    Globals.screen,
                    Globals.RectColor,
                    Globals.status_rect
                )
                text_surface3 = Globals.base_font.render(
                    f"status:game started",
                    True, Globals.Color_basic
                )
                text_surface4 = Globals.base_font.render(
                    f"Masha stats will drop in a minute", True,
                    Globals.Color_basic
                )
                Globals.hunger_text_surface = Globals.base_font.render(
                    "I am not hungry",
                    True, Globals.Color_basic
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
        tamagochik = Tamagochi()
        tamagochik.getinfo(Globals.Profile, Globals.winer)
        tamagochik.time = time.time()
        self.events(tamagochik,
                    tamagochik.coverter(time.ctime().split()[3]) - tamagochik.date)
        # hunger
        pygame.draw.rect(Globals.screen,
                         Globals.RectColor, Globals.hunger_rect)
        Globals.hunger_text_surface = Globals.base_font.render(
            f"hunger:{tamagochik.hunger}",
            True, Globals.Color_basic)
        Globals.screen.blit(Globals.hunger_text_surface,
                            (
                                Globals.hunger_rect.x + Globals.first_line_x,
                                Globals.hunger_rect.y + Globals.first_line_y))
        # happines
        pygame.draw.rect(Globals.screen,
                         Globals.RectColor, Globals.happines_rect)
        Globals.happines_text_surface = Globals.base_font.render(
            f"happines:{tamagochik.happines}", True,
            Globals.Color_basic)
        Globals.screen.blit(Globals.happines_text_surface, (
            Globals.happines_rect.x + Globals.first_line_x,
            Globals.happines_rect.y + Globals.first_line_y))
        # status
        pygame.draw.rect(Globals.screen,
                         Globals.RectColor, Globals.status_rect)
        text_surface3 = Globals.base_font.render(
            f"status:game started", True, Globals.Color_basic)
        text_surface4 = Globals.base_font.render(
            f"Masha stats will drop in a minute", True, Globals.Color_basic)
        Globals.screen.blit(text_surface3,
                            (
                                Globals.status_rect.x + Globals.first_line_x,
                                Globals.status_rect.y + Globals.first_line_y))
        Globals.screen.blit(text_surface4,
                            (Globals.status_rect.x + Globals.second_line_x,
                             Globals.status_rect.y + Globals.second_line_y))
        return tamagochik

    def button_happy(self, tamagochik):
        try:
            if tamagochik.happines <= \
                    Globals.happines_limit_top - Globals.happines_increase_by_click:
                tamagochik.happines += Globals.happines_increase_by_click
            else:
                pygame.draw.rect(Globals.screen,
                                 Globals.RectColor, Globals.status_rect)
                text_surface3 = Globals.base_font.render(
                    f"status:game started",
                    True, Globals.Color_basic)
                text_surface4 = Globals.base_font.render(
                    f"Masha stats will drop in a minute",
                    True, Globals.Color_basic)
                Globals.hunger_text_surface = Globals.base_font.render(
                    "I am not borred boss", True,
                    Globals.Color_basic)
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
        x = tamagochik.hunger
        pygame.draw.rect(Globals.screen,
                         Globals.RectColor, Globals.hunger_rect)
        Globals.hunger_text_surface = Globals.base_font.render(
            f"hunger:{tamagochik.hunger}", True, Globals.Color_basic)
        Globals.screen.blit(Globals.hunger_text_surface,
                            (
                                Globals.hunger_rect.x + Globals.first_line_x,
                                Globals.hunger_rect.y + Globals.first_line_y))

        pygame.draw.rect(Globals.screen,
                         Globals.RectColor, Globals.happines_rect)
        Globals.happines_text_surface = Globals.base_font.render(
            f"happines:{tamagochik.happines}", True,
            Globals.Color_basic)
        Globals.screen.blit(Globals.happines_text_surface, (
            Globals.happines_rect.x + Globals.first_line_x,
            Globals.happines_rect.y + Globals.first_line_y))

    def mouse_is_hovered_on_button(self, mouse):
        for x, y, text in zip(
                [Globals.button_x1, Globals.button_x2, Globals.button_x3],
                [Globals.button_y1, Globals.button_y2, Globals.button_y3],
                [Globals.button_text1, Globals.button_text2, Globals.button_text3]):
            if x <= mouse[0] <= x + Globals.width and y <= mouse[1] <= \
                    y + Globals.height:
                pygame.draw.rect(Globals.screen,
                                 Globals.color_light, [x, y, Globals.width, Globals.height])

            else:
                pygame.draw.rect(Globals.screen,
                                 Globals.color_dark, [x, y, Globals.width, Globals.height])
            # superimposing the text onto our button
            Globals.screen.blit(text, (x, y))
