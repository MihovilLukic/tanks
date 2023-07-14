import turtle

# Set up the game window
window = turtle.Screen()
window.title("Space Invaders")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Create the player's spaceship
player = turtle.Turtle()
player.color("red")
player.penup()
player.speed(0)
player.goto(0, -250)

# Draw the player's spaceship
player_shape = [(0, 20), (-10, 0), (10, 0)]
player.shapesize(stretch_wid=2, stretch_len=4)
player.setheading(90)
player.shape("triangle")
player.goto(0, -250)

# Player's movement
player_speed = 15

def move_left():
    x = player.xcor()
    x -= player_speed
    if x < -380:
        x = -380  # Limit the player's movement within the window
    player.setx(x)

def move_right():
    x = player.xcor()
    x += player_speed
    if x > 380:
        x = 380
    player.setx(x)

def fire_bullet():
    global bullet_state
    if bullet_state == "ready":
        bullet_state = "fire"
        x = player.xcor()
        y = player.ycor() + 10
        bullet.goto(x, y)
        bullet.showturtle()

# Keyboard bindings
window.listen()
window.onkeypress(move_left, "Left")
window.onkeypress(move_right, "Right")
window.onkeypress(fire_bullet, "space")

# Create the bullet
bullet = turtle.Turtle()
bullet.color("white")
bullet.shape("arrow")
bullet.penup()
bullet.speed(0)
bullet.shapesize(stretch_wid=0.5, stretch_len=0.5)
bullet.hideturtle()
bullet.goto(0, -400)
bullet.setheading(90)

bullet_speed = 20
bullet_state = "ready"

def move_bullet():
    global bullet_state
    if bullet_state == "fire":
        y = bullet.ycor()
        y += bullet_speed
        bullet.sety(y)

    # Check if the bullet has reached the top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bullet_state = "ready"

# Create the enemy aliens
enemies = []
enemy_count = 5

for i in range(enemy_count):
    enemy = turtle.Turtle()
    enemy.color("green")
    enemy.shape("turtle")
    enemy.penup()
    enemy.speed(0)
    enemy.goto(-200 + i * 100, 250)
    enemies.append(enemy)

# Collision detection
def is_collision(obj1, obj2):
    distance = obj1.distance(obj2)
    if distance < 20:  # Adjust the value as needed
        return True
    return False

# Main game loop
while True:
    window.update()

    move_bullet()

    # Check for collision between bullet and enemies
    for enemy in enemies:
        if is_collision(bullet, enemy):
            bullet.hideturtle()
            bullet_state = "ready"
            enemy.goto(-200, 250)
            enemy.color("green")  # Change enemy color or update as needed
