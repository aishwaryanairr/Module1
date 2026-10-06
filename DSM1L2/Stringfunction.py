# ============================================================
# COMMON STRING OPERATIONS
# ============================================================
#
# len()      → Finds the number of characters in a string
# lower()    → Converts the string to lowercase
# upper()    → Converts the string to uppercase
# split()    → Splits a string into a list
# join()     → Joins items into a string
# find()     → Finds the position of a character or word
# replace()  → Replaces part of a string with another value
# +          → Joins two or more strings (concatenation)
#
# ============================================================


text = "Hello Python Programming"


# 1️⃣ LENGTH
print(len(text))
# Output: 24


# 2️⃣ LOWERCASE
print(text.lower())
# Output: hello python programming


# 3️⃣ UPPERCASE
print(text.upper())
# Output: HELLO PYTHON PROGRAMMING


# 4️⃣ SPLIT
print(text.split())
# Output: ['Hello', 'Python', 'Programming']


# 5️⃣ JOIN
words = ["Hello", "Python"]
print(" ".join(words))
# Output: Hello Python


# 6️⃣ FIND
print(text.find("Python"))
# Output: 6


# 7️⃣ REPLACE
print(text.replace("Python", "Java"))
# Output: Hello Java Programming


# 8️⃣ CONCATENATION
first_name = "Aishwarya"
last_name = "Nair"

print(first_name + " " + last_name)
# Output: Aishwarya Nair
