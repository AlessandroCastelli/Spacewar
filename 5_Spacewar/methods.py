import pygame
from pygame.image import load
import logging

def _get_sprite(name, with_alpha=True):
    try:
        path = f"./sprites/{name}.png"
        loaded_sprite = load(path)
        if with_alpha:
            return loaded_sprite.convert_alpha()
        else:
            return loaded_sprite
    except Exception as e:
        logging.exception(f'error loading sprite {name}')
        return None