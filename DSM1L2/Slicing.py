text = "PYTHON"

# Character positions in the string
#
# Character:   P   Y   T   H   O   N
# Positive:    0   1   2   3   4   5
# Negative:   -6  -5  -4  -3  -2  -1


# 1️⃣ SINGLE POSITION — Indexing string[index]
print(text[0])  # Positive index 0 → "P"
print(text[3])  # Positive index 3 → "H"
print(text[-1])  # Negative index -1 → "N"
print(text[-3])  # Negative index -3 → "H"
print(text[0:2])


# 2️⃣ WITH STEP — Slicing with a step string[start : stop : step]
print(text[::2])  # Every 2nd character → "PTO"
print(text[1::2])  # Every 2nd character → "YHN"


# 3️⃣ REVERSE — Reverse slicing
print(text[::-1])  # Reverse the string → "NOHTYP"
