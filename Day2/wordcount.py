#fuction that counts the occurrences or characters in a word.
#counts one word
#counts one of each
#should count multiple occurrences
#should include punctuation
#
#
#
#
#
def words(string):
	x = {}
	word_list = string.split()
	for word in word_list:
		if word.isdigit():
			word = int(word)
		if word in x:
			x[word] = x[word] + 1
		else:
			x[word] = 1
	return x
