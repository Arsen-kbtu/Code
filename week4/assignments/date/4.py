import datetime
x = datetime.datetime(2023, 5, 16)
y = datetime.datetime(2023, 2, 23)
z =int(x.strftime("%j"))-int(y.strftime("%j"))
print(z*24*60*60)
