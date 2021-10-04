import sys, pygame, random, time
from collections import deque
pygame.init()
pygame.font.init()
pygame.display.init()
size = width, height = 495, 495
green = (0,128,0)
black = (0, 0, 0)
red = (128, 0, 0)
white = (128, 128, 128)
fps_controller = pygame.time.Clock()
stage = pygame.display.set_mode(size)
pygame.display.set_caption('Python Snake')
stage.fill(black)
snk = deque()
snk_len = 3
tick_counter = 0
game_over = False
food = ''
food_exists = False
direction = 'right'
done = False
MOVEEVENT, t, trail = pygame.USEREVENT+1, 100, []
pygame.time.set_timer(MOVEEVENT, t)
score_font = pygame.font.Font('freesansbold.ttf', 15)

def your_score(score):
    text_size = [0, 0, 105, 13]
    pygame.draw.rect(stage, black, text_size)
    value = score_font.render("Your Score: " + str(score), True, white)
    stage.blit(value, [0, 0])

def draw_food():
    global food_exists
    global food
    food_check = False
    if not food_exists:
        f = 0
        x_food = random.randrange(0, 476, 25)
        y_food = random.randrange(0, 476, 25)
        for x in snk:
            if x_food == x.x_pos and y_food == x.y_pos:
                f = 1
        if f == 0:
            food = pygame.draw.rect(stage, red, (x_food, y_food, 20, 20))
            food_exists = True
def draw_snk(left, top):
    snk_size = left, top, 20 , 20
    pygame.draw.rect(stage, green, snk_size)
    pygame.display.update()
    return pygame.draw.rect(stage, green, snk_size)
class snk_bod(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = draw_snk(x_pos, y_pos)
        self.rect = draw_snk(x_pos, y_pos)
        self.x_pos = x_pos
        self.y_pos = y_pos
    def is_collided_with(self, sprite):
       return self.rect.colliderect(sprite) 
    def __del__(self):
        self.kill()
def snk_init():
    global food_exists
    global game_over
    global direction
    snk.append(snk_bod(250, 250)) 
    snk.append(snk_bod(225, 250)) 
    snk.append(snk_bod(200, 250))
    food_exists = False
    direction = 'right'
    game_over = False
def tick():
    global food_exists
    global food
    draw_food()
    global tick_counter
    if not game_over:
        global food
        global food_exists
        global done
        your_score(len(snk) - 3)
        pygame.display.update()
        if snk[0].is_collided_with(food):
            food_exists = False
            snk.append(snk_bod(snk[-1].x_pos, snk[-1].y_pos))
        for x in snk:
            if snk.index(x) != 0:
                if x.x_pos == snk[0].x_pos and x.y_pos == snk[0].y_pos:
                    game_over_func()
                    break
        if not (495 >= snk[0].x_pos >= 0):
            game_over_func()
        if not (495 >= snk[0].y_pos >= 0):
            game_over_func() 
        if direction == 'left':
            #snk_bod(snk[0].x_pos - 25, snk[0].y_pos)
            x = snk_bod(snk[0].x_pos - 25, snk[0].y_pos)
            snk.appendleft(x)
            snk_pop = snk.pop()
            pygame.draw.rect(stage, black, (snk_pop.x_pos, snk_pop.y_pos, 20, 20))
            snk_pop.__del__()
            
        elif direction == 'right':
            #snk_bod(snk[0].x_pos + 25, snk[0].y_pos)
            x = snk_bod(snk[0].x_pos + 25, snk[0].y_pos)
            snk.appendleft(x)
            snk_pop = snk.pop()
            pygame.draw.rect(stage, black, (snk_pop.x_pos, snk_pop.y_pos, 20, 20))
            snk_pop.__del__()

        elif direction == 'up':
            #snk_bod(snk[0].x_pos, snk[0].y_pos - 25)
            x = snk_bod(snk[0].x_pos, snk[0].y_pos - 25)
            snk.appendleft(x)
            snk_pop = snk.pop()
            pygame.draw.rect(stage, black, (snk_pop.x_pos, snk_pop.y_pos, 20, 20))
            snk_pop.__del__()
            
        elif direction == 'down':
            #snk_bod(snk[0].x_pos, snk[0].y_pos + 25)
            x = snk_bod(snk[0].x_pos , snk[0].y_pos + 25)
            snk.appendleft(x)
            snk_pop = snk.pop()
            pygame.draw.rect(stage, black, (snk_pop.x_pos, snk_pop.y_pos, 20, 20))
            snk_pop.__del__()
        
snk_init()
def game_over_func():
    global snk
    global tick_counter
    global game_over
    game_over = True
    stage.fill('black')
    snk = []
    snk = deque()
    tick_counter = 0
    snk_init()

while not done:
    if not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                game_over = True
            elif (pygame.key.get_pressed()[pygame.K_q]):
                done = True
                game_over = True
            elif event.type == MOVEEVENT:
                tick()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if direction != 'right' and 'left':
                        direction = 'left'
                        time.sleep(.03)
                elif event.key == pygame.K_RIGHT:
                    if direction != 'left' and 'right':
                        direction = 'right'
                        time.sleep(.03)
                elif event.key == pygame.K_UP:
                    if direction != 'down' and 'up':
                        direction = 'up'
                        time.sleep(.03)
                elif event.key == pygame.K_DOWN:
                    if direction != 'up' and 'down':
                        direction = 'down'
                        time.sleep(.03)
    
    # Refresh game screen
    pygame.display.update()
    # Refresh rate
    fps_controller.tick(50)
    
    