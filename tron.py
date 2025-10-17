import pygame
import sys

class Player:
    def __init__(self, name, color, startX, startY, life):
        self.name = name
        self.color = color
        self.x = startX
        self.y = startY
        self.startX = startX
        self.startY = startY
        self.xMouv = 0
        self.yMouv = 0
        self.life = life
        self.start = True
    
    def moveDrawCol(self, screen):
        self.x += self.xMouv
        self.y += self.yMouv
        if self.x < 0 or self.x >= 699 or self.y < 0 or self.y >= 699:
            self.life -= 1
            return False
        color = screen.get_at((self.x, self.y))
        if (color == (0,150,255) or color == (255,150,0)) and not self.start:
            self.life -= 1
            return False
        else:
            pygame.draw.rect(screen, self.color, (self.x, self.y, 3, 3))
            return True

    def direction(self, xMouv, yMouv):
        self.start = False
        self.xMouv = xMouv
        self.yMouv = yMouv

    def setdirection(self):
        return (self.xMouv, self.yMouv)
    
    def setlife(self):
        return self.life
    
    def reset(self):
        self.start = True
        self.x = self.startX
        self.y = self.startY
        self.xMouv = 0
        self.yMouv = 0

    def setname(self):
        return self.name

def textobj(text, font):
    textzone = font.render(text, True, (255,255,255))
    return textzone, textzone.get_rect()

def draw_grid(screen, grid_size=20, color=(0, 60, 120)):
    width, height = screen.get_size()
    for x in range(0, width, grid_size):
        pygame.draw.line(screen, color, (x, 0), (x, height))
    for y in range(0, height, grid_size):
        pygame.draw.line(screen, color, (0, y), (width, y))

print("Name player 1 using arrow keys:")
name1 = input("Player 1 name: ")
p1 = Player(name1, (0,150,255), 500, 300, 2)

print("Name player 2 using WASD:")
name2 = input("Player 2 name: ")
p2 = Player(name2, (255,150,0), 200, 300, 2)

print("Entering the Grid...")

pygame.init()
clock = pygame.time.Clock()
font = pygame.font.SysFont('calibri', 40)
screen = pygame.display.set_mode([700,700])
pygame.display.set_caption("TRON Lightcycles")

screen.fill((5, 5, 15))
draw_grid(screen, grid_size=20, color=(0, 60, 120))
pygame.draw.rect(screen, p1.color, (p1.x, p1.y, 3, 3))
pygame.draw.rect(screen, p2.color, (p2.x, p2.y, 3, 3))
pygame.display.update()

while p1.setlife() > 0 and p2.setlife() > 0:
    go = True
    while go:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and p1.setdirection()[1] != 3:
                    p1.direction(0, -3)
                elif event.key == pygame.K_RIGHT and p1.setdirection()[0] != -3:
                    p1.direction(3, 0)
                elif event.key == pygame.K_DOWN and p1.setdirection()[1] != -3:
                    p1.direction(0, 3)
                elif event.key == pygame.K_LEFT and p1.setdirection()[0] != 3:
                    p1.direction(-3, 0)
                if event.key == pygame.K_w and p2.setdirection()[1] != 3:
                    p2.direction(0, -3)
                elif event.key == pygame.K_d and p2.setdirection()[0] != -3:
                    p2.direction(3, 0)
                elif event.key == pygame.K_s and p2.setdirection()[1] != -3:
                    p2.direction(0, 3)
                elif event.key == pygame.K_a and p2.setdirection()[0] != 3:
                    p2.direction(-3, 0)
        if not p1.moveDrawCol(screen) or not p2.moveDrawCol(screen):
            screen.fill((5, 5, 15))
            draw_grid(screen, grid_size=20, color=(0, 60, 120))
            p1.reset()
            p2.reset()
            pygame.draw.rect(screen, p1.color, (p1.x, p1.y, 3, 3))
            pygame.draw.rect(screen, p2.color, (p2.x, p2.y, 3, 3))
            pygame.display.update()
            go = False
        textgnd, textbox = textobj(f"{p1.setname()}: {p1.setlife()}      {p2.setname()}: {p2.setlife()}", font)
        textbox.center = (350, 40)
        screen.blit(textgnd, textbox)
        pygame.display.update()
        clock.tick(60)

if p1.setlife() == 0:
    winner = p2.setname()
else:
    winner = p1.setname()

screen.fill((5, 5, 15))
draw_grid(screen, grid_size=20, color=(0, 60, 120))
textgnd, textbox = textobj(winner + " won!", font)
textbox.center = (350,350)
screen.blit(textgnd, textbox)
pygame.display.update()
pygame.time.wait(3000)
pygame.quit()
