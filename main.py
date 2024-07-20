import pygame 
import time
pygame.init()


''' RGB color '''
back_color = (200,255,255)
black = (0,0,0)
yellow = (255, 255, 0)
blue = (80, 80, 255)
red = (255, 0, 0)
green = (0, 255, 0)

dark_blue = (0, 0, 100)
light_red = (250, 128, 114)
light_green = (200, 255, 200)

''' window object '''
window = pygame.display.set_mode((500, 500))
window.fill(back_color)
clock = pygame.time.Clock()

'''Area class (Parent Class) '''
class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = color

    def color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(window, self.fill_color, self.rect)

    def outline(self, frame_color, thickness):
        pygame.draw.rect(window, frame_color, self.rect, thickness)

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)  

''' Label class (child class) '''
class Label(Area):
    def set_text(self, text, fsize=12, text_color=black):
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)

    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        window.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

''' card sprites '''
cards = list()

num_card = 4

x = 70

start_time = time.time()
cur_time = start_time

''' game interface '''
time_text = Label(x=0, y=0, width=50, height=50, color=back_color)
time_text.set_text(text='Time:', fsize=40, text_color=dark_blue)
time_text.draw(shift_x=20, shift_y=20)

timer = Label(x=50, y=55, width=50, height=40, color=back_color)
timer.set_text(text='0', fsize=40, text_color=dark_blue)
timer.draw(0,0)

point_text = Label(x=380, y=0,width=50, height=50, color=back_color)
point_text.set_text(text='Points:', fsize=40, text_color=dark_blue)
point_text.draw(shift_x=20, shift_y=20)

point = Label(x=430, y=55, width=50, height=40, color=back_color)
point.set_text(text='0', fsize=40, text_color=dark_blue)
point.draw(shift_x=0, shift_y=0)


for i in range(num_card):
    # one card object
    new_card = Label(x, y=170, width=70, height=100, color=yellow)

    new_card.outline(frame_color=blue, thickness=20)
    new_card.set_text(text='CLICK', fsize=25)

    # to add new_card objects into empty list
    cards.append(new_card)

    # increase x position using counter
    x = x + 100

from random import randint

wait = 0

points = 0

'''game loop'''
while True:

    if wait == 0:
        wait = 40 #how many ticks of the label will be in one place
        click = randint(1, num_card)
        for i in range(num_card):
            cards[i].color(yellow)
            if (i + 1) == click:
                cards[i].draw(10, 40)
            else:
                cards[i].fill()
    else:
        wait -= 1

    
    #checking the click on each tick:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            for i in range(num_card):
                #looking for the card that the click hit
                if cards[i].collidepoint(x,y):
                    if i + 1 == click: # if there is a label on the card, we color it green, add a point
                        cards[i].color(green)

                        points =+ 1

                    else: #otherwise color it red, minus a point
                        cards[i].color(red)

                        points =- 1

                    cards[i].fill()

                    point.set_text(text=str(points), fsize=40, text_color=dark_blue)
                    point.draw(0,0 )



    ''' Losing and Winning '''
    new_time = time.time()

    if new_time - start_time  >= 11:
        lose = Label(0, 0, 500, 500, light_red)
        lose.set_text("Time's up!!!", 60, dark_blue)
        lose.draw(110, 180)
        break

    if int(new_time) - int(cur_time) == 1:
        timer.set_text(str(int(new_time - start_time)),40, dark_blue)
        timer.draw(0,0)
        cur_time = new_time

    if points >= 2:
        win = Label(0, 0, 500, 500, light_red)
        win.set_text("You won!!!", 60, dark_blue)
        win.draw(140, 180)
        resul_time = Label(90, 230, 250, 250, light_green)
        resul_time.set_text("Completion time: " + str (int(new_time - start_time)) + " sec", 40, dark_blue)

        resul_time.draw(0, 0)

        break


    pygame.display.update()

    clock.tick(40)

pygame.display.update()
