import pygame
from sys import exit
from random import randint, choice


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk_1_ = pygame.image.load('graphics/Marvin_Walk_1.png').convert_alpha()
        player_walk_1 = pygame.transform.scale(player_walk_1_, (80, 70))
        player_walk_2_ = pygame.image.load('graphics/Marvin_Walk_2.png').convert_alpha()
        player_walk_2 = pygame.transform.scale(player_walk_2_, (80, 70))
        self.player_walk = [player_walk_1, player_walk_2]
        self.player_index = 0
        self.player_jump = pygame.image.load('graphics/Marvin_Walk_1.png').convert_alpha()
        self.player_jump = pygame.transform.scale(self.player_jump, (80, 70))

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom=(80, 300))
        self.gravity = 0

        self.jump_sound = pygame.mixer.Sound('audio/jump.wav')
        self.jump_sound.set_volume(0.5)

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
            self.jump_sound.play()
        elif keys[pygame.K_l] and self.rect.bottom >= 300:
            laser = Laser(self.rect)
            all_sprites.add(laser)
            laser_group.add(laser)

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()

        if type == 'fly':
            fly_1 = pygame.image.load('graphics/fly/fly1.png').convert_alpha()
            fly_2 = pygame.image.load('graphics/fly/fly2.png').convert_alpha()
            self.frames = [fly_1, fly_2]
            y_pos = 210
        else:
            snail_1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
            snail_2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
            self.frames = [snail_1, snail_2]
            y_pos = 300

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom=(randint(900, 1100), y_pos))

    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

        def update(self):
            self.animation_state()
            self.rect.x -= 6
            self.destroy()

        def destroy(self):
            if self.rect.x <= -100:
                self.kill()

    class Laser(pygame.sprite.Sprite):
        def __init__(self, player_rect):
            super().__init__()
            laser_image = pygame.image.load('graphics/laser.png').convert_alpha()
            self.image = pygame.transform.scale(laser_image, (30, 10))
            self.rect = self.image.get_rect(midleft=player_rect.midright)
            self.alive = True

        def update(self):
            if self.alive:
                self.rect.x += 10
                if self.rect.x > 800:
                    self.kill()

                # Verificar colisão com obstáculos
                if pygame.sprite.spritecollide(self, obstacle_group, True):
                    self.alive = False
            else:
                self.kill()

    def display_score():
        current_time = int(pygame.time.get_ticks() / 1000) - start_time
        score_surf = test_font.render(f'Score: {current_time}', False, (64, 64, 64))
        score_rect = score_surf.get_rect(center=(400, 50))
        screen.blit(score_surf, score_rect)
        return current_time

    def collision_sprite():
        if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
            obstacle_group.empty()
            return False
        else:
            return True

    pygame.init()
    screen = pygame.display.set_mode((800, 400))
    pygame.display.set_caption('RUN MARVIN RUN')
    clock = pygame.time.Clock()
    test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
    game_active = False
    start_time = 0
    score = 0

    bg_music = pygame.mixer.Sound('audio/music.mp3')
    bg_music.play(loops=-1)

    all_sprites = pygame.sprite.Group()
    player = pygame.sprite.GroupSingle()
    player.add(Player())
    all_sprites.add(player)

    obstacle_group = pygame.sprite.Group()
    laser_group = pygame.sprite.Group()

    sky_surface = pygame.image.load('graphics/sky_.png').convert()
    ground_surface = pygame.image.load('graphics/ground_1.png').convert()

    snail_frame_1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
    snail_frame_2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
    snail_frames = [snail_frame_1, snail_frame_2]
    snail_frame_index = 0
    snail_surf = snail_frames[snail_frame_index]

    fly_frame1 = pygame.image.load('graphics/fly/fly1.png').convert_alpha()
    fly_frame2 = pygame.image.load('graphics/fly/fly2.png').convert_alpha()
    fly_frames = [fly_frame1, fly_frame2]
    fly_frame_index = 0
    fly_surf = fly_frames[fly_frame_index]

    player_walk_1_ = pygame.image.load('graphics/Marvin_Walk_1.png').convert_alpha()
    player_walk_1 = pygame.transform.scale(player_walk_1_, (80, 70))
    player_walk_2_ = pygame.image.load('graphics/Marvin_Walk_2.png').convert_alpha()
    player_walk_2 = pygame.transform.scale(player_walk_2_, (80, 70))
    player_walk = [player_walk_1, player_walk_2]
    player_index = 0
    player_jump = pygame.image.load('graphics/Marvin_Walk_1.png').convert_alpha()

    player_surf = player_walk[player_index]
    player_rect = player_surf.get_rect(midbottom=(80, 300))
    player_gravity = 0

    player_stand = pygame.image.load    ('graphics/Marvin_Walk_1.png').convert_alpha()
    player_stand = pygame.transform.scale(player_stand, (200, 195))
    player_stand_rect = player_stand.get_rect(center=(400, 200))

game_name = test_font.render('Super Marvin', False, 'white')
game_name_rect = game_name.get_rect(center=(400, 80))

game_message = test_font.render('Press space to run', False, 'white')
game_message_rect = game_message.get_rect(center=(400, 330))


obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                    player_gravity = -20

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = int(pygame.time.get_ticks() / 1000)

        if game_active:
            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(choice(['fly', 'snail', 'snail', 'snail'])))

            if event.type == snail_animation_timer:
                if snail_frame_index == 0:
                    snail_frame_index = 1
                else:
                    snail_frame_index = 0
                snail_surf = snail_frames[snail_frame_index]

            if event.type == fly_animation_timer:
                if fly_frame_index == 0:
                    fly_frame_index = 1
                else:
                    fly_frame_index = 0
                fly_surf = fly_frames[fly_frame_index]

    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        score = display_score()

        all_sprites.draw(screen)
        all_sprites.update()

        for laser in laser_group:
            if pygame.sprite.spritecollide(laser, obstacle_group, True):
                laser.alive = False

        game_active = collision_sprite()
    else:
        screen.fill((131, 150, 144))
        screen.blit(player_stand, player_stand_rect)
        obstacle_group.empty()
        player_rect.midbottom = (80, 300)
        player_gravity = 0

        score_message = test_font.render(f'Your Score: {score}', False, 'white')
        score_message_rect = score_message.get_rect(center=(400, 330))
        screen.blit(game_name, game_name_rect)

        if score == 0:
            screen.blit(game_message, game_message_rect)
        else:
            screen.blit(score_message, score_message_rect)

    pygame.display.update()
    clock.tick(60)


