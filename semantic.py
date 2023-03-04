# =========== Libraries ============= #
import spacy



nlp = spacy.load('en_core_web_sm')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
word4 = nlp("gecko")
word5 = nlp("chameleon")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
print(word4.similarity(word5))


""" Note as per the task requirement: 
The results are (with 'en_core_web_md'): 
0.5929930274321619
0.40415016164997786
0.22358825939615987
1.0000000415082995

I've added 2 new words: gecko & chameleon and the result of comparing their similarity is quite interesting as it is: 1.0000000415082995
I was expecting a number between 0 and 1, closer to 1 as these animals are quite similar, but I am surprised that the number is greater than 1. 


If I run the same program with 'en_core_web_sm', the results are quite different: 
0.6770565478895127
0.7276309976205778
0.6806929391210822
0.5940569289195583

It's really interesting that now a different pair of words have the highest similarity and the same for the lowest. 

"""

tokens = nlp("cat apple monkey banana")

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))


sentence_to_compare = 'Why is my can on the car'

sentences = ["where did my dog go", 
             "Hello, there is my car",
             "I've lost my car in my car",
             "I'd like my boat back",
             "I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)