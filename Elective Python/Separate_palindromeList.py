
def sepPalindrome(wordList):
  palList = []
  for word in wordList:
    if word == word[::-1]:
      palList.append(word)
    
  return palList


wordList = [] 
n = int(input("Enter the number of items in the list: "))
for i in range(n):
  str = input("Enter string: ")
  wordList.append(str)

print(sepPalindrome(wordList))

