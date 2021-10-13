# Make a function that converts a word to pig latin. The rules of pig latin are:

# If the word has more than 3 letters:
# 1. Take the first letter of a word and move it to the end
# 2. Add -ay to the word
# Otherwise leave the word alone.


def pig_latin(word):
    if len(word) >= 4:
        sliced = word[1:] + word[0]
        return sliced + "ay"
    else:
        return word


print(pig_latin("hi"))

# slice notation: https://stackoverflow.com/questions/509211/understanding-slice-notation
