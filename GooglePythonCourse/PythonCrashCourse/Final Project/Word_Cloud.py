"""

 - Project goal
Create a dictionary with words and word frequencies that can be passed to the generate_from_frequencies
function of the WordCloud class.

Once you have the dictionary, use this code to generate the word cloud image:

cloud = wordcloud.WordCloud()
cloud.generate_from_frequencies(frequencies)
cloud.to_file("myfile.jpg")

Before processing any text, you need to remove all the punctuation marks.
To do this, you can go through each line of text, character-by-character, using the isalpha() method.
This will check whether or not the character is a letter.

To split a line of text into words, you can use the split() method.

Before storing words in the frequency dictionary, check if they’re part of the "uninteresting"
set of words (for example: "a", "the", "to", "if"). Make this set a parameter to your function so
that you can change it if necessary.

 - Input file
For the input file, you need to provide a file that contains text only.
For the text itself, you can copy and paste the contents of a website you like.
Or you can use a site like Project Gutenberg to find books that are available online.
You could see what word clouds you can get from famous books, like a Shakespeare play or a novel
by Jane Austen.

"""


def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its",
                           "they", "them", "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be",
                           "been", "being", "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when",
                           "where", "how", "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very",
                           "can", "will", "just"]

    # LEARNER CODE START HERE

    result = {}
    a = file_contents.split()
    for word in a:
        if word.lower() in uninteresting_words:
            pass
        else:
            for letter in word:
                if letter in punctuations:
                    letter.replace(punctuations, "")
            if word not in result.keys():
                result[word] = 0
            else:
                result[word] += 1


text = "love is a thing that is hard to forgot and, is need much more to love"
file_contents = calculate_frequencies(text)
