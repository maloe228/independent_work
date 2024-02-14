x = int(input())
y = int(input())
x1 = 0
y1 = 0

if x > y:
	y1 = (x+y)/2
	x1 = x*y*2
	print(x1,y1)
else:
	x1 = x*y*2
	y1 = (x+y)/2
	print(x1,y1)
