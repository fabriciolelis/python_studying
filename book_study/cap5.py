#def print_myname():
	#print "Fabricio"
	
#def do_n(f,n):
	#for i in range(n):
		#f()
	
#do_n(print_myname,4)

from swampy.TurtleWorld import *
import math

#def check_fermat(a,b,c,n):
	#if (n > 2 and ((math.pow(a,n) + math.pow(b,n)) == (math.pow(c,n)))):
		#print "Holly smokes, Fermat was wrong!"
	#else:
		 #print "No, that doesn't work"

#def print_cmds():
	#a = raw_input('Type ""a"" value\n')
	#a= float(a)
	#b = raw_input('Type ""b"" value\n')
	#b = float(b)
	#c = raw_input('Type ""c"" value\n')
	#c = float(c)
	#n = raw_input('Type ""n"" value\n')
	#n = int(n)
	#check_fermat(a,b,c,n)

#def is_triangle(a,b,c):
	#if a > (b+c):
		#print "No"
	#elif b > (a+c):
		#print "No"
	#elif c > (a+b):
		#print "No"
	#else:
		#print "Yes"

#def print_cmds():
	#first_side = float(raw_input('Type ""a"" value\n'))
	#second_side = float(raw_input('Type ""b"" value\n'))
	#third_side = float(raw_input('Type ""c"" value\n'))l
	#is_triangle(first_side,second_side,third_side)

#print_cmds()

world = TurtleWorld()
bob = Turtle()

def draw(t, length, n):
	if n == 0:
		return
	angle = 50
	fd(t, length*n)
	lt(t, angle)
	draw(t, length, n-1)
	rt(t, 2*angle)
	draw(t, length, n-1)
	lt(t, angle)
	bk(t, length*n)

draw(bob,9,3)
