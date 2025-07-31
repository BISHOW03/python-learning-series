"""
🔧 STRING METHODS & OPERATIONS (For AI/ML Engineers)
"""

# 1. CASE CONVERSION
s = "heLLo WoRLd"
print("1. CASE CONVERSION")
print(s.lower())       # Output: 'hello world'  #small letter
print(s.upper())       # Output: 'HELLO WORLD'  # capital letter
print(s.title())       # Output: 'Hello World'   # first letter capital
print(s.capitalize())  # Output: 'Hello world'


# 2. WHITESPACE REMOVAL
s = "   hello   "
a = "Bishow"
print("2. WHITESPACE REMOVAL")
print(s.strip())       # Output: 'hello'    remove whitespace from both
print(s.lstrip())      # Output: 'hello   '   put space in last
print(s.rstrip())      # Output: '   hello'   put space in first

print(a.strip())
print(a.lstrip())
print(a.rstrip())


# 3. REPLACING SUBSTRINGS
text = "I like Python. Python is fun."
print(text.replace("Python", "AI"))  # replace python to AI
# Output: 'I like AI. AI is fun.'



# 4. SPLITTING STRINGS
msg = "apple,banana,cherry"
print(msg.split(','))       # Output: ['apple', 'banana', 'cherry']



# 5. JOINING STRINGS
words = ['HTML', 'CSS', 'JS']
print(" - ".join(words))    # Output: 'HTML - CSS - JS'



# 6. SEARCHING STRINGS
s = "machine learning"
print("6. SEARCHING STRINGS")
print(s.find("learn"))   # Output: 8
print(s.find("xyz"))     # Output: -1



# 7. COUNTING SUBSTRINGS
txt = "AI, AI, and more AI"
print(txt.count("AI"))   # how many times it occurs
# Output: 3

print("\n")

# 8. START/END CHECKS
s = "deep learning"
print(s.startswith("deep"))     # Output: True
print(s.endswith("learning"))   # Output: True
print(s.endswith("ram"))        # output: False 
