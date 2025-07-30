def msort(a):
    if len(a) <= 1:
        return a

    m = len(a) // 2
    l = msort(a[:m])
    r = msort(a[m:])

    return mrg(l, r)

def mrg(l, r):
    res = []
    i = j = 0

    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            res.append(l[i])
            i += 1
        else:
            res.append(r[j])
            j += 1

    res.extend(l[i:])
    res.extend(r[j:])
    return res

# Example
if __name__ == "__main__":
    a = [5, 2, 9, 1, 5, 6]
    print(msort(a))
