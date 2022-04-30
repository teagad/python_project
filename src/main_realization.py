import pickle
import pygame
from src.background import Background
from src.events import Event
from src.globals import Globals
from src.InputBox import InputBox as imbox
from src.main_logic import Game_logic

class Realization:
    """Реализация игровой логики
    
    1)Имеет параметр 
    game Класса Game_logic

    2)Имеет методы
    choosing_tamagochi (Располагает картинки всех тамагочи на экран чтобы выбрать)

    event_loop_of_choosing_tamagochi (Event loop для выбора тамагочи)

    main_event_loop (Основной event loop игры)

    get_profiles_length (Находит длину названия каждого профиля )

    clicked_profile (Ивент луп для выбора профиля)

    check_profiles_count (Проверка на то может ли игрок создать нового персонажа)

    start_new_profile (Запуск игры для новичка)

    start_old_profile (Запуск игры для старичка)
    """

    def __init__(self):
       """" 
       Параметры: 
            game(Game_logic)
       """
       self.game = Game_logic()

    # choosing tamagochi
    def choosing_tamagochi(self, old=1):
        """Располагает картинки всех тамагочи на экран чтобы выбрать

            Параметры: 
                old(int): 1 Если игрок новый, 0 если кже играл
        
        """
        first_tamagochi_coordinate_x = 0
        second_tamagochi_coordinate_x = 200
        third_tamagochi_coordinate_x = 400
        coordinate_y = 100
        tamagochi_coords = [(first_tamagochi_coordinate_x, coordinate_y),
                    (second_tamagochi_coordinate_x, coordinate_y),
                    (third_tamagochi_coordinate_x, coordinate_y)]
        BackGround = Background('assets/background_image.png', [0, 0])
        Globals.screen.blit(BackGround.image, BackGround.rect)
        if old:
            Globals.screen.blit(Globals.profile_text_surface, Globals.profile_rect)
        for animal, coord in zip(
                Globals.tamagochis.values(),
                tamagochi_coords
        ):
            image = pygame.image.load(animal)
            image = pygame.transform.scale(image, Globals.tamagochisize)
            Globals.screen.blit(image, coord)
        pygame.display.update()

    def event_loop_of_choosing_tamagochi(self, old=1):
        """Event loop для выбора тамагочи
            Параметры: 
                old(int): 1 Если игрок новый, 0 если кже играл
        """
        running = True
        input_box1 = imbox(250, 600, 300, 64)
        Colordelete = (30, 30, 30)

        # self.game.print_all_profiles()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    running = self.game.check_choosing_tamagochi(mouse)
                if old:
                    x = input_box1.handle_event(event)
                    if x:
                        Globals.profile = x
                    input_box1.update()
                    pygame.draw.rect(Globals.screen,
                                     (Colordelete),
                                     input_box1.rect
                                     )
                    input_box1.draw(Globals.screen)
                self.game.update_screen
            mouse = pygame.mouse.get_pos()

    def main_event_loop(self):
        """Основной event loop игры"""
        clickable = True
        while Globals.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    try:
                        tamagochik.setinfo(Globals.profile, Globals.winer)
                    except NameError:
                        pass
                    Globals.running = False
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
        """Находит длину названия каждого профиля 

            Возвращаемое значение:
                profiles_str(dict): Словарь где ключи это название профилей а значения их длинна

        """
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
        """Ивент луп для выбора профиля
                Возвращаемое значение:
                    1 если нажали на какой то профиль
        """
        running = True
        text = "Profiles : "
        black = (0,0,0)
        text_surface = Globals.profile_text_font.render(
            text, True,
            black
        )
        start_length = text_surface.get_width()
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
                                    Globals.profile = list(array.keys())[i]
                                    print(list(array.keys())[i])
                                    return 1
                        pasts += j

            mouse = pygame.mouse.get_pos()
            pygame.display.update()

    def check_profiles_count(self):
        """Проверка на то может ли игрок создать нового персонажа
                Возвращаемое значение:
                    1 если можно создать профиль 0 иначе
        """
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
        """Запуск игры для новичка"""
        screensize = (700, 700)
        pygame.display.set_caption("Russian tamagochi")
        pygame.display.set_mode(screensize)
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
        """Запуск игры для старичка"""
        screensize = (700, 700)
        self.game.print_all_profiles()
        if self.clicked_profile():
            pygame.display.set_caption("Russian tamagochi")
            pygame.display.set_mode(screensize)
            self.choosing_tamagochi(0)
            self.event_loop_of_choosing_tamagochi(0)
            self.game.draw_background()
            self.game.place_tamagochi_picture()
            self.game.making_textbox()
            self.game.render_textboxes()
            self.main_event_loop()
