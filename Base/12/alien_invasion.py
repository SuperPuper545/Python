import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion():
    """ Класс управления ресурсами и поведением игры. """

    def __init__(self):
        """ Инициализирует игру и создаёт игровые ресурсы. """
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self.screen)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """ Запуск основного цикла игры. """
        while True:
            self.ship.update()
            self._update_bullets()
            #Отслеживание событий клавиатуры и мыши.
            self._check_events()
            #При каждом проходе цикла перерисовывается экран.
            self._update_screen()
        


    def _check_events(self):
        """ Обрабатывает нажатия клавиш и события мыши. """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Реагирует на нажатие клавиш."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            pygame.quit()
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        '''elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True'''

    def _check_keyup_events(self, event):
        """Реагирует на отпускание клавиш."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        '''elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False'''

    def _fire_bullet(self):
        """ Создание нового снаряда и включение его в группу bullets. """
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """ Обновляет позиции снарядов и уничтожает старые снаряды """
        #Обновляет позиции снарядов.
        self.bullets.update()
        #Удалиение снарядов, вышедших за край экрана.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        
    def _update_screen(self):
        """ Обновляет изобржение на экране и отображает новый экран. """
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        #Отображение последнего прорисованного экрана.
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()

if __name__ == "__main__":
    #Создание экземпляра и запуск игры.
    ai = AlienInvasion()
    ai.run_game()
