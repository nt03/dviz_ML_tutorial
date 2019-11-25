# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 22:41:08 2019

@author: tneha
"""

import pandas as pd
import spacy
import re

nlp = spacy.load("en_core_web_md")


def get_lemma(item):   
    
    """
    For every record the function returns a dict of:
    number of tokens: num_tokens,
    number of vectors: num_vectors,
    comma separated list of tokens with no vector: oov_tokens
    
    """
    
    
    lemma_notent = []
    ents = []
    
    tokens = nlp(item)
    
    #ents = [t.text for t in tokens.ents]
    
    for ent in tokens.ents:
        if ent.label_ not in ["PERSON", "DATE", "TIME", "CARDINAL", "ORDINAL", "PERCENT", "MONEY", "QUANTITY"]:
            ents.append(ent.text)
    
    ents = list(set(ents))
     

    for token in tokens:
        if token.text not in ents:
            lemma_notent.append(token.lemma_)
            
        
    lemma_notent = list(set(lemma_notent))
    
    return (" ".join(lemma_notent), " ".join(ents))
    
    
    
    

def main():       
    
    reviews = pd.read_csv("../data/airbnb/reviews_cleaned.csv")
    
    
    revs = reviews.reviews.to_list()
     
    lem = []
    lem_ent = []
    
    for r in revs:
        r = re.sub(r"[^'a-zA-Z\s]", '', r)
        l, e = get_lemma(r)
        lem.append(l)
        lem_ent.append(e)
        
    
    reviews['lemma_notent'] = lem
    reviews['lemma_ent'] = lem_ent
    
    reviews.to_csv("../data/airbnb/reviews_cleaned_lemma.csv", index= False)
               
    
    

if __name__== "__main__" :
    main()  

    