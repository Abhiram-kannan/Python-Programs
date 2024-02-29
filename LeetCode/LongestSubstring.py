#substring without repeting characters
"""
def SubstringLength(str):
    index = ""
    count = -1
    substring = ""
    for i in range(len(str)):
      count += 1
      if str[i] in index:
        break
      else:
        substring += str[i]
        index += str[i]
    print("The answer is : ", substring , "and its length is " , count)

str = input("Enter a string: ")
"""

def LongestSubstring(str):
  start = 0
  length = 0
  charmap = {}
  substring = ""
  for i ,char in enumerate(str):
    if char in charmap and charmap[char]>start:
      start = charmap[char] + 1
    else:
      length = max(length, i - start + 1)
    charmap[char] = i
  return length
  return substring


str = input("Enter a string: ")
print(LongestSubstring(str))