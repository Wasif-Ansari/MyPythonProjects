from spellchecker import SpellChecker

corrector = SpellChecker()

word = input("Enter any word: ")

if word in corrector:
    print("Already Correct")
else:
    correct_word = corrector.correction(word)
    print("Correct Spelling is ", correct_word)