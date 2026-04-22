import pygame

# Player Class
# -----------------------------
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.width = 16
        self.height = 16
        self.speed = 2
        self.rect = pygame.rect.Rect(self.x, self.y, self.width, self.height)

        self.moving_left = False
        self.moving_right = False
        self.on_ground = False

        self.y_vel = 1


    def update(self):
        if self.moving_left:
            self.rect.x -= self.speed

        if self.moving_right:
            self.rect.x += self.speed

        if not self.on_ground:
            self.y_vel += 0.5
            self.rect.y += self.y_vel
            print("not on ground")

    def handle_input(self):
        pass

    def move(self):
        pass
        
    def draw(self, surface):
        pygame.draw.rect(surface, "blue", self.rect)

