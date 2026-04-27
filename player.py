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
        self.speed = 5
        self.rect = pygame.rect.Rect(self.x, self.y, self.width, self.height)

        self.moving_left = False
        self.moving_right = False
        self.on_ground = False

        self.y_vel = 0
        self.jump_velocity = -10
        self.can_double_jump = True

    def update(self):
        if self.moving_left:
            self.rect.x -= self.speed

        if self.moving_right:
            self.rect.x += self.speed

        self.y_vel += 0.5
        
        self.rect.y += self.y_vel
            


    def handle_input(self):
        pass

    def move(self):
        pass
        
    def draw(self, surface):
        pygame.draw.rect(surface, "blue", self.rect)

    def jump(self):
        if self.on_ground:
            self.y_vel = self.jump_velocity
            self.on_ground = False

        elif self.can_double_jump:
            self.y_vel = self.jump_velocity
            self.on_ground = False
            self.can_double_jump = False

