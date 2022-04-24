import time
import pygame
from tamagochi import tamagochi
from globals import Globals
import pickle

# imported module
pygame.init()

# title
pygame.display.set_caption("Russian Tamagochi")


class Game_logic():
    def update_screen(self):
        pygame.display.update()

    def print_all_profiles(self):
        profiles_str = []
        try:
            with open('data.pickle', 'rb') as f:
                dic = pickle.load(f)
                print(dic)
                for profile in dic.items():
                    if profile[0][0] not in profiles_str:
                        profiles_str += [profile[0][0]]
                str = ",".join(profiles_str)
                Profile_array = f'Profiles : {str}'
                Profile_array_text_surface = Globals.base_font.render(Profile_array, True, Globals.Color_basic)
                Globals.screen.blit(Profile_array_text_surface, Globals.Profile_array_rect)
        except:
            Profile_array = f'Profiles : it`s empty now'
            Profile_array_text_surface = Globals.base_font.render(Profile_array, True, Globals.Color_basic)
            Globals.screen.blit(Profile_array_text_surface, Globals.Profile_array_rect)

    # choosing tamagochi
    def choosing_tamagochi(self):
        Globals.screen.blit(Globals.BackGround.image, Globals.BackGround.rect)
        Globals.screen.blit(Globals.Profile_text_surface, Globals.Profile_rect)
        for animal, coord in zip(Globals.tamagochis.values(), Globals.tamagochi_coords):
            image = pygame.image.load(animal)
            image = pygame.transform.scale(image, Globals.tamagochisize)
            Globals.screen.blit(image, coord)

    def event_loop_of_choosing_tamagochi(self):
        Running = True
        self.print_all_profiles()
        while Running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Running = False
                x = Globals.input_box1.handle_event(event)
                if x: Globals.Profile = x
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Globals.first_tamagochi_coordinate_x <= mouse[0] <= Globals.first_tamagochi_coordinate_x + \
                            Globals.tamagochisize[
                                0] and Globals.coordinate_y <= mouse[1] <= Globals.coordinate_y + Globals.tamagochisize[
                        1]:
                        Globals.winer = Globals.tamagochis["tamagochi1"]
                        Running = False
                    if Globals.second_tamagochi_coordinate_x <= mouse[0] <= Globals.second_tamagochi_coordinate_x + \
                            Globals.tamagochisize[
                                0] and Globals.coordinate_y <= mouse[1] <= Globals.coordinate_y + Globals.tamagochisize[
                        1]:
                        Globals.winer = Globals.tamagochis["tamagochi2"]
                        Running = False
                    if Globals.third_tamagochi_coordinate_x <= mouse[0] <= Globals.third_tamagochi_coordinate_x + \
                            Globals.tamagochisize[
                                0] and Globals.coordinate_y <= mouse[1] <= Globals.coordinate_y + Globals.tamagochisize[
                        1]:
                        Globals.winer = Globals.tamagochis["tamagochi3"]
                        Running = False
                Globals.input_box1.update()
                pygame.draw.rect(Globals.screen, (Globals.Colordelete), Globals.input_box1.rect)
                Globals.input_box1.draw(Globals.screen)
                self.update_screen
            mouse = pygame.mouse.get_pos()

    def draw_background(self):
        Globals.screen.blit(Globals.BackGround.image, Globals.BackGround.rect)

    def place_tamagochi_picture(self):
        image = pygame.image.load(Globals.winer)
        image = pygame.transform.scale(image, Globals.tamagochisize)
        Globals.screen.blit(image, Globals.tmagochi_coordinates)

    def making_textbox(self):
        pygame.draw.rect(Globals.screen, Globals.RectColor, Globals.happines_rect)
        pygame.draw.rect(Globals.screen, Globals.RectColor, Globals.hunger_rect)
        pygame.draw.rect(Globals.screen, Globals.RectColor, Globals.status_rect)

    def render_textboxes(self):
        Globals.screen.blit(Globals.happines_text_surface, (
            Globals.happines_rect.x + Globals.first_line_x, Globals.happines_rect.y + Globals.first_line_y))
        Globals.screen.blit(Globals.hunger_text_surface,
                            (
                                Globals.hunger_rect.x + Globals.first_line_x,
                                Globals.hunger_rect.y + Globals.first_line_y))
        Globals.screen.blit(Globals.status_text_surface,
                            (
                                Globals.status_rect.x + Globals.first_line_x,
                                Globals.status_rect.y + Globals.first_line_y))

    def hunger_death(self, tamagochik):
        pygame.draw.rect(Globals.screen, Globals.RectColor, Globals.status_rect)
        text_surface3 = Globals.base_font.render("your Masha died ", True,
                                                 Globals.Color_basic)
        text_surface4 = Globals.base_font.render(f"The game will end in {Globals.time_sleep} sec", True,
                                                 Globals.Color_basic)
        Globals.screen.blit(text_surface3,
                            (
                                Globals.status_rect.x + Globals.first_line_x,
                                Globals.status_rect.y + Globals.first_line_y))
        Globals.screen.blit(text_surface4,
                            (Globals.status_rect.x + Globals.second_line_x,
                             Globals.status_rect.y + Globals.second_line_y))
        self.update_screen()
        tamagochik.setinfo(Globals.Profile, Globals.winer, Globals.basic_hunger, Globals.basic_happines)
        time.sleep(Globals.time_sleep)
        Globals.Running = False

    def notice_about_hunger(self):
        pygame.draw.rect(Globals.screen, Globals.RectColor, Globals.status_rect)
        text_surface3 = Globals.base_font.render(f"status:game started", True, Globals.Color_basic)
        text_surface4 = Globals.base_font.render(f"Masha stats will drop in a minute", True, Globals.Color_basic)
        text_surface2 = Globals.base_font.render("i am hungry!", True, Globals.Color_basic)
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
        pygame.draw.rect(Globals.screen, Globals.RectColor, Globals.status_rect)
        text_surface3 = Globals.base_font.render("Your pet died from lonliness!", True,
                                                 Globals.Color_basic)
        text_surface4 = Globals.base_font.render(f"The game will end in {Globals.time_sleep} sec", True,
                                                 Globals.Color_basic)
        Globals.screen.blit(text_surface3,
                            (
                                Globals.status_rect.x + Globals.first_line_x,
                                Globals.status_rect.y + Globals.first_line_y))
        Globals.screen.blit(text_surface4,
                            (Globals.status_rect.x + Globals.second_line_x,
                             Globals.status_rect.y + Globals.second_line_y))
        self.update_screen(self)
        tamagochik.setinfo(Globals.Profile, Globals.winer, Globals.basic_hunger, Globals.basic_happines)
        time.sleep(Globals.time_sleep)
        Globals.Running = False

    def very_borred(self):
        pygame.draw.rect(Globals.screen, Globals.RectColor, Globals.status_rect)
        text_surface3 = Globals.base_font.render(f"status:game started", True, Globals.Color_basic)
        text_surface4 = Globals.base_font.render(f"Masha stats will drop in a minute", True, Globals.Color_basic)
        text_surface2 = Globals.base_font.render("Nobody loves me!", True, Globals.Color_basic)
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
        pygame.draw.rect(Globals.screen, Globals.RectColor, Globals.status_rect)
        text_surface3 = Globals.base_font.render(f"status:game started", True, Globals.Color_basic)
        text_surface4 = Globals.base_font.render(f"Masha stats will drop in a minute", True, Globals.Color_basic)
        text_surface2 = Globals.base_font.render("I’m bored!", True, Globals.Color_basic)
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
        pygame.draw.rect(Globals.screen, Globals.RectColor, Globals.status_rect)
        text_surface3 = Globals.base_font.render(f"status:game started", True, Globals.Color_basic)
        text_surface4 = Globals.base_font.render(f"Masha stats will drop in a minute", True, Globals.Color_basic)
        text_surface2 = Globals.base_font.render("It`s all okay!", True, Globals.Color_basic)
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
            if delta != None:
                if delta > Globals.delta_time:
                    tamagochik.time = time.time() - (delta - Globals.delta_time * int(delta / Globals.delta_time))
                    tamagochik.hunger += int(delta / Globals.delta_time)
                    tamagochik.happines -= int(delta / Globals.delta_time)
            else:
                delta = time.time() - tamagochik.time
                if delta > Globals.delta_time:
                    tamagochik.time = time.time()
                    tamagochik.hunger += Globals.hunger_decrease
                    tamagochik.happines -= Globals.happines_decrease
                    if tamagochik.happines > Globals.bored and tamagochik.hunger < Globals.vary_hungry:
                        self.all_fine()
                if tamagochik.hunger > Globals.hunger_limit:
                    self.hunger_death(tamagochik)
                elif tamagochik.hunger > Globals.vary_hungry:
                    self.notice_about_hunger()
                elif tamagochik.happines < Globals.happines_limit:
                    self.happines_death(tamagochik)
                elif tamagochik.happines < Globals.vary_bored:
                    self.very_borred()
                elif tamagochik.happines < Globals.bored:
                    self.borred()
        except NameError:
            pass

    def hunger_button_pressed(self, tamagochik):
        try:
            if tamagochik.hunger >= Globals.hunger_decrease_by_click:
                tamagochik.hunger -= Globals.hunger_decrease_by_click
            else:
                pygame.draw.rect(Globals.screen, Globals.RectColor, Globals.status_rect)
                text_surface3 = Globals.base_font.render(f"status:game started", True, Globals.Color_basic)
                text_surface4 = Globals.base_font.render(f"Masha stats will drop in a minute", True,
                                                         Globals.Color_basic)
                Globals.hunger_text_surface = Globals.base_font.render("I am not hungry", True, Globals.Color_basic)
                Globals.screen.blit(Globals.hunger_text_surface, (
                    Globals.status_rect.x + Globals.third_line_x, Globals.status_rect.y + Globals.third_line_y))
                Globals.screen.blit(text_surface3, (
                    Globals.status_rect.x + Globals.first_line_x, Globals.status_rect.y + Globals.first_line_y))
                Globals.screen.blit(text_surface4, (
                    Globals.status_rect.x + Globals.second_line_x, Globals.status_rect.y + Globals.second_line_y))
        except NameError:
            pass

    def live_button_pressed(self):
        tamagochik = tamagochi()
        tamagochik.getinfo(Globals.Profile, Globals.winer)
        tamagochik.time = time.time()
        self.events(tamagochik, tamagochik.coverter(time.ctime().split()[3]) - tamagochik.date)
        # hunger
        pygame.draw.rect(Globals.screen, Globals.RectColor, Globals.hunger_rect)
        Globals.hunger_text_surface = Globals.base_font.render(f"hunger:{tamagochik.hunger}", True, Globals.Color_basic)
        Globals.screen.blit(Globals.hunger_text_surface,
                            (
                                Globals.hunger_rect.x + Globals.first_line_x,
                                Globals.hunger_rect.y + Globals.first_line_y))
        # happines
        pygame.draw.rect(Globals.screen, Globals.RectColor, Globals.happines_rect)
        Globals.happines_text_surface = Globals.base_font.render(f"happines:{tamagochik.happines}", True,
                                                                 Globals.Color_basic)
        Globals.screen.blit(Globals.happines_text_surface, (
            Globals.happines_rect.x + Globals.first_line_x, Globals.happines_rect.y + Globals.first_line_y))
        # status
        pygame.draw.rect(Globals.screen, Globals.RectColor, Globals.status_rect)
        text_surface3 = Globals.base_font.render(f"status:game started", True, Globals.Color_basic)
        text_surface4 = Globals.base_font.render(f"Masha stats will drop in a minute", True, Globals.Color_basic)
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
            if tamagochik.happines <= Globals.happines_limit - Globals.happines_increase_by_click:
                tamagochik.happines += Globals.happines_increase_by_click
            else:
                pygame.draw.rect(Globals.screen, Globals.RectColor, Globals.status_rect)
                text_surface3 = Globals.base_font.render(f"status:game started", True, Globals.Color_basic)
                text_surface4 = Globals.base_font.render(f"Masha stats will drop in a minute", True,
                                                         Globals.Color_basic)
                Globals.hunger_text_surface = Globals.base_font.render("I am not borred boss", True,
                                                                       Globals.Color_basic)
                Globals.screen.blit(Globals.hunger_text_surface, (
                    Globals.status_rect.x + Globals.third_line_x, Globals.status_rect.y + Globals.third_line_y))
                Globals.screen.blit(text_surface3, (
                    Globals.status_rect.x + Globals.first_line_x, Globals.status_rect.y + Globals.first_line_y))
                Globals.screen.blit(text_surface4, (
                    Globals.status_rect.x + Globals.second_line_x, Globals.status_rect.y + Globals.second_line_y))
        except NameError:
            pass

    def update_game(self, tamagochik):
        x = tamagochik.hunger
        pygame.draw.rect(Globals.screen, Globals.RectColor, Globals.hunger_rect)
        Globals.hunger_text_surface = Globals.base_font.render(f"hunger:{tamagochik.hunger}", True, Globals.Color_basic)
        Globals.screen.blit(Globals.hunger_text_surface,
                            (
                                Globals.hunger_rect.x + Globals.first_line_x,
                                Globals.hunger_rect.y + Globals.first_line_y))

        pygame.draw.rect(Globals.screen, Globals.RectColor, Globals.happines_rect)
        Globals.happines_text_surface = Globals.base_font.render(f"happines:{tamagochik.happines}", True,
                                                                 Globals.Color_basic)
        Globals.screen.blit(Globals.happines_text_surface, (
            Globals.happines_rect.x + Globals.first_line_x, Globals.happines_rect.y + Globals.first_line_y))

    def mouse_is_hovered_on_button(self, mouse):
        for x, y, text in zip([Globals.button_x1, Globals.button_x2, Globals.button_x3],
                              [Globals.button_y1, Globals.button_y2, Globals.button_y3],
                              [Globals.button_text1, Globals.button_text2, Globals.button_text3]):
            if x <= mouse[0] <= x + Globals.width and y <= mouse[1] <= y + Globals.height:
                pygame.draw.rect(Globals.screen, Globals.color_light, [x, y, Globals.width, Globals.height])

            else:
                pygame.draw.rect(Globals.screen, Globals.color_dark, [x, y, Globals.width, Globals.height])
            # superimposing the text onto our button
            Globals.screen.blit(text, (x, y))

    def main_event_loop(self):
        clickable = True
        while Globals.Running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    try:
                        tamagochik.setinfo(Globals.Profile, Globals.winer)
                    except NameError:
                        pass
                    Globals.Running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Globals.button_x1 <= mouse[0] <= Globals.button_x1 + Globals.width and Globals.button_y1 <= \
                            mouse[
                                1] <= Globals.button_y1 + Globals.height:
                        self.hunger_button_pressed(tamagochik)
                    if Globals.button_x2 <= mouse[0] <= Globals.button_x2 + Globals.width and Globals.button_y2 <= \
                            mouse[
                                1] <= Globals.button_y2 + Globals.height and clickable:
                        clickable = False
                        tamagochik = self.live_button_pressed()
                    if Globals.button_x3 <= mouse[0] <= Globals.button_x3 + Globals.width and Globals.button_y3 <= \
                            mouse[
                                1] <= Globals.button_y3 + Globals.height:
                        self.button_happy(tamagochik)
            try:
                self.update_game(tamagochik)
                self.events(tamagochik)
            except NameError:
                pass
            mouse = pygame.mouse.get_pos()
            self.mouse_is_hovered_on_button(mouse)
            self.update_screen()
