class Solution:
    def calPoints(self, operations: List[str]) -> int:
        final_scores = []
        for i in range(len(operations)):
            
            if operations[i] == '+':
                final_scores.append(final_scores[len(final_scores)-2]+final_scores[len(final_scores)-1])
            elif operations[i] == 'D':
                final_scores.append(final_scores[len(final_scores)-1]*2)
            elif operations[i] == 'C':
                final_scores.pop()
            else:
                final_scores.append(int(operations[i]))
        return sum(final_scores)
