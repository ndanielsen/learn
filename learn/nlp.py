"""
NLP analysis functions


Author:
Nathan Danielsen
nathan.danielsen [at] gmail.com
"""

import nltk
from nltk.stem.snowball import SnowballStemmer


class NLP(object):
	"""
	Using some basic NLP methods to analyze text


	Inspiration found here:
	https://github.com/ndanielsen/A-Smattering-of-NLP-in-Python

	"""
	def __init__(self, title, text):
		self.title = title
		self.text = text
		self.tokens = [word for sent in nltk.sent_tokenize(self.text) for word in nltk.word_tokenize(sent)]
		self.sentences = nltk.sent_tokenize(self.text)
		

	def count(self):
		token_dict = {}
		for token in sorted(set(self.tokens))[:30]:
    		 token_dict[token] = str(self.tokens.count(token))
		return token_dict


	def stemmer(self):
		""" 
		Takes a list tokens and stems them into a list.
		Stemming is the process of reducing a word to its base/stem/root form. 
		"""

		stemmer = SnowballStemmer("english")
		stemmed_tokens = [stemmer.stem(t) for t in self.tokens]
		
		for token in sorted(stemmed_tokens):
			print token + ' [' + str(stemmed_tokens.count(token)) + ']'


	def lemmatizer(self):
		lemmatizer = nltk.WordNetLemmatizer()
		temp_sent = "Several women told me I have lying eyes."
		stemmer = SnowballStemmer("english")
		
		print [stemmer.stem(t) for t in nltk.word_tokenize(temp_sent)]
		print [lemmatizer.lemmatize(t) for t in nltk.word_tokenize(temp_sent)]





if __name__ == '__main__':
	title = "This is a title"

	text = "facilisis lorem tristique aliquet. Phasellus fermentum convallis"

	mrtesty = NLP(title, text)
	
	assert len(mrtesty.sentences) == 2

	assert mrtesty.count() == {'tristique': '1', 'Phasellus': '1', 'lorem': '1', 'convallis': '1', '.': '1', 'facilisis': '1', 'aliquet': '1', 'fermentum': '1'}



	shaketitle = "King Lear"

	shaketext = 	"""
					KING LEAR	Meantime we shall express our darker purpose.
		Give me the map there. Know that we have divided
		In three our kingdom: and 'tis our fast intent
		To shake all cares and business from our age;
		Conferring them on younger strengths, while we
		Unburthen'd crawl toward death. Our son of Cornwall,
		And you, our no less loving son of Albany,
		We have this hour a constant will to publish
		Our daughters' several dowers, that future strife
		May be prevented now. The princes, France and Burgundy,
		Great rivals in our youngest daughter's love,
		Long in our court have made their amorous sojourn,
		And here are to be answer'd. Tell me, my daughters,--
		Since now we will divest us both of rule,
		Interest of territory, cares of state,--
		Which of you shall we say doth love us most?
		That we our largest bounty may extend
		Where nature doth with merit challenge. Goneril,
		Our eldest-born, speak first.

		GONERIL	Sir, I love you more than words can wield the matter;
		Dearer than eye-sight, space, and liberty;
		Beyond what can be valued, rich or rare;
		No less than life, with grace, health, beauty, honour;
		As much as child e'er loved, or father found;
		A love that makes breath poor, and speech unable;
		Beyond all manner of so much I love you.

		CORDELIA	[Aside]  What shall Cordelia do?
		Love, and be silent.

		LEAR	Of all these bounds, even from this line to this,
		With shadowy forests and with champains rich'd,
		With plenteous rivers and wide-skirted meads,
		We make thee lady: to thine and Albany's issue
		Be this perpetual. What says our second daughter,
		Our dearest Regan, wife to Cornwall? Speak.
				"""

	shakestest = NLP(shaketitle, shaketext)

	print shakestest.title
	print shakestest.lemmatizer()