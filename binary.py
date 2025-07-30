class Searcher:
    def __init__(self, numbers):
        self.numbers = number

    def binary(self, tgt):
        left = 0
        right_boundary = len(self.numbers) - 1
        while left <= right_boundary:
            mid = (left + right_boundary) // 2
            if self.numbers[mid] == tgt:
                return mid
            elif self.numbers[mid] < tgt:
                left = mid + 1
            else:
                right_boundary = mid - 1
        return -1

def main_func():
    listToCheck = [2, 4, 6, 8, 10, 12, 14] 
    target = 10
    s = Searcher(listToCheck)
    idx = s.binary(target)
    print("Found at index:", idx)

main_func()
