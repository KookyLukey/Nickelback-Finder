from __future__ import print_function
from app import app
import wordParse
import sys
from app.models import Lyrics
import nltk
from nltk.corpus import wordnet
import operator

def word_freq(lyric):

    fullwordlist = wordParse.stripNonAlphaNum(lyric)
    wordlist = wordParse.removeStopwords(fullwordlist, wordParse.stopwords)
    dictionary = wordParse.wordListToFreqDict(wordlist)
    sorteddict = wordParse.sortFreqDict(dictionary)

    sorteddict = [(t[1], t[0]) for t in sorteddict]

    return dict(sorteddict)

def get_synonyms(input_phrase):
    synonyms = []
    nltk.data.path.append('./nltk_data/')

    for syn in wordnet.synsets(input_phrase):
    	for l in syn.lemmas():
    		synonyms.append(l.name())

    return synonyms

def get_highest_songs(all_songs):
    # Takes in a dictionary and returns the highest three songs depending on the weight
    top_3 = sorted(all_songs, key=all_songs.get, reverse=True)[:3]

    i = 0
    while i < len(top_3):
        if all_songs.get(top_3[i]) <= 0:
            del top_3[i]
        else:
            i += 1

    return ', '.join(top_3)

#
# Main method called from routes
#
def get_all_songs(input_phrase):
    master_songs = {}
    compared = {}
    lyrics = Lyrics.query.all()

    for ly in lyrics:
        song_weight = 0
        word_count = word_freq(ly.lyrics.lower())
        word_count_keys = word_count.keys()

        # Get synonyms from the input phrase using nltk
        synonyms = get_synonyms(input_phrase)
        synonyms = synonyms + [input_phrase] + [wordParse.getPlural(input_phrase)] + [wordParse.getPastPresent(input_phrase)]

        #Inner join on the two lists then count up all of the occurences of the words
        compared[ly.song_name] = list(set(synonyms) & set(word_count_keys))
        print(compared[ly.song_name])
        for song in compared.get(ly.song_name):
             song_weight = song_weight + word_count.get(song)

        master_songs[ly.song_name] = song_weight

    #If all song weights are zero print this
    if all(value == 0 for value in master_songs.values()):
        master_songs["Unfortunately your input did not match any songs."] = 99

    return get_highest_songs(master_songs)
