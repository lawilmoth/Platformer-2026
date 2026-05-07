import pygame

# -----------------------------
# Enemy Class
# -----------------------------
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, platforms, width=20, height=20, color="red"):
        super().__init__()
        self.x = x
        self.y = y
        self.start_x = x
        self.start_y = y
        self.width = width
        self.height = height
        self.color = color
        self.platforms = platforms

        self.rect = pygame.rect.Rect(self.x, self.y, self.width, self.height)
        self.rect.x, self.rect.y = x, y
        self.y_vel = 0
        self.on_ground = False

    def update(self):
        self.prev_rect = self.rect.copy()
        self.y_vel += 0.5
        for platform in self.platforms:
            self.check_ground(platform)
        if self.on_ground:
            self.y_vel = 0
        self.rect.y += self.y_vel
        

    def check_ground(self, platform):
        if self.y_vel >= 0:
            if pygame.sprite.collide_rect(self, platform):
                self.rect.bottom = platform.rect.top
                self.on_ground = True

    def move(self):
        pass

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def respawn(self):
        self.x = self.start_x
        self.y = self.start_y

