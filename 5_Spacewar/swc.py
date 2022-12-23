from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame
import sys
from pygame.math import Vector2
from spaceship import Spaceship
from missle import Missle
from planet import Planet
from laser import Laser
import logging
import logmanager

logmanager.get_configured_logger()

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
		self.missles1 = []
		self.missles2 = []
		self.planetgame = None
		self.player1 = 1
		self.player2 = 2
		self.laser1 = None
		self.laser2 = None

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
			if self.game == 3:
				self._show_end()

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
			if (event.type == pygame.KEYDOWN and event.key == pygame.K_s) and self.game == 0:
				if self.player1 == 1:
					self.player1 = 2
					self.player2 = 1
				else:
					self.player1 = 1
					self.player2 = 2
			if (event.type == pygame.KEYDOWN and event.key == pygame.K_i) and (self.game == 0 or self.game == 1):
				if self.game == 0:
					self.game = 1
				else:
					self.game = 0
			if (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN) and self.game == 0:


				ship1 = Spaceship((self.width*1/4, self.height/2), 0, self.player1)
				self.spaceships.append(ship1)

				ship2 = Spaceship((self.width*3/4, self.height/2), 180, self.player2)
				self.spaceships.append(ship2)

				if self.planet:
					self.planetgame = Planet((self.width/2, self.height/2))
				
				self.game = 2
			
			keys = pygame.key.get_pressed()
			if (event.type == pygame.KEYDOWN and event.key == pygame.K_d) and self.game == 2:
				self.spaceships[0].change_angle(False)
			if (keys[pygame.K_d]) and self.game == 2:
				self.spaceships[0].change_angle(False)
			if (event.type == pygame.KEYDOWN and event.key == pygame.K_a) and self.game == 2:
				self.spaceships[0].change_angle(True)
			if (keys[pygame.K_a]) and self.game == 2:
				self.spaceships[0].change_angle(True)

			if (event.type == pygame.KEYDOWN and event.key == pygame.K_l) and self.game == 2 and self.singleplayer == False:
				self.spaceships[1].change_angle(False)
			if (keys[pygame.K_l]) and self.game == 2 and self.singleplayer == False:
				self.spaceships[1].change_angle(False)
			if (event.type == pygame.KEYDOWN and event.key == pygame.K_j) and self.game == 2 and self.singleplayer == False:
				self.spaceships[1].change_angle(True)
			if (keys[pygame.K_j]) and self.game == 2 and self.singleplayer == False:
				self.spaceships[1].change_angle(True)

			if (event.type == pygame.KEYDOWN and event.key == pygame.K_w) and self.game == 2:
				self.spaceships[0].start = True
				self.spaceships[0].update_velocity()

			if (event.type == pygame.KEYDOWN and event.key == pygame.K_i) and self.game == 2 and self.singleplayer == False:
				self.spaceships[1].start = True
				self.spaceships[1].update_velocity()

			if (event.type == pygame.KEYDOWN and event.key == pygame.K_e) and self.game == 2:
				if self.spaceships[0].energy > self.spaceships[0].energy_missle:
					missle = Missle(self.spaceships[0].position, self.spaceships[0].new_angle)
					self.missles1.append(missle)
					self.spaceships[0].energy = self.spaceships[0].energy - self.spaceships[0].energy_missle
			
			if (event.type == pygame.KEYDOWN and event.key == pygame.K_o) and self.game == 2 and self.singleplayer == False:
				if self.spaceships[1].energy > self.spaceships[1].energy_missle:
					missle = Missle(self.spaceships[1].position, self.spaceships[1].new_angle)
					self.missles2.append(missle)
					self.spaceships[1].energy = self.spaceships[1].energy - self.spaceships[1].energy_missle
			
			if (event.type == pygame.KEYDOWN and event.key == pygame.K_q) and self.game == 2:
				if self.spaceships[0].energy >= self.spaceships[0].energy_laser:
					self.laser1 = Laser(self.spaceships[0].position, self.spaceships[0].new_angle)
					self.spaceships[0].energy = self.spaceships[0].energy - self.spaceships[0].energy_laser
			
			if (event.type == pygame.KEYDOWN and event.key == pygame.K_u) and self.game == 2 and self.singleplayer == False:
				if self.spaceships[1].energy >= self.spaceships[1].energy_laser:
					self.laser2 = Laser(self.spaceships[1].position, self.spaceships[1].new_angle)
					self.spaceships[1].energy = self.spaceships[1].energy - self.spaceships[1].energy_laser
			
			if (event.type == pygame.KEYDOWN and event.key == pygame.K_h) and self.game == 3:
				self.spaceships = []
				self.missles1 = []
				self.missles2 = []
				self.planetgame = None
				self.laser1 = None
				self.laser2 = None
				self.game = 0
				

			


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

		self.write = self._write_text("player 1: movement with wad, missle with e and laser with q", 30, (255,255,255), self.width / 2, self.height / 2)
		self.write = self._write_text("player 2: movement with ijl, missle with o and laser with u", 30, (255,255,255), self.width / 2, self.height / 2 + 200)

		self.write = self._write_text("Press i to back home", 30, (255,255,255), self.width / 3 * 2.5, self.height / 2 + 400)
		pygame.display.flip()

	def _show_game(self):
		self.screen.fill((0,0,0))
		self.write = self._write_text("Player 1", 30, (255,255,255), 130, self.height * 1/15)
		self.write = self._write_text("Life: " + str(self.spaceships[0].life), 25, (255,255,255), 130, self.height * 1/9)
		self.write = self._write_text("Player 2", 30, (255,255,255), self.width - 130, self.height * 1/15)
		self.write = self._write_text("Life: " + str(self.spaceships[1].life), 25, (255,255,255), self.width - 130, self.height * 1/9)
		try:
			for (i, spaceship) in enumerate(self.spaceships):
				spaceship.draw(self.screen)
			for (i, missle) in enumerate(self.missles1):
				missle.draw(self.screen)
			for (i, missle) in enumerate(self.missles2):
				missle.draw(self.screen)
			
			if self.planet:
				self.planetgame.draw(self.screen)
			

			for missle in self.missles2:
				missle.start = True
				missle.move()
				if missle.collides_with(self.spaceships[0]):
					if self.spaceships[0].life > 1:
						self.spaceships[0].life = self.spaceships[0].life - missle.damage
						self.missles2.remove(missle)
						del missle
					else:
						self.spaceships[0].life = 0
						self.game = 3
				if self.planet and missle.collides_with(self.planetgame):
					self.missles2.remove(missle)
					del missle
			
			for missle in self.missles1:
				missle.start = True
				missle.move()
				if missle.collides_with(self.spaceships[1]):
					if self.spaceships[1].life > 1:
						self.spaceships[1].life = self.spaceships[1].life - missle.damage
						self.missles1.remove(missle)
						del missle
					else:
						self.spaceships[1].life = 0
						self.game = 3
				if self.planet and missle.collides_with(self.planetgame):
					self.missles1.remove(missle)
					del missle
			
			for spaceship in self.spaceships:
				spaceship.move()
				if spaceship.energy < 401:
					spaceship.energy = spaceship.energy + 1
				if self.planet and spaceship.collides_with(self.planetgame):
					spaceship.life = spaceship.life  - self.planetgame.damage
					self.game = 3
			
			if self.spaceships[0].energy >= 400:
				self.write = self._write_text("Laser ball available", 20, (255,0,0), 160, self.height * 1/6)
			
			if self.spaceships[1].energy >= 400:
				self.write = self._write_text("Laser ball available", 20, (255,0,0), self.width - 160, self.height * 1/6)

			if self.laser1 != None:
				self.laser1.start = True
				self.laser1.move()
				self.laser1.draw(self.screen)
				if self.laser1.collides_with(self.spaceships[1]):
					if self.spaceships[1].life > 2:
						self.spaceships[1].life = self.spaceships[1].life - self.laser1.damage
						self.laser1 = None
					else:
						self.spaceships[1].life = 0
						self.game = 3
				if self.planet and self.laser1.collides_with(self.planetgame):
					self.laser1 = None

			if self.laser2 != None:
				self.laser2.start = True
				self.laser2.move()
				self.laser2.draw(self.screen)
				if self.laser2.collides_with(self.spaceships[0]):
					if self.spaceships[0].life > 2:
						self.spaceships[0].life = self.spaceships[0].life - self.laser2.damage
						self.laser2 = None
					else:
						self.spaceships[0].life = 0
						self.game = 3
				if self.planet and self.laser2.collides_with(self.planetgame):
					self.laser2 = None

		except Exception as e:
			logging.exception('error loading ships')
		
		self._destroy_missles()

		self._destroy_lasers()

		self.check_spaceship_position()

		pygame.display.flip()
	
	def _show_end(self):
		self.screen.fill((0,0,0))
		self.write = self._write_text("GAME OVER", 90, (255,255,255), self.width / 2, self.height / 3.5)
		if self.spaceships[0].life > 0 and self.spaceships[1].life < 1:
			self.write = self._write_text("Player 1 Win", 90, (255,255,255), self.width / 2, self.height / 2)
		else:
			self.write = self._write_text("Player 2 Win", 90, (255,255,255), self.width / 2, self.height / 2)
		
		self.write = self._write_text("Press h to home", 30, (255,255,255), self.width / 3 * 2.5, self.height / 2 + 400)

		pygame.display.flip()

	def _destroy_missles(self):
		for missle in self.missles1:
			if (missle.psx > self.width + 60 or missle.psx < 0 - 60) or (missle.psy > self.height + 60 or missle.psy < 0 - 60):
				self.missles1.remove(missle)
				del missle
		for missle in self.missles2:
			if (missle.psx > self.width + 60 or missle.psx < 0 - 60) or (missle.psy > self.height + 60 or missle.psy < 0 - 60):
				self.missles2.remove(missle)
				del missle
	
	def _destroy_lasers(self):
		if self.laser1 != None:
			if (self.laser1.psx > self.width + 100 or self.laser1.psx < 0 - 100) or (self.laser1.psy > self.height + 100 or self.laser1.psy < 0 - 100):
				self.laser1 = None
		if self.laser2 != None:
			if (self.laser2.psx > self.width + 100 or self.laser2.psx < 0 - 100) or (self.laser2.psy > self.height + 100 or self.laser2.psy < 0 - 100):
				self.laser2 = None
	
	def check_spaceship_position(self):
		for spaceship in self.spaceships:
			if spaceship.psx > self.width + 30:
				spaceship.position = (0 - 30, spaceship.psy)
			if spaceship.psx < 0 - 30:
				spaceship.position = (self.width + 30, spaceship.psy)
			if spaceship.psy > self.height + 30:
				spaceship.position = (spaceship.psx, 0 - 30)
			if spaceship.psy < 0 - 30:
				spaceship.position = (spaceship.psx, self.height + 30)






if __name__ == '__main__':
	try:
		spacewar = Spacewar()
		spacewar.main_loop()
	except:
		quit()