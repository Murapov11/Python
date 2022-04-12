#Imports
import pygame, sys
from pygame.locals import *
import random, time

#Initialzing the pygame
pygame.init()

#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()

#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0

#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("AnimatedStreet.png") # loading a backgroud

#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

# Create a Coin class 
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50,50)) # create a surface
        self.image.fill((255,232,0)) # Fill to the yellow color 
        self.rect = self.image.get_rect() # convert to self rect
        self.rect.y = 0
        self.rect.x = random.randint(10,SCREEN_WIDTH-50) #Generate random position for x value
    def move(self):
        self.rect.y += 5 # moving with speed 5
        # if we do not collide with player then again generate on the top 
        if self.rect.y > SCREEN_HEIGHT:
            self.rect.y = 0
            self.rect.x = random.randint(10,SCREEN_WIDTH-10)

# create an Enemy class
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect() # creating a rect object
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0) # creating a random position

      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED) # move_ip it is the rectangle function which help to change the position
        if (self.rect.bottom > 600):
            SCORE += 1 # if we do not collide with player , then + 1 point to the score 
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# PLayer class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect() # create a rect object 
        self.rect.center = (160, 520) # set the center 
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        # moving PLayer object to the right or to the left 
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
                  

#Setting up Sprites        
P1 = Player()
E1 = Enemy()
C1 = Coin()

#Creating Sprites Groups
points = pygame.sprite.Group()
enemies = pygame.sprite.Group()
enemies.add(E1)
points.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000) # each time after 1 second will appear this event
# creating a score to the points 
cnt = 0 
#Game Loop
pygame.mixer.music.load('background.wav')
pygame.mixer.music.play(0)
while True:
   
    #Cycles through all events occuring  
    for event in pygame.event.get():
        # OUR-EVENT 
        if event.type == INC_SPEED:
              SPEED += 0.5    
        # SIMPLE-EVENT    
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

     # blitting our background to the surface 
    DISPLAYSURF.blit(background, (0,0))
    #creating surfaces
    scores = font_small.render(str(SCORE), True, BLACK)
    earnpoints = font_small.render(str(cnt),True,BLACK)
    # bliting the surfaces
    DISPLAYSURF.blit(scores, (10,10))
    DISPLAYSURF.blit(earnpoints,(300,10))
    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)
        
         

    #To be run if collision occurs between Player and COIN
    if pygame.sprite.spritecollide(P1,points,True):
        cnt += 1 # increase the count 
        print(cnt)
        C1 = Coin() # verating a new sprite Coin 
        # adding our Sprite to the Group 
        points.add(C1)
        all_sprites.add(C1)

    #To be run if collision occurs between Player and Enemy

    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.music.stop() # stop the background music 
          pygame.mixer.Sound('crash.wav').play() # playing a crash music 
          time.sleep(1)
                   
          DISPLAYSURF.fill(RED) # fill to the red 
          # blitting surface
          DISPLAYSURF.blit(game_over, (30,250))
          
          pygame.display.update() # updating the display!!!
          for entity in all_sprites:
                entity.kill() # killing the sprite objects 
          time.sleep(2)
          pygame.quit() # quit the pygame 
          sys.exit()        # exit frm python
        
    pygame.display.update()
    FramePerSec.tick(FPS)
