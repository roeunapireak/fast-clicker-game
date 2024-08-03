import pygame
import time

pygame.init()

''' variables '''
background_color = (200,255,255)
yellow = (255, 255, 0)
black = (0,0,0)
blue = (80, 80, 255)
red = (255, 0, 0)
green = (0, 255, 0)
dark_blue = (0, 0, 100)
light_red = (250, 128, 114)
light_green = (200, 255, 200)


'''' programme window application '''

window = pygame.display.set_mode((500, 500))
window.fill(background_color)

click = pygame.time.Clock()

''' Area Class '''
class Area():
    def __init__(self, x=0, y=0, width=0, height=0, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = color

    def fill(self): # create one ractangle
        pygame.draw.rect(window, self.fill_color, self.rect)

    def outline(self, frame_color, thickness):
        pygame.draw.rect(window, frame_color, self.rect, thickness)

    def color(self, new_color):
        self.fill_color = new_color

    def is_collide(self, x, y):
        return self.rect.collidepoint(x, y)


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

start_time = time.time()
current_time = start_time

''' Game Interface'''
time_text = Label(0,0,50,50,background_color)
time_text.set_text('Time:',40, dark_blue)
time_text.draw(20, 20)

timer = Label(50,55,50,40,background_color)
timer.set_text('0', 40, dark_blue)
timer.draw(0,0)

score_text = Label(380,0,50,50,background_color)
score_text.set_text('Point:',45, dark_blue)
score_text.draw(20,20)
 
score = Label(430,55,50,40,background_color)
score.set_text('0', 40, dark_blue)
score.draw(0,0)

from random import randint

wait = 0

points = 0

''' game loop '''
while True:

    new_time = time.time()

    # if new_time - start_time  >= 11:
    #     win = Label(0, 0, 500, 500, light_red)
    #     win.set_text("Time's up!!!", 60, dark_blue)
    #     win.draw(110, 180)
    #     break
    
    if int(new_time) - int(current_time) == 1: 
        timer.set_text(str(int(new_time - start_time)),40, dark_blue)
        timer.draw(0,0)
        current_time = new_time

    # if points >= 5:
    #     lose = Label(0, 0, 500, 500, light_green)
    #     lose.set_text("You won!!!", 60, dark_blue)
    #     lose.draw(140, 180)

    #     resul_time = Label(90, 230, 250, 250, light_green)
    #     resul_time.set_text("Completion time: " + str (int(new_time - start_time)) + " sec", 40, dark_blue)
    #     resul_time.draw(0, 0)

    #     break


    if wait == 0:
        wait = 20
        random_index = randint(1, num_cards)

        for index in range(num_cards):
            cards[index].color(yellow)

            if (index + 1) == random_index:
                cards[index].draw(10, 40)

            else:
                cards[index].fill()
    else:
        wait -= 1


    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x,y = event.pos
        
            for index in range(num_cards):

                if cards[index].is_collide(x, y):
                    
                    # if clicked then show GREEN, if not show RED
                    if (index + 1) == random_index:
                        cards[index].color(green)

                        points += 1

                    else:
                        cards[index].color(red)
                        
                        points -= 1

                    cards[index].fill()

                    score.set_text(str(points), 40, dark_blue)
                    score.draw(0, 0)


    pygame.display.update()

    click.tick(40)

# pygame.display.update()