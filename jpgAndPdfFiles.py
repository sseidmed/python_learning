import os, shutil

#os.makedirs('C:\\Users\\Shahlo\\Desktop\\code related\\python_work\\randomfiles\\')
os.chdir('C:\\Users\\Shahlo\\Desktop\\code related\\python_work\\randomfiles\\')

for i in range(20):
	
	myFile = open('spam%s.txt' % (i + 1), 'w')
	myFile.write("This contains number: %s" % (i + 1))
	
	myFile.close()

#backup the entire folder and its contents
shutil.copytree('C:\\Users\\Shahlo\\Desktop\\code related\\python_work\\randomfiles\\', 'C:\\Users\\Shahlo\\Desktop\\code related\\python_work\\randomfiles_backup\\')

#os.makedirs('C:\\Users\\Shahlo\\Desktop\\code related\\python_work\\randomfiles\\stuff\\')

mypath = 'C:\\Users\\Shahlo\\Desktop\\code related\\python_work\\randomfiles\\'
backup = 'C:\\Users\\Shahlo\\Desktop\\code related\\python_work\\randomfiles_backup'
for folderName, subfolders, filenames in os.walk(mypath):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        if filename.lower().endswith('.jpg') or filename.lower().endswith('.pdf'):
            print('FILE INSIDE ' + folderName + ': '+ filename)
            print(os.path.join(folderName, filename))
            shutil.copy(os.path.join(folderName, filename), backup)

    print('')
print("Backup finished")
