import syllapy

with open ("test.txt", "r") as f:
    tweet = f.read()

def count_syllables(tweet):
    #split text into single words
    words = tweet.split()

    #create a list of syllables
    syllables = []

    #get syllable count and append to list
    for word in words:
        syllables.append(syllapy.count(word))

    #add all syllables together
    total = 0
    for syllable in syllables:
        total += syllable

    if total == 17:
        haiku_dict = dict(zip(words, syllables))

    #print(haiku_dict)
    return haiku_dict

tweet_to_haiku = count_syllables(tweet)

def format_dict_to_string(tweet_to_haiku):
    line_one = ""
    line_two = ""
    line_three = ""

    

print(format_dict_to_string(tweet_to_haiku))