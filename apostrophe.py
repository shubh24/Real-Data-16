import nltk
import enchant
eng_check = enchant.Dict("en_US")

def add_apostrophe(input):
	sents = nltk.sent_tokenize(input)
	mod_sents = ""
	for s in sents:
		words = nltk.word_tokenize(s)
		pos_tags = nltk.pos_tag(words)
		for i in range(len(pos_tags)-1):
			if len(pos_tags[i][0][:-1]) > 1 and pos_tags[i][0][-1] == "s" and eng_check.check(pos_tags[i][0][:-1].lower()) and pos_tags[i][1][0] == "N" and (pos_tags[i+1][1][0] == "N" or pos_tags[i+1][1][0] == "J"):
				s = s.replace(pos_tags[i][0], pos_tags[i][0][:-1] + "\'" + "s")
		mod_sents = mod_sents + s + " "
	return mod_sents.rstrip(" ")


if __name__ == "__main__":
	input = raw_input()
	output = add_apostrophe(input)		
	print output