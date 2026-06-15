class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for k in range(len(arr)-1):
            arr[k] = max(arr[k+1:])
        arr[len(arr) - 1] = -1
        return arr