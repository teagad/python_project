import pygame
import time
from src.globals import Globals
pygame.init()

class Event():
    def hunger_death(self, tamagochik):
        basic_hunger = 20
        basic_happines = 20
        time_sleep = 5
        pygame.draw.rect(Globals.screen,
                         Globals.RectColor,
                         Globals.status_rect
                         )
        text_surface3 = Globals.base_font.render(
            "your Masha died ", True,
            Globals.Color_basic
        )
        text_surface4 = Globals.base_font.render(
            f"The game will end in {time_sleep} sec",
            True,
            Globals.Color_basic
        )
        Globals.screen.blit(text_surface3,
                            (
                                Globals.status_rect.x + Globals.first_line_x,
                                Globals.status_rect.y + Globals.first_line_y))
        Globals.screen.blit(text_surface4,
                            (Globals.status_rect.x + Globals.second_line_x,
                             Globals.status_rect.y + Globals.second_line_y))
        pygame.display.update()
        tamagochik.to_top()
        tamagochik.setinfo(
            Globals.Profile,
            Globals.winer,
            basic_hunger,
            basic_happines
        )
        time.sleep(time_sleep)
        Globals.Running = False

    def notice_about_hunger(self):
        pygame.draw.rect(Globals.screen,
                         Globals.RectColor, Globals.status_rect)
        text_surface3 = Globals.base_font.render(
            f"status:game started",
            True, Globals.Color_basic
        )
        text_surface4 = Globals.base_font.render(
            f"Masha stats will drop in a minute",
            True, Globals.Color_basic
        )
        text_surface2 = Globals.base_font.render(
            "i am hungry!",
            True, Globals.Color_basic
        )
        Globals.screen.blit(text_surface2,
                            (
                                Globals.status_rect.x + Globals.third_line_x,
                                Globals.status_rect.y + Globals.third_line_y))
        Globals.screen.blit(text_surface3,
                            (
                                Globals.status_rect.x + Globals.first_line_x,
                                Globals.status_rect.y + Globals.first_line_y))
        Globals.screen.blit(text_surface4,
                            (Globals.status_rect.x + Globals.second_line_x,
                             Globals.status_rect.y + Globals.second_line_y))

    def happines_death(self, tamagochik):
        basic_hunger = 20
        basic_happines = 20
        time_sleep = 5
        pygame.draw.rect(Globals.screen,
                         Globals.RectColor, Globals.status_rect)
        text_surface3 = Globals.base_font.render(
            "Your pet died from lonliness!", True,
            Globals.Color_basic
        )
        text_surface4 = Globals.base_font.render(
            f"The game will end in {time_sleep} sec", True,
            Globals.Color_basic
        )
        Globals.screen.blit(text_surface3,
                            (
                                Globals.status_rect.x + Globals.first_line_x,
                                Globals.status_rect.y + Globals.first_line_y))
        Globals.screen.blit(text_surface4,
                            (Globals.status_rect.x + Globals.second_line_x,
                             Globals.status_rect.y + Globals.second_line_y))
        pygame.display.update()
        tamagochik.to_top()
        tamagochik.setinfo(
            Globals.Profile,
            Globals.winer,
            basic_hunger,
            basic_happines
        )
        time.sleep(time_sleep)
        Globals.Running = False

    def very_borred(self):
        pygame.draw.rect(Globals.screen,
                         Globals.RectColor, Globals.status_rect)
        text_surface3 = Globals.base_font.render(
            f"status:game started",
            True, Globals.Color_basic
        )
        text_surface4 = Globals.base_font.render(
            f"Masha stats will drop in a minute",
            True, Globals.Color_basic
        )
        text_surface2 = Globals.base_font.render(
            "Nobody loves me!",
            True, Globals.Color_basic
        )
        Globals.screen.blit(text_surface2,
                            (
                                Globals.status_rect.x + Globals.third_line_x,
                                Globals.status_rect.y + Globals.third_line_y))
        Globals.screen.blit(text_surface3,
                            (
                                Globals.status_rect.x + Globals.first_line_x,
                                Globals.status_rect.y + Globals.first_line_y))
        Globals.screen.blit(text_surface4,
                            (Globals.status_rect.x + Globals.second_line_x,
                             Globals.status_rect.y + Globals.second_line_y))

    def borred(self):
        pygame.draw.rect(Globals.screen,
                         Globals.RectColor, Globals.status_rect)
        text_surface3 = Globals.base_font.render(
            f"status:game started",
            True, Globals.Color_basic
        )
        text_surface4 = Globals.base_font.render(
            f"Masha stats will drop in a minute",
            True, Globals.Color_basic
        )
        text_surface2 = Globals.base_font.render(
            "I’m bored!",
            True, Globals.Color_basic
        )
        Globals.screen.blit(text_surface2,
                            (
                                Globals.status_rect.x + Globals.third_line_x,
                                Globals.status_rect.y + Globals.third_line_y))
        Globals.screen.blit(text_surface3,
                            (
                                Globals.status_rect.x + Globals.first_line_x,
                                Globals.status_rect.y + Globals.first_line_y))
        Globals.screen.blit(text_surface4,
                            (Globals.status_rect.x + Globals.second_line_x,
                             Globals.status_rect.y + Globals.second_line_y))

    def all_fine(self):
        pygame.draw.rect(Globals.screen,
                         Globals.RectColor, Globals.status_rect)
        text_surface3 = Globals.base_font.render(
            f"status:game started",
            True, Globals.Color_basic
        )
        text_surface4 = Globals.base_font.render(
            f"Masha stats will drop in a minute",
            True, Globals.Color_basic
        )
        text_surface2 = Globals.base_font.render(
            "It`s all okay!",
            True, Globals.Color_basic
        )
        Globals.screen.blit(text_surface3,
                            (
                                Globals.status_rect.x + Globals.first_line_x,
                                Globals.status_rect.y + Globals.first_line_y))
        Globals.screen.blit(text_surface4,
                            (Globals.status_rect.x + Globals.second_line_x,
                             Globals.status_rect.y + Globals.second_line_y))
        Globals.screen.blit(text_surface2,
                            (
                                Globals.status_rect.x + Globals.third_line_x,
                                Globals.status_rect.y + Globals.third_line_y))

    def events(self, tamagochik, delta=None):
        try:
            delta_time = 60
            hunger_limit = 40
            happines_limit = 1
            if delta:
                if delta > delta_time:
                    hunger_time = 0
                    happy_time = 0
                    iteracions = int(delta / delta_time)
                    remainder = delta - delta_time * iteracions
                    tamagochik.time = time.time() - remainder
                    tamagochik.hunger += int(delta / delta_time)
                    delta1 = time.time() - tamagochik.time
                    if tamagochik.hunger >= hunger_limit:
                        t = tamagochik.hunger - hunger_limit
                        tamagochik.hunger = hunger_limit
                        hunger_time = delta1 + t * delta_time
                    tamagochik.happines -= int(delta / delta_time)
                    if tamagochik.happines <= happines_limit:
                        t = -tamagochik.happines + happines_limit
                        tamagochik.happines = happines_limit
                        happy_time = delta1 + t * delta_time
                    if max(hunger_time, happy_time):
                        tamagochik.date_of_birth += max(hunger_time, happy_time)
                        return
            else:
                bored = 7
                vary_hungry = 30
                vary_bored = 5
                hunger_decrease = 1
                happines_decrease = 1
                delta = time.time() - tamagochik.time
                if delta > delta_time:
                    tamagochik.time = time.time()
                    tamagochik.hunger += hunger_decrease
                    tamagochik.happines -= happines_decrease
                    if tamagochik.happines > bored and \
                            tamagochik.hunger < vary_hungry:
                        self.all_fine()
                if tamagochik.hunger >= hunger_limit:
                    self.hunger_death(tamagochik)
                elif tamagochik.hunger >= vary_hungry:
                    self.notice_about_hunger()
                elif tamagochik.happines <= happines_limit:
                    self.happines_death(tamagochik)
                elif tamagochik.happines <= vary_bored:
                    self.very_borred()
                elif tamagochik.happines <= bored:
                    self.borred()
        except NameError:
            pass
