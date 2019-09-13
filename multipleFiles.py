import os

#os.makedirs('C:\\Users\\Shahlo\\Desktop\\code related\\python_work\\randomfiles\\')
os.chdir('C:\\Users\\Shahlo\\Desktop\\code related\\python_work\\randomfiles\\')

for i in range(20):
	
	myFile = open('spam%s.txt' % (i + 1), 'w')
	myFile.write("This contains number: %s" % (i + 1))
	
	myFile.close()
