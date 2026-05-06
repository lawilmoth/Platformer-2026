import pygame

# -----------------------------
# Platform Class
# -----------------------------
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color = "green"):
        super().__init__()
        self.x = x
        self.y = y
        self.start_x = x
        self.start_y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.color = color
        
    def draw(self, surface):
        pygame.draw.rect(surface, self.color , self.rect)
