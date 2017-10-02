#ENTIRE CODE FOR Flying Phoenix
#Created by Suyash Unnithan
import pygame
import time
from random import randint

black = (0,0,0)
white = (255,255,255)
blue = (51, 175, 247)
red = (183, 16, 16)
red2 = (200,0,0)
green = (67, 170, 11)
orange = (242, 143, 21)
bright_red = (255,0,0)
bright_green = (0,255,0)

pygame.init()

surfaceWidth = 800
surfaceHeight = 500

imageHeight = 33
imageWidth = 111

surface = pygame.display.set_mode((surfaceWidth,surfaceHeight))
pygame.display.set_caption('Flying Phoenix')

icon = pygame.image.load('phoenix3.png')
pygame.display.set_icon(icon)

clock = pygame.time.Clock()

#Addition of Phoenix
img = pygame.image.load('phoenix4.png')

#Start menu
def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        surface.blit(background_image, [0,0])
        smallText2 = pygame.font.SysFont('comicsansms',20)
        typTextSurf, typTextRect = makeTextObjs3('Unnithan Games Presents', smallText2)
        typTextRect.center =  surfaceWidth / 2, ((surfaceHeight / 2 - 170))
        surface.blit(typTextSurf, typTextRect)
        
        largeText2 = pygame.font.SysFont('comicsansms',100)
        TextSurf, TextRect = makeTextObjs2("Flying Phoenix", largeText2)
        TextRect.center = ((surfaceWidth/2),(surfaceHeight/2) - 100)
        surface.blit(TextSurf, TextRect)
        
        smallText2 = pygame.font.SysFont('comicsansms',20)
        typTextSurf, typTextRect = makeTextObjs3('Use the UP Arrow Key to Stop Flames the Phoenix from Touching the Ice Poles.', smallText2)
        typTextRect.center =  surfaceWidth / 2, ((surfaceHeight / 2))
        surface.blit(typTextSurf, typTextRect)

        button("Start",340,350,100,50,green,bright_green,main)

        pygame.display.update()
        clock.tick(15)

#Button Function
def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(surface, ac,(x,y,w,h))
        
        if click[0] == 1 and action != None:
            action()
            
    else:
        pygame.draw.rect(surface, ic,(x,y,w,h))

    smallText = pygame.font.SysFont('comicsansms',20)
    textSurf, textRect = makeTextObjs4(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    surface.blit(textSurf, textRect)
    
#Addition of Score
def score(count):
    font = pygame.font.SysFont('comicsansms', 20)
    text = font.render("Score: "+str(count), True, white)
    surface.blit(text, [0,0])

#background photo
background_image = pygame.image.load("background.jpg").convert()

#Adding Ice Poles
def blocks(x_block, y_block, block_width, block_height, gap):
    pygame.draw.rect(surface, blue, [x_block, y_block, block_width, block_height])
    pygame.draw.rect(surface, blue, [x_block, y_block+block_height+gap, block_width, surfaceHeight])

#Replaying or Quiting the Game

def replay_or_quit():
    for event in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT]):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        elif event.type == pygame.KEYDOWN:
            continue

        return event.key
    
    return None

def makeTextObjs2(text, font):
    textSurface = font.render(text, True, orange)
    return textSurface, textSurface.get_rect()

def makeTextObjs3(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def makeTextObjs4(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def makeTextObjs(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def msgSurface(text):
    smallText = pygame.font.SysFont('comicsansms', 20)
    largeText = pygame.font.SysFont('comicsansms', 150)

    titleTextSurf, titleTextRect = makeTextObjs(text, largeText)
    titleTextRect.center = surfaceWidth / 2, surfaceHeight / 2
    surface.blit(titleTextSurf, titleTextRect)

    typTextSurf, typTextRect = makeTextObjs('Press any key to continue', smallText)
    typTextRect.center =  surfaceWidth / 2, ((surfaceHeight / 2) + 100)
    surface.blit(typTextSurf, typTextRect)

    pygame.display.update()
    time.sleep(1)

    while replay_or_quit() == None:
        clock.tick()

    main()

    
#Game over Function

def gameOver():
    msgSurface('You Froze!')
    
def helicopter(x, y, image):
    surface.blit(img, (x,y))

def main():
    #Location of Phoenix at Starting Point on Screen
    x = 150
    y = 200
    y_move = 0

    current_score = 0

    x_block = surfaceWidth
    y_block = 0

    block_width = 75
    block_height = randint(0,(surfaceHeight/2))
    gap = 115
    block_move = 6
    
    game_over = False

    while not game_over:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
#Movement of Phoenix (Up 5 and Down 5)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_move = -5
                    is_shoot = True
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    y_move = 5

        y += y_move

        surface.blit(background_image, [0,0])
        helicopter(x ,y, img)
        
        blocks(x_block, y_block, block_width, block_height, gap)
        x_block -= block_move

        score(current_score)
        
#Boundaries for Phoenix
        if y > surfaceHeight-33 or y < 0:
            gameOver()

        if x_block < (-1*block_width):
            x_block = surfaceWidth
            block_height = randint(0, (surfaceHeight / 2))

        if x + imageWidth > x_block:
            if x < x_block + block_width:
                if y < block_height:
                    if x - imageWidth < block_width + x_block:
                        gameOver()

        if x + imageWidth > x_block:
            if y + imageHeight > block_height+gap:
                if x < block_width + x_block:
                    gameOver()

        if x < x_block and x > x_block - block_move:
            current_score += 1
#Increasing Difficulty
        if 7 <= current_score < 10:
            block_move = 7
            gap = 105
        if 10 <= current_score < 20:
            block_move = 8
            gap = 95
        if 20 <= current_score < 40:
            block_move = 10
            gap = 90
        if 40 <= current_score < 100:
            block_move = 12
            gap = 80
                    
        pygame.display.update()
        clock.tick(60)

game_intro()
main()
pygame.quit()
quit()
