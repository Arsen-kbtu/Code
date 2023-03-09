import re
txt = '''
a
aaa_asd_feasf_dwef
llllaob
red_madrobot
abb_cvv
'''
x = re.findall('[a-z]+_[a-z]+', txt)
print(x)
