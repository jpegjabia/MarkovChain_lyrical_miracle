import re
import os
import string 
import random
import graph

def get_words_from_text(text_path):
    with open(text_path, 'r') as f:
        text = f.read()

        # remove such places as: [text in here]
        text = re.sub(r'\[(.+)\]', ' ', text)

        text = ' '.join(text.split()) #turns whitespace into just space
        text = text.lower() #make everything lowercase to compare stuff
        text = text.translate(str.maketrans('', '', string.punctuation))  #removes all punctuation
    
    words = text.split() #split on spaces again
    return words 

def make_graph(words):
    g = graph.Graph() 
    previous_word = None

    #for each word check that word is in the graph and add it if not
    #if there was a previous word, then add an edge if it doesn't exist
    # otherwise, increment weight by 1 
    # set our word to previous word and iteratae
    # we want to generate the probability mappings before composing 

    for word in words: 
        word_vertex = g.get_vertex(word)
        if previous_word:
            previous_word.increment_edge(word_vertex)

        previous_word = word_vertex
    g.generate_probability_mappings()
    return g 

def compose(g, words, length=0):
    composition = []
    word = g.get_vertex(random.choice(words))
    for _ in range(length):
        composition.append(word.value)
        word = g.get_next_word(word)
    return composition


def main(artist):
#get the words from the text
#make a graph using those words
#get the next word for x number of words (defined by user)
#show the result to the user

    #words = get_words_from_text('texts/hp_sorcerer_stone.txt')
    words = []
    # listdr = list directory / lists every single file from the folder with the artist's name  
    for song_file in os.listdir(f'songs/{artist}'):
        if song_file == '.DS_Store':
            continue 
        song_words = get_words_from_text(f'songs/{artist}/{song_file}')
        words.extend(song_words)


    g = make_graph(words)
    composition = compose(g, words, 100)
    return ' '.join(composition) 


if __name__ == '__main__':
    print(main('taylor_swift'))


