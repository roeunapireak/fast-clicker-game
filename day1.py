import pygame

pygame.init()

''' variables '''
background_color = (200,255,255)
yellow = (255, 255, 0)
black = (0,0,0)
blue = (80, 80, 255)
green = (0, 255, 0)
red = (255, 0, 0)


'''' programme window application '''

window = pygame.display.set_mode((500, 500))
window.fill(background_color)

timer = pygame.time.Clock()

''' Area Class '''
class Area():
    def __init__(self, x=0, y=0, width=0, height=0, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = color

    def fill(self): # create one ractangle
        pygame.draw.rect(window, self.fill_color, self.rect)

    def outline(self, frame_color, thickness):
        pygame.draw.rect(window, frame_color, self.rect, thickness)


''' Label Class '''
class Label(Area):
    def set_text(self, text, fsize=20, text_color=black):
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)

    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        window.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

cards = [] # data storage
num_cards = 4

x = 70

for i in range(num_cards):
   new_card = Label(x, 170, 70, 100, yellow)
   new_card.outline(blue, 10)
   new_card.set_text('CLICK', 26)
   cards.append(new_card)

   x = x + 100

wait = 0

''' game loop '''
while True:

    for card in cards:
        card.draw(10,40)


    pygame.display.update()

    timer.tick(40)

