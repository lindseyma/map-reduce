book = open("book.txt", "r").read().split()
words = [x.strip("!()[];:,./?") for x in book]

##find the frequency of a single word
def single(word):
	word=word.lower()
	return len(filter(lambda c: c.lower() == word, words))

print single("the")
print single("Lizzy")

##find the total frequency of a group of words
def group(words):
	##create list of result for frequency of each word
	frequencyList = [single(word) for word in words]
	##use reduce to add each frequency in list
	return reduce(lambda a,b: a+b, frequencyList)

print group(["the", "Lizzy"])