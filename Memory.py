# implementation of card game - Memory

import simplegui
import random


# helper function to initialize globals
def new_game():
    global n, expose, l1, state, turn, c1, c2
    state, turn = 0, 0  
    l1=range(8)
    l1.extend(range(8))
    random.shuffle(l1)
    expose = [False] * 16
     
# define event handlers
def mouseclick(pos):
    global n, expose, l1, state, turn, c1, c2
    n = list(pos)[0]//50
    if not expose[n]:
        if state == 0:
            c1 = n
            expose[n] = True
            state = 1
        elif state == 1:
            c2 = n
            expose[n] = True
            state = 2
            turn += 1
            label.set_text("Turns = " + str(turn))
        else:
            if l1[c1] != l1[c2]:
                expose[c1] = False
                expose[c2] = False
            c1 = n
            expose[n] = True
            state = 1
                

def draw(canvas):
    for i in range(16):
        if expose[i]:
            canvas.draw_text(str(l1[i]),(12+50*i,65), 50, 'White')          
        else:
            canvas.draw_polygon([(50*i, 0), (50*(i+1), 0), (50*(i+1), 100),(50*i, 100)], 2, 'Orange', 'Green')
    label.set_text("Turns = " + str(turn))




# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)


# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric