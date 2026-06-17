class Solution:
    def calPoints(self, operations: List[str]) -> int:
        final_scores = []
        for operation in operations:
            
            if operation == '+':
                final_scores.append(final_scores[len(final_scores)-2]+final_scores[len(final_scores)-1])
            elif operation == 'D':
                final_scores.append(final_scores[len(final_scores)-1]*2)
            elif operation == 'C':
                final_scores.pop()
            else:
                final_scores.append(int(operation))
        return sum(final_scores)
