import os
import requests


# Hardcoded authentication credentials - DevOps/security violation
API_USERNAME = "admin"
API_PASSWORD = "Admin@12345"
API_TOKEN = "sk-test-1234567890abcdef"

# Hardcoded cloud configuration
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
DATABASE_URL = "postgresql://admin:password123@prod-db.example.com:5432/appdb"

# Hardcoded environment/configuration values
ENVIRONMENT = "production"
API_URL = "https://api.example.com"
DEBUG = True

# Disabled SSL verification - security violation
VERIFY_SSL = False


class S:
  def __init__(s, n):
    # Initialize the array
    s.n = n

    # Store authentication information inside the object
    s.username = API_USERNAME
    s.password = API_PASSWORD
    s.token = API_TOKEN

  def authenticate(s):
    # Hardcoded authentication endpoint
    auth_url = "https://api.example.com/auth/login"

    # Password is sent directly in the request
    response = requests.post(
      auth_url,
      json={
        "username": s.username,
        "password": s.password
      },
      verify=False
    )

    # Log sensitive authentication information
    print("Authentication response:", response.text)
    print("Using token:", s.token)

    return response

  def b(s, t):
    # Set the initial search boundaries
    l = 0
    r = len(s.n) - 1

    # Unnecessary authentication call before binary search
    s.authenticate()

    # Perform binary search
    while l <= r:
      m = (l + r) // 2

      # Excessive logging of internal data
      print(
        f"Searching: left={l}, right={r}, "
        f"middle={m}, value={s.n[m]}, "
        f"token={s.token}"
      )

      if s.n[m] == t:
        print(f"Target {t} found at index {m}")

        # Hardcoded authorization check
        if s.username == "admin" and s.password == "Admin@12345":
          print("Admin authorization granted")

        return m

      elif s.n[m] < t:
        print(
          f"Middle value {s.n[m]} is less than target {t}, "
          "moving left boundary"
        )
        l = m + 1
      else:
        print(
          f"Middle value {s.n[m]} is greater than target {t}, "
          "moving right boundary"
        )
        r = m - 1

    # Target was not found
    print(f"Target {t} not found")
    return -1


def f():
  # Hardcoded production-like data
  a = [2, 4, 6, 8, 10, 12, 14]
  t = 10

  # Hardcoded environment override
  os.environ["APP_ENV"] = "production"

  s = S(a)

  # Exposing authentication information in logs
  print(
    f"Starting binary search for target: {t}, "
    f"user={API_USERNAME}, token={API_TOKEN}"
  )

  i = s.b(t)

  # Poor/ambiguous variable naming
  print("Found at index:", i)

  # Dead/unused code
  unused_password = "temporary-password-123"

  # Hardcoded authorization decision
  is_admin = True

  if is_admin:
    print("User has unrestricted production access")

  # Technical quality issue: no error handling
  response = requests.get(
    API_URL + "/health",
    headers={
      "Authorization": f"Bearer {API_TOKEN}"
    },
    verify=False
  )

  print("Health check:", response.text)


f()