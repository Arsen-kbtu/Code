with open(r"text.txt", 'r') as text:
    lines = len(text.readlines())
    print('Total Number of lines:', lines)