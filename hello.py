import time
import pygame
from pygame.locals import *

class Player:
    def __init__(self,location,speed,default_sprite):
        self.location = location
        self.speed = speed
        self.default_sprite = default_sprite

    def moveRight(self):
        self.location[0] += self.speed

    def moveLeft(self):
        self.location[0] -= self.speed

    def moveUp(self):
        self.location[1] -= self.speed

    def moveDown(self):
        self.location[1] += self.speed

class App:
    def __init__(self):
        self.player = Player([0,0],10.0,"gomes_2022.gif")
        self.enemy = Player([120,120],5.0,"bolsa.gif")
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self._image_enemy = None
        self.size = self.weight, self.height = 640, 400
 
    def on_init(self):
        pygame.init()
        pygame.mixer.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        self._image_surf = pygame.image.load(self.player.default_sprite).convert()
        self._image_enemy = pygame.image.load(self.enemy.default_sprite).convert()

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.player.moveLeft()
                self.enemy.moveLeft()
            if event.key == pygame.K_RIGHT:
                self.player.moveRight()
                self.enemy.moveRight()
            if event.key == pygame.K_UP:
                self.player.moveUp()
                self.enemy.moveUp()
            if event.key == pygame.K_DOWN:
                self.player.moveDown()
                self.enemy.moveDown()

    def on_loop(self):
        if self.player.location == self.enemy.location:
            print("Colisao")
            sound = pygame.mixer.Sound("juca.wav")
            sound.play()
            time.sleep(5)
        #pass
    def on_render(self):
        self._display_surf.fill((0,0,0))
        self._display_surf.blit(self._image_surf,self.player.location)
        self._display_surf.blit(self._image_enemy,self.enemy.location)
        pygame.display.flip()
        #pass
    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()

if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()

