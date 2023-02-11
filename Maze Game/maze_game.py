from pygame import *

win_width = 700
win_height = 500

class GameSprite():
    def method():
        print("Hello World")

    def reset():
        print("Reset")

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def reset():
        GameSprite.reset()

class Enemy(GameSprite):
    def update(self):
        if (self.rect.x > 10):
            self.rect.x -= self.speed
        if (self.rect.x < -10):
            self.rect.x += self.speed
    def reset():
        GameSprite.reset()   


class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height, width, height):
        super().__init__()
        self.color_1 = color_1
        self.width = width
        self.height = height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



window = display.set_mode((win_width, win_height))
display.set_caption("Catch-up")
background = transform.scale(image.load("background.jpg"), (win_width, win_height))

game = True
player = Player()
monster = Enemy()

while game:
    window.blit(background,(0, 0))
    monster.update()
    for e in event.get():
        if e.type == QUIT:
            game = False
            player.reset()
            monster.reset()

    if (key.get_pressed()):
        player.update()    
        
display.update()