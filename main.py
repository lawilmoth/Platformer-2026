import pygame
import sys

from enemy import Enemy
from platforms import Platform
# -----------------------------
# Constants
# -----------------------------
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900
FPS = 60


# -----------------------------
# Game Class
# -----------------------------
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        
        from player import Player
        
        pygame.display.set_caption("Platformer")

        self.clock = pygame.time.Clock()
        self.running = True

        self.level_offset = 0

        self.platforms = pygame.sprite.Group()
        self.platforms.add(Platform(0, 300, 400, 100))
        self.platforms.add(Platform(400, 350, 200, 100))
        self.platforms.add(Platform(750, 250, 300, 100))
        self.platforms.add(Platform(1250, 250, 300, 100))
        self.platforms.add(Platform(1750, 550, 300, 100))
        self.platforms.add(Platform(2000, 20, 100, 800, "blue"))

        self.player = Player(0, 0)

    def handle_keydown_events(self, event):
        if event.key == pygame.K_LEFT:
            self.player.moving_left = True
        if event.key == pygame.K_RIGHT:
            self.player.moving_right = True
        if event.key == pygame.K_LSHIFT:
            self.player.is_sprinting = True
            
        if event.key == pygame.K_SPACE:
            self.player.jump()

    def handle_keyup_events(self, event):
        if event.key == pygame.K_LEFT:
            self.player.moving_left = False
        if event.key == pygame.K_RIGHT:
            self.player.moving_right = False
        if event.key == pygame.K_LSHIFT:
            self.player.is_sprinting = False



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

        if self.player.rect.left >= 700:
            for platform in self.platforms:
                platform.rect.x -= self.player.x_vel
            
            self.player.rect.x -= self.player.x_vel
            self.level_offset += self.player.x_vel
            print(self.level_offset)

        if self.player.rect.top >= SCREEN_HEIGHT + self.player.height:
            self.player.respawn()
            for platform in self.platforms:
                platform.rect.x -= self.level_offset 
            self.level_offset = 0

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
            self.check_collisions()
            self.draw()

        pygame.quit()
        sys.exit()

    def check_collisions(self):
        self.player.on_ground = False

        platform_collisions = pygame.sprite.spritecollide(self.player, self.platforms, dokill=False)
        
        for platform in platform_collisions:
            if self.player.y_vel >= 0:
                if self.player.prev_rect.bottom <= platform.rect.top:
                    self.player.rect.bottom = platform.rect.top
                    self.player.y_vel = 0 
                    self.player.on_ground = True
                    self.player.can_double_jump = True
            
            
            if self.player.x_vel > 0: 
                if self.player.prev_rect.right <= platform.rect.left:
                    self.player.rect.right = platform.rect.left
                    self.player.x_vel = 0
                    
            if self.player.x_vel < 0:
                if self.player.prev_rect.left >= platform.rect.right:
                    self.player.rect.left = platform.rect.right
                    self.player.x_vel = 0

            #Hitting head when jumping
            if self.player.y_vel < 0:
                if self.player.prev_rect.top >= platform.rect.bottom:
                    self.player.rect.top = platform.rect.bottom
                    self.player.y_vel = 0 
                    
            
            

# -----------------------------
# Entry Point
# -----------------------------
if __name__ == "__main__":
    game = Game()
    game.run()