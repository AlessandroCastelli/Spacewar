import pygame
from pygame.math import *
from pygame.image import load
from pygame.transform import rotozoom
from methods import *
import logging
import logmanager

class Entity:
    def __init__(self, position, sprite, speed, angle):
        self.position = Vector2(position)
        self.psx, self.psy = self.position
        self.sprite = sprite
        self.angle = angle
        self.new_angle = angle
        self.radius = sprite.get_width() / 2
        self.speed = speed
        self.velocity = Vector2(self.speed, 0).rotate(-self.angle)
        self.start = False

    def draw(self, surface):
        self.psx, self.psy = self.position
		#rotazione immagine
        rotated_image = rotozoom(self.sprite, self.new_angle, 1.0)
		#coordinate immagine ruotata
        blit_position = Vector2(self.psx, self.psy) - (Vector2(self.radius)) #(Vector2(rotated_image.get_size())/2)
        
        surface.blit(rotated_image, blit_position)

    def update_velocity(self):
        self.angle = self.new_angle
        self.velocity = Vector2(self.speed, 0).rotate(-self.angle)

    def move(self):
        if self.start:
            self.position += self.velocity

    def collides_with(self, other_obj):
        distance = self.position.distance_to(other_obj.position)
        return distance < self.radius + other_obj.radius