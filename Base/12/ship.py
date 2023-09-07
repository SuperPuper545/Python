import pygame
from settings import Settings

class Ship():
    """ Класс для управления кораблём. """

    def __init__(self, ai_game):
        """ Инициализирует корабль и задаёт его начальную позицию. """
        self.screen = ai_game
        self.screen_rect = ai_game.get_rect()
        self.settings = Settings()

        #Загружает изображение коробля и получает прямоугольник.
        self.image = pygame.image.load("player.bmp")
        self.rect = self.image.get_rect()
        #Каждый новый корабль появляется у нижнего края экрана.
        self.rect.midbottom = self.screen_rect.midbottom
        #Сохранение вещественных координат коробля.
        self.x = float(self.rect.x)
        #self.y = float(self.rect.y)
        #Флаг перемещения
        self.moving_right = False
        self.moving_left = False
        #self.moving_up = False
        #self.moving_down = False

    def update(self):
        """ Обновляет позицию коробля с учётом флага. """
        #Обновляет атрибуты x, не rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        '''if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed'''  

        #Обновление атрибута rect на основании self.x.
        self.rect.x = self.x
        #self.rect.y = self.y
         

    def blitme(self):
        """ Рисует корабль в текущей позиции. """
        self.screen.blit(self.image, self.rect)

