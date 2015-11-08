#def right_justify(s):
	#space = 70 * ' '
	#print(space + s)

#right_justify('allen')

def print_spam(s):
	print s

def do_twice(f,s):
	f(s)
	f(s)

def do_four(f,s):
	do_twice(f,s)
	do_twice(f,s)

#do_twice(print_spam,'spam')
#do_four(print_spam,'spam')

def print_square():
	print '+', '-', '-','-','-','+', '-', '-','-','-','+', '-', '-','-','-','+', '-', '-','-','-','+', '-', '-','-','-','+' 
	print '|        ','|        ','|        ','|        ','|        ','|'
	print '|        ','|        ','|        ','|        ','|        ','|'
	print '|        ','|        ','|        ','|        ','|        ','|'
	print '|        ','|        ','|        ','|        ','|        ','|'
	print '+', '-', '-','-','-','+', '-', '-','-','-','+', '-', '-','-','-','+', '-', '-','-','-','+', '-', '-','-','-','+'
	print '|        ','|        ','|        ','|        ','|        ','|'
	print '|        ','|        ','|        ','|        ','|        ','|' 
	print '|        ','|        ','|        ','|        ','|        ','|'
	print '|        ','|        ','|        ','|        ','|        ','|'
	print '+', '-', '-','-','-','+', '-', '-','-','-','+', '-', '-','-','-','+', '-', '-','-','-','+', '-', '-','-','-','+'

def print_twice(f):
	f()
	f()
	
#print_square()
print_twice(print_square)
