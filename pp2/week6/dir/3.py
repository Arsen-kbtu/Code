import os
path = 'C:\\Users\\Динара\\Documents\\PP\\PYTHON\\week6\\dir'
print("A path exists:", os.path.exists(path))
if os.path.exists(path):
    print(os.path.basename(path))
    print(os.path.dirname(path))
