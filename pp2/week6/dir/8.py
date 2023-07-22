import os
path = 'C:\\Users\\Динара\\Documents\\PP\\PYTHON\\week6\\dir\\del.txt'
if os.access(path, os.F_OK):
    os.remove('C:\\Users\\Динара\\Documents\\PP\\PYTHON\\week6\\dir\\del.txt')
    print("Path deleted")
else:
    print("path doesnt exist")