from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame
import sys
from pygame.math import Vector2
from spaceship import Spaceship
import logging
import logmanager

class Spacewar:

	def __init__(self):
		self._init_pygame()
		self.screen = pygame.display.set_mode((1600, 900))
		self.clock = pygame.time.Clock()
		self.game = 0
		self.width, self.height = pygame.display.get_surface().get_size()
		self.singleplayer = True
		self.gravity = False
		self.planet = False
		self.spaceships = []
		self.direction = None
		logmanager.get_configured_logger()

	def _init_pygame(self):
		pygame.init()
		pygame.display.set_caption("SPACEWAR")
		logging.debug('SPACEWAR')

	def main_loop(self):
		while True:
			self.clock.tick(60)
			self._keyboard_input()
			if self.game == 0:
				self._show_home()
			if self.game == 1:
				self._show_info()
			if self.game == 2:
				self._show_game()

	def _keyboard_input(self):
		for event in pygame.event.get():
			if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or event.type == pygame.QUIT:
				quit()
			if (event.type == pygame.KEYDOWN and event.key == pygame.K_m) and self.game == 0:
				self.singleplayer = not self.singleplayer
			if (event.type == pygame.KEYDOWN and event.key == pygame.K_g) and self.game == 0:
				self.gravity = not self.gravity
			if (event.type == pygame.KEYDOWN and event.key == pygame.K_p) and self.game == 0:
				self.planet = not self.planet
			if (event.type == pygame.KEYDOWN and event.key == pygame.K_i) and (self.game == 0 or self.game == 1):
				if self.game == 0:
					self.game = 1
				else:
					self.game = 0
			if (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN) and self.game == 0:
				self.spaceships[0] = Spaceship((self.width/2, self.height/2), Vector2(3, 0).rotate(0), 1)
				self.spaceships[1] = Spaceship((self.width/2, self.height/2), Vector2(3, 0).rotate(0), 2)
				self.game = 2
				
			if (event.type == pygame.KEYDOWN and event.key == pygame.K_d) and self.game == 2:
				self.direction = "right"
			if (event.type == pygame.KEYDOWN and event.key == pygame.K_a) and self.game == 2:
				self.direction = "left"


	def _write_text(self, string, fontSize, color, x, y):
		font = pygame.font.Font('./font/BungeeShade-Regular.ttf', fontSize)
		text = font.render(string, True, color)
		rect = text.get_rect()
		rect.center = (x, y)
		self.screen.blit(text, rect)

	def _show_home(self):
		self.screen.fill((0,0,0))
		self.write = self._write_text("SPACEWAR", 90, (255,255,255), self.width / 2, self.height / 3.5)
		self.write = self._write_text("Press enter to play", 30, (255,255,255), self.width / 5, self.height / 2)

		self.write = self._write_text("Press M to change mode", 30, (255,255,255), self.width / 3 * 2.5, self.height / 2)
		self.write = self._write_text("singleplayer: " + str(self.singleplayer), 30, (255,255,255), self.width / 3 * 2.5, self.height / 2 + 40)

		self.write = self._write_text("Press s to change spaceship", 30, (255,255,255), self.width / 5, self.height / 2 + 200)

		self.write = self._write_text("Press g to set gravity", 30, (255,255,255), self.width / 3 * 2.5, self.height / 2 + 200)
		self.write = self._write_text("gravity: " + str(self.gravity), 30, (255,255,255), self.width / 3 * 2.5, self.height / 2 + 240)

		self.write = self._write_text("Press p for the planet", 30, (255,255,255), self.width / 5, self.height / 2 + 360)
		self.write = self._write_text("planet: " + str(self.planet), 30, (255,255,255), self.width / 5, self.height / 2 + 400)

		self.write = self._write_text("Press i for info", 30, (255,255,255), self.width / 3 * 2.5, self.height / 2 + 400)

		pygame.display.flip()
	
	def _show_info(self):
		self.screen.fill((0,0,0))
		self.write = self._write_text("Information", 90, (255,255,255), self.width / 2, self.height / 3.5)

		self.write = self._write_text("player 1: movement with wasd, missle with y and laser with c", 30, (255,255,255), self.width / 2, self.height / 2)
		self.write = self._write_text("player 2: movement with ijkl, missle with . and laser with n", 30, (255,255,255), self.width / 2, self.height / 2 + 200)

		self.write = self._write_text("Press i to back home", 30, (255,255,255), self.width / 3 * 2.5, self.height / 2 + 400)
		pygame.display.flip()

	def _show_game(self):
		self.screen.fill((0,0,0))
		try:
			if self.singleplayer:
				if not self.gravity and not self.planet:
					for (i, spaceship) in enumerate(self.spaceships):
						logging.info(f'loading ship {i}')
						print(f'loading ship {i}')
						spaceship.draw(self.screen, 500, 500)
		except Exception as e:
			logging.exception('error loading ships')
		pygame.display.flip()

		







if __name__ == '__main__':
	try:
		spacewar = Spacewar()
		spacewar.main_loop()
	except:
		quit()