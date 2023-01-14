# -*- coding: utf-8 -*-
"""
//Mert Karagöz
"""

import nltk
from nltk.util import ngrams
#from collections import defaultdict

    #read contents from the directory
with open('C:/Users/vndlz/Desktop/hw01_tiny.txt', encoding ='utf8') as f:
    contents = f.read()
    #eski dosyayı bozmamak için
    #UNK eklenmiş halde yeni bir tiny2 dosyası oluşturdum
with open('C:/Users/vndlz/Desktop/hw01_tiny2.txt', encoding ='utf8') as f:
    contents2 = f.read()
        
    
    #get and print sentence list
    sentenceList = nltk.tokenize.sent_tokenize(contents)
    print("there are "+ str(len(sentenceList))+ " sentences in the text")    
    #make the sentence lowerCase
    contentsLowercase = contents.lower()
    #remove punctuation words
    removedPunctiations = nltk.RegexpTokenizer(r"\w+")
    #get words without punctuations
    wordList = removedPunctiations.tokenize(contentsLowercase)
    #pass wordList to ngramList for later use.
    ngramList = wordList
    print("there are "+ str(len(wordList)) + " words in text")    
    #find unique words(append the word to array if the word is not in array)
    uniqueWordList = []
    for wordList in wordList:
     if wordList not in uniqueWordList:
      uniqueWordList.append(wordList)
    print("there are " + str(len(uniqueWordList))+" Unique Words in the text")
    
    #find unigram probabilities
    #get unigram words frequency in text
    unigrams = ngrams(ngramList, 1)
    unigramFreq = nltk.FreqDist(unigrams)
    #divide unigram word frequency to total word count in text file
    unigramProbabilities ={k: round(v/len(ngramList),2)
                          for k, v in sorted(unigramFreq.items(),key=lambda item:item[1], reverse = True)}
    #print unigram values.
    print("-----UNIGRAM Probabilities(Descending)-----")
    print(unigramProbabilities)
    
    #find bigram probabilities
    #find bigrams in the text file
    bigrams = ngrams(ngramList, 2)
    #find the frequency of bigrams in the text file
    bigramFreq = nltk.FreqDist(bigrams)
    #find the average of unigram probabilities with an average value
    unigramFreqAvg = 5.1
    #divide bigram word frequencies to total bigram count.
    bigramProbabilities = {k: round(v/unigramFreqAvg,2) 
                           for k, v in sorted(bigramFreq.items(),key=lambda item:item[1], reverse = True)}
    print("-----BIGRAM Probabilities(Descending)-----")
    print(bigramProbabilities)
    
    ###
    sentenceList2 = nltk.tokenize.sent_tokenize(contents2)
    contentsLowercase2 = contents2.lower()
    removedPunctiations2 = nltk.RegexpTokenizer(r"\w+")
    wordList2 = removedPunctiations2.tokenize(contentsLowercase2)
    ##find the bigram freq of new text
    bigrams2 = ngrams(wordList2,2)
    bigramFreq2 = nltk.FreqDist(bigrams2)
    #smoothing k value
    smoothingValue = 0.5
    #apply k smoothing to find new bigram probabilities
    bigramProbabilities2 = {k: round((v + smoothingValue)/(unigramFreqAvg + (smoothingValue * len(bigramFreq2))),2) 
                            for k, v in sorted(bigramFreq2.items(),key=lambda item:item[1], reverse = True )}
    print("-----BIGRAM FREQS WITH UNK WORDS and SMOOTHED k VALUES(Descending)-----")
    print(bigramProbabilities2)
    
    ##make first sentence input from keyboard.
    inputSentence = input("input a sentence 1-> ") 
    contentsLowercase3 = inputSentence.lower()
    removedPunctiations3 = nltk.RegexpTokenizer(r"\w+")
    wordList3 =  removedPunctiations3.tokenize(contentsLowercase3)
    for i in range(len(wordList3)):
        wordFlag = 0
        for j in range(len(uniqueWordList)):
            if uniqueWordList[j] == wordList3[i]:
                wordFlag = 1
                break
        if wordFlag != 1:
            wordList3[i] = "UNK"
    print("ORNEK CUMLE 1: -> "+str(wordList3))
    wordList3 = wordList2.__add__(wordList3)
    bigrams3 = ngrams(wordList3,2)
    bigramFreq3 = nltk.FreqDist(bigrams3)
    #Find Probabilities with Smoothing Technique
    bigramProbabilities3 = {k: round((v+1)/(unigramFreqAvg+len(wordList3)),2) 
                           for k, v in sorted(bigramFreq3.items(),key=lambda item:item[1], reverse = True)}
    print("-----SMOOTHED BIGRAM PROBABILITIES OF INPUT SENTENCE 1")
    print(bigramProbabilities3)
    
    ##make second sentence input from keyboard.
    inputSentence2 = input("input a sentence 2-> ") 
    contentsLowercase4 = inputSentence2.lower()
    removedPunctiations4 = nltk.RegexpTokenizer(r"\w+")
    wordList4 =  removedPunctiations4.tokenize(contentsLowercase4)
    for i in range(len(wordList4)):
        wordFlag = 0
        for j in range(len(uniqueWordList)):
            if uniqueWordList[j] == wordList4[i]:
                wordFlag = 1
                break
        if wordFlag != 1:
            wordList4[i] = "UNK"         
    print("ORNEK CUMLE 2: -> "+str(wordList4))
    wordList4 = wordList2.__add__(wordList4)
    bigrams4 = ngrams(wordList4,2)
    bigramFreq4 = nltk.FreqDist(bigrams4)
    #Find Probabilities with Smoothing Technique
    bigramProbabilities4 = {k: round((v+1)/(unigramFreqAvg+len(wordList4)),2) 
                           for k, v in sorted(bigramFreq4.items(),key=lambda item:item[1], reverse = True)}
    print("-----SMOOTHED BIGRAM PROBABILITIES OF INPUT SENTENCE 2")
    print(bigramProbabilities4)
