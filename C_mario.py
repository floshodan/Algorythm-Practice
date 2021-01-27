
height = 4;

def draw(height):
	for i in range(1, height+1):
		print('#'*i)

def draw2(height):
	for i in range(0, height):
		for j in range (0,i+1):
			print('#', end="")
		print('\r')

def draw3(height):
	if(height == 0):
		return 
	draw3(height-1)
	for i in range(height):
		print('#', end="")
	print('\r')
draw3(4)
