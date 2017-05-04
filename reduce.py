book = open("book.txt", "r").read().split()
words = [x.strip("!()[];:,./?") for x in book]

##find the frequency of a single word
def single(word):
	word=word.lower()
	return len(filter(lambda c: c.lower() == word, words))

print single("the")
print single("Lizzy")
