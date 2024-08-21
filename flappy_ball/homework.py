import pgzrun
import random

TITLE = "Flappy ball"
WIDTH = 800
HEIGHT = 800

R=random.randint(0,255)
G=random.randint(0,255)
B=random.randint(0,255)

rand_color = (R,G,B)
gravity = random.randint(200,3000)
class Ball_one:
   def __init__(self,current_x,current_y):
      self.x = current_x
      self.y = current_y
      self.vx = 200
      self.vy = 0
      self.radius = random.randint(30,80)

   def draw(self):
      pos = (self.x,self.y)
      screen.draw.filled_circle(pos,self.radius,rand_color)

"""class Ball_two:
   def __init__(self,current_x,current_y):
      self.x = current_x
      self.y = current_y
      self.vx = 200
      self.vy = 0
      self.radius = random.randint(30,80)

      def draw(self):
         pos = (self.x,self.y)
         screen.draw.filled_circle(pos,self.radius,rand_color)    

         ball_one =  Flappy_ball(50,100)
         ball_two = Flappy_ball(49,100)

         def draw():
            screen.clear()
            ball_one.draw()
            ball_two.draw()"""

ball_one = Ball_one(36,300)
ball_two = Ball_one(48,500)

def draw():
   screen.clear()
   ball_one.draw()
   ball_two.draw()



def update(dt):
    uy =  ball_one.vy
    uy = ball_two.vy
    ball_one.vy += gravity * dt
    ball_two.vy += gravity * dt
    ball_one.y += (uy + ball_one.vy) * 0.5 * dt

    if ball_one.y > HEIGHT - ball_one.radius:
        ball_one.y = HEIGHT - ball_one.radius
        ball_one.vy = -ball_one.vy * 0.9
    ball_one.x += ball_one.vx *dt
    if ball_one.x > WIDTH-ball_one.radius or ball_one.x < ball_one.radius + 10 :
        
        ball_one.vx = ball_one.vx

pgzrun.go()



