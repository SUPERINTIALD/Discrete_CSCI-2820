from typing import List
class Homework9:
    def find_Inspector(self, n: int, trust: List[List[int]]) -> int:
        trusts = trust[0][1]
        for i in trust:
            if i[0] == trusts:
                return -1
        return trusts
# For testing your code uncomment below lines.
# c = Homework9()
# n = 2
# trust = [[1,2]]
# print(c.find_Inspector(n, trust))
# trust2= [[1,2],[2,1]]
# print(c.find_Inspector(n,trust2))
# Comment or delete the above test code before submitting.

