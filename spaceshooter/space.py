import pygame
import params


class Sprite:

    def __init__(self, texture, xy=None):
        if xy is None:
            xy = [0, 0]
        self.img = pygame.image.load(texture)
        self.rect = self.img.get_rect()
        self.rect.x = xy[0]
        self.rect.y = xy[1]
        self.speed = [0, 0]
        self.direction = [0, 0]

    def move(self):
        self.rect.move_ip(self.speed[0]*self.direction[0], self.speed[1]*self.direction[1])

    def render(self, screen):
        screen.blit(self.img, (self.rect.x, self.rect.y))


class Player(Sprite):

    missile_speed = 1
    fire_delay = 0

    def __init__(self, speed=0.5):
        super().__init__(params.player_ship)
        self.rect.x = 1
        self.rect.y = params.SIZE_Y - self.img.get_height()
        self.speed = [speed, 0]
        self.missiles = []


    def update(self):
        Player.fire_delay -= 1
        self.move()
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > params.SIZE_X - self.img.get_width():
            self.rect.x = params.SIZE_X - self.img.get_width()
        self.missiles[:] = [mis for mis in self.missiles if mis.update()]

    def render(self, screen):
        super().render(screen)
        for mis in self.missiles:
            mis.render(screen)

    def shoot(self):
        if Player.fire_delay <= 0:
            self.missiles.append(Missile([self.rect.x+self.img.get_width()/2, self.rect.y]))
            Player.fire_delay = params.player_fire_delay


class Missile(Sprite):

    speed = 2

    def __init__(self, xy):
        super().__init__(params.missile, xy)
        self.object = pygame.image.load(params.missile)
        self.rect.x = self.rect.x - self.object.get_width()/2
        self.speed = [0, Missile.speed]
        self.direction = [0, -1]

    def update(self):
        if self.rect.y < 0:
            return False
        self.move()
        return True


class Ufo(Sprite):

    speed = 1

    def __init__(self, xy):
        super().__init__(params.ufo_one, xy)
        self.speed = [0, Ufo.speed]
        self.direction = [0, 1]
        self.move_delay = 5

    def update(self, missiles):

        if self.rect.y > params.SIZE_Y:
            return False
        if self.move_delay <= 0:
            self.move()
            self.move_delay = 5
        else:
            self.move_delay -= 1
        if self.collide_bullets(missiles) == 1:
            return False
        return True

    def render(self, screen):
        super().render(screen)

    def collide_bullets(self, missiles):
        for mis in missiles:
            return mis.rect.colliderect(self.rect)
