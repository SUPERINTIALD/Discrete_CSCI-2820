
#DO NOT CHANGE THE NAMES OF THE FILE, CLASS or METHOD
import math
class Homework8():
	def permutation(self, s):#calc permutation
		if self.palindrome(s):
			return 0
		count = self.counts(s)
		total_permutations = self.factorial(len(s))
		for count in count.values():
			total_permutations //= self.factorial(count)
		return total_permutations
	
	def palindrome(self, s):
		return s == s[::-1] #get palindrome
	
	def counts(self, s):#count each palindrome string
		count = {}
		for char in s:
			if char in count:
				count[char] += 1
			else:
				count[char] = 1
		return count
	
	def factorial(self, n):#factorials calc
		if n <= 1:
			return 1
		else:
			return n * self.factorial(n - 1)




# For testing your code uncomment below lines.
# l = Homework8()
# print(l.permutation("lemon"))
# print(l.permutation("event"))
# print(l.permutation("radar"))
# print(l.permutation(""))
# Comment or delete the above test code before submitting.
