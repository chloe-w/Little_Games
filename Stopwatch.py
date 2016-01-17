# template for "Stopwatch: The Game"
import simplegui

# define global variables
t = 0
A = 0
B = 0
C = 0
D = 0
x = 0
y = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global A, B, C, D
    A = t // 600
    S = (t - A * 600) // 10
    B = S // 10
    C = S % 10
    D = t - A * 600 - S * 10
    return str(A) + ":"+ str(B) + str(C) + ":" + str(D)    
            
# define event handlers for buttons; "Start", "Stop", "Reset"
def button_handler1():
    timer.start()
    global check
    check = True
    
def button_handler2():
    timer.stop()
    global x, y
    global check
    if check is True:
        check = False
        y += 1
        if D == 0:
            x += 1
        
def button_handler3():
    global t, x, y
    timer.stop()
    t = 0
    x = 0
    y = 0
    
# define event handler for timer with 0.1 sec interval
def timer_handler():
    global t
    t += 1
    print t

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(t), [70,105], 24, "Red")
    canvas.draw_text(str(x) + "/" + str(y), [170,20], 18, "Red")

    # create frame
frame = simplegui.create_frame("Stopwatch", 200,200)

# register event handlers
timer = simplegui.create_timer(100, timer_handler)
button1 = frame.add_button("Start", button_handler1)
button2 = frame.add_button("Stop", button_handler2)
button3 = frame.add_button("Reset", button_handler3)
frame.set_draw_handler(draw_handler)


# start frame
frame.start()

# Please remember to review the grading rubric

