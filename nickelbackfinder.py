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

    #print(sorteddict, file=sys.stderr)

    return sorteddict

def get_all_songs():
    master_songs = {}
    lyrics = Lyrics.query.all()

    for ly in lyrics:
        word_count = word_freq(ly.lyrics.lower())
        top_5 = word_count[:10]
        master_songs[ly.song_name] = top_5

    #print(master_songs, file=sys.stderr)
    return master_songs

def compare_input_to_songs(input_phrase):
    synonyms = []

    for syn in wordnet.synsets(input_phrase):
        for l in syn.lemmas():
            synonyms.append(l.name())

    print(set(synonyms), file=sys.stderr)
