import re
txt = '''
lmsdfsm
Wfkwefm
kplmkMJLKMMplplp
'''
x = re.findall('[A-Z]+[a-z]+', txt)
print(x)
