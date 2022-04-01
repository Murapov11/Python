import pygame
pygame.init()
pygame.mixer.init()
screen=pygame.display.set_mode((800, 600))
bg=pygame.transform.scale(pygame.image.load('img.jpg'),(800,600))
mlist=['1.mp3','2.mp3','3.mp3']
stop=False
i=0
def play():
    global i
    if i > len(mlist) - 1:
        i = 0
    if i < 0:
        i = len(mlist) - 1
    pygame.mixer.music.load(mlist[i])
    pygame.mixer.music.play()
while True:
    screen.blit(bg,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            raise SystemExit
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if stop == True:
                pygame.mixer.music.unpause()
            else:
                play()
        if keys[pygame.K_DOWN]:
            pygame.mixer.music.pause()
            stop=True
        if keys[pygame.K_LEFT]:
            i -= 1
            play()
        if keys[pygame.K_RIGHT]:
            i += 1
            play()
        if keys[pygame.K_SPACE]:
            pygame.mixer.music.play(-1)
    pygame.display.update()

