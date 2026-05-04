import pygame
from sprite_sheet_parser import parse_sprite_sheet, scale_frames
# Player Class
# -----------------------------

player_sheet = pygame.image.load("assets/DinoSprites - doux.png").convert_alpha()

idle_frames = parse_sprite_sheet(
    sheet=player_sheet, 
    start_x=0,
    start_y=0,
    frame_count=4,
    columns=24,
    rows=1
)

idle_frames = scale_frames(idle_frames, 2)

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.checkpoint_x = x
        self.checkpoint_y = y
        self.lives = 3
        
        self.x = x
        self.y = y
        self.width = 16
        self.height = 16
        self.speed = 5

        self.moving_left = False
        self.moving_right = False
        self.on_ground = False

        self.y_vel = 0
        self.jump_velocity = -10
        self.can_double_jump = True

        self.frames = idle_frames
        self.frame_index = 0
        self.animation_speed = 0.2
        self.flip_x = False
        self.image = self.frames[0]
        self.rect = self.image.get_rect()
        self.animation_count = 0
        


    def update(self):
        if self.moving_left:
            self.rect.x -= self.speed

        if self.moving_right:
            self.rect.x += self.speed

        self.y_vel += 0.5
        
        self.rect.y += self.y_vel
            
        self.update_frames()


    def handle_input(self):
        pass

    def move(self):
        pass
        
    def draw(self, surface):
        #pygame.draw.rect(surface, "blue", self.rect)
        surface.blit(self.image, self.rect)

    def jump(self):
        if self.on_ground:
            self.y_vel = self.jump_velocity
            self.on_ground = False

        elif self.can_double_jump:
            self.y_vel = self.jump_velocity
            self.on_ground = False
            self.can_double_jump = False


    def respawn(self):
        self.rect.x = self.checkpoint_x
        self.rect.y = self.checkpoint_y
        self.lives -= 1
        print(self.lives)

    def update_frames(self):
        self.animation_count += self.animation_speed

        if self.animation_count >= 1:
            self.frame_index = (self.frame_index + 1) % len(self.frames)
            self.animation_count = 0

        current_frame = self.frames[self.frame_index]

        if self.moving_left:
            current_frame = pygame.transform.flip(current_frame, True, False)

        self.image = current_frame
        
