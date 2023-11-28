
#DO NOT CHANGE THE NAMES OF THE FILE, CLASS or METHOD
class Homework4:
    def smallCount(self, nums):
        # Start your code from here
        result = []

        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    count += 1
            result.append(count)
        return result
# For testing your code uncomment below lines.
# l = Homework4()
# print(l.smallCount([8,1,2,2,3]))
# Comment or delete the above test code before submitting.
