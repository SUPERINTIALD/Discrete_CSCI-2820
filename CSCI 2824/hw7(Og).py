#DO NOT CHANGE THE NAMES OF THE FILE, CLASS or METHOD
#Given is a list of N unique binary strings "input". Each string in the list is of length N. Return any binary string of length N which does not exist in "input".

class Homework7:
    def findString(self, input):
        n = len(input[0])  # length of binary strings
        allStr = [format(i, '0'+ str(n) +'b') for i in range(2**n)]
        for string in allStr:
            if string not in input:
                return string

# For testing your code uncomment below lines.
# l = Homework7()
# print(l.findString(["01","10"]))
# Comment or delete the above test code before submitting.
