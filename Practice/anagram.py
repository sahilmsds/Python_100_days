word1 = input("Enter the first word: ").lower()
word2 = input("Enter the second word: ").lower()

if word1 == word2:
    print("You enterd same word twice.")
elif len(word1) != len(word2):
    print("It is not an ANAGRAM.\nLengths of both words are Different from each other.")
elif sorted(word1) == sorted(word2):
    print("That's a ANAGRAM")
else:
    print("Not a ANAGRAM.")
    