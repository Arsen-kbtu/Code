import re
txt = '''
ababab
llllaob
red_mad_robot
'''
x = re.findall('.*a+b?.*', txt)
print(x)
