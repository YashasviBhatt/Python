import pygame as pg                         # importing pygame
x = pg.init()                               # initializing all modules of pygame
#print(x)                                    # print a tuple indicating number of successful and unsuccessful modules imported from pygame
# there is no need to return the value in a variable simply typing pg.init() can also work

# setting up the pygame window
# set mode take a tuple as arguments which will take the size of window i.e width and height
gameWindow = pg.display.set_mode((400, 400))
# setting the title of pygame window
pg.display.set_caption('Pygame Learning')

# game specific variables
# since pygame doesn't have any inbuilt function to hold the pygame window open thus we need to create an exit flag
# as soon as the value of exit flag becomes true then the window will close itself too
exit_flag = False                           # setting the default value of exit flag to be False so that it won't close

# creating game loop
while not exit_flag:
    for event in pg.event.get():            # fetching event from event queue (managed by pygame)
        if event.type == pg.QUIT:
            exit_flag = True
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                print('You have pressed Right Arrow Key')
            elif event.key == pg.K_LEFT:
                print('You have pressed Left Arrow Key')
            elif event.key == pg.K_UP:
                print('You have pressed Up Arrow Key')
            elif event.key == pg.K_DOWN:
                print('You have pressed Down Arrow Key')

pg.quit()