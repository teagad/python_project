import pygame

pygame.init()
pg = pygame


class InputBox:
    """Создан для ввода текста пользователями
    
    1)Имеет параметры 
    rect(pygame.Rect),color(pygame.Color),text(str),txt_surface(pygame.Surface),active(bool)

    2)Имеет методы 
    handle_event(считывает event при нажатие мышкой на него переводится в активное состояние,при нажатие enter сохраняет текст,при нажатие backspace удаляет последний символ)
    update  (Обновляет размеры InputBox если вышли за его рамки)
    draw    (Чертит нашу коробку) 
    
    """

    def __init__(self, x, y, w, h, text=''):
        """
        Параметры:
        ----------
        rect(pygame.Rect):
            Наша коробка для ввода
        color(pygame.Color):
            зелёный  цвет
        text(str):
            Текст который вводят
        txt_surface(pygame.Surface):
            Текст который вводят
        active(bool):
            Можно ли вводить текст
        """
        self.rect = pg.Rect(x, y, w, h)
        self.color = pg.Color('green')
        self.text = text
        font = pg.font.Font(None, 32)
        self.txt_surface = font.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        """(считывает event при нажатие мышкой на него переводится в активное состояние,
        при нажатие enter сохраняет текст,
        при нажатие backspace удаляет последний символ

            Параметры: 
                event(Event)

            Возвращаемое значение:
                x(str): имя профиля

        
        """
        COLOR_INACTIVE = pg.Color('green')
        COLOR_ACTIVE = pg.Color('dodgerblue2')
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
                    x = self.text
                    self.text = ''
                    print(f"profile: {x}")
                    return x
                elif event.key == pg.K_BACKSPACE:
                    k = self.text[:-1]
                    self.text = k
                else:
                    max_line_len = 6
                    if len(self.text) > max_line_len:
                        pass
                    else:
                        self.text += event.unicode

    def update(self):
        """Обновляет размеры InputBox если вышли за его рамки"""
        rect_width = 200
        delta_width = 10
        width = max(rect_width, self.txt_surface.get_width() + delta_width)
        self.rect.w = width

    def draw(self, screen):
        """Чертит нашу коробку

                Параметры: 
                    screen(pygame.Surface): наш экран 
        """
        FONT = pg.font.Font(None, 32)
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect, 2)
        # Re-render the text.
        self.txt_surface = FONT.render(self.text, True, self.color)
        # Blit the text.
        delta_x = 5
        delta_y = 5
        screen.blit(self.txt_surface, (self.rect.x + delta_x,
                                         self.rect.y + delta_y))
        pygame.display.update()
