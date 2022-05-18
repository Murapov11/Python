# importing modules 
import pygame
import random
pygame.init() # initializing pygame

import psycopg2

#DEFAULT
score = 0
level = 1

conn = psycopg2.connect(

            host='localhost',
            database='snake',
            user='postgres',
            password='yerkhan2003',
)
cursor = conn.cursor()

username = input('Please enter your username \n')
sql1 = f"select * from snaketable where username = '{username}'"
cursor.execute(sql1)
levs = cursor.fetchall()

if len(levs) == 0:
  print('INSERTING')
  sql2 = f"insert into snaketable(username,score,level) values ('{username}','0','1')"
  cursor.execute(sql2)
  conn.commit()
  score = 0
  level = 1
else:
  score = int(levs[0][1])
  level = int(levs[0][2])


WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
BLOCK_SIZE = 20 
screen = pygame.display.set_mode((500,500)) # create a screen 

# RGB --> COLORS
WHITE = (255,255,255)
WHITE_2 = (150,180,250)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

# create class WALL
class Wall():
  def __init__(self):
    self.body = []
    self.create_wall(1)
    
  def create_wall(self,level):
    for i in range(0, 500, 1):
      for j in range (0,level,1):
       self.body.append([i,j])
  
  def draw(self ):
    for x, y in self.body:
      pygame.draw.rect(screen, RED, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)) # drawing wall on the screen


clock = pygame.time.Clock()

#create a Grid with help of drawing rectangle
def draw_grid():
  for i in range(0, WINDOW_WIDTH, BLOCK_SIZE):
    for j in range(0, WINDOW_HEIGHT, BLOCK_SIZE):
      pygame.draw.rect(screen, WHITE_2, (i, j, BLOCK_SIZE, BLOCK_SIZE), 1)

 # create a Food class object.   
class Food:
  def __init__(self):
      self.generate_random_pos()
  
  def my_round(self, value, base=BLOCK_SIZE):
    return base * round(value / base) # to round to the closest begininig point
  
  def generate_random_pos(self):
    self.x = self.my_round(random.randint(0, WINDOW_WIDTH - BLOCK_SIZE))
    self.y = self.my_round(random.randint(0, WINDOW_HEIGHT - BLOCK_SIZE))
    # checking that food do not lye on the wall or snake
    for x in snake.body:
        if (self.y == 0) or (self.x == x[0] and self.y == x[1]):
            self.generate_random_pos()
            break
        
  # the drawing a food 
  def draw(self):
    pygame.draw.rect(screen, BLUE, (self.x, self.y, BLOCK_SIZE, BLOCK_SIZE))

# create a class
class Snake:
  def __init__(self):
      self.body = [[200, 200] , [220, 200]]
      self.dx = BLOCK_SIZE
      self.dy = 0
      self.speed = 3
   #drawing a snake blocks 
  def draw(self):
    for i, (x, y) in enumerate(self.body):
      color = RED if i == 0 else GREEN
      pygame.draw.rect(screen, color, (x , y , BLOCK_SIZE, BLOCK_SIZE))
      #print(x,y)
  
  # move such : last = previous >>>> and head + dx 
  def move(self):
    for i in range(len(self.body) - 1, 0, -1):
      self.body[i][0] = self.body[i - 1][0]
      self.body[i][1] = self.body[i - 1][1]

    self.body[0][0] += self.dx
    self.body[0][1] += self.dy

# creating OBJECTS
snake = Snake()
wall = Wall()
food = Food()

# variables to show level and score


cnt = 0 
pause = False

running = True 
while running:
  font = pygame.font.SysFont('castellar' ,32)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sql3 = f"update snaketable set score = '{score}' , level = '{level}' where username = '{username}'"
      cursor.execute(sql3)
      conn.commit()
      running = False
      # keyboard control
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
          pause = True 
      if event.key == pygame.K_RIGHT:
        snake.dx = BLOCK_SIZE
        snake.dy = 0
      if event.key == pygame.K_LEFT:
        snake.dx = -BLOCK_SIZE
        snake.dy = 0
      if event.key == pygame.K_UP:
        snake.dx = 0
        snake.dy = -BLOCK_SIZE
      if event.key == pygame.K_DOWN:
        snake.dx = 0
        snake.dy = BLOCK_SIZE 
     
  while pause:
      sql3 = f"update snaketable set score = '{score}' , level = '{level}' where username = '{username}'"
      cursor.execute(sql3)
      conn.commit()
      pause_ = font.render('PAUSE',True,(255,0,0))
      screen.blit(pause_,(175,200)) # blit a PAUSE WORD; 
      pygame.display.update()

      for event in pygame.event.get():
          if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                pause = False
# checking of colliding with wall
  if snake.body[0][1] == 0:
      running = False
# checking  WITH  playing area 
  if snake.body[0][0] < 0:
      snake.body[0][0] = 500 
  if snake.body[0][0] > 500:
      snake.body[0][0] = 0
  # eating a food
  if snake.body[0][0]  == food.x and snake.body[0][1]  == food.y:
    snake.body.append([0, 0])
    food.generate_random_pos()
    score += 1
  # level up and speed up conditions
  if score % 3 == 0 and score != cnt :
      snake.speed += 3
      cnt = score
      level += 1
      wall.create_wall(level)
      wall.draw()

  # creating a Font object 
  text_score = font.render(f'SCORE : {score}',True,(255,255,0))
  text_level = font.render(f'LEVEL : {level}',True,(255,255,0))

  screen.fill(BLACK)



  draw_grid()
  snake.draw()
  snake.move()
  wall.draw()
  food.draw()
  screen.blit(text_score,(0,25)) # blit a score 
  screen.blit(text_level,(300,25)) # blit a level
  pygame.display.update()
  clock.tick(snake.speed)