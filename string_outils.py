def column_format(word):
	"""
	returns the word formatted so that the letters are in columns of 4 separated by tabs
	"""
	i = 0
	j = 0
	k = 0
	formated = list()
	if len(word) < 0:
		return None
	for i in range(len(word)):
		if j == 0:
			formated.append(word[i])
			j += 1
		else:
			formated[k] += "\t" + word[i]
			j += 1
		if j == 4:
			k += 1
			j = 0
	for i in formated:
		print(i)

def replace_underscore(word, char, to_compare):
	"""
	replaces underscores of secret word with char when it appears in the string to compare
	"""
	for i in range(len(to_compare)):
		if to_compare[i] == char:
			word = (word[:(i * 2)] + char + word[((i * 2) + 1):])
	return word




