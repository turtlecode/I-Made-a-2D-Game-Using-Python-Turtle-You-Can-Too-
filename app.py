import turtle, random

# --- SETUP SCREEN ---
s = turtle.Screen()
s.setup(600, 600)               # Create a 600x600 window
s.title("Catch Game!")          # Window title
s.tracer(0)                     # Turn off auto-updating for smoother animation

# --- CREATE PADDLE ---
p = turtle.Turtle()
p.shape("square")
p.shapesize(1, 5)               # Make it a wide rectangle
p.penup()
p.goto(0, -260)                 # Position near bottom

# --- CREATE BALL ---
b = turtle.Turtle()
b.shape("circle")
b.penup()
b.goto(0, 260)                  # Start near top
b.dy = -6                       # Ball's vertical speed (downward)

# --- SCORE TEXT ---
score = 0
h = turtle.Turtle()
h.hideturtle()
h.penup()
h.goto(-280, 260)
h.write("Score: 0", font=("Arial", 16, "normal"))

# --- MOVE PADDLE FUNCTIONS ---
def left():
    x = p.xcor() - 40
    p.setx(-280 if x < -280 else x)  # Keep paddle inside window

def right():
    x = p.xcor() + 40
    p.setx(280 if x > 280 else x)

s.onkey(left, "Left")
s.onkey(right, "Right")
s.listen()

# --- RESET BALL FUNCTION ---
def reset_ball():
    b.goto(random.randint(-250, 250), 260)  # Random X position at top
    b.dy = -6 - (score // 5)                # Ball gets faster as score increases

# --- GAME OVER SCREEN ---
def game_over():
    h.clear()
    h.goto(0, 0)
    h.write(f"Game Over\nScore: {score}", align="center", font=("Arial", 18, "normal"))

# --- MAIN GAME LOOP ---
def loop():
    global score
    b.sety(b.ycor() + b.dy)                 # Move ball downward
    if b.ycor() < -300:                     # Missed the ball
        game_over()
        s.update()
        return
    if b.distance(p) < 50 and b.ycor() < -200:  # Collision with paddle
        score += 1
        h.clear()
        h.goto(-280, 260)
        h.write(f"Score: {score}", font=("Arial", 16, "normal"))
        reset_ball()                        # Drop new ball
    s.update()
    s.ontimer(loop, 30)                     # Repeat every 30ms

# --- START GAME ---
reset_ball()
loop()
turtle.mainloop()
