import pygame
import os
from datetime import datetime
now = datetime.now()
current_minute = now.strftime("%M")
current_second = now.strftime("%S")  #approximately 1 second is equal to 6
current_second = int(current_second)
current_minute = int(current_minute)
print("Current Time is :", current_minute)
_image_library = {}
def centercord(image, angle, x, y):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(center=(x, y)).center)
    return new_rect
def rot_center(image, angle, x, y):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(center=(x, y)).center)
    return rotated_image
def get_image(path):
    global _image_library
    image = _image_library.get(path)
    if image == None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path)
        _image_library[path] = image
    return image
pygame.init()
screen = pygame.display.set_mode((900, 900))
done = False
clock = pygame.time.Clock()
minute = float(670)
second = float(780)
minute = minute-(6*current_minute)
second = second-(6*current_second)
x1 = float(minute)
x2 = float(second)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    x1 = x1-0.00625
    x2 = x2-0.375
    screen.fill((255, 255, 255))
    image0 = get_image('micky.jpg')
    image1 = get_image('image1.png')
    image2 = get_image('mickeyclock2.png')
    screen.blit(rot_center(image0, 0, 10, 10), centercord(image0, 0, 450, 450))
    screen.blit(rot_center(image1, x1, 10, 10), centercord(image1, x1, 450, 450))
    screen.blit(rot_center(image2, x2, 10, 10), centercord(image2, x2, 450, 450))
    pygame.display.flip()
    clock.tick(60)