import nltk
import numpy as np
import wordninja
import tools
import json
from nltk.tag import StanfordNERTagger
from nltk.tag import StanfordNERTagger
all_ingredients=np.load('processed_data/all_ingredients.npy')

def segment_ingredient(ingredient):
    return wordninja.split(ingredient)

def ingredient_to_str(ingredient):
    return ' '.join(ingredient)

def tag_ingredients_stanford(ingredient):
    st7 = StanfordNERTagger('/usr/local/stanford-ner-2018-10-16/classifiers/english.muc.7class.distsim.crf.ser.gz',
                            '/usr/local/stanford-ner-2018-10-16/stanford-ner.jar')
    print(ingredient)
    res = st7.tag(ingredient)
    return res

def tag_ingredients_nltk(ingredient):
    res=nltk.pos_tag(ingredient)
    return res

def get_nn_ingredient(ingredient,tag_ingredients=tag_ingredients_nltk):
    res=[]
    list_ingredients=segment_ingredient(ingredient)
    tag_i=tag_ingredients(list_ingredients)
    for i in tag_i:
        if i[1]=='NN' or i[1]=='NNS':
            res.append(i[0])
    return res

def seprate_ingredient():
    dict={}
    for i in all_ingredients:
        return_list=get_nn_ingredient(i)
        dict[i]=return_list
    tools.wirte_result(json.dumps(dict),'seprate_ingredient.json')
    return dict
