from os import environ

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
from pygame.math import Vector2
from pygame.image import load
from pygame.transform import rotozoom


class Missle:
    def __init__(self, position, angle):
        self.position = Vector2(position)
        self.velocity = 3
        self.angle = angle
