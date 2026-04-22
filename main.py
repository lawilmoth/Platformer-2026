import pygame
import sys

from player import Player
from enemy import Enemy
from platforms import Platform
# -----------------------------
# Constants
# -----------------------------
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 480
FPS = 60


# -----------------------------
# Game Class
# -----------------------------
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Platformer")

        self.clock = pygame.time.Clock()
        self.running = True


        self.platforms = pygame.sprite.Group()
        self.platforms.add(Platform(200, 300, 100, 100))
        self.platforms.add(Platform(400, 350, 200, 100))

        self.player = Player(0, 0)

    def handle_keydown_events(self, event):
        if event.key == pygame.K_LEFT:
            self.player.moving_left = True
        if event.key == pygame.K_RIGHT:
            self.player.moving_right = True
        if event.key == pygame.K_UP:
            self.player.moving_up = True
        if event.key == pygame.K_DOWN:
            self.player.moving_down = True

    def handle_keyup_events(self, event):
        if event.key == pygame.K_LEFT:
            self.player.moving_left = False
        if event.key == pygame.K_RIGHT:
            self.player.moving_right = False
        if event.key == pygame.K_UP:
            self.player.moving_up = False
        if event.key == pygame.K_DOWN:
            self.player.moving_down = False


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                self.handle_keydown_events(event)

            if event.type == pygame.KEYUP:
                self.handle_keyup_events(event)


    def update(self):
        self.player.update()

    def draw(self):
        self.screen.fill((30, 30, 30))
        for platform in self.platforms:
            platform.draw(self.screen)

        self.player.draw(self.screen)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.handle_events()
            self.update()
            self.draw()

        pygame.quit()
        sys.exit()



# -----------------------------
# Entry Point
# -----------------------------
if __name__ == "__main__":
    game = Game()
    game.run()