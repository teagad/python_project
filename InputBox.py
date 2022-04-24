import pygame

pygame.init()
pg = pygame


class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = pg.Color('green')
        self.text = text
        self.txt_surface = pg.font.Font(None, 32).render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
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
                    self.text += event.unicode

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def draw(self, screen):
        FONT = pg.font.Font(None, 32)
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect, 2)
        # Re-render the text.
        self.txt_surface = FONT.render(self.text, True, self.color)
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        pygame.display.update()
