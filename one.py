import string

alpha = list(string.ascii_lowercase)

print("please type a string:")
myWord = raw_input()
stringWord = myWord.lower().split()

letterList = list()
cipherShift = 4

for word in stringWord:
  m = ""
  for letter in word:
    k = alpha.index(letter)
    l = (k + cipherShift) % 26
    m += alpha[l]
  letterList.append(m)

n = " ".join(letterList)

print(n)
