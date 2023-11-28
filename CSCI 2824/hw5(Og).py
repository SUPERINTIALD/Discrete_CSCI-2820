#DO NOT CHANGE THE NAMES OF THE FILE, CLASS or METHOD

class Homework5:
    def arrayGCD(self, arr):
        # Start your code from here
        smallest = min(arr)
        largest = max(arr)
        
        return self.gcd(smallest, largest)
    def gcd(self, a, b):
        if b == 0:
            return a
        else:
            return self.gcd(b, a % b)
# For testing your code uncomment below lines.
# l = Homework5()
# print(l.arrayGCD([2,3,4,10]))
# Comment or delete the above test code before submitting.