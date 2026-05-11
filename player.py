import pygame
from sprite_sheet_parser import parse_sprite_sheet, scale_frames
# Player Class
# -----------------------------

player_sheet = pygame.image.load("assets/DinoSprites - vita.png").convert_alpha()

idle_frames = parse_sprite_sheet(
    sheet=player_sheet, 
    start_x=0,
    start_y=0,
    frame_count=4,
    columns=24,
    rows=1,
    trim_bottom= 2,
    trim_right=4,
    trim_left=4
)

walk_frames = parse_sprite_sheet(
    sheet=player_sheet, 
    start_x=4*24,
    start_y=0,
    frame_count=6,
    columns=24,
    rows=1,
    trim_bottom= 2,
    trim_right=4,
    trim_left=4
)

jump_frames = parse_sprite_sheet(
    sheet=player_sheet, 
    start_x=11*24,
    start_y=0,
    frame_count=1,
    columns=24,
    rows=1,
    trim_bottom= 2,
    trim_right=4,
    trim_left=2
)

hurt_frames = parse_sprite_sheet(
    sheet=player_sheet, 
    start_x=14*24,
    start_y=0,
    frame_count=3,
    columns=24,
    rows=1,
    trim_bottom= 2,    
    trim_right=4,
    trim_left=4 
)

sprint_frames = parse_sprite_sheet(
    sheet=player_sheet, 
    start_x=18*24,
    start_y=0,
    frame_count=6,
    columns=24,
    rows=1,
    trim_bottom= 2
)

idle_frames = scale_frames(idle_frames, 2)
walk_frames = scale_frames(walk_frames, 2)
jump_frames = scale_frames(jump_frames, 2)
hurt_frames = scale_frames(hurt_frames, 2)
sprint_frames = scale_frames(sprint_frames, 2)

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, game):
        super().__init__()
        self.checkpoint_x = x
        self.checkpoint_y = y
        self.lives = 3
        
        self.x = x
        self.y = y
        self.game = game
        self.width = 16
        self.height = 16
        self.walk_speed = 5
        self.sprint_speed = 7

        self.facing_left = False
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
        self.is_walking = False
        self.is_sprinting = False
        self.is_hurt = False
        self.x_vel = 0
        
        self.rect.x, self.rect.y = x, y

    def update(self):
        self.prev_rect = self.rect.copy()
        self.x_vel = 0
        if self.is_sprinting:
            self.x_vel = self.sprint_speed
        elif self.is_walking:
            self.x_vel = self.walk_speed

        if self.moving_left:
            self.is_walking = True
            self.facing_left = True
            self.x_vel = -self.x_vel

        elif self.moving_right:
            self.is_walking = True
            self.facing_left = False
            self.x_vel = self.x_vel


        else: 
            self.x_vel = 0
            self.is_walking  = False
            #self.is_sprinting = False

        self.rect.x += self.x_vel
        
        self.game.check_wall_collisions()

        self.y_vel += 0.5
        self.rect.y += self.y_vel
        self.game.check_vertical_collisions()
        
            
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
        self.y_vel = 0
        self.can_double_jump = True

    def update_frames(self):
        self.animation_count += self.animation_speed

        if self.is_hurt:
            self.frames = hurt_frames
        
        elif not self.on_ground:
            self.frames = jump_frames

        elif self.is_sprinting:
            self.frames = sprint_frames

        elif self.is_walking:
            self.frames = walk_frames

        else:
            self.frames = idle_frames



        if self.animation_count >= 1:
            self.frame_index = self.frame_index + 1 
            self.animation_count = 0

        self.frame_index %= len(self.frames)
        current_frame = self.frames[self.frame_index]

        if self.facing_left:
            current_frame = pygame.transform.flip(current_frame, True, False)

        self.image = current_frame
        self.mask = pygame.mask.from_surface(self.image)
        

    def land(self):
        self.y_vel = 0
        self.on_ground = True
        self.can_double_jump = True