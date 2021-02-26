# Challenge - Functions Exercise

# Create a function named tripleprint that takes a string as a parameter
# and prints that string 3 times in a row.
# So if I passed in the string "hello",
# it would print "hellohellohello"

#function
def tripleprint(word):
	print("{}{}{}".format(word,word,word))

#word to be passed
word = "hello"

#to let user input word
# word = input("Enter String:")

#use fxn on word
tripleprint(word)