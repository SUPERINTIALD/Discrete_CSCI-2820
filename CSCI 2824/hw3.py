#DO NOT CHANGE THE NAMES OF THE FILE, CLASS or METHOD
import math

class Triangle:
    def hypotenuse(self, a, b):
        #Start writing your code here
        h = math.sqrt(((2*a/b)**2 + b**2))
        return math.floor(h)
# For testing your code uncomment below lines.

t = Triangle()
print(t.hypotenuse(6, 3))
print(t.hypotenuse(54, 9))
print(t.hypotenuse(78, 12))
print(t.hypotenuse(1474, 67))
print(t.hypotenuse(2526, 56))
# Comment or delete the above test code before submitting.