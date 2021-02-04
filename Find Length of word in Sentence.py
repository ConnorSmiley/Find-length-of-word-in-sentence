def x_length_words(sentence, x):
  word = sentence.split(" ")
  for i in word:
    if len(i) < x:
      return False
    else:
      return True


print(x_length_words("i like apples", 2))
# should print False
print(x_length_words("he likes apples", 2))
# should print True
