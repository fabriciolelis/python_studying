import math
#def compare(x,y):
	#if x > y:
		#return 1
	#elif x == y:
		#return 0
	#elif x < y:
		#return -1

#def hypotenyse(x,y):
	#square_sideX = x**2
	#square_sideY = y**2
	#sum_square = square_sideX + square_sideY
	#result = math.sqrt(sum_square)
	#return result

def is_between(x,y,z):
	if x <= y and y <= z:
		return True
	else:
		return False

def print_cmds():
	x = int(raw_input('Type ""x"" value\n'))
	y = int(raw_input('Type ""y"" value\n'))
	z = int(raw_input('Type ""z"" value\n'))
	#temp = compare(x,y)
	temp = is_between(x,y,z)
	print(temp)

print_cmds()
