from swampy.TurtleWorld import *
import math

world = TurtleWorld()
bob = Turtle()
print bob

#def square(t,length):
	#for i in range(4):
		#fd(t,length)
		#lt(t)

def polyline(t, n, length, angle):
	for i in range(n):
		fd(t, length)
		lt(t, angle)

def polygon(t,length,n):
	angle = 360.0 / n
	polyline(t,n,length,angle)


def arc(t, r, angle):
	arc_length = 2 * math.pi * r * angle / 360
	n = int(arc_length / 3) + 1
	step_length = arc_length / n
	step_angle = float(angle) / n
	polyline(t,n,step_length, step_angle)

def circle(t, r):
	arc(t,r,360)
	
bob.delay = 0.01
circle(bob,100)
#square(bob,100)
#polygon(bob,30,4)
wait_for_user()
