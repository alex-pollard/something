import math
try:
    radius = int((input("Input circle radius")))
    print ("Your circle is of area:", int(radius*(math.pi*math.pi)))
except:
    print("Usage: Input must be a single number")