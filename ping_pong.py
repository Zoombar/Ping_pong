from pygame import *
window = display.set_mode((700, 500))
display.set_caption('Ping Pong')
background = transform.scale(image.load('background.jpg'), (700, 500))
win_height = 500
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

game = True

while game:
    window.blit(background, (0,0))

    for e in event.get():
        if e.type == QUIT:
            game = False
    player1.update_l()
    player1.reset()
    player2.update_r()
    player2.reset()
    display.update()
    clock.tick(FPS)
