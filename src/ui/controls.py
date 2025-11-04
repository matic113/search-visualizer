import pygame

class Button:
    def __init__(self, x, y, width, height, text, color, hover_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.font = pygame.font.Font(None, 36)

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, self.hover_color, self.rect)
        else:
            pygame.draw.rect(screen, self.color, self.rect)

        text_surf = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False

class Dropdown:
    def __init__(self, x, y, width, height, main, options):
        self.rect = pygame.Rect(x, y, width, height)
        self.main = main
        self.options = options
        self.draw_menu = False
        self.selected_index = 0
        self.font = pygame.font.Font(None, 36)

    def draw(self, screen):
        pygame.draw.rect(screen, (50, 50, 50), self.rect, 2)
        text_surf = self.font.render(self.main, True, (255, 255, 255))
        screen.blit(text_surf, self.rect.inflate(-10, -10))

        if self.draw_menu:
            for i, option in enumerate(self.options):
                rect = self.rect.copy()
                rect.y += (i + 1) * self.rect.height
                pygame.draw.rect(screen, (50, 50, 50), rect)
                text_surf = self.font.render(option, True, (255, 255, 255))
                screen.blit(text_surf, rect.inflate(-10, -10))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.draw_menu = not self.draw_menu
            elif self.draw_menu:
                for i, option in enumerate(self.options):
                    rect = self.rect.copy()
                    rect.y += (i + 1) * self.rect.height
                    if rect.collidepoint(event.pos):
                        self.selected_index = i
                        self.main = self.options[i]
                self.draw_menu = False

class Slider:
    def __init__(self, x, y, width, height, min_val, max_val, initial_val):
        self.rect = pygame.Rect(x, y, width, height)
        self.min_val = min_val
        self.max_val = max_val
        self.val = initial_val
        self.knob_rect = pygame.Rect(x, y, 10, height)
        self.update_knob_pos()

    def update_knob_pos(self):
        self.knob_rect.centerx = self.rect.x + (self.val - self.min_val) / (self.max_val - self.min_val) * self.rect.width

    def draw(self, screen):
        pygame.draw.rect(screen, (100, 100, 100), self.rect)
        pygame.draw.rect(screen, (200, 200, 200), self.knob_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.val = self.min_val + (event.pos[0] - self.rect.x) / self.rect.width * (self.max_val - self.min_val)
                self.update_knob_pos()
        elif event.type == pygame.MOUSEMOTION:
            if event.buttons[0] and self.rect.collidepoint(event.pos):
                self.val = self.min_val + (event.pos[0] - self.rect.x) / self.rect.width * (self.max_val - self.min_val)
                self.update_knob_pos()

class Controls:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.font = pygame.font.Font(None, 36)
        self.buttons = {}
        self.sliders = {}
        self.dropdowns = {}

    def add_button(self, name, x, y, width, height, text, color, hover_color):
        self.buttons[name] = Button(x, y, width, height, text, color, hover_color)

    def add_dropdown(self, name, x, y, width, height, main, options):
        self.dropdowns[name] = Dropdown(x, y, width, height, main, options)

    def add_slider(self, name, x, y, width, height, min_val, max_val, initial_val):
        self.sliders[name] = Slider(x, y, width, height, min_val, max_val, initial_val)

    def draw(self, screen):
        for button in self.buttons.values():
            button.draw(screen)
        for dropdown in self.dropdowns.values():
            dropdown.draw(screen)
        for slider in self.sliders.values():
            slider.draw(screen)

    def handle_event(self, event):
        for dropdown in self.dropdowns.values():
            dropdown.handle_event(event)
        for slider in self.sliders.values():
            slider.handle_event(event)
