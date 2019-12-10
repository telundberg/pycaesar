import string

alpha = list(string.ascii_lowercase)

print("please type a string:")
myWord = raw_input()
stringWord = myWord.lower().split()
cipherShift = 4

cipherAlpha = list()

for alphaIndex in range(len(alpha)):
  alphaIndex = (alphaIndex + cipherShift) % 26
  cipherAlpha.append(alpha[alphaIndex])

cipherText = list()

for word in stringWord:
  cipherWord = ""
  for letter in word:
    j = alpha.index(letter)
    k = cipherAlpha[j]
    cipherWord += k
  cipherText.append(cipherWord)

print(" ".join(cipherText))
