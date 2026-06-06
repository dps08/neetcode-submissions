from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    high_score = 0
    high_scorer = None
    for student, score in scores:
        if high_score <= score:
            high_scorer = student
            high_score = score
    return high_scorer

# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
