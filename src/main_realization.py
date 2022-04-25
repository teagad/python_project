import pickle
import pygame
from src.events import Event
from src.main_logic import Game_logic
from src.globals import Globals


class Realization:

    def __init__(self):
        self.game = Game_logic()

    # choosing tamagochi
    def choosing_tamagochi(self, old=1):
        Globals.screen.blit(Globals.BackGround.image, Globals.BackGround.rect)
        if old:
            Globals.screen.blit(Globals.Profile_text_surface, Globals.Profile_rect)
        for animal, coord in zip(
                Globals.tamagochis.values(),
                Globals.tamagochi_coords
        ):
            image = pygame.image.load(animal)
            image = pygame.transform.scale(image, Globals.tamagochisize)
            Globals.screen.blit(image, coord)
        pygame.display.update()

    def event_loop_of_choosing_tamagochi(self, old=1):
        running = True
        # self.game.print_all_profiles()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    running = self.game.check_choosing_tamagochi(mouse)
                if old:
                    x = Globals.input_box1.handle_event(event)
                    if x:
                        Globals.Profile = x
                    Globals.input_box1.update()
                    pygame.draw.rect(Globals.screen,
                                     (Globals.Colordelete),
                                     Globals.input_box1.rect
                                     )
                    Globals.input_box1.draw(Globals.screen)
                self.game.update_screen
            mouse = pygame.mouse.get_pos()

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
                    if Globals.button_x1 <= mouse[0] <= \
                            Globals.button_x1 + Globals.width \
                            and Globals.button_y1 <= \
                            mouse[1] <= Globals.button_y1 + Globals.height:
                        self.game.hunger_button_pressed(tamagochik)
                    if Globals.button_x2 <= mouse[0] <= \
                            Globals.button_x2 + Globals.width and \
                            Globals.button_y2 <= \
                            mouse[1] <= Globals.button_y2 + Globals.height \
                            and clickable:
                        clickable = False
                        tamagochik = self.game.live_button_pressed()
                    if Globals.button_x3 <= mouse[0] <= \
                            Globals.button_x3 + Globals.width and \
                            Globals.button_y3 <= \
                            mouse[1] <= Globals.button_y3 + Globals.height:
                        self.game.button_happy(tamagochik)
            try:
                eve = Event()
                self.game.update_game(tamagochik)
                eve.events(tamagochik)
            except NameError:
                pass
            mouse = pygame.mouse.get_pos()
            self.game.mouse_is_hovered_on_button(mouse)
            self.game.update_screen()

    def get_profiles_length(self):
        black = (0, 0, 0)
        profiles_str = {}
        with open('data.pickle', 'rb') as f:
            dic = pickle.load(f)
            for profile in dic.items():
                if profile[0][0] not in profiles_str:
                    text = profile[0][0] + ','
                    text_surface = Globals.profile_text_font.render(
                        text, True,
                        black
                    )
                    profiles_str[profile[0][0]] = text_surface.get_width()
                    # print(profile[0][0])
            print(profiles_str)
            return profiles_str

    def clicked_profile(self):
        running = True
        start_length = Globals.text_surface.get_width()
        array = self.get_profiles_length()
        letter_height = 40
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    return 0
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pasts = 0
                    for i, j in enumerate(list(array.values())):
                        if mouse[0] <= j + pasts + start_length and \
                                mouse[0] > start_length:
                            print(mouse[0])
                            if 5 < mouse[1] < letter_height:
                                with open('data.pickle', 'rb') as f:
                                    dic = pickle.load(f)
                                    Globals.Profile = list(array.keys())[i]
                                    print(list(array.keys())[i])
                                    return 1
                        pasts += j

            mouse = pygame.mouse.get_pos()
            pygame.display.update()

    def check_profiles_count(self):
        profiles_str = []
        red = (255, 0, 0)
        legal_profiles_count = 2
        try:
            with open('data.pickle', 'rb') as f:
                dic = pickle.load(f)
                print(dic)
                for profile in dic.items():
                    if profile[0][0] not in profiles_str:
                        profiles_str += [profile[0][0]]
                if len(profiles_str) > legal_profiles_count:
                    Profile_array_rect = pygame.Rect(0, 450, 200, 64)
                    profile_array = 'maximum count of profiles is 3'
                    profile_array_text_surface = Globals.profile_text_font.render(
                        profile_array, True,
                        red
                    )
                    Globals.screen.blit(
                        profile_array_text_surface,
                        Profile_array_rect
                    )
                    return 0
                return 1
        except Exception:
            return 1

    def start_new_profile(self):
        pygame.display.set_caption("Russian tamagochi")
        pygame.display.set_mode(Globals.screensize)
        self.choosing_tamagochi()
        self.event_loop_of_choosing_tamagochi()
        self.game.draw_background()
        # placing tamagochi picture
        self.game.place_tamagochi_picture()
        # making text box
        self.game.making_textbox()
        # render at position stated in arguments
        self.game.render_textboxes()
        # starting event
        # events
        self.main_event_loop()

    def start_old_profile(self):
        self.game.print_all_profiles()
        if self.clicked_profile():
            pygame.display.set_caption("Russian tamagochi")
            pygame.display.set_mode(Globals.screensize)
            self.choosing_tamagochi(0)
            self.event_loop_of_choosing_tamagochi(0)
            self.game.draw_background()
            self.game.place_tamagochi_picture()
            self.game.making_textbox()
            self.game.render_textboxes()
            self.main_event_loop()
