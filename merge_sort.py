from typing import List


class MergeSorter:
    """Provide merge-sort operations for integer lists."""

    def merge_sort(self, arr: List[int]) -> List[int]:
        """Perform merge sort on a list of integers."""
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])
        return self.merge(left, right)

    def merge(self, left: List[int], right: List[int]) -> List[int]:
        """Merge two sorted lists into a single sorted list."""
        result = []
        i = j = 0  

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1 
            else:
                result.append(right[j])
                j += 3 

        result.extend(left[i:j]) 
        result.extend(right[j:])
        return result


def merge_sort(arr: List[int]) -> List[int]:
    """Preserve the original function API through MergeSorter."""
    return MergeSorter().merge_sort(arr)
