"""Welcome to the Pig Latin Translator"""

# In this project python will ask the user for a word.
# Then python will turn the word into a Pig Latin Word.
# It will do so by taking the first letter of the word and putting it at the end.
# Then it will add 'ay' after the last letter.
# For example Pig would be igpay in Pig Latin.

print "Welcome to the Pig Latin translator!" \
      " In this project the computer will turn a word you enter into a Pig Latin Word!"

def pyg_latin():
    pyg = 'ay'
    original = raw_input('Enter a word: ')

    if len(original) > 0 and original.isalpha():
        word = original.lower()
        first = word[0]
        new_word = word + first + pyg
        new_word = new_word[1:len(new_word)]
        print new_word
    else:
        print "Invalid"
        pyg_latin()
pyg_latin()
# This is the end of the pig latin translator
