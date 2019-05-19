import nltk
import random
from nltk import word_tokenize
from nltk import sent_tokenize, word_tokenize
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')

def UnigramModel(tokenized_text):
    final_table = {}
    for token in tokenized_text:
        if token in final_table:
            final_table[token] += 1
        else:
            final_table[token] = 1
    #return final_table
    return [final_table, len(tokenized_text)]
# given a genre, return a "dictionary with dictionaries inside" and the # of seen bigrams
# where outside keys are the first words in existing bigrams,
# and values are dictionaries with the subsequent word as key
# and counts of such bigram as value
def BigramModel(tokenized_text):
    uniCounts, unilength = UnigramModel(tokenized_text)
    finalb_table = {}
    num_bigrams = 0
    for i in range(0, unilength - 1):
        if tokenized_text[i] in finalb_table:
            if tokenized_text[i + 1] in finalb_table[tokenized_text[i]]:
                finalb_table[tokenized_text[i]][tokenized_text[i + 1]] += 1
            else:
                finalb_table[tokenized_text[i]][tokenized_text[i + 1]] = 1
                num_bigrams =num_bigrams + 1
        else:
            finalb_table[tokenized_text[i]] = {}
            finalb_table[tokenized_text[i]][tokenized_text[i + 1]] = 1
            num_bigrams = num_bigrams +1
    return finalb_table
#


# import random
#
# #input min and max number of words to generate, a genre and the optional part
# #of a sentence with default value ='', return a randomly generated sentence using bigrams
def merge_two_dicts(x, y):
    """Given two dicts, merge them into a new dict as a shallow copy."""
    z = x.copy()
    z.update(y)
    return z

def flatten(l):
    flatList = []
    for elem in l:
        # if an element of a list is a list
        # iterate over this list and add elements to flatList
        if type(elem) == list:
            for e in elem:
                flatList.append(e)
        else:
            flatList.append(elem)
    return flatList

def removeDuplicates(listofElements):

    # Create an empty list to store unique elements
    uniqueList = []

    # Iterate over the original list and for each element
    # add it to uniqueList, if its not already there.
    for elem in listofElements:
        if elem not in uniqueList:
            uniqueList.append(elem)

    # Return the list of unique elements
    return uniqueList

def get_biSentence(wordds="<s>"):

    f = open("corpus.txt")
    txt = f.read()
    textsentences = sent_tokenize(txt)
    sent = []
    tokens = []
    for i in textsentences:
        sent.append("s " + i + " /s")
    for i in sent:
        tokens += word_tokenize(i)
    unigram = {}
    for token in tokens:
        if token in unigram:
            unigram[token] += 1
        else:
            unigram[token] = 1
    bigram = {}


#
#

    for i in range(1,len(tokens)):
        if tokens[i-1] in bigram:
            if tokens[i] in bigram[tokens[i-1]]:
                bigram[tokens[i-1]][tokens[i]] += 1
            else:
                bigram[tokens[i-1]][tokens[i]] = 1
        else:
            bigram[tokens[i-1]] = {tokens[i]:1}
    print("Displaying Bigram:")
    print (bigram)
    print("Commencing Bi-gram sentence synthesize...")
    sentence = "s "
    last = "s"


    for i in  range(100):
        next_word = bigram[last]
        keys = list(next_word.keys())
        occorence= unigram[last]
        chance = []
        # for sentence in sent_text:
#     tokenized_text = nltk.word_tokenize(sentence)
#     #tagged = nltk.pos_tag(tokenized_text)
#     #print(tokenized_text)
#     print(get_uniCounts(tokenized_text))



        #looking at previous words and deciding what to synthsize next
        for j in next_word:
            chance.append(next_word[j]/occorence)
        Model = random.choices(keys, chance, k=1)
        sentence = sentence + str(Model[0]) + " "
        last = str(Model[0])
    print(sentence)



def get_uniSentence(word="<s>"):

    sentence=""
    generating=True
    last_word=word
    lst=[]
    lst2=[]
    dicc={}
    print("Displaying Unigram: ")
    print(uni_list)
    print("Commencing Uni-gram sentence synthesize...")
    while (generating):
        for i in range(len(uni_list)):
            lst.append(list(uni_list[i].keys()))
        #print(lst)
        flat=flatten(lst)
        flat=removeDuplicates(flat)
        next=random.choice(flat)
        #print(next)
        last_word=next
        if last_word==".":
            generating=False
        sentence=sentence+' '+last_word

    #print(flatten(lst))
    return sentence






f=open('corpus.txt', 'r')
f=f.read()
sent_text = nltk.sent_tokenize(f)
uni_list=[]
final_list=[]
for sentence in sent_text:
    t_text = nltk.word_tokenize(sentence)
    t_text.insert(0,"<s>")
    t_text.append("</s>")
    uni_list.append(UnigramModel(t_text)[0])
    final_list.append(BigramModel(t_text))
decide=input("Press 1 for Uni-gram and 2 for Bi-gram sentence synthesis:  ")
if decide=="1":
    print(get_uniSentence())
elif decide == "2":
    print(get_biSentence())
else:
    print("Wrong input. Re-run again")
