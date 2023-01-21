# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 22:38:02 2021

@author:Sadafa Pasha
"""

#Function to read file
def readFile():
    p = file1.read()

    print(p)

#Function to count total number of tokens
def countTokens():
    q = file1.read()
    L = q.split()

    print("The total number of tokens are:", len(L))

#Function to find frequency of a particular token
def countToken(str1):
    t = file1.read()
    COUNT = t.count(str1)
    
    print("The frequency of", str1, "is:", COUNT)



#Function to find normalised frequency of a particular token
def normalisedFrequency(str2):
    y = file1.read()
    k = y.lower()
    j = y.split()

    count = k.count(str2)

    print("The normalised frequency of", str2, "is:", count/len(j))
    

#Function to find total number of sentences
def sentenceCount():
    l = list(file1)
    d = 0

    for i in l:
        d = d + len(i.split('.'))

    print("The total number of sentences are:", d)



#Function to find sentence containing words
def sentenceContaining(str3):
    m = []

    n = file1.read()
    for i in n.split('\n'):
        if str3 in i.lower():
            m.append(i.strip())
    print(m)
   




while True:
    
    filename = input("Enter file name to read:")
    file1 = open(filename,"r")


    print("\nMAIN MENU")
    print("1. Read file")
    print("2. Token Count")
    print("3. Frequency of a particular token")
    print("4. Normalised Frequency")
    print("5. Sentence Count")
    print("6. Sentence Containing")
    print("7. Exit")
    choice = int(input("Enter your choice"))

    if choice == 1:
        readFile()
    elif choice == 2:
        countTokens()
    elif choice == 3:
        print("Enter token to find frequency")
        token1 = input()
        countToken(token1)
    elif choice == 4:
        print("Enter token to find normalised frequency")
        token2 = input()
        normalisedFrequency(token2)
    elif choice == 5:
        sentenceCount()
    elif choice == 6:
        print("Enter token to find the sentence:")
        token3 = input()
        sentenceContaining(token3)
    else:
        break

    file1.close()


