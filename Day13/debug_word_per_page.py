# word_per_page = 0
# pages = int(input("Number of Pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# to debug this kind of bugs use print() functions.
# below code is the corrected version of above code
word_per_page = 0
pages = int(input("Number of Pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)