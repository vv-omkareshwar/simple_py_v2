    def msort(a):
        print(f"Sorting: {a}")
        if len(a) <= 1:
            print(f"Base case reached, returning: {a}")
            return a

        m = len(a) // 2
        print(f"Splitting at index {m}: left={a[:m]}, right={a[m:]}")
        l = msort(a[:m])
        r = msort(a[m:])

        print(f"Merging: left={l}, right={r}")
        return mrg(l, r)

    def mrg(l, r):
        print(f"Merging arrays: {l} and {r}")
        res = []
        i = j = 0

        while i < len(l) and j < len(r):
            if l[i] <= r[j]:
                print(f"  Appending {l[i]} from left array")
                res.append(l[i])
                i += 1
            else:
                print(f"  Appending {r[j]} from right array")
                res.append(r[j])
                j += 1

        res.extend(l[i:])
        res.extend(r[j:])
        print(f"Merged result: {res}")
        return res

    # Examples
    if __name__ == "__main__":
        # Example 1: Mixed unsorted array
        print("\n=== Example 1: Mixed unsorted array ===")
        a = [5, 2, 9, 1, 5, 6]
        result1 = msort(a)
        print(f"Final sorted result: {result1}")
        
        # Example 2: Already sorted array
        print("\n=== Example 2: Already sorted array ===")
        b = [1, 2, 3, 4, 5]
        result2 = msort(b)
        print(f"Final sorted result: {result2}")
        
        # Example 3: Reverse sorted array
        print("\n=== Example 3: Reverse sorted array ===")
        c = [9, 7, 5, 3, 1]
        result3 = msort(c)
        print(f"Final sorted result: {result3}")
        
        # Example 4: Array with duplicates
        print("\n=== Example 4: Array with duplicates ===")
        d = [3, 1, 3, 1, 3]
        result4 = msort(d)
        print(f"Final sorted result: {result4}")
        
        # Example 5: Single and empty arrays
        print("\n=== Example 5: Single element array ===")
        e = [42]
        result5 = msort(e)
        print(f"Final sorted result: {result5}")
