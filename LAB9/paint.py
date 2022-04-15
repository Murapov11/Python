import pygame
import time

pygame.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clock = pygame.time.Clock()

prev,cur = None,None
screen.fill(WHITE)
# background is white !!!

game_over = False 
mode = 'pen' # по - дефоулту
color = BLUE  # по-дефоулту


#color selection
surf2 = pygame.Surface((80,20))
surf2.fill(WHITE)

# DRAW a rectangle to choose a color 
pygame.draw.rect(surf2,RED,(60,0,20,20))  
pygame.draw.rect(surf2,(255,232,0),(40,0,20,20))
pygame.draw.rect(surf2,BLACK,(20,0,20,20))
pygame.draw.rect(surf2,GREEN,(0,0,20,20))

screen.blit(surf2,(420,0)) # blit colors to the main surfaces 
while not game_over:
    surf = pygame.Surface((SCREEN_WIDTH,SCREEN_HEIGHT),pygame.SRCALPHA) # surface transparent !!!
    # simple loop
    for event in pygame.event.get():
        # condition for quit
        if event.type == pygame.QUIT:
            game_over = True

        #if mode will be romb
        if mode == 'romb':
            if event.type == pygame.MOUSEBUTTONDOWN:
                prev = pygame.mouse.get_pos() # taking a mousebottondoun position
            if event.type == pygame.MOUSEMOTION:
                if prev:
                   cur = pygame.mouse.get_pos() # taking a current position 
                   x = max(abs(prev[0]-cur[0]),abs(prev[1]-cur[1])) # to get maximum betbeen X and Y
                   # we draw TWO TRIANGLES and add it together
                   pygame.draw.polygon(surf, color, [ (prev[0] + (x/2),prev[1]), (prev[0],prev[1] + (x/2)), (prev[0] + x,prev[1] + (x/2))])
                   pygame.draw.polygon(surf, color, [  (prev[0] + (x/2),prev[1] + x), (prev[0],prev[1] + (x/2)), (prev[0] + x,prev[1] + (x/2) )])
                   screen.blit(surf,(0,0))
                   pygame.display.update()
                   time.sleep(0.09999)
                   # ERAZE OUR TRIANGLE
                   pygame.draw.polygon(screen, WHITE, [ (prev[0] + (x/2),prev[1]), (prev[0],prev[1] + (x/2)), (prev[0] + x,prev[1] + (x/2))])
                   pygame.draw.polygon(screen, WHITE, [  (prev[0] + (x/2),prev[1] + x), (prev[0],prev[1] + (x/2)), (prev[0] + x,prev[1] + (x/2) )])
             
            if event.type == pygame.MOUSEBUTTONUP:
                    # finally draw our romb
                   pygame.draw.polygon(surf, color, [  (prev[0] + (x/2),prev[1] + x), (prev[0],prev[1] + (x/2)), (prev[0] + x,prev[1] + (x/2) )])
                   pygame.draw.polygon(surf, color, [ (prev[0] + (x/2),prev[1]), (prev[0],prev[1] + (x/2)), (prev[0] + x,prev[1] + (x/2))])
                   screen.blit(surf,(0,0))
                   pygame.display.update()
                   time.sleep(0.09999)
                   prev = None 
    # if mode will be equal triangle 
        if mode == 'equaltri':
            if event.type == pygame.MOUSEBUTTONDOWN:
                prev = pygame.mouse.get_pos() # taking a mouse botton position 
            if event.type == pygame.MOUSEMOTION:
                if prev:
                   cur = pygame.mouse.get_pos() # taking a current position 
                   x = max(abs(prev[0]-cur[0]),abs(prev[1]-cur[1])) # maximum size between x and y
                   # DRAW a TRIANGLE
                   pygame.draw.polygon(surf, color, [(prev[0],prev[1]+x), (prev[0] + (x/2),prev[1]), (prev[0] + x,prev[1] + x)])
                   screen.blit(surf,(0,0))
                   pygame.display.update()
                   time.sleep(0.09999)
                   # eREAZE TRIANGLE
                   pygame.draw.polygon(screen, WHITE, [(prev[0],prev[1]+x), (prev[0] + (x/2),prev[1]), (prev[0] + x,prev[1] + x)])
            if event.type == pygame.MOUSEBUTTONUP:
                # finally blitting a triangle 
                   pygame.draw.polygon(surf, color, [(prev[0],prev[1]+x), (prev[0] + (x/2),prev[1]), (prev[0] + x,prev[1] + x)])
                   screen.blit(surf,(0,0))
                   pygame.display.update()
                   time.sleep(0.09999)
                   prev = None 
            # if mode will be right triangle 
        if mode == 'right':
            if event.type == pygame.MOUSEBUTTONDOWN:
                prev = pygame.mouse.get_pos() # taking a  mousebottondown positions 
            if event.type == pygame.MOUSEMOTION:
                if prev:
                   cur = pygame.mouse.get_pos()  # taking a current position
                   # draw righttri as 3 lines
                   pygame.draw.line(surf,color,prev,cur)
                   pygame.draw.line(surf,color,prev,(prev[0],cur[1]))
                   pygame.draw.line(surf,color,(prev[0],cur[1]),cur)
                   screen.blit(surf,(0,0))
                   pygame.display.update()
                   time.sleep(0.099999)
                   #eraze lines
                   pygame.draw.line(screen,WHITE,prev,cur)
                   pygame.draw.line(screen,WHITE,prev,(prev[0],cur[1]))
                   pygame.draw.line(screen,WHITE,(prev[0],cur[1]),cur)
            if event.type == pygame.MOUSEBUTTONUP:
                # finally blitting
                   pygame.draw.line(screen,color,prev,cur)
                   pygame.draw.line(screen,color,prev,(prev[0],cur[1]))
                   pygame.draw.line(screen,color,(prev[0],cur[1]),cur)
                   prev = None 
            # if mode will be square 
        if mode == 'square':
            if event.type == pygame.MOUSEBUTTONDOWN:
                prev = pygame.mouse.get_pos() # taking a mousebottondown position 
            if event.type == pygame.MOUSEMOTION:
                if prev:
                    cur = pygame.mouse.get_pos() # taking a current position
                    # draw a square
                    pygame.draw.rect(surf,color,(min(prev[0],cur[0]),min(prev[1],cur[1]),max(abs(prev[0]-cur[0]),abs(prev[1]-cur[1])),max(abs(prev[0]-cur[0]),abs(prev[1]-cur[1]))))
                    screen.blit(surf,(0,0))
            if event.type == pygame.MOUSEBUTTONUP:
                # finally blitting
                screen.blit(surf,(0,0))
                prev = None 
        #if mode will be eraser
        if mode == 'eraser':
            if event.type == pygame.MOUSEBUTTONDOWN :
                prev = pygame.mouse.get_pos() # taking a mousebottondown coordinate
            if event.type == pygame.MOUSEMOTION:
                if prev:
                    cur = pygame.mouse.get_pos() # taking a current mouse position
                    pygame.draw.line(screen,WHITE,prev,cur,5) # drawing line with White color
                    prev = cur 
            if event.type == pygame.MOUSEBUTTONUP:
                prev = None
                # if mode will be pen
        if mode == 'pen':
            if event.type == pygame.MOUSEBUTTONDOWN :
                prev = pygame.mouse.get_pos() # taking a mousebottondown coordinate
            if event.type == pygame.MOUSEMOTION:
                if prev:
                    cur = pygame.mouse.get_pos() # taking a current mouse position
                    pygame.draw.line(screen,color,prev,cur,1) # drawing line with " color "
                    prev = cur 
            if event.type == pygame.MOUSEBUTTONUP:
                prev = None
                # if mode circle 
        if mode == 'circle':
            if event.type == pygame.MOUSEBUTTONDOWN:
                prev = pygame.mouse.get_pos()# taking a mousebottondown coordinate

            if event.type == pygame.MOUSEMOTION:
                if prev:
                    cur = pygame.mouse.get_pos() # taking a current mouse position
                    # draw ellipse to the transparent surface
                    pygame.draw.ellipse(surf,color,(min(prev[0],cur[0]),min(prev[1],cur[1]),abs(cur[0]-prev[0]),abs(cur[1]-prev[1])),3) 
                    screen.blit(surf,(0,0))
                    pygame.display.update()
                    time.sleep(0.099999)
                    pygame.draw.ellipse(screen,WHITE,(min(prev[0],cur[0]),min(prev[1],cur[1]),abs(cur[0]-prev[0]),abs(cur[1]-prev[1])),3) 



            if event.type == pygame.MOUSEBUTTONUP:
                # final blitting. With out White color blitting.
                pygame.draw.ellipse(screen,color,(min(prev[0],cur[0]),min(prev[1],cur[1]),abs(cur[0]-prev[0]),abs(cur[1]-prev[1])),3) 
                screen.blit(surf,(0,0))
                prev = None   

        if mode == 'rect':
            if event.type == pygame.MOUSEBUTTONDOWN :
                prev = pygame.mouse.get_pos() # taking a mousebuttondown position
            if event.type == pygame.MOUSEMOTION:
                if prev:
                    cur = pygame.mouse.get_pos()
                    # DRAW rectangle to transparent surface 
                    pygame.draw.rect(surf,color,(min(prev[0],cur[0]),min(prev[1],cur[1]),abs(cur[0]-prev[0]),abs(cur[1]-prev[1])),3) 
                    screen.blit(surf,(0,0))
                    pygame.display.update()
                    time.sleep(0.099999)
                    # update with white color
                    pygame.draw.rect(screen,WHITE,(min(prev[0],cur[0]),min(prev[1],cur[1]),abs(cur[0]-prev[0]),abs(cur[1]-prev[1])),3) 
            if event.type == pygame.MOUSEBUTTONUP:
                # final blitting
                pygame.draw.rect(surf,color,(min(prev[0],cur[0]),min(prev[1],cur[1]),abs(cur[0]-prev[0]),abs(cur[1]-prev[1])),3) 
                screen.blit(surf,(0,0))
                prev = None

        # COLOR SELECTION 
        if event.type == pygame.MOUSEBUTTONDOWN :
           x = pygame.mouse.get_pos()
           #print(x,x[0],x[1])
           # condition with coordinates to choose a color
           if  x[0] >= 420 and x[0] <= 440 and x[1] >= 0 and x[1] <= 20:
               color = GREEN
               print('color is green')
           if  x[0] >= 440 and x[0] <= 460 and x[1] >= 0 and x[1] <= 20:
               color = BLACK
               print('color is black ')

           if  x[0] >= 460 and x[0] <= 480 and x[1] >= 0 and x[1] <= 20:
               color = (255,232,0)
               print('color is Yellow')

           if  x[0] >= 480 and x[0] <= 500 and x[1] >= 0 and x[1] <= 20:
               color = RED
               print('color is RED')
        
        # MODE SELECTION
        # mode conditions with keyboard.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_u:
                mode = 'romb'
            if event.key == pygame.K_q:
                mode = 'equaltri'
            if event.key == pygame.K_t:
                mode = 'right'
            if event.key == pygame.K_r:
                mode = 'rect'
            if event.key == pygame.K_e:
                mode = 'eraser'
            if event.key == pygame.K_c:
                mode = 'circle'
            if event.key == pygame.K_p:
                mode = 'pen'
            if event.key == pygame.K_s:
                mode = 'square'
    #print(mode)
    #print(pygame.mouse.get_pos())
    pygame.display.update()
    clock.tick(30)
pygame.quit()