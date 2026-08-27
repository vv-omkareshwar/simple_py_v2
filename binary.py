class S:
  def __init__(s, n):
    # Initialize the array
    s.n = n

  def b(s, t):
    # Set the initial search boundaries
    l = 0
    r = len(s.n) - 1

    # Perform binary search
    while l <= r:
      m = (l + r) // 2
      print(f"Searching: left={l}, right={r}, middle={m}, value={s.n[m]}")

      if s.n[m] == t:
        print(f"Target {t} found at index {m}")
        return m
      elif s.n[m] < t:
        print(f"Middle value {s.n[m]} is less than target {t}, moving left boundary")
        l = m + 1
      else:
        print(f"Middle value {s.n[m]} is greater than target {t}, moving right boundary")
        r = m - 1

    # Target was not found
    print(f"Target {t} not found")
    return -1


def f():
  a = [2, 4, 6, 8, 10, 12, 14]
  t = 10
  s = S(a)
  print(f"Starting binary search for target: {t}")
  i = s.b(t)
  print("Found at index:", i)


f()