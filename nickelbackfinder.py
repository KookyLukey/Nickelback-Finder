from __future__ import print_function
from app import app
import wordParse
import sys
from app.models import Lyrics
import nltk
from nltk.corpus import wordnet

def word_freq(lyric):

    fullwordlist = wordParse.stripNonAlphaNum(lyric)
    wordlist = wordParse.removeStopwords(fullwordlist, wordParse.stopwords)
    dictionary = wordParse.wordListToFreqDict(wordlist)
    sorteddict = wordParse.sortFreqDict(dictionary)

    return dict(sorteddict)

def get_all_songs(input_phrase):
    master_songs = {}
    compared = {}
    lyrics = Lyrics.query.all()

    for ly in lyrics:
        word_count = word_freq(ly.lyrics.lower())
        word_count_values = word_count.values()

        compared[ly.song_name] = list(set(compare_input_to_songs(input_phrase)) & set(word_count_values))

        master_songs[ly.song_name] = len(compared[ly.song_name])

    print(master_songs, file=sys.stderr)
    return master_songs

def compare_input_to_songs(input_phrase):
    synonyms = []
    nltk.data.path.append('./nltk_data/')

    for syn in wordnet.synsets(input_phrase):
    	for l in syn.lemmas():
    		synonyms.append(l.name())

    return synonyms
