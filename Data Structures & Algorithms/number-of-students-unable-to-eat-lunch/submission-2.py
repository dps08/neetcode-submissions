from collections import Counter

class Solution:
    def countStudents(self, students, sandwiches):
        count = Counter(students)

        for sandwich in sandwiches:
            if count[sandwich] > 0:
                count[sandwich] -= 1
            else:
                break

        return count[0] + count[1]