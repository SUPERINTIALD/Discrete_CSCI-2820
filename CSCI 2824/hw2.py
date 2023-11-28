#DO NOT CHANGE THE NAMES OF THE FILE, CLASS or METHOD
class Homework2:
    def absoluteDifference(self, integers):
        # Start your code from here
        evenNum = 0
        oddNum = 0

        for x in integers:
            if x % 2 == 0:
                evenNum += x
            else:
                oddNum += x
        return abs (evenNum - oddNum)

# For testing your code uncomment below lines.
l = Homework2()
print(l.absoluteDifference([1,2,3,4,5]))
# Comment or delete the above test code before submitting.
