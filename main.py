import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

block_colour = (53,115,255)

car_width = 73

game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Keepy Uppy!')
clock = pygame.time.Clock()

dog_img = pygame.image.load('dog.png')

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(count), True, black)
    game_display.blit(text, (0,0))

def things(thing_x, thing_y, thing_w, thing_h, colour):
    pygame.draw.rect(game_display, colour, [thing_x, thing_y, thing_w, thing_h])

def dog(x, y):
    game_display.blit(dog_img, (x,y))

def text_objects(text, font):
    text_surface = font.render(text, True, black)
    return text_surface, text_surface.get_rect()

def message_display(text):
    large_text = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, large_text)
    TextRect.center = ((display_width / 2), (display_height / 2))
    game_display.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()

def crash():
    message_display('You crashed!')

def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        game_display.fill(white)
        large_text = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("Keepy Uppy!", large_text)
        TextRect.center = ((display_width / 2), (display_height / 2))
        game_display.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(15)

