import os,sys
app = os.path.abspath(os.path.dirname(__file__))
a=sys.path.append(f'../{app}/par')
print(a)

from par import text
text.func()
