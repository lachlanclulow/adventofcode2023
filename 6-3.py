import math
import re

print((lambda t:abs(math.floor((-t[0]+math.sqrt(abs(t[0]**2-4*t[1])))/2)-math.floor((-t[0]-math.sqrt(abs(t[0]**2-4*t[1])))/(2))))((lambda x:(int(x[0]),int(x[1])))(re.match("Time:[ ]+(\d+)\nDistance:[ ]+(\d+)", """Time:        62649190\nDistance:   553101014731074""").groups())))
