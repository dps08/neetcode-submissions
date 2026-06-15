class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest = -1

        for k in range(len(arr) - 1, -1, -1):
            current = arr[k]
            arr[k] = greatest
            greatest = max(greatest, current)

        return arr