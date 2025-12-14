import pygame

class GameObject:
    def __init__(self, x, y, speed):
        self._x = x
        self._y = y
        self._speed = speed

    def move(self):
        self._y += self._speed

    def draw(self, screen):
        pygame.draw.rect(
            screen,
            (0, 255, 0),
            (self._x, self._y, 60, 20)
        )
