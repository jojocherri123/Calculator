
#importing required Modules
#Pygame website: https://www.pygame.org/
import pygame
from pygame.locals import *
import time
import math

#creating a function OUTSIDE the class for square root
def sqrt(b):
        a=math.sqrt(b)
        return a

#creating a Main class for the calculator
class Main():
    #initializing pygame
    def __init__(self):
        pygame.init()

    #main loop
    def run(self):
        #resolution of the window
        self.rez = 500,600
        self.Display = pygame.display.set_mode((self.rez))
        #setting an icon
        pygame.display.set_icon(pygame.image.load('Icon.png'))
        #setting a caption
        pygame.display.set_caption("Calculator")

        #variables for equatoin and the answer of the equation
        self.equation = ""
        self.answer = None

        #identifying if window should or should not be running
        running = True
        #regular while loop
        while running:
            #looking for pygame events like, mouse click/move/scroll, closing the window, and keyboard typing
            for event in pygame.event.get():
                #the quit event which would set running to false, quiting the window
                if event.type == pygame.QUIT:
                    running = False 

            #making a grey background
            self.Display.fill((200,200,200))
            
            #using the button function (bellow you will find it) creating buttons
            #the action is what the button does (we set functions obviously, you will find them bellow too)
            #lambda makes python treat the function like the function and not execute it immediatly, only when called
            self.button("0",100,500,100,100,(0,0,0),(100,100,100), action=lambda: self.EditEquation("0"))
            self.button("1",000,400,100,100,(0,0,0),(100,100,100), action=lambda: self.EditEquation("1"))
            self.button("2",100,400,100,100,(0,0,0),(100,100,100), action=lambda: self.EditEquation("2"))
            self.button("3",200,400,100,100,(0,0,0),(100,100,100), action=lambda: self.EditEquation("3"))
            self.button("4",000,300,100,100,(0,0,0),(100,100,100), action=lambda: self.EditEquation("4"))
            self.button("5",100,300,100,100,(0,0,0),(100,100,100), action=lambda: self.EditEquation("5"))
            self.button("6",200,300,100,100,(0,0,0),(100,100,100), action=lambda: self.EditEquation("6"))
            self.button("7",000,200,100,100,(0,0,0),(100,100,100), action=lambda: self.EditEquation("7"))
            self.button("8",100,200,100,100,(0,0,0),(100,100,100), action=lambda: self.EditEquation("8"))
            self.button("9",200,200,100,100,(0,0,0),(100,100,100), action=lambda: self.EditEquation("9"))

            self.button("+",300,500,100,100,(0,0,0),(100,100,100),action =lambda: self.EditEquation("+"))
            self.button("-",300,400,100,100,(0,0,0),(100,100,100),action =lambda: self.EditEquation("-"))
            self.button("×",300,300,100,100,(0,0,0),(100,100,100),action =lambda: self.EditEquation("*"))
            self.button("÷",300,200,100,100,(0,0,0),(100,100,100),action =lambda: self.EditEquation("/"))
            self.button("Sqrt",400,200,100,100,(0,0,0),(100,100,100),action =lambda: self.EditEquation("sqrt("))
            self.button("(",400,300,100,100,(0,0,0),(100,100,100),action =lambda: self.EditEquation("("))
            self.button(")",400,400,100,100,(0,0,0),(100,100,100),action =lambda: self.EditEquation(")"))
            self.button(".",400,500,100,100,(0,0,0),(100,100,100),action =lambda: self.EditEquation("."))
            self.button("C",000,500,100,100,(0,0,0),(100,100,100),action =lambda: self.Clear())
            self.button("=",200,500,100,100,(0,0,0),(100,100,100),action =lambda: self.evaluate(self.equation))

            # making a text displaying the equation
            font = pygame.font.SysFont('', 60)
            img = font.render(str(self.equation), True, (0,0,0))
            self.Display.blit(img, (0, 0))

            # making a test displaying the final result of the equation
            sum = pygame.font.SysFont('', 30)
            img1 = sum.render(str(self.answer), True, (0,0,0))
            self.Display.blit(img1, (0, 60))

            #updating the screen
            pygame.display.flip()
            pygame.time.wait(30)

    # function to edit the equation
    def EditEquation(self, num):
        self.equation = self.equation + num
    
    # function to clear the equation
    def Clear(self):
        self.equation = ""

    # function to solve the equation
    def evaluate(self, num):
        # if it fails it gives SYNTAX ERROR instead of the answer
        # we do try and except so it doesnt crash the calculator
        try:
            self.answer = eval(self.equation)
        except:
            self.answer = "SYNTAX ERROR"

    # making a text object function for the buttons
    def text_objects(text, font, color):
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()

    # button function
    # msg = message or text on the button
    # x = x coordinate, y = y coordinate, w = width, h = height, ic = color of button
    # ac = color of button when cursor is hovering over it
    # action = action of button when pressed
    def button(self,msg,x,y,w,h,ic,ac,action=None):
        # getting the mouse position
        mouse = pygame.mouse.get_pos()
        # identifying when mouse clicks
        click = pygame.mouse.get_pressed()

        # cheking if the cursor is over the button
        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            pygame.draw.rect(self.Display, ac,(x,y,w,h))
            #if cursor clicks while it's on the button it does the action
            if click[0] == 1 and action != None:
                action()
                time.sleep(0.2)
        # if the cursor is not on the button then it draws the button normaly
        else:
            pygame.draw.rect(self.Display, ic,(x,y,w,h))
        
        # drawing the text on the button
        smallText = pygame.font.Font("freesansbold.ttf",20)
        textSurf, textRect = Main.text_objects(msg, smallText, (0,255,255))
        textRect.center = ( (x+(w/2)), (y+(h/2)) )

        self.Display.blit(textSurf, textRect)

# running the code
if __name__ == "__main__":

    mainRun = Main()
    mainRun.run()
