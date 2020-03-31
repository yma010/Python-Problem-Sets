# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 18:49:10 2019

@author: Marvin
"""
def score(word, f):
    """
       word, a string of length > 1 of alphabetical 
             characters (upper and lowercase)
       f, a function that takes in two int arguments and returns an int

       Returns the score of word as defined by the method:

    1) Score for each letter is its location in the alphabet (a=1 ... z=26) 
       times its distance from start of word.  
       Ex. the scores for the letters in 'adD' are 1*0, 4*1, and 4*2.
    2) The score for a word is the result of applying f to the
       scores of the word's two highest scoring letters. 
       The first parameter to f is the highest letter score, 
       and the second parameter is the second highest letter score.
       Ex. If f returns the sum of its arguments, then the 
           score for 'adD' is 12 
    """
    import string
    scorelist=[0]*len(word)
    loop_tracker=0
    for char in word:
       loop_tracker+=1
       if char.islower():
          alphabet_location=string.ascii_lowercase.find(char)+1
          index=loop_tracker-1
          scorelist.extend([alphabet_location*index])
       else:
          alphabet_location=string.ascii_uppercase.find(char)+1
          index=loop_tracker-1
          scorelist.extend([alphabet_location*index])
    max_score=max(scorelist)
    scorelist.remove(max_score)
    next_max=max(scorelist)
    return f(max_score,next_max)
    
def f(x1,x2):
  return x1+x2

print(score('adD', f))