import pygame
from sys import exit

pygame.init()

width = 800
height = 400

bg_music = pygame.mixer.Sound('Assets/Masterpiecev2.mp3')
bg_music.play()
excel_jumps = 0
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('SmartSheet Runner')
clock = pygame.time.Clock()
game_active = True

test_font = pygame.font.Font('Assets/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('Assets/Sky.png').convert()
ground_surface = pygame.image.load('Assets/ground.png').convert()
text_surface = test_font.render('Excel Documents Swerved:' + str(excel_jumps), False, 'Black')
text_rect = text_surface.get_rect(center = (400,50))

excel_surface = pygame.image.load('Assets/excel2.png').convert_alpha()
excel_rect = excel_surface.get_rect(bottomright = (600,300))

gary_surface = pygame.image.load('Assets/Gbot.png').convert_alpha()
gary_rect = gary_surface.get_rect(midbottom = (80,300))

gary_gravity = 0


while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and gary_rect.bottom >= 300:
                gary_gravity = -20.5

    if game_active:

        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface,(0,300))



        screen.blit(text_surface, text_rect)
        excel_rect.x -= 4
        if excel_rect.right <= 0:
            excel_rect.left = 800
            excel_jumps+=1
            text_surface = test_font.render('Excel Documents Swerved:' + str(excel_jumps), False, 'Black')
        screen.blit(excel_surface, excel_rect)

        gary_gravity += 1
        gary_rect.y += gary_gravity
        if gary_rect.bottom >= 300: gary_rect.bottom = 300
        screen.blit(gary_surface, gary_rect)

        #collision
        if excel_rect.colliderect(gary_rect):
            bg_music.stop()
            bg_end = pygame.mixer.Sound('Assets/audiomass-output.mp3')
            bg_end.play()
            game_active = False


    pygame.display.update()
    clock.tick(60)
