from pygame import *
window = display.set_mode((700, 500))
display.set_caption('Ping Pong')
background = transform.scale(image.load('background.jpg'), (700, 500))
win_height = 500
speed_x = 3
speed_y = 3
clock = time.Clock()
FPS = 60

class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       sprite.Sprite.__init__(self)
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
 
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
   def update_r(self):
       keys = key.get_pressed()
       if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_DOWN] and self.rect.y < win_height - 150:
           self.rect.y += self.speed
   def update_l(self):
       keys = key.get_pressed()
       if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_s] and self.rect.y < win_height - 150:
           self.rect.y += self.speed


player1 = Player('wall.png', 30, 200,50,150, 4)
player2 = Player('wall.png', 630, 200,50,150, 4)
ball = GameSprite('ball.png',270,130,130,80,4)

game = True
finish = False

font.init()
font1 = font.Font(None, 55)
lose1 = font1.render('PLAYER 1 LOSE!', True, (180, 0, 0))
font2 = font.Font(None, 55)
lose2 = font2.render('PLAYER 2 LOSE!', True, (180, 0, 0))

while game:
    window.blit(background, (0,0))
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y

    if ball.rect.y > win_height-50 or ball.rect.y < 0:
        speed_y *= -1
    
    if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
        speed_x *= -1
    
    if ball.rect.x < 0:
        finish = True
        window.blit(lose1, (200,200))
    
    if ball.rect.x > 700:
        finish = True
        window.blit(lose2, (200,200))

    player1.update_l()
    player1.reset()
    player2.update_r()
    player2.reset()
    ball.reset()
    ball.update()
    display.update()
    clock.tick(FPS)
