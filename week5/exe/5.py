import re
txt = '''
alllldb
fwmeklfkmlef
amfmkfjeijf
'''
x = re.findall(r".*a.*b$", txt)
print(x)
