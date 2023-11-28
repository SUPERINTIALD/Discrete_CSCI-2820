#DO NOT CHANGE THE NAMES OF THE FILE, CLASS or METHOD
class Homework6:
    def isPower(self, n):
        # Start your code from here
        if n == 1:
            return True
        elif n < 17:
            return False
        else:
            return self.isPower(n/17)
# For testing your code uncomment below lines.
# l = Homework6()
# print(l.isPower(17))
# Comment or delete the above test code before submitting.
