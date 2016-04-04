import nltk
from nltk.corpus import gutenberg
words = gutenberg.words()
words = [i.lower() for i in words]

def separate_hashtag(hashtag):	
	current_possible_words = []
	i = len(hashtag) + 1
	while i > 1:
		i -= 1
		if hashtag[:i].lower() in words:
			current_possible_words.append(hashtag[:i])
			if i == len(hashtag):
				return current_possible_words
			else:
				temp = separate_hashtag(hashtag[i:])
				for j in temp:
					current_possible_words.append(j)
				return current_possible_words

if __name__ == "__main__":
	args = int(raw_input())
	hashtags = []
	possible_words = []
	for i in range(0,args):
		hashtags.append(raw_input())
	for i in hashtags:
		possible_words.append(separate_hashtag(i))
	for i in possible_words:
		print ' '.join(j for j in i)