import time
from numpy import sort
import pygame
from src.globals import Globals
from src.main_realization import Realization
from src.main_logic import Game_logic
pygame.init()

class Menu:
    def __init__(self):
        self.screen = ""
        self.screen_set()
        self.menu_event_loop()

    def screen_set(self):
        black = (0, 0, 0)
        silver = (192, 192, 192)
        button_font = pygame.font.Font(None, 32)

        new_profile_text = "New profile"
        new_profile_text_surface = button_font.render(new_profile_text,
                                                      True, black)
        display_size = (700, 500)

        old_profile_text = "Old profile"
        old_profile_text_surface = button_font.render(old_profile_text,
                                                      True, black)
        top_text = "Top of tamagochi"
        top_text_surface = button_font.render(top_text,
                                              True, black)
        x = 15
        y = 30
        self.screen = pygame.display.set_mode(display_size)
        self.screen.blit(Globals.BackGround.image, Globals.BackGround.rect)
        pygame.display.set_caption("menu")
        pygame.draw.rect(self.screen, (silver), Globals.new_profile_C)
        pygame.draw.rect(self.screen, (silver), Globals.old_profile_C)
        pygame.draw.rect(self.screen, (silver), Globals.top_C)
        self.screen.blit(new_profile_text_surface, (
            Globals.new_profile_C[0] + x, Globals.new_profile_C[1] + y))
        self.screen.blit(old_profile_text_surface, (
            Globals.old_profile_C[0] + x, Globals.old_profile_C[1] + y))
        self.screen.blit(top_text_surface, (
            Globals.top_C[0] + x, Globals.top_C[1] + y))
        pygame.display.flip()

    def top_tamagochi(self):
        display_size = (500, 500)
        self.screen = pygame.display.set_mode(display_size)
        self.screen.blit(Globals.BackGround.image, Globals.BackGround.rect)
        # try:
        array = []
        profiles = []
        try:
            with open('top.txt', 'r') as f:
                for lines in f:
                    if lines != "\n":
                        profiles += [lines.split()[0]]
                        array += [lines.split()[1]]
                array = [*map(float, array)]
                arrays = [(b, a) for b, a in sorted(zip(array, profiles))]
                array, profiles = zip(*arrays)
                my_font = pygame.font.SysFont('Comic Sans MS', 45)
                start = [0, 0]
                step = 30
                count = 1
                for top_elem, profile in zip(array[::-1], profiles[::-1]):
                    format_float = "{:.2f}".format(top_elem)
                    text = f"{count} : {profile}-{format_float} minutes"
                    text_surface = my_font.render(text, False, (0, 0, 0))
                    self.screen.blit(text_surface, (start[0], start[1]))
                    start[1] += step
                    count += 1
                text = "will close in 5 sec."
                text_surface = my_font.render(text, False, (0, 0, 0))
                self.screen.blit(text_surface, start)
        except Exception:
            start = [0, 0]
            my_font = pygame.font.SysFont('Comic Sans MS', 45)
            text = "Top is empty will close in 5 sec."
            text_surface = my_font.render(text, False, (0, 0, 0))
            self.screen.blit(text_surface, start)

        pygame.display.flip()
        time.sleep(5)
        self.screen_set()
        self.menu_event_loop()

    def mouse_posesion(self):
        real = Realization()
        game = Game_logic()
        if pygame.mouse.get_pos()[0] >= Globals.new_profile_C[0] \
                and pygame.mouse.get_pos()[1] >= Globals.new_profile_C[1]:
            if pygame.mouse.get_pos()[0] <= \
                    Globals.new_profile_C[0] + Globals.new_profile_C[2] \
                    and pygame.mouse.get_pos()[1] <= \
                    Globals.new_profile_C[1] + Globals.new_profile_C[3]:
                if real.check_profiles_count():
                    real.start_new_profile()
                    return 0
        if pygame.mouse.get_pos()[0] >= Globals.old_profile_C[0] \
                and pygame.mouse.get_pos()[1] >= Globals.old_profile_C[1]:
            if pygame.mouse.get_pos()[0] <= \
                    Globals.old_profile_C[0] + Globals.old_profile_C[2] \
                    and pygame.mouse.get_pos()[1] <= \
                    Globals.old_profile_C[1] + Globals.old_profile_C[3]:
                if game.print_all_profiles():
                    real.start_old_profile()
                    return 0
        if pygame.mouse.get_pos()[0] >= Globals.top_C[0] \
                and pygame.mouse.get_pos()[1] >= Globals.top_C[1]:
            if pygame.mouse.get_pos()[0] <= \
                    Globals.top_C[0] + Globals.top_C[2] \
                    and pygame.mouse.get_pos()[1] <= \
                    Globals.top_C[1] + Globals.top_C[3]:
                self.top_tamagochi()
                return 0
        return 1

    def menu_event_loop(self):
        menuAtivo = True
        while menuAtivo:
            for evento in pygame.event.get():
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    menuAtivo = self.mouse_posesion()

                if evento.type == pygame.QUIT:
                    menuAtivo = False
            pygame.display.update()
